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
	"""Framerate-based update func.
	"""
	time += delta
	if time > 1:
		$Brain.update()
		time = 0


func _draw():
	"""This function will be shifted to a seperate drawer node, specified
	in the dna.
	"""
	draw_colored_polygon(points, Color(0.709804, 0.176471, 0.176471))
