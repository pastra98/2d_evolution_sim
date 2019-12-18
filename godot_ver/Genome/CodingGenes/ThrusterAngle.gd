extends "Gene.gd"

var expression_gradient

func _init (gradient, is_dominant: bool, g_name := "ThrusterAngle").(is_dominant, g_name):
	self.expression_gradient = gradient


func get_angle(decimal: int):
	"""Returns an angle ranging from 0 to 180 depending on the position
	of the calling segment. This position is expressed as an int ranging from
	0 to 11, and is the parameter for decimal.
	"""
	var gradient = expression_gradient.get_gradient(decimal)
	return 180 * gradient