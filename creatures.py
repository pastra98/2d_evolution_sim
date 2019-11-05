class Creature:
    """class responsible from creatures
    """
    def __init__(self, genotype):
        """instantiates a creature type
        """
        self.genotype = genotype
        self.updateDirs = False # thruster direction change next update
        self.applyThr = False # thrust to be applied next update
        self.mass = 1 # will be described in genome
        self.position = (50,50) # will be described in genome


    def build_phenotype(self):
        """builds a genotype body based on limited amt of genes.
        """
        # parameters defining shape of body
        shape = self.genotype.extract_dna("shape")
        length = self.genotype.extract_dna("length")
        width = self.genotype.extract_dna("width")
        # list of all thrusters
        self.thruster_list = self.genotype.extract_dna("thrusters")

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
        self.shape = pymunk.Poly(body, self.points)
        # TODO: change how thruster list is created, and make it store
        # each thrusters position.


    def update(self):
        """this function gets called by the main loop and handles all
        of an agents actions.
        """
        # ask the brain to calculate new directions and return them
        # for now I'm using a control function, stored in movement
        movement = self.get_directions()

        if self.updateDirs:
            self.update_directions()
        if self.applyThr:
            self.apply_thrust()


    def get_directions(self):
        """bandaid solution for testing if apply thrust works.
        """
        pass


    def update_directions(self, directions):
        """changes thrust vectors (thruster[3]) of specified thrusters.
        directions[0] : Nr. of thruster, directions[1] : angle to add.
        """
        for instruction in directions:
            thruster = self.thruster_list[directions[0]]
            new_angle = thruster[2] + directions[1]
            vec = pygame.math.Vector2(thruster[0], thruster[1])
            vec.normalize()
            vec.rotate(new_angle)
            self.thruster_list[directions[0]][3] = vec


    def apply_thrust(self, applyTo):
        """applies thrust to every thruster in thruster list.
        applyTo : for now just list with int of every thruster to fire.
        """
        for instruction in applyTo:
            thruster = self.thruster_list[applyTo]
            self.body.apply_impulse_at_local_point(thruster[3])

