from genes import Genome
from genes import Gene
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
space.gravity = 0, 0
space.damping = 0.95 # basically global friction for every body

# defining genome and genes of creature
karl_genome = Genome()
shape_gene = Gene("shape", [0.4, 0.8, 0.7, 0.3])
width_gene = Gene("width", 50)
length_gene = Gene("length", 200)
thr1_gene = Gene("thruster", [1, True, 0, 90])
thr2_gene = Gene("thruster", [3, True, 90, 180])
karl_genepool = [shape_gene, width_gene, length_gene, thr1_gene, thr2_gene]
# adding genes to karl
karl_genome.append_genes(karl_genepool)

# creating creature with given genome
karl = Creature(karl_genome)
karl.birth()
space.add(karl.body, karl.shape)

# temporary obstacle setup
line_moment = pymunk.moment_for_segment(0, (0, 0), (500, 300), 10)
line_body = pymunk.Body(10, line_moment, body_type=pymunk.Body.STATIC)
line_body.position = (350, -80)

line_shape = pymunk.Segment(line_body, (0, 0), (500, 300), 10)
space.add(line_shape, line_body)

# Main loop
game_running = True
while game_running:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    # move based on key input
    elif ev.type == pygame.KEYDOWN:
        if ev.key == pygame.locals.K_w:
            karl.thruster_sys.move("forward")
        elif ev.key == pygame.locals.K_s:
            karl.thruster_sys.move("backward")
        elif ev.key == pygame.locals.K_a:
            karl.thruster_sys.move("left")
        elif ev.key == pygame.locals.K_d:
            karl.thruster_sys.move("right")
        elif ev.key == pygame.locals.K_q:
            karl.thruster_sys.turn("left")
        elif ev.key == pygame.locals.K_e:
            karl.thruster_sys.turn("right")

    screen.fill((255, 255, 255))
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    space.debug_draw(draw_options)
    space.step(0.02)
    pygame.display.flip()
