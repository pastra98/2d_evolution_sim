extends Node

var dna
var data
var creature_path

func translate():
	self.dna = get_parent().dna
	self.data = get_parent().temp_data
	self.creature_path = get_parent().creature_path

