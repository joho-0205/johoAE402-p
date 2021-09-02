import time

import pygame
white = (255,255,255)
red = (255,0,0)
orange = (242,133,0)
yellow = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
purple = (255,0,255)
sky = (135,206,235)
black = (0,0,0)
color = [red,orange,yellow,green,blue,purple]
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sunrise&Sunset")
done = False
clock = pygame.time.Clock()
x = 100
y = 300
ex = 300
ey = 300
sx = 350
sy = 100
scr_color = sky
count = 0
run = 1
gobl = 0
while not done:
    screen.fill(scr_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for i in range(len(color)):
        if scr_color == sky:
            pygame.draw.arc(screen,color[i],[x-i*10,y-i*10,ex+i*20,ey+i*20],0,3,10)
        else:
            pass
    for i in range(40):
        if 350<=sx<760 and run ==1:
            pygame.draw.circle(screen, yellow, [sx, sy], 60)
            sx += 0.01
            sy += 0.005
        elif 350<=sx<760 and run == 0:
            pygame.draw.circle(screen, white, [sx, sy], 60)
            sx += 0.01
            sy += 0.005
        elif 350>sx>-60:
            pass
        else:
            gobl = 1
            break
    for j in range(40):
        if 350>sx>=-60 and run == 1:
            pygame.draw.circle(screen, yellow, [sx, sy], 60)
            sx += 0.01
            sy -= 0.005
        elif 350>sx>=-60 and run == 0:
            pygame.draw.circle(screen, white, [sx, sy], 60)
            sx += 0.01
            sy -= 0.005
        else:
            pass
    if gobl == 1:
        if count>=2000:
            scr_color = sky
            sx = -60
            count = 0
            run = 1
            gobl = 0
        else:
            scr_color = black
            run = 0
            count = count + 1
            print(count)
    else:
        pass
    pygame.display.flip()
    clock.tick(60)
pygame.quit()