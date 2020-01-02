extends Node2D

var nearest_food
var pos: Vector2
onready var sensor = get_node("../Sensor")
onready var thruster_system = get_node("../ThrusterSystem")

func update():
	pos = get_global_position()
	
	nearest_food = find_nearest_food()
	if typeof(nearest_food) == TYPE_VECTOR2:
		thruster_system.target = nearest_food

 
func find_nearest_food():
	# make this function nicer pls
	var areas = sensor.get_overlapping_areas()
	var sorted_areas = []
	for area in areas:
		if area.is_in_group("food"):
			sorted_areas.append([pos.distance_to(area.get_global_position()), area])
	if not sorted_areas.empty():
		return sorted_areas.min()[1].get_global_position()