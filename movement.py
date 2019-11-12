import pymunk
import pygame.locals

# This file contains everything concerned with moving creatures in
# simulated space. It contains a thruster class and a transcriptor for
# generating thrusters based on dna. Will add a ThrusterSystem class.

class ThrusterTranscriptor:
    """Builds a list of thrusters and updates transcription_data with it.
    Can only be run after ShapeTranscriptor has run.
    To-Do: Limit thrust vector, Max_thrust_strength parameter.
    """
    def __init__(self):
        """Thruster requires points to be already transcribed.
        """
        self.required_data = ["body", "points"]

    def run(self, rna, data):
        """Starts transcription process for building thrusters.
        """
        for check_data in self.required_data:
            if check_data not in data:
                return None

        self.point_l = data["points"]
        self.body = data["body"]
        self.rna = rna
        thruster_l = self.make_thrusters()
        return {"thruster_l" : thruster_l}

    def make_thrusters(self):
        """method that initializes all thrusters described in the rna.
        """
        thruster_l = [] # this gets returned to main transcriptor.
        blueprints = self.rna["thruster"]

        for instruction in blueprints:
            instruction = instruction.data
            point = self.point_l[instruction[0]] # instruction[0] : index
            m_point = (point[0], point[1]*-1) # mirror point by mult y * -1
            mirrored = instruction[1]
            start_a = instruction[2]
            end_a = instruction[3]

            # check if thruster on right side and angle is valid
            if point[1] > 0 and start_a < end_a and end_a <= 180:
                if mirrored:
                    t_r = Thruster(point, start_a, end_a, True)
                    t_l = Thruster(m_point, 360-start_a, 360-end_a, True)
                    thruster_l.extend([t_r, t_l])
                else:
                    t_r = Thruster(point, start_a, end_a, False)
                    thruster_l.append(t_r)

            # check if thruster on left side and angle is valid
            elif point[1] < 0 and start_a > end_a and end_a >= 180:
                if mirrored:
                    t_r = Thruster(m_point, 360-start_a, 360-end_a, True)
                    t_l = Thruster(point, start_a, end_a, True)
                    thruster_l.extend([t_r, t_l])
                else:
                    t_l = Thruster(point, start_a, end_a, False)
                    thruster_l.append(t_l)

        return thruster_l
        # make a ThrusterSystem object, that tracks all thrusters
        # and performs updates and thrusting. this object should have
        # a reference to the creature body and be the interface to the
        # brain.



class Thruster:
    """Builds a single thruster with the methods update, apply thrust.
    """
    def __init__(self, point, start_a, end_a, mirrored):
        self.point = point
        self.start_a = start_a
        self.end_a = end_a
        self.mirrored = mirrored
        self.vec = pygame.math.Vector2(1,0) # vec pointing 9 o'clock

    def update_direction(self, firing_rad_percent):
        """changes thrust vector of specified thruster. Method: calculates
        angle within firing radius. If fire_rad = 0. -> angle = start_a,
        if fire_rad = 1. -> angle = end_a.
        """
        new_angle = start_a + firing_rad_percent * (end_a - start_a)
        # vec pointing 9 o'clock is rotated clockwise
        self.vec = pygame.math.Vector2(-1, 0).rotate(-new_angle)

    def apply_thrust(self, power):
        """applies thrust of specified strength.
        """
        self.vec *= power

# TESTING AREA
# trans_data = {"body" : "somebody", "points" : [(-10,2), (0,5), (10,2),
#                                                (10,-2), (0,-5), (-10,-2)]}
# rna = {"thruster" : [[0, True, 0, 90], [2, True, 90, 180]]}
# test_transc = ThrusterTranscriptor()
# t_list = test_transc.run(rna, trans_data)
# for thruster in t_list:
#     print(thruster.point, thruster.start_a, thruster.end_a, thruster.mirrored)
