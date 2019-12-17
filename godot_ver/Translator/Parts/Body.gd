extends RigidBody2D

var points = PoolVector2Array([Vector2(100,0),
							   Vector2(0,0),
							   Vector2(0,100)])

var collider = ConvexPolygonShape2D.new()
var shape_owner

func _ready():
	collider.set_point_cloud(points)
	self.create_shape_owner(shape_owner)
	self.shape_owner_add_shape(0, collider)
