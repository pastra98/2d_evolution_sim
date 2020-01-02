extends RigidBody2D

var time = 0

func _ready():
	add_torque(25.0)


func _process(delta):
	time += delta
	if time > 1:
		print(transform.get_rotation())
		time = 0
 

func _draw():
	"""This function will be shifted to a seperate drawer node, specified
	in the dna.
	"""
	draw_line(Vector2(0, -30), Vector2(0, 30), Color.red, 10)


# func _input(event):
	# """Just a temporary func here, this file will handle other stuff later
	# """
	# if event.is_key_pressed(KEY_W):
		# print("hi")
	# var vec = Vector2(1,0)
	# print(vec.rotated(deg2rad(180)))
	# print(deg2rad(90))