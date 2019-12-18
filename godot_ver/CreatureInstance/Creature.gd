extends RigidBody2D

onready var brain = $"Brain"

var pos: Vector2
var id: String
var points: PoolVector2Array
var collider = ConvexPolygonShape2D.new()
var shape_owner

func _ready():
	set_global_position(self.pos)
	collider.set_point_cloud(points)
	self.create_shape_owner(shape_owner)
	self.shape_owner_add_shape(0, collider)


func _process(delta):
	"""Framerate-based update func.
	"""
	update()
	# if Input.is_action_pressed("ui_up"):
		# get_node("ThrusterSystem").move("forward")
	# if Input.is_action_pressed("ui_down"):
		# get_node("ThrusterSystem").move("back")
	# if Input.is_action_pressed("ui_left"):
		# get_node("ThrusterSystem").move("left")
	# if Input.is_action_pressed("ui_right"):
		# get_node("ThrusterSystem").move("right")
	# if Input.is_action_pressed("ui_down"):
		# get_node("ThrusterSystem").hello()
	# brain.update()


func _draw():
	"""This function will be shifted to a seperate drawer node, specified
	in the dna.
	"""
	draw_colored_polygon(points, Color(0.709804, 0.176471, 0.176471))
