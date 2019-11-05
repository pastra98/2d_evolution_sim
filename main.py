from genes import Genome
from creatures import Creature

import pygame
import pymunk.pygame_util
import pymunk
import pygame.locals

# initializing pygame world
pygame.init()
screen = pygame.display.set_mode((1000, 500))

# initializing Physics world
space = pymunk.Space()
space.gravity = 0, -0.7

# defining genome and genes of creature
karl_genome = Genome()
karl_genome.append_gene("shape", [0.2, 0.6, 0.8, 1, 0.9, 0.7, 0.6, 0.2])
karl_genome.append_gene("width", 50)
karl_genome.append_gene("length", 200)

# todo: implement mirroring for thruster gene
karl_genome.append_gene("thrusters", [[1,0], [2,0], [4,0], [5,0]])

# creating creature with given genome
karl = Creature(karl_genome)
karl.build_phenotype()
space.add(karl.body, karl.shape)


# Main loop
game_running = True
while game_running:
   ev = pygame.event.poll()
   if ev.type == pygame.QUIT:
       pygame.quit()

   screen.fill((255, 255, 255))
   draw_options = pymunk.pygame_util.DrawOptions(screen)
   space.debug_draw(draw_options)
   space.step(0.02)
   pygame.display.flip()
