extends Node

var Food = preload("Food.tscn")

func _input(event):
	if event is InputEventMouseButton:
		if event.button_index == 1 and event.is_pressed():
			var new_food = Food.instance()
			new_food.set_global_position(event.position)
			add_child(new_food)