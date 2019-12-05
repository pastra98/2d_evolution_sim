import pymunk
import pygame.locals

# This file contains everything that has to do with the physical
# appearance of creatures. At the moment it contains a transcriptor
# that returns a creatures points, physics body and physics shape.

class ShapeTranslator:
    """Calculates a list of points describing the shape of the creature.
    Uses this information to build a pymunk body and shape.
    """
    def __init__(self):
        """Required data would be in init(), but ShapeTranscriptor does
        not require any data to be already transcripted.
        """
        pass

    def run(self, rna, data):
        """Starts transcription process for calculating points of the
        creature, and generating pymunk body and shape. Returns points,
        body and shape to main transcriptor. Doesn't use data, but should
        be included to be uniform with other transcriptors.
        """
        points = self.calculate_points(rna)
        body, shape = self.body_and_shape(points)
        return {"points" : points, "body" : body, "shape" : shape}

    def calculate_points(self, rna):
        """Extracts gene data from rna.
        Can only use one gene for each of shape, length and width.
        shape : list of floats(1=>x=>0) that are multiplied with width
        lenght : int, total creature length (minus a bit, pls fix)
        width : int, total creature width
        """
        # reads genes from rna, only one data element used per gene.
        # this is why index[0].
        shape = rna["shape"][0].data
        length = rna["length"][0].data
        width = rna["width"][0].data

        points = [] # list of all points to construct poly
        vertebra = length/len(shape) # distance between each vertebra
        spine = (length/2) * -1 # x_value of first vert

        # calculate all the points that make up body
        for p in shape:
            point = (spine, p * width)
            points.append(point)
            spine += vertebra
        for p in reversed(points): # step through points in reverse
            point = (p[0], p[1] * -1) # revert y coord of point -> bottom
            points.append(point)

        return points

    def body_and_shape(self, points):
        """Takes a list of points defined in a clock-wise order and
        generates a dynamic pymunk physics body with appropriate moment,
        and a corresponding shape. Returns the body and shape.
        To-Do: calculate mass based on shape.
        """
        mass = 1 # arbitrary value for now
        # creating pymunk body
        moment = pymunk.moment_for_poly(mass, points)
        body = pymunk.Body(mass, moment) # pos is defined in creature
        shape = pymunk.Poly(body, points)

        return body, shape


