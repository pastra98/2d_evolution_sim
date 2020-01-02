extends Node2D

var test: Vector2
var thrusters: Array # thrusters are already child, maybe change this?
var target: Vector2
var time = 0
 

func _process(delta):
	"""Movement update method could be called here or in update method
	that gets called by brain, such that it only updates, when brain
	updates.
	"""
	time += delta
	if time > 1:
		var impulse = calculate_desired_impulse()
		print(impulse)
		# movement_decision(impulse)
		time = 0


func _draw():
	for t in thrusters:
		draw_line(t.attach_point, t.start_vec_draw, Color.blue, 5)
		draw_line(t.attach_point, t.end_vec_draw, Color.green, 5)


func calculate_desired_impulse():
	"""takes target position, calculates vector from creature to target,
	normalizes this vector, and transforms it to allow comparing it to thruster
	vectors. 
	"""
	var desired_impulse = get_global_position() - target
	# desired_impulse = desired_impulse.normalized()
	# desired_impulse = desired_impulse.rotated(transform.get_rotation()) * -1
	# return desired_impulse
	return rad2deg(desired_impulse.angle())


func movement_decision(impulse: Vector2):
	var some_list = []

	for thruster in thrusters:
		some_list.append(thruster.get_movement_efficiency(impulse))
	
	# print(get_global_position() - target)
	# print(impulse)
	print(some_list)