extends Node

var s_length = load("res://Genome/CodingGenes/Length.gd").new(200, true)
var s_width = load("res://Genome/CodingGenes/Width.gd").new(50, true)
var s_shape = load("res://Genome/CodingGenes/Shape.gd").new([0.2, 0.5, 0.6, 0.3], true)
var genome = preload("res://Genome/Genome.gd")

func _ready():
    get_node("Button").connect("pressed", self, "_on_Button_pressed")

func _on_Button_pressed():
	var s_genome = genome.new()
	s_genome.append_genes([s_length, s_width, s_shape])
	GenotypeManager.new_creature(s_genome.dna, Vector2(150,0))