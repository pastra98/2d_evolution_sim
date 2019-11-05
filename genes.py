class Genome:
    """class that holds the dna with all it's genes.
    """
    def __init__(self):
        """ innitializes and creates dna
        """
        self.dna = []


    def append_gene(self, g_type, g_data):
        """creates a gene, appends a gene to the dna, and returns it.
        """
        gene = [g_type, g_data]
        self.dna.append(gene)
        return gene


    def extract_dna(self, g_type):
        """returns the data of first gene of described type in dna.
        Could later be changed to return a list of multiple genes
        describing the same thing.
        """
        for gene in self.dna:
            if gene[0] == g_type:
                return gene[1]

