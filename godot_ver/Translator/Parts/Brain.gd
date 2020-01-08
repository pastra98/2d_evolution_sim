extends Node2D

var closest_food
var rng = RandomNumberGenerator.new()
var next_random_choice = 1

onready var sensor = get_node("../Sensor") # make this defined procedurally
onready var thruster_system = get_node("../ThrusterSystem")

func update_state():
	closest_food = find_closest_food()
	if typeof(closest_food) == TYPE_VECTOR2:
		thruster_system.target = closest_food

 
func find_closest_food():
	var areas = sensor.get_overlapping_areas()
	var min_distance = sensor.sensor_shape.radius
	var closest_food
	
	for area in areas:
		if area.is_in_group("food"):
			var distance = global_position.distance_to(area.global_position)
			if distance < min_distance:
				min_distance = distance
				closest_food = area
	if typeof(closest_food) != TYPE_NIL:
		return closest_food.global_position
	# if no food is found pick random target and don't change until end of counter	
	next_random_choice -= 1
	if next_random_choice < 0:
		next_random_choice = 20
		rng.randomize()
		var rand_x = rng.randi_range(-800, 800)
		var rand_y = rng.randi_range(-800, 800)
		print("random location")
		return global_position + Vector2(rand_x, rand_y)