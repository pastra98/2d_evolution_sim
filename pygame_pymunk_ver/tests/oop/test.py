class Gene:
    """class that describes a single gene
    """
    def __init__(self, g_type, g_data):
        """initializes a gene of given type with given data
        """
        self.type = g_type
        self.data = g_data
        self.is_expressed = True


class Transcriptor:
    def __init__(self):
        self.data = {}
        self.rna = {}
        self.a_transcriptor = ATrans()
        self.d_transcriptor = DTrans()
        self.trans_l = [self.a_transcriptor, self.d_transcriptor]

    def read_genome(self, genes):
        """returns a dict of every gene type described in dna
        """
        for gene in genes:
            if gene.type in self.rna:
                self.rna[gene.type].append(gene.data)
            else:
                self.rna[gene.type] = [gene.data]

    def express_genome(self):
        """Starts transcription process of every subtranscriptor stored
        in the transcriptor list. If transcriptor has required data,
        it performs transcription and is subsequently removed from the
        list. If a transcriptor is unable to run, it is passed over, and
        the express genome recursively calls itself until every
        transcriptor has run.
        """
        for trans in self.trans_l:
            trans_d = trans.run(self.rna, self.data)
            if trans_d == None:
                pass
            else:
                self.data.update(trans_d)
                self.trans_l.remove(trans)

        if len(self.trans_l) > 0:
            self.express_genome()
        else:
            return self.data


class ATrans:
    def __init__(self):
        self.req_data = ["d"] # requires no data

    def run(self, rna, data):
        for check_data in self.req_data:
            if check_data in data.keys():
                t_data = self.a_read_data(rna, data)
                return t_data
            else:
                return None

    def a_read_data(self, rna, data):
        t_data = {}
        gene_a = rna["a"]
        gene_d = rna["d"]
        t_data["a"] = "I like {}, and {}".format(gene_a, gene_d)
        return t_data


class DTrans:
    def __init__(self):
        self.req_data = None

    def run(self, rna, data):
        t_data = self.d_read_data(rna, data)
        return t_data

    def d_read_data(self, rna, data):
        t_data = {}
        gene_d = rna["d"]
        t_data["d"] = "Gene d says {}".format(gene_d)
        return t_data


# genes
gene_a = Gene("a", 1)
gene_b = Gene("a", 2)
gene_c = Gene("b", 3)
gene_d = Gene("b", 4)
gene_e = Gene("d", 5)
dna = [gene_a, gene_b, gene_c, gene_d, gene_e]

main_trans = Transcriptor()
main_trans.read_genome(dna)
main_trans.express_genome()

print(main_trans.data)
