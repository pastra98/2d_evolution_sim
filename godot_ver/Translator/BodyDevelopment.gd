extends Node

var ThrusterSystem = preload("res://Translator/Parts/ThrusterSystem.tscn")
var Thruster = preload("res://Translator/Parts/Thruster.gd")

var dna
var data
var creature_path
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
	points.clear()
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
	for i in range(points.size() / 2): # No list slicing  
		var scaled = (points[i].x + length/2) / length # position relative to length
		if thruster_hox.is_expressed(scaled):
			make_thruster_pair(i, scaled, TS_path)


func make_thruster_pair(point_index: int, scaled: float, TS_path: String):
	var angle_gene = dna["ThrusterAngle"]
	var strength_gene = dna["ThrusterStrength"]

	# extracting genetic information for angle and strength based on position
	var decimal = stepify(scaled, 0.1) * 10 # Make usable as array index
	var angle = angle_gene.get_angle(decimal)
	var strength = max_thruster_strength * strength_gene.get_strength(decimal)

	# THIS NEEDS TO BE CALCULATED BASED ON STRENGTH
	var arc = PI / 3

	# creature shape left and right of the specified point
	# var front_angle = (points[point_index + 1] - points[point_index]).angle()
	# var back_angle = (points[point_index - 1] - points[point_index]).angle()

	# make sure thrust angle is outside of creature body
	# if angle + arc/2 > front_angle:
		# angle = front_angle
	# if angle - arc/2 < back_angle:
		# angle = back_angle
	
	# Instance two thrusters
	var point = points[point_index]

	var upper_thruster = Thruster.new(point, angle, arc, strength)
	get_node(TS_path).add_child(upper_thruster)

	var lower_thruster = Thruster.new(point*Vector2(1,-1), -angle, arc, strength)
	get_node(TS_path).add_child(lower_thruster)