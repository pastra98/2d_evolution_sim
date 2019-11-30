from translators import Transcriptor

# Holds DNA and performs all relevant actions

class Genome:
    """class that holds the dna with all it's genes. Also contains
    a Transcriptor object that is required for expressing gene
    functions.
    """
    def __init__(self):
        """initializes dna and transcriptor used for reading and
        expressing genes.
        """
        self.dna = []

    def append_genes(self, genes):
        """appends multiple genes to the dna.
        """
        for gene in genes:
            self.dna.append(gene)

    def transcribe_genome(self):
        """Reads a gene, determines if it should be expressed and
        assigns it to a list, based on its type. This list represents
        the data of all genes of a given type. All gene types are then
        added to a dictionary. The transcriptor is then fed this dict.
        """
        self.to_transcribe = {}
        for gene in self.dna:
            if gene.is_expressed:
                if gene.type in self.to_transcribe:
                    self.to_transcribe[gene.type].append(gene)
                else:
                    self.to_transcribe[gene.type] = [gene]

        self.transcriptor = Transcriptor(self.to_transcribe)


# Describes a single gene
class Gene:
    """class that describes a single gene
    """
    def __init__(self, g_type, g_data):
        """initializes a gene of given type with given data
        """
        self.type = g_type
        self.data = g_data
        self.is_expressed = True



