extends Node

func _init(is_dominant: bool, name: String):
	self.name = name
	self.is_dominant = is_dominant

"""Common functions for mutation and such are overwritten by the inherited
gene types.
"""