extends Node2D

var test: Vector2
var thrusters: Array # thrusters are already child, maybe change this?
var target: Vector2
var time = 0
 
var desired_direction: Vector2
var target_vector = target - position

func update_movement():
	var desired_angle = desired_ocs_impulse_angle()
	movement_decision(desired_angle)

	desired_direction = Vector2(80,0).rotated(desired_angle)
	target_vector = target - global_position
	print(target, position)
	update()


func _draw():
	draw_line(Vector2(0,0), desired_direction, Color.white, 2)
	draw_line(Vector2(0,0), target_vector, Color.yellow, 2)
	for t in thrusters:
		draw_line(t.attach_point, t.start_vec_draw, Color.blue, 5)
		draw_line(t.attach_point, t.end_vec_draw, Color.green, 5)
		pass


func desired_ocs_impulse_angle():
	"""I fucking hate angles so much. Worst code ever.
	"""
	var desired_impulse = target - global_position 
	var creature_rotation = get_node("..").rotation
	desired_impulse = desired_impulse.rotated(-creature_rotation)
	# desired_impulse = desired_impulse * -1
	return desired_impulse.angle_to(Vector2(-1,0))


func movement_decision(desired_angle):
	var some_list = []

	for thruster in thrusters:
		if thruster.get_movement_efficiency(desired_angle) > 0.9:
			var imp_pos = thruster.attach_point
			var imp_vec = Vector2(5,0).rotated(desired_angle) * -1
			get_parent().apply_impulse(imp_pos, imp_vec)