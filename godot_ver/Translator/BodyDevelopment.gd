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
	for i in range(points.size() / 2): # No list slicing 🙁
		var scaled = (points[i].x + length/2) / length # position relative to length
		if thruster_hox.is_expressed(scaled):
			make_thruster_pair(i, scaled, TS_path)


func make_thruster_pair(point_index: int, scaled: float, TS_path: String):
	var angle_gene = dna["ThrusterAngle"]
	var strength_gene = dna["ThrusterStrength"]

	# extracting genetic information for angle and strength based on position
	var decimal = stepify(scaled, 0.1) * 10
	var angle = angle_gene.get_angle(decimal)
	var strength = max_thruster_strength * strength_gene.get_strength(decimal)

	# limits of the thrusting radius
	var thrust_radius = 45
	var start_vec = Vector2(1, 0).rotated(deg2rad(angle - thrust_radius/2))
	var end_vec = Vector2(1, 0).rotated(deg2rad(angle + thrust_radius/2))

	# creature shape left and right of the specified point
	var front_vec = (points[point_index - 1] - points[point_index]).normalized()
	var back_vec = (points[point_index + 1] - points[point_index]).normalized()

	# make sure thrust angle is outside of creature body
	if start_vec.y < back_vec.y:
		start_vec = back_vec
	if end_vec.y < front_vec.y:
		end_vec = front_vec
	
	# Instance two thrusters
	var u_point = points[point_index]
	var l_point = Vector2(u_point.x, u_point.y * -1)

	var upper_thruster = Thruster.new(u_point, start_vec, end_vec, strength)
	get_node(TS_path).thrusters.append(upper_thruster)
	get_node(TS_path).add_child(upper_thruster)

	start_vec.y *= -1 # mirror along y axis
	end_vec.y *= -1 # mirror along y axis
	var lower_thruster = Thruster.new(l_point, start_vec, end_vec, strength)
	get_node(TS_path).thrusters.append(lower_thruster)
	get_node(TS_path).add_child(lower_thruster)
	get_node(TS_path)._draw()