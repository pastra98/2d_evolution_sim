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
        self.genome.transcript_genome()
        self.data_dict = self.genome.translator.translate_genome()
        self.thruster_sys = self.data_dict["thruster_sys"]
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


