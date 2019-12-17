extends Node2D

var thrusters = []

func _ready():
	pass 


func move(direction: String):
	if direction == "forward":
		find_thruster(1,0).apply_impulse() #yadaada
	if direction == "back":
		find_thruster(1,0).apply_impulse() #yadaada
	if direction == "left":
		find_thruster(1,0).apply_impulse() #yadaada
	if direction == "right":
		find_thruster(1,0).apply_impulse() #yadaada


func find_thruster(x,y):
	pass