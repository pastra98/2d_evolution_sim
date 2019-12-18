extends "Gene.gd"

var expression_zones

func _init(expression_zones, is_dominant: bool, g_name := "ThrusterHox").(is_dominant, g_name):
	self.expression_zones = expression_zones

func is_expressed(scaled_value: float):
	return expression_zones.check_expression_zones(scaled_value)