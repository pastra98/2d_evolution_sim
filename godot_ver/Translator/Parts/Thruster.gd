extends Node2D

var attach_point: Vector2
var angle: float
var min_angle: float
var max_angle: float
var arc: float
var strength: float

var start_vec_draw: Vector2
var end_vec_draw: Vector2

func _init(attach_point, angle, arc, strength):
	self.attach_point = attach_point 
	self.strength = strength
	self.angle = angle
	self.arc = arc

	var arc_limits = []
	for a in [angle + arc/2, angle - arc/2]:
		if a > PI:
			a = -TAU + a
		elif a < -PI:
			a = TAU + a
		arc_limits.append(a)
	self.min_angle = arc_limits[0]
	self.max_angle = arc_limits[1]

	self.start_vec_draw = attach_point + Vector2(20,0).rotated(angle - arc/2)
	self.end_vec_draw = attach_point + Vector2(20,0).rotated(angle + arc/2)
 
 
func get_movement_efficiency(target_angle):
	var projection = 0
	# make this func also return which angle to use!!!
	if target_angle > (angle - arc/2) and target_angle < (angle + arc/2):
		return 1 # Max efficiency
	for p_angle in [min_angle, max_angle]:
		if (target_angle * p_angle) < 0: # signs don't match
			# Project a on target by summing absolute dist. of both angles to PI
			if cos(TAU - abs(target_angle) - abs(p_angle)) > projection:
				projection = cos(TAU - abs(target_angle) - abs(p_angle))
		elif cos(target_angle - p_angle) > projection:
			projection = cos(target_angle - p_angle)
	return projection 