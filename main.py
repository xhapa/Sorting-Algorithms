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

col_order = [x for x in range(image.get_height())]
random.shuffle(col_order)

def burble_sort(lst, slicer):
  n = len(lst)
  for i in range(n): # n steps
    for j in range(0,n-i-1): # n-i-1 steps
      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
        draw(slicer)
  return lst

def insertion_sort(lst, slicer):
  n = len(lst)
  for i in range(1,n): # n-1 steps
    key = lst[i]
    actual_pos = i - 1
    while actual_pos >= 0 and lst[actual_pos] > key: # n steps 
      lst[actual_pos + 1] = lst[actual_pos]
      actual_pos-=1
    lst[actual_pos + 1] = key
    draw(slicer)
  return lst


def draw_screen():
    SCREEN.blit(image,(0,0))
    pygame.display.update()

def draw(slicer):
    slicer.draw_slices(SCREEN)
    pygame.display.update()

def main():
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    draw_screen()

    while running:
        clock.tick(FPS)
        pixel = pygame.PixelArray(image)
        sli = Slicer(image.get_height(), pixel, col_order)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        draw(sli)
        insertion_sort(col_order, sli)
    main()

if __name__=='__main__':
    main()