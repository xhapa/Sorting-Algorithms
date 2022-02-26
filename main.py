import pygame
from datetime import datetime
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

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        rv = func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time-initial_time
        print(f'Execution time was {time_elapsed.total_seconds()} seconds')
        return rv
    return wrapper

@execution_time
def burble_sort(lst, slicer):
  n = len(lst)
  for i in range(n): # n steps
    for j in range(0,n-i-1): # n-i-1 steps
      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
        draw(slicer)
  return lst

@execution_time
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

@execution_time
def merge_sort(lst, slicer):
    if len(lst) > 1:
        midle = len(lst)//2
        left_lst = lst[:midle]
        right_lst = lst[midle:]
        print(left_lst, '*'*5, right_lst)

        merge_sort(left_lst, slicer)
        merge_sort(right_lst, slicer)

        i = 0
        j = 0
        # main idx
        k = 0

        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i+=1
            else:
                lst[k] = right_lst[j]
                j+=1

            k+=1

        while i < len(left_lst):
            lst[k] = left_lst[i]
            i+=1
            k+=1

        while j < len(right_lst):
            lst[k] = right_lst[j]
            j+=1
            k+=1

        print(f'Left{left_lst}, Right{right_lst}')
        print(lst)
        print('-'  * 50)
    return lst

def draw_screen():
    SCREEN.fill((255,255,255))
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
        slicer = Slicer(image.get_height(), pixel, col_order)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                burble_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                insertion_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                merge_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                random.shuffle(col_order)
        draw(slicer)
    main()

if __name__=='__main__':
    main()