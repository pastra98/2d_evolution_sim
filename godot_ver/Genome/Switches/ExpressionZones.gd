extends Node

var mutation_chance = 0.4
var nz_probability = 0.3
var remove_probability = 0.1
var nz_size = 0.1

var rng = RandomNumberGenerator.new()
var expression_zones = []

func _init(expression_zones: Array):
	"""Expression zone must be an array containing at least one other array
	inside. However the array can't be deeper than that. The nested arrays
	represent zones of gene expression, where the values must range from
	0.0 to 1.0, the first value beeing larger than the second, no more than
	2 floats per array. Arrays must not overlap.
	"""
	self.expression_zones = expression_zones


func check_expression_zones(scaled_value: float):
	for zone in expression_zones:
		if scaled_value >= zone[0] and scaled_value <= zone[1]:
			return true
	return false


func mutate():
	rng.randomize()
	if rng.randf() <= mutation_chance:
		if rng.randf() <= nz_probability:
			new_zone()
		if rng.randf() <= remove_probability:
			remove_zone()


func remove_zone():
	if expression_zones.size() != 0:
		rng.randomize()
		var index = rng.randi_range(0, expression_zones.size() - 1)
		expression_zones.remove(index)


func new_zone():
	rng.randomize()
	var start = rng.randf()
	var end = start + nz_size
	if end > 1: end = 1
	expression_zones.append([start, end])
	merge_intervals()


func merge_intervals():
	expression_zones.sort()
	expression_zones.invert()
	var merged = []

	for higher in expression_zones:
		if not merged:
			merged.append(higher)
		else:
			var lower = merged[-1]
			if higher[0] <= lower[1]:
				var upper_bound = max(lower[1], higher[1])
				merged[-1] = [lower[0], upper_bound]
			else:
				merged.append(higher)
	expression_zones = merged
