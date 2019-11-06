import pymunk
import pygame.locals

class Creature:
    """class responsible from creatures
    """
    def __init__(self, genotype):
        """instantiates a creature type
        """
        self.genotype = genotype
        self.updateDirs = True # thruster direction change next update
        self.applyThr = False # thrust to be applied next update
        self.mass = 1 # will calculated based on area in the future
        self.position = (900,250) # will be described in genome


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
            spine += vertebra
            point = (spine, p * width)
            self.points.append(point)

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
        self.thrusterList = []
        for thr in TL:
            coords = self.points[thr[0]]
            vec = pygame.math.Vector2(0,coords[1])
            self.thrusterList.append([coords, thr[1], vec.normalize()])


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


    def get_directions(self):
        """bandaid solution for testing if apply thrust works.
        """
        pass


    def update_directions(self, directions):
        """changes thrust vectors (thruster[3]) of specified thrusters.
        directions[0] : Nr. of thruster, directions[1] : angle to add.
        Lot's to fix here, for now angle to add only valid if 45>a>0
        """
        for instruction in directions:
            thruster = self.thrusterList[instruction[0]]
            new_angle = thruster[1] + instruction[1]
            vec = pygame.math.Vector2(0, 1)
            vec = vec.rotate(new_angle)
            self.thrusterList[instruction[0]][2] = vec


    def apply_thrust(self, applyTo):
        """applies thrust to every thruster in thruster list.
        applyTo : for now just list with int of every thruster to fire.
        """
        for thr_number in applyTo:
            thruster = self.thrusterList[thr_number]
            self.body.apply_impulse_at_local_point(thruster[2])

