# Transcriptors are responsible for performing the instructions of genes
# and temporarily storing relevant data described in genes.
import pymunk
import pygame.locals

class ShapeTranscriptor:
    """Calculates a list of points describing the shape of the creature.
    Uses this information to build a pymunk body and shape.
    """
    def express_shape(self):
        """Starts transcription process for calculating points of the
        creature, and generating pymunk body and shape. Add points,
        body and shape to transcription data.
        """
        points = self.calculate_points()
        body, shape = self.body_and_shape(points)
        # Update transcription_data dict
        self.transcription_data.update({"points" : points,
                                        "body" : body, "shape" : shape})

    def calculate_points(self):
        """Extracts gene data from rna.
        Can only use one gene for each of shape, length and width.
        shape : list of floats(1=>x=>0) that are multiplied with width
        lenght : int, total creature length (minus a bit, pls fix)
        width : int, total creature width
        """
        # collect data from Base dict, only one data element used per type
        # this is why index[0]
        shape = self.rna["shape"][0].data
        length = self.rna["length"][0].data
        width = self.rna["width"][0].data

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


class ThrusterTranscriptor:
    """Builds a list of thrusters and updates transcription_data with it.
    Can only be run after ShapeTranscriptor has run.
    To-Do: Limit thrust vector, Max_thrust_strength parameter.
    """
    def express_thrusters(self):
        """Starts transcription process for building thrusters.
        """
        thruster_l = [] # this is the data that will be passed to creature
        thruster_data = self.rna["thruster"]

        for bluepr in thruster_data:
            bluepr = bluepr.data # access data of gene
            if bluepr[1] == "lr": # two thruster described as one
                thrusters = self.mirrored_thr(bluepr[0],
                                              bluepr[2], bluepr[3])
                thruster_l.extend(thrusters) # add both thrusters
            elif bluepr[1] == "r":
                thruster = self.build_thr(bluepr[0], True,
                                          bluepr[2], bluepr[3])
                thruster_l.append(thruster) # add a right thruster
            elif bluepr[1] == "l":
                thruster = self.build_thr(bluepr[0], False,
                                          bluepr[2], bluepr[3])
                thruster_l.append(thruster) # add a left thruster

        self.transcription_data.update({"thruster_l" : thruster_l})

    def mirrored_thr(self, p_index, start_a, end_a):
        """calls build_thr twice to produce one thruster on each side,
        and returns both of them
        """
        l_thruster = self.build_thr(p_index, False, start_a, end_a, True)
        # subtraction from 360 deg mirrors the angle
        r_thruster = self.build_thr(p_index, True, 360 - start_a,
                                                   360 - end_a, True)
        return [l_thruster, r_thruster] # watch out, nested list!

    def build_thr(self, p_index, is_right, start_a, end_a, mirr=False):
        """Constructs a single thruster. Thrusters are a list.
        """
        points = self.transcription_data["points"]

        if is_right:
            location = points[p_index]
        else: # thruster on left side --> search list in reverse
            location = points[::-1][p_index]

        vec = pygame.math.Vector2(0, 1) # starting vec of thruster
        return [location, mirr, start_a, end_a, vec] # finished thruster


class Transcriptor(ShapeTranscriptor, ThrusterTranscriptor):
    """This class contains all methods that are required for transcription.
    Somewhat analogous to ribosomes, mRNA, proteins and everything to
    do with gene transcription and expression.
    To-Do : Figure out if updating of transcription_data should happen
    here or in parent classes.
    """
    def __init__(self, genes_to_express):
        """Initializes with a dictionary that contains all genes that
        should be expressed (genes_to_transcribe).
        Returns a second dict that stores all information returned
        by subtranscriptors(parent classes).
        """
        self.transcription_data = {}
        self.rna = genes_to_express # genes to be expressed

    def express_genome(self):
        """hands the dict of expressed genes to the specialized sub-
        transcriptors. Compiles the transcription_data dictionary from
        all data returned by subtranscriptors.
        """
        self.express_shape()
        self.express_thrusters()

        return self.transcription_data


