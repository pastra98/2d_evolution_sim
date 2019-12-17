extends Node

var zones = preload("res://Genome/Switches/ExpressionZones.gd")

func _ready():
	var switch = zones.new([[0.1, 0.2]])
	for x in range(1, 100):
		switch.mutate()
		if 100 % x == 0:
			print(switch.expression_zones)
