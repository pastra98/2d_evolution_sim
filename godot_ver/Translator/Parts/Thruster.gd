extends Node2D

var angle: float
var min_angle: float
var max_angle: float

var arc: float
var strength: float

# debugging vars, fix this shit
var draw_angle: float
var update_draw = false

func _init(attach_point, angle, arc, strength):
	self.position = attach_point 
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
	_draw()
 
 
func get_movement_efficiency(target_angle):
	update_draw = false
	var projection = 0
	# make this func also return which angle to use!!!
	if target_angle > (angle - arc/2) and target_angle < (angle + arc/2):
		update_draw = true
		draw_angle = target_angle
		update()
		return 1 # Max efficiency
	for p_angle in [min_angle, max_angle]:
		if (target_angle * p_angle) < 0: # signs don't match
			# Project a on target by summing absolute dist. of both angles to PI
			if cos(TAU - abs(target_angle) - abs(p_angle)) > projection:
				projection = cos(TAU - abs(target_angle) - abs(p_angle))
		elif cos(target_angle - p_angle) > projection:
			projection = cos(target_angle - p_angle)
	return projection 


func _draw():
	draw_line(position, position + Vector2(20,0).rotated(angle - arc/2), Color.white, 3)
	draw_line(position, position + Vector2(20,0).rotated(angle + arc/2), Color.white, 3)
	if update_draw:
		draw_line(position, Vector2(60,0).rotated(draw_angle), Color.yellow, 5)