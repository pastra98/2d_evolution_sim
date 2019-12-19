extends Node2D

var attach_point: Vector2
var start_vec: Vector2
var end_vec: Vector2
var strength: float

var start_vec_draw: Vector2
var end_vec_draw: Vector2

func _init(attach_point, start_vec, end_vec, strength):
	self.attach_point = attach_point 
	self.start_vec = start_vec
	self.end_vec = end_vec
	self.strength = strength

	self.start_vec_draw = attach_point + start_vec * strength * 10
	self.end_vec_draw = attach_point + end_vec * strength * 10


func _draw():
	draw_line(attach_point, start_vec_draw, Color.blue, 5)
	draw_line(attach_point, end_vec_draw, Color.green, 5)