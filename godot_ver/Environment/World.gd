extends Node2D

var Food = preload("Food.tscn")

func _unhandled_input(event):
	"""Just a temporary func here, this file will handle other stuff later
	"""
	if event is InputEventMouseButton:
		if event.button_index == 1 and event.is_pressed():
			var new_food = Food.instance()

			new_food.set_global_position(get_global_mouse_position())
			add_child(new_food)