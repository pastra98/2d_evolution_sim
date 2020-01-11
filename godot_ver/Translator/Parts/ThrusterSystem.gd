extends Node2D

var test: Vector2
var target: Vector2
var time = 0
 
var desired_direction: Vector2

func update_movement():
	var desired_angle = desired_ocs_impulse_angle()
	movement_decision(desired_angle)
	
	desired_direction = (target - global_position).rotated(-get_parent().rotation)
	update() # update the drawn vectors


func _draw():
	draw_line(Vector2(0,0), desired_direction, Color.yellow, 2)


func desired_ocs_impulse_angle():
	"""I fucking hate angles so much. Worst code ever.
	"""
	var desired_impulse = (target - global_position) * -1
	desired_impulse = desired_impulse.angle_to(Vector2(1,0))
	desired_impulse += get_parent().rotation
	return desired_impulse


func movement_decision(desired_angle):
	var some_list = []
	for thruster in get_children():
		some_list.append(thruster.get_movement_efficiency(desired_angle))
		if thruster.get_movement_efficiency(desired_angle) > 0.7:
			thruster.apply_thrust()