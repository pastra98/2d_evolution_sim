extends Camera2D

var dragging = false

func _input(event):
	if event is InputEventMouseButton and event.button_index == BUTTON_RIGHT:
		dragging = true
		if dragging and !event.pressed:
            dragging = false

	if event is InputEventMouseMotion and dragging:
		position -= event.relative