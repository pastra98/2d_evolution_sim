extends Node

var is_dominant
var g_name

func _init(is_dominant: bool, g_name: String):
	self.is_dominant = is_dominant
	self.g_name = g_name


"""Common functions for mutation and such are overwritten by the inherited
gene types.
"""