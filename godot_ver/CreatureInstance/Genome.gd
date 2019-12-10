extends Node

class Gene:
	"""Initializes a single gene.
	"""
	func _init(g_type: String, g_data, is_expressed: bool):
		var type = g_type
		var data = g_data
		var expressed = is_expressed


func _init():
	"""Constructor for DNA. Each key in the dict represents one type of gene.
	Every gene is contained within an array, that is mapped in the dna to it's
	corresponding key(type).
	"""
	var dna: Dictionary


func append_gene(gene: Gene):
	"""Append a single gene, map it based on type to corresponding dict key.
	"""
	if self.dna.has(gene.type):
		self.dna[gene.type].append(gene)
	else:
		self.dna[gene.type] = [gene]


func append_genes(genes: Array):
	pass

