import pygame

def update_sim(element):
    element += 1
    return element

def display_sim(element):
    print(element)

pygame.init()
screen = pygame.display.set_mode((1000, 500))

ticks_per_second = 60 # game speed, how often an update is called
skip_ticks = 1000 / ticks_per_second # change this to change gamespeed
max_frameskip = 10 # should be adjusted if gamespeed should change

next_tick = pygame.time.get_ticks()

x = 0
game_running = True

while game_running:
    loops = 0

    while pygame.time.get_ticks() > next_tick and loops < max_frameskip:
        x = update_sim(x)
        next_tick += skip_ticks
        loops += 1

    display_sim(x)


