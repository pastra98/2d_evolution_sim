import pymunk
import pygame.locals

class Creature:
    """class responsible for creatures
    """
    def __init__(self, genotype):
        """instantiates a creature type
        """
        self.genotype = genotype
        self.updateDirs = True # thruster direction change next update
        self.applyThr = False # thrust to be applied next update
        self.mass = 1 # will calculated based on area in the future
        self.position = (500,260) # will be described somewhere else


    def build_phenotype(self):
        """builds a genotype body based on limited amt of genes.
        """
        # parameters defining shape of body
        shape = self.genotype.extract_dna("shape")
        length = self.genotype.extract_dna("length")
        width = self.genotype.extract_dna("width")

        self.points = [] # list of all points to construct poly
        vertebra = length/len(shape) # distance between each vertebra
        spine = (length/2) * -1 # x_value of first vert

        # calculating all the points that make up body
        for p in shape:
            point = (spine, p * width)
            self.points.append(point)
            spine += vertebra

        for p in reversed(self.points):
            point = (p[0], p[1] * -1)
            self.points.append(point)

        # creating pymunk body
        moment = pymunk.moment_for_poly(self.mass, self.points)
        self.body = pymunk.Body(self.mass, moment)
        self.body.position = self.position
        self.shape = pymunk.Poly(self.body, self.points)

        # list of all thrusters
        TL = self.genotype.extract_dna("thrusters")
        self.thruster_l = []
        for t in TL:
            vec = pygame.math.Vector2(0, 1)
            if t[1] == "lr":
                mirror = True
            else:
                mirror = False
            if t[1] == "r" or mirror:
                coords = self.points[t[0]]
                start = t[2]
                end = t[3]
                self.thruster_l.append([coords, mirror, start, end, vec])
            if t[1] == "l" or mirror:
                vec = vec.rotate(180)
                if mirror:
                    start = 360 - t[2]
                    end = 360 - t[3]
                else:
                    start = t[2]
                    end = t[3]
                left_side = self.points[::-1]
                coords = left_side[t[0]]
                self.thruster_l.append([coords, mirror, start, end, vec])



    def update(self):
        """this function gets called by the main loop and handles all
        of an agents actions.
        """
        # ask the brain to calculate new directions and return them
        # for now I'm using a control function in the main loop

        # if self.updateDirs:
        #     self.update_directions()
        # if self.applyThr:
        #     self.apply_thrust()


    def update_directions(self, directions):
        """Passes multiple direction instructions to self.update_directions
        instr[0] : Nr. of thruster, instr[1] : percent of firing radius
        """
        for instr in directions:
            thr_index = instr[0]
            firing_rad = instr[1]
            start_a = self.thruster_l[thr_index][2] # indexed in thr_l
            end_a = self.thruster_l[thr_index][3] # indexed in thr_l
            self.update_direction(thr_index, firing_rad, start_a, end_a)


    def update_direction(self, thr_index, firing_rad_percent, start_a, end_a):
        """changes thrust vector (thruster[4]) of specified thruster.
        Method: calculates angle within firing radius. Angle is determined by:
        If fire_rad = 0. -> angle = start_a, fire_rad = 1. -> angle = end_a
        """
        new_angle = start_a + firing_rad_percent * (end_a - start_a)
        # vec pointing 9 o'clock is rotated clockwise
        vec = pygame.math.Vector2(-1, 0).rotate(-new_angle)
        self.thruster_l[thr_index][4] = vec # update vec component


    def apply_thrust(self, applyTo):
        """applies thrust to every thruster in thruster list.
        applyTo : for now just list with int of every thruster to fire.
        """
        for thr_number in applyTo:
            thr = self.thruster_l[thr_number]
            self.body.apply_impulse_at_local_point(-thr[4], thr[0])

