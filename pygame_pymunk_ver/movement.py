import pymunk
import pygame.locals

# This file contains everything concerned with moving creatures in
# simulated space. It contains a thruster class and a transcriptor for
# generating thrusters based on dna. Will add a ThrusterSystem class.

class ThrusterTranslator:
    """Builds a list of thrusters and updates transcription_data with it.
    Can only be run after ShapeTranscriptor has run.
    To-Do: Limit thrust vector, Max_thrust_strength parameter.
    """
    def __init__(self):
        """Thruster requires points to be already transcribed.
        """
        self.required_data = ["body", "points"]

    def run(self, rna, data):
        """Starts translation process for building thrusters.
        """
        for check_data in self.required_data:
            if check_data not in data:
                return None

        self.point_l = data["points"]
        self.rna = rna
        thruster_l = self.make_thrusters()
        thruster_sys = ThrusterSystem(thruster_l, data["body"])
        return {"thruster_l" : thruster_l, "thruster_sys" : thruster_sys}

    def make_thrusters(self):
        """method that initializes all thrusters described in the rna.
        """
        thruster_l = [] # this gets returned to main translator.
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


class Thruster:
    """Builds a single thruster with the methods update, apply thrust.
    """
    def __init__(self, point, start_a, end_a, mirrored):
        self.point = point
        self.start_a = start_a
        self.end_a = end_a
        self.mirrored = mirrored
        self.vec = (-1, 0)  # Initial pointing 9 o'clock

    def update(self, rad, power=1):
        """changes thrust vector of specified thruster. Method: calculates
        angle within firing radius. If rad = 0. -> angle = start_a,
        if rad = 1. -> angle = end_a. power is multiplied with vec.
        """
        new_angle = self.start_a + rad * (self.end_a-self.start_a)
        vec = pygame.math.Vector2(-1, 0).rotate(-new_angle) * power
        self.vec = (vec.x, vec.y)



class ThrusterSystem:
    """Manages all thrusters of a creature.
    """
    def __init__(self, thruster_l, body):
        self.thruster_l = thruster_l
        self.body = body

    def turn(self, direction):
        if direction == "left":
            apply_to = [self.thruster_l[0], self.thruster_l[3]]
            self.thruster_l[0].update(1)
            self.thruster_l[3].update(0)
        elif direction == "right":
            apply_to = [self.thruster_l[1], self.thruster_l[2]]
            self.thruster_l[1].update(1)
            self.thruster_l[2].update(0)

        for t in apply_to:
            impulse = (-t.vec[0], -t.vec[1])
            self.body.apply_impulse_at_local_point(impulse, t.point)

    def move(self, direction):
        if direction == "forward":
            apply_to = [self.thruster_l[2], self.thruster_l[3]]
            self.thruster_l[2].update(1)
            self.thruster_l[3].update(1)
        elif direction == "backward":
            apply_to = [self.thruster_l[0], self.thruster_l[1]]
            self.thruster_l[0].update(0)
            self.thruster_l[1].update(0)
        elif direction == "left":
            apply_to = [self.thruster_l[0], self.thruster_l[2]]
            self.thruster_l[0].update(1)
            self.thruster_l[2].update(0)
        elif direction == "right":
            apply_to = [self.thruster_l[1], self.thruster_l[3]]
            self.thruster_l[1].update(1)
            self.thruster_l[3].update(0)

        for t in apply_to:
            impulse = (-t.vec[0], -t.vec[1])
            self.body.apply_impulse_at_local_point(impulse, t.point)


