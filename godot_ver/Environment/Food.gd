extends Area2D
var time = 0

func _ready():
	self.connect("body_entered", self, "self_destruct")


func self_destruct(body):
	queue_free()