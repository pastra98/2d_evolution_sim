extends Node2D

var angle # removed typing because receiving ints is also possible.
var min_angle
var max_angle

var arc
var strength
var exceeds_pi = false

var update_draw = false
var current_angle: float
onready var body = get_node("../..")

func _init(attach_point, angle, arc, strength):
	self.position = attach_point
	self.strength = strength
	self.angle = angle
	self.arc = arc

	var arc_limits = []
	for a in [angle - arc/2, angle + arc/2]:
		if a > PI:
			a = -TAU + a
		elif a < -PI:
			a = TAU + a
		arc_limits.append(a)
	self.min_angle = arc_limits[0]
	self.max_angle = arc_limits[1]
	if min_angle > max_angle:
		exceeds_pi = true
	_draw()
 
 
func get_movement_efficiency(target_angle):
	var projection = 0
	# make this func also return which angle to use!!!
	# this can be vastly improved
	current_angle = target_angle
	if target_angle > min_angle:
		if exceeds_pi:
			return 1
		elif target_angle < max_angle:
			return 1
	elif exceeds_pi and target_angle < max_angle:
		return 1

	for p_angle in [min_angle, max_angle]:
		if (target_angle * p_angle) < 0: # signs don't match
			# Project a on target by summing absolute dist. of both angles to PI
			if cos(TAU - abs(target_angle) - abs(p_angle)) > projection:
				projection = cos(TAU - abs(target_angle) - abs(p_angle))
		elif cos(target_angle - p_angle) > projection:
			projection = cos(target_angle - p_angle)
	return projection 


func apply_thrust():
	var impulse = Vector2(5, 0).rotated(current_angle + global_rotation) 
	# uses graphics coords for some reason (inverted y)
	body.apply_impulse(position * Vector2(-1, 1), impulse * Vector2(-1, 1))
	update_draw = true
	update()


func _draw():
	draw_line(Vector2(0, 0), Vector2(20,0).rotated(min_angle), Color.white, 3)
	draw_line(Vector2(0, 0), Vector2(20,0).rotated(max_angle), Color.green, 3)
	if update_draw:
		draw_line(Vector2(0, 0), Vector2(60,0).rotated(current_angle), Color.yellow, 5)