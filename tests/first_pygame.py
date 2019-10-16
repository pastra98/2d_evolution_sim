import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 500))

class Main:

    def __init__(self):
        while True:
           ev = pygame.event.poll()
           if ev.type == pygame.QUIT:
               pygame.quit()
           # game logic, maybe update function

           self.draw()


    def draw(self):
        screen.fill((255, 0, 0))
        for obj in objects:
            obj.update()
            obj.draw()

        pygame.display.flip()


class Mover:

    def __init__(self, x, y):
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.acc = pygame.math.Vector2(0.001, 0)


    def update(self):
        self.vel += self.acc
        self.pos += self.vel


    def draw(self):
        pygame.draw.circle(screen, (0, 0, 0), (int(self.pos.x),
                                               int(self.pos.y)), 30)




ball = Mover(50, 50)
objects = [ball]
game = Main()
