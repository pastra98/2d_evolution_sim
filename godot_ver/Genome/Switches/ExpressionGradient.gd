extends Node

var mutation_chance = 0.1
var mutation_size = 0.1
var gradient: Array

var rng = RandomNumberGenerator.new()

func _init(gradient: Array):
	"""Gradient represents an Array of 11 floats ranging from 0 to 1
	"""
	if gradient.size() != 11:
		return "Array must be of size 11"
	self.gradient = gradient


func get_gradient(index: int):
	if index < 0 or index > 10:
		return "Index must be for Array of size 11"
	return gradient[index]


func mutate():
	rng.randomize()
	if rng.randf() <= mutation_chance:
		rng.randomize()
		if rng.randf() <= 0.5:
			gradient[rng.randi_range(11)] += mutation_size
		else:
			gradient[rng.randi_range(11)] -= mutation_size
		# missing! make sure it doesn't exceed 1 or goes below 0!!!