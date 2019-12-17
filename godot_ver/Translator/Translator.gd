extends Node

var dna: Dictionary
var creature_path: NodePath
var temp_data = Dictionary()

func express_dna(dna, c_path):
	temp_data.clear()
	self.dna = dna
	self.creature_path = c_path
	$BodyDevelopment.translate()