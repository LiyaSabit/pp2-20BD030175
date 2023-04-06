import pygame
from datetime import datetime
import math

WIDTH = 800
HEIGHT = 1000

pygame.init()

t = datetime.now()

angs = -(int(t.strftime("%S"))*6) - 6
angm = -(int(t.strftime("%M"))*6 + (int(t.strftime("%S"))*6 /60) ) + 30

background = pygame.image.load('main-clock.png')
left = pygame.image.load('left-hand.png')
right = pygame.image.load('right-hand.png')

seconds = pygame.Surface((WIDTH-200,HEIGHT/2-300), pygame.SRCALPHA)
seconds.blit(left, (0, 0))
newsec = seconds
recs = seconds.get_rect(center=(WIDTH//2, HEIGHT//2))

minutes = pygame.Surface((WIDTH,HEIGHT//3-200), pygame.SRCALPHA)
minutes.blit(right, (0, 0))
newmin = minutes
recm = minutes.get_rect(center=(WIDTH//2, HEIGHT//2))

def rotate(image, rect, angle):
    newim = pygame.transform.rotate(image, angle)
    rect = newim.get_rect(center=rect.center)
    return newim, rect

screen = pygame.display.set_mode((WIDTH,HEIGHT))
done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background,(0, 40))
    screen.blit(seconds,recs)   
    screen.blit(minutes,recm)

    seconds, recs = rotate(newsec, recs, angs)
    minutes, recm = rotate(newmin, recm, angm)

    angs -= 0.099 
    angm -= 0.099/60

    pygame.display.flip()
