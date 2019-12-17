extends Node

var dna
var data
var creature_path
var ThrusterSystem = preload("res://Translator/Parts/ThrusterSystem.tscn")
var TS_path: String
var Thruster = preload("res://Translator/Parts/Thruster.gd")

func translate():
	self.dna = get_parent().dna
	self.data = get_parent().temp_data
	self.creature_path = get_parent().creature_path


func body_development():
	calculate_points()
	new_thruster_system()


func calculate_points():
	var shape = dna["shape"].dimensions
	var length = dna["length"].length
	var width = dna["width"].width
	
	var points = Array()
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

 
func new_thruster_system():
	var thruster_system = ThrusterSystem.instance()
	get_node(creature_path).add_child(thruster_system)
	self.TS_path = str(creature_path) + "/ThrusterSystem"
 

func new_thruster(test):
	var thruster = Thruster.new(test)
	get_node(TS_path).thrusters.append(thruster)