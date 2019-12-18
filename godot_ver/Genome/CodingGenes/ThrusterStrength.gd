extends "Gene.gd"

var expression_gradient

func _init (gradient, is_dominant: bool, g_name := "ThrusterStrength").(is_dominant, g_name):
	self.expression_gradient = gradient


func get_strength(decimal: int):
	"""Returns an angle ranging from 0 to 180 depending on the position
	of the calling segment. This position is expressed as an int ranging from
	0 to 11, and is the parameter for decimal.
	"""
	return expression_gradient.get_gradient(decimal)