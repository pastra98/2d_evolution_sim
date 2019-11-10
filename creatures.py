import pymunk
import pygame.locals


class Creature:
    """class responsible for creatures
    """
    def __init__(self, genotype):
        """instantiates a creature type
        """
        self.genome = genotype
        self.updateDirs = True # thruster direction change next update
        self.applyThr = False # thrust to be applied next update
        self.position = (500,260) # will be described somewhere else

    def birth(self):
        """builds a genotype body based on limited amt of genes.
        """
        self.genome.transcribe_genome()
        self.data_dict = self.genome.transcriptor.express_genome()
        self.thruster_l = self.data_dict["thruster_l"]
        self.body = self.data_dict["body"]
        self.shape = self.data_dict["shape"]
        self.body.position = self.position


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


