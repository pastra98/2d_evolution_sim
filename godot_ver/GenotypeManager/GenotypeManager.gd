extends Node

var creature = preload("res://CreatureInstance/Creature.tscn")
onready var creatures_node = $"/root/Main/World/Creatures"
var creature_counter = 0

func new_creature(dna: Dictionary, pos: Vector2):
	"""Creates a new creature according to given DNA, at a given position.
	Assigns its number as an id.
	"""
	creature_counter += 1
	var creature_inst = creature.instance()
	creature_inst.pos = pos
	creature_inst.id = str(creature_counter)
	
	creatures_node.add_child(creature_inst)
	Translator.express_dna(dna, creature_inst.get_path())
	