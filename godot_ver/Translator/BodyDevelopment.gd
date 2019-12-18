extends Node

var dna
var data
var creature_path
var ThrusterSystem = preload("res://Translator/Parts/ThrusterSystem.tscn")
var Thruster = preload("res://Translator/Parts/Thruster.gd")
var points = Array()
var length
var max_thruster_strength = 10

func translate():
	self.dna = get_parent().dna
	self.data = get_parent().temp_data
	self.creature_path = get_parent().creature_path
	body_shape()
	appendage_development()


func body_shape():
	var shape = dna["shape"].dimensions
	var width = dna["width"].width
	self.length = dna["length"].length
	
	var vertebra = length / (shape.size() - 1) # distance between each vert.
	var spine = -(length/2) # x_value of first vert

	for p in shape:
	    points.append(Vector2(spine, p * width))
	    spine += vertebra
	var reversed = points.duplicate() # no reverse iterator in gdscript ):
	reversed.invert() # also doesn't like multiple method calls in one line
	for p in reversed:
	    points.append(Vector2(p[0], -p[1])) # revert y coord of point -> bottom
	
	get_node(creature_path).points = PoolVector2Array(points)


func appendage_development():
	# make a new thruster system
	var thruster_system = ThrusterSystem.instance()
	get_node(creature_path).add_child(thruster_system)
	var TS_path = str(creature_path) + "/ThrusterSystem"

	# thruster hox gene decides where thrusters will develop
	var thruster_hox = dna["ThrusterHox"]
	for i in range(points.size() / 2): # No list slicing ):
		var scaled = (points[i].x + length/2) / length # position relative to length
		if thruster_hox.is_expressed(scaled):
			make_thruster_pair(i, scaled)


func make_thruster_pair(point_index: int, scaled: float):
	var angle_gene = dna["ThrusterAngle"]
	var strength_gene = dna["ThrusterStrength"]

	var decimal = stepify(scaled, 0.1) * 10
	var angle = angle_gene.get_angle(decimal)
	var strength = max_thruster_strength * strength_gene.get_strength(decimal)

	print(point_index)
	# print(decimal)
	# print(angle)
	# print(strength)
	# divide angle by strength

	if point_index == 0:
		pass # don't limit the start angle, because it's the first point
	elif point_index == points.size() - 1: # check if that is correct!
		pass # don't limit the end angle, because it's the last point
	else:
		pass
	
	var front_vec = points[point_index - 1] - points[point_index]
	var back_vec = points[point_index + 1] - points[point_index]
	print("front_vec %s" % rad2deg(front_vec.angle()))
	print("back_vec %s" % rad2deg(back_vec.angle()))