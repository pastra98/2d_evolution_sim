extends Node

var dna = Dictionary()

func _init():
	"""Constructor for DNA. Each key in the dict represents one type of gene.
	Every gene is contained within an array, that is mapped in the dna to it's
	corresponding key(type).
	"""
	pass # not really anything


func append_gene(gene):
	"""Append a single gene, map it based on type to corresponding dict key.
	"""
	dna[gene.g_name] = gene


func append_genes(genes: Array):
	"""Append multiple genes.
	"""
	for gene in genes:
		self.append_gene(gene)
	

