extends Node

var genome = preload("res://Genome/Genome.gd")

var length = load("res://Genome/CodingGenes/Length.gd").new(200, true)
var width = load("res://Genome/CodingGenes/Width.gd").new(50, true)
var shape = load("res://Genome/CodingGenes/Shape.gd").new([0.3, 0.6, 0.4, 0.3], true)

var t_hox_switch = load("res://Genome/Switches/ExpressionZones.gd").new([[0.2,0.4], [0.6,0.8]])
var thruster_hox = load("res://Genome/CodingGenes/ThrusterHox.gd").new(t_hox_switch, true)

var t_angle_switch_prefab = preload("res://Genome/Switches/ExpressionGradient.gd")
var t_angle_switch = t_angle_switch_prefab.new([0,0,0,0.9,0,0,0,0.2,0,0,0])
var thruster_angle = load("res://Genome/CodingGenes/ThrusterAngle.gd").new(t_angle_switch, true)

var t_strength_switch_prefab = preload("res://Genome/Switches/ExpressionGradient.gd")
var t_strength_switch = t_strength_switch_prefab.new([0,0,0,0.1,0,0,0,0.1,0,0,0])
var thruster_strength = load("res://Genome/CodingGenes/ThrusterStrength.gd").new(t_strength_switch, true)

func _ready():
    get_node("Button").connect("pressed", self, "_on_Button_pressed")

func _on_Button_pressed():
	var c_genome = genome.new()
	c_genome.append_genes([length, width, shape, thruster_hox, thruster_angle, thruster_strength])
	GenotypeManager.new_creature(c_genome.dna, Vector2(0,0))