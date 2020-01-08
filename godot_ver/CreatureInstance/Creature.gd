extends RigidBody2D

var time = 0
var id: String
var points: PoolVector2Array
var collider = ConvexPolygonShape2D.new()
var shape_owner

func _ready():
	collider.set_point_cloud(points)
	var shape_id = create_shape_owner(shape_owner)
	shape_owner_add_shape(shape_id, collider)


func _process(delta):
	"""Framerate-based update method.
	"""
	time += delta
	if time > 0.5:
		$Brain.update_state()
		$ThrusterSystem.update_movement()
		time = 0


func _draw():
	"""This function will be shifted to a seperate drawer node, specified
	in the dna.
	"""
	draw_colored_polygon(points, Color.blue)
