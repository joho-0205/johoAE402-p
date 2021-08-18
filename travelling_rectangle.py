import time

import pygame
import random
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
pygame.init()
size = (500,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Travelling Rectangle")
done = False
clock = pygame.time.Clock()


x = 0
y = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=1
        if x<0:
            x = 0
    elif keys[pygame.K_RIGHT]:
        x+=1
        if x>490:
            x = 490
    elif keys[pygame.K_UP]:
        y-=1
        if y<0:
            y = 0
    elif keys[pygame.K_DOWN]:
        y+=1
        if y>490:
            y = 490
    elif keys[pygame.K_SPACE]:
        time.sleep(0.1)
        x = random.randint(0,500)
        y = random.randint(0,500)
    else:
        pass


    screen.fill(WHITE)
    pygame.draw.rect(screen,RED,[x,y,10,10])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()