from genes import Genome
from creatures import Creature

import pygame
import pymunk
import pygame.locals

# initializing pygame world
pygame.init()
screen = pygame.display.set_mode((1000, 500))

# initializing Physics world
space = pymunk.Space()
space.gravity = 0, 0

# defining genome and genes of creature
karl_genome = Genome()
karl_genome.append_gene("shape", [0.2, 0.4, 0.8, 1, 1, 0.7, 0.5, 0.2])
karl_genome.append_gene("width", 100)
karl_genome.append_gene("length", 400)
karl_genome.append_gene("thrusters", [[]])

# creating creature with given genome
karl = Creature(karl_genome)

karl_points = karl.build_phenotype()
print(karl_points)
