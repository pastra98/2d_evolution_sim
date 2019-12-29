extends Node2D

var thrusters = [] # thrusters are already child, maybe change this?
var target: Vector2
var time = 0 # Should I get rid of this stuff?

func _ready():
	pass
 

func _process(delta):
	"""Movement update method could be called here or in update method
	that gets called by brain, such that it only updates, when brain
	updates.
	"""
	time += delta
	if time > 1:
		print(target)
		var transform = thrusters[0].get_global_transform()
		print(transform.xform(thrusters[0].start_vec))
		time = 0


func _draw():
	for t in thrusters:
		draw_line(t.attach_point, t.start_vec_draw, Color.blue, 5)
		draw_line(t.attach_point, t.end_vec_draw, Color.green, 5)