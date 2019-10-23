import pygame
import pygame.locals
import pymunk
import pymunk.pygame_util

pygame.init()
screen = pygame.display.set_mode((1000, 500))

space = pymunk.Space()      # Create a Space which contain the simulation
space.gravity = 0, 0    # Set its gravity



class Main:

    def __init__(self):
        while True:
           ev = pygame.event.poll()
           if ev.type == pygame.QUIT:
               pygame.quit()
           elif ev.type == pygame.KEYDOWN:
               if ev.key == pygame.locals.K_UP:
                   ball.body.apply_impulse_at_local_point((0, 1))
               elif ev.key == pygame.locals.K_DOWN:
                   ball.body.apply_impulse_at_local_point((0, -1))
               elif ev.key == pygame.locals.K_LEFT:
                   ball.body.apply_impulse_at_local_point((-1, 0))
               elif ev.key == pygame.locals.K_RIGHT:
                   ball.body.apply_impulse_at_local_point((1, 0))

           space.step(0.02)        # Step the simulation one step forward
           self.draw()


    def draw(self):
        screen.fill((255, 255, 0))
        # for obj in objects:
        #     obj.update()
        #     obj.draw()

        draw_options = pymunk.pygame_util.DrawOptions(screen)
        space.debug_draw(draw_options)
        pygame.display.flip()


class Mover:

    def __init__(self, x, y):
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()

        self.moment = pymunk.moment_for_circle(1, 0, 30)
        self.body = pymunk.Body(1, self.moment)
        self.body.position = self.pos

        self.shape = pymunk.Circle(self.body, 30)
        space.add(self.body, self.shape)


    def update(self):
        self.pos = pymunk.pygame_util.to_pygame(self.body.position, screen)
        self.pos = pygame.math.Vector2(self.pos[0], self.pos[1])


    def move(self):
        pass


    def draw(self):
        pygame.draw.circle(screen, (0, 0, 0), (int(self.pos.x),
                                               int(self.pos.y)), 30)

# temporary obstacle setup
line_body = pymunk.Body(body_type=pymunk.Body.STATIC)
line_body.position = (0, 200)

line_shape = pymunk.Segment(line_body, (0, 0), (400, -200), 10)
space.add(line_shape)


ball = Mover(50, 250)
objects = [ball]
game = Main()
