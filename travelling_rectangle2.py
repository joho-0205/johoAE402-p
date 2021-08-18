import time

import pygame
import random
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
pygame.init()
size = (1440,794)
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
        if x>1410:
            x = 1410
    elif keys[pygame.K_UP]:
        y-=1
        if y<0:
            y = 0
    elif keys[pygame.K_DOWN]:
        y+=1
        if y>764:
            y = 764
    elif keys[pygame.K_SPACE]:
        x = random.randint(0,1440)
        y = random.randint(0,794)
    else:
        pass


    screen.fill(WHITE)
    pygame.draw.rect(screen,RED,[x,y,30,30])

    pygame.display.flip()

    clock.tick(60)

    time.sleep(0.001)
pygame.quit()