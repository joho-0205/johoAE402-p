import math

import pygame,time,random
black = (0,0,0)
yellow = (255, 255, 102)
blue = (0, 153, 255)
size = (500,500)
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("畫臉")
done = True
PI = math.pi
tear = []
tear2 = []
for i in range(5):
    x = random.randint(180,205)
    y = random.randint(187,205)
    tear.append([x,y])
for i in range(5):
    x = random.randint(295,325)
    y = random.randint(187,205)
    tear2.append([x,y])
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            tear[i][0] = x
    screen.fill(black)
    pygame.draw.circle(screen,yellow,(250,250),150,1)
    pygame.draw.line(screen,yellow,(250,230),(235,260),1)
    pygame.draw.line(screen, yellow, (235, 260),(265,260), 1)
    pygame.draw.line(screen, yellow, (250, 230), (265, 260), 1)
    pygame.draw.arc(screen, yellow, [180,280,135,135], PI/2,PI, 2)
    pygame.draw.arc(screen, yellow, [180, 280, 135, 135],0, PI/2, 2)
    pygame.draw.circle(screen,yellow,(195,185),10,0)
    pygame.draw.circle(screen, yellow, (310, 185), 10, 0)
    for i in range(len(tear)):
        pygame.draw.circle(screen,blue,tear[i],4,0)
        tear[i][1] +=1
        if tear[i][1]>400:
            y = random.randint(187,205)
            tear[i][1] = y
            x = random.randint(180, 205)
    for i in range(len(tear2)):
        pygame.draw.circle(screen,blue,tear2[i],4,0)
        tear2[i][1] +=1
        if tear2[i][1]>400:
            y = random.randint(187,205)
            tear2[i][1] = y
            x = random.randint(295,325)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()