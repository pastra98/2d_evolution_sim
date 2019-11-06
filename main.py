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
space.gravity = 0, -0.07
# space.damping = 0.8 # basically global friction for every body

# defining genome and genes of creature
karl_genome = Genome()
karl_genome.append_gene("shape",[0.2, 0.6, 0.8, 1, 0.9, 0.7, 0.6, 0.2])
karl_genome.append_gene("width",50)
karl_genome.append_gene("length",200)

# todo: implement mirroring for thruster gene
# thruster[1] (startAngle): 270<topvec>45 / 225>botvec>90
karl_genome.append_gene("thrusters", [[0, 0], [1, 45],
                                      [14, 90], [15, 180]])

# creating creature with given genome
karl = Creature(karl_genome)
karl.build_phenotype()
space.add(karl.body, karl.shape)

# collection of turning instructions
forward = [[1,45], [2,0]]
left = [[0,0]]
right = [[3,180]]

# temporary obstacle setup
line_moment = pymunk.moment_for_segment(0, (0, 0), (600, 300), 10)
line_body = pymunk.Body(10, line_moment, body_type=pymunk.Body.STATIC)
line_body.position = (350, -50)

line_shape = pymunk.Segment(line_body, (0, 0), (600, 300), 10)
space.add(line_shape)

# Main loop
game_running = True
while game_running:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()
    # move based on key input
    elif ev.type == pygame.KEYDOWN:
        if ev.key == pygame.locals.K_UP:
            karl.update_directions(forward)
            karl.apply_thrust([1, 2])
        elif ev.key == pygame.locals.K_LEFT:
            karl.update_directions(left)
            karl.apply_thrust([0])
        elif ev.key == pygame.locals.K_RIGHT:
            karl.update_directions(right)
            karl.apply_thrust([3])

    screen.fill((255, 255, 255))
    draw_options = pymunk.pygame_util.DrawOptions(screen)
    space.debug_draw(draw_options)
    space.step(0.02)
    pygame.display.flip()
