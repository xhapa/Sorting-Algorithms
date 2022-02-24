import pygame
from pygame.locals import *
import random
from slicer import Slicer

pygame.display.set_caption('Sorting Algorithms')
pygame.font.init()
WIDTH, HEIGHT = 1000, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
image = pygame.image.load('messi.jpg')
SCREEN.blit(image,(0,0))
print(image.get_height(), type(image.get_height()))
col_order = [x for x in range(image.get_height())]
random.shuffle(col_order)
print(col_order)

def draw(slicer):
    slicer.draw_slices(SCREEN)
    pygame.display.update()

def main():
    pygame.init()
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(FPS)
        pixel = pygame.PixelArray(image)
        sli = Slicer(image.get_height(), pixel, col_order)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        draw(sli)
        col_order.sort()
    main()

if __name__=='__main__':
    main()