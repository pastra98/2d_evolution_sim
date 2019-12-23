extends Node

var dna
var data
var creature_path

var Brain = preload("res://Translator/Parts/Brain.tscn")

func translate():
	self.dna = get_parent().dna
	self.data = get_parent().temp_data
	self.creature_path = get_parent().creature_path

	var new_brain = Brain.instance()
	get_node(creature_path).add_child(new_brain)