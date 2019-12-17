import pygame
import pygame.locals
import pymunk
import pymunk.pygame_util

pygame.init()

screen = pygame.display.set_mode((1000, 500))
layer_1 = pygame.Surface((1000, 10000))

# initializing Physics world
space = pymunk.Space()
space.gravity = (0, -10)
space.damping = 0.95 # basically global friction for every body

# temporary obstacle setup
line_moment = pymunk.moment_for_segment(0, (0, 0), (200, 100), 10)
line_body = pymunk.Body(0, line_moment, body_type=pymunk.Body.STATIC)
line_body.position = (0, 0)
line_shape = pymunk.Segment(line_body, (0, 0), (200, 100), 10)
space.add(line_shape)

x = 0
for b in range(20):
    x += 40
    ball_moment = pymunk.moment_for_circle(1, 0, 15)
    ball_body = pymunk.Body(1, ball_moment)
    ball_body.position = (x, 10000)
    ball_shape = pymunk.Circle(ball_body, 15)
    space.add(ball_shape, ball_body)

# a clock
clock = pygame.time.Clock()
dt = 0

# Main loop
game_running = True
camera = pygame.Vector2(0, 0)
while game_running:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        pygame.quit()

    pressed = pygame.key.get_pressed()
    camera_move = pygame.Vector2()
    if pressed[pygame.K_UP]: camera_move += (0, 1)
    elif pressed[pygame.K_LEFT]: camera_move += (1, 0)
    elif pressed[pygame.K_DOWN]: camera_move += (0, -1)
    elif pressed[pygame.K_RIGHT]: camera_move += (-1, 0)
    if camera_move.length() > 0: camera_move.normalize_ip()
    camera += camera_move*(dt/2)

    dt = clock.tick(60)
    space.step(0.02)

    draw_options = pymunk.pygame_util.DrawOptions(layer_1)
    layer_1.fill((255, 255, 255))
    space.debug_draw(draw_options)

    screen.fill((255, 255, 255))
    screen.blit(layer_1, camera)
    pygame.display.flip()
