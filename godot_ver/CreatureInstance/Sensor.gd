extends Area2D

var sensor_shape = CircleShape2D.new()
var sensor

func _ready():
	sensor_shape.radius = 200
	var sensor_id = create_shape_owner(sensor)
	shape_owner_add_shape(sensor_id, sensor_shape)
	print(sensor_shape)