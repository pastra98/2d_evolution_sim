import pygame
import pymunk
import pymunk.pygame_util
import pygame.locals

pygame.init()
screen = pygame.display.set_mode((1000, 500))

space = pymunk.Space()
space.gravity = 0, -0.07

# triangle creation func, takes position arguments
def create_tri(x, y):
    pos = pygame.math.Vector2(x, y)
    points = (-25, -25), (25, -25), (0, 25)

    moment = pymunk.moment_for_poly(1, points)
    body = pymunk.Body(1, moment)
    body.position = pos

    shape = pymunk.Poly(body, points)
    return body, shape

# creating a triangle
tri2 = create_tri(700, 400)
space.add(tri2[0], tri2[1])

# temporary obstacle setup
line_moment = pymunk.moment_for_segment(0, (0, 0), (600, 300), 10)
line_body = pymunk.Body(10, line_moment, body_type=pymunk.Body.STATIC)
line_body.position = (150, 0)

line_shape = pymunk.Segment(line_body, (0, 0), (600, 300), 10)
space.add(line_shape)

# Main loop
game_running = True
while game_running:
   ev = pygame.event.poll()
   if ev.type == pygame.QUIT:
       pygame.quit()
   elif ev.type == pygame.KEYDOWN:
       if ev.key == pygame.locals.K_UP:
           tri2[0].apply_impulse_at_local_point((0, 1))
       elif ev.key == pygame.locals.K_DOWN:
           tri2[0].apply_impulse_at_local_point((0, -1))
       elif ev.key == pygame.locals.K_LEFT:
           tri2[0].apply_impulse_at_local_point((0.2, 0.5), (0, -25))
       elif ev.key == pygame.locals.K_RIGHT:
           tri2[0].apply_impulse_at_local_point((-0.2, 0.5), (0, -25))
   screen.fill((255, 255, 255))
   draw_options = pymunk.pygame_util.DrawOptions(screen)
   space.debug_draw(draw_options)
   space.step(0.02)
   pygame.display.flip()

#, body_type=pymunk.Body.STATIC
