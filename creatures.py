class Creature:
    """class ŕesponsible fro creatures
    """
    def __init__(self, genotype):
        """instantiates a creature type
        """
        self.genotype = genotype

    def build_phenotype(self):
        """builds a genotype body based on limited amt of genes.
        """
        shape = self.genotype.extract_dna("shape")
        length = self.genotype.extract_dna("length")
        width = self.genotype.extract_dna("width")

        self.points = [] # list of all points to construct poly
        vertebra = length/len(shape) # distance between each vertebra
        spine = (length/2) * -1 # x_value of first vert

        for p in shape:
            spine += vertebra
            point = (spine, p * width)
            self.points.append(point)

        for p in reversed(self.points):
            point = (p[0], p[1] * -1)
            self.points.append(point)

        return self.points
