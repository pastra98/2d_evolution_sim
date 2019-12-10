extends Node2D

func _ready():
	pass # Replace with function body.

func _draw():
	draw_colored_polygon(get_parent().points, Color(0.709804, 0.176471, 0.176471))

func _process(delta):
	update()
