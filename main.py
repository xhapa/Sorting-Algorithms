import pygame
from datetime import datetime
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

exec_list = []

def execution_time(exec_list, algorithm):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            initial_time = datetime.now()
            rv = func(*args, **kwargs)
            final_time = datetime.now()
            time_elapsed = final_time-initial_time
            print(f'Execution time was {time_elapsed.total_seconds()} seconds')
            exec_list.append((algorithm, time_elapsed.total_seconds()))
            return rv
        return wrapped
    return wrapper

@execution_time(exec_list, 'Burble Sort')
def burble_sort(lst, slicer):
  n = len(lst)
  for i in range(n): # n steps
    for j in range(0,n-i-1): # n-i-1 steps
      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
        draw(slicer)
  return lst

@execution_time(exec_list, 'Insertion Sort')
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

@execution_time(exec_list, 'Merge Sort')
def merge_sort(lst, slicer):
    merge_sort_alg(lst, 0, len(lst)-1, slicer)

def merge_sort_alg(lst, left, right, slicer):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(lst, left, middle, slicer)
        merge_sort_alg(lst, middle+1, right, slicer)
        merge(lst, left, right, middle, slicer)

def merge(lst, left, right, middle, slicer):
    left_part = lst[left: middle+1]
    right_part = lst[middle+1: right+1]

    left_idx, right_idx = 0, 0

    for lst_idx in range(left, right+1):
        if left_idx < len(left_part) and right_idx < len(right_part):
            if left_part[left_idx] <= right_part[right_idx]:
                lst[lst_idx] = left_part[left_idx]
                left_idx+=1
            else:
                lst[lst_idx] = right_part[right_idx]
                right_idx+=1
        elif left_idx < len(left_part):
            lst[lst_idx] = left_part[left_idx]
            left_idx+=1
        else:
            lst[lst_idx] = right_part[right_idx]
            right_idx+=1
    draw(slicer)
    return lst

@execution_time(exec_list, 'Quick Sort')
def quick_sort(lst, slicer):
    quick_sort_alg(lst, 0, len(lst)-1, slicer)

def quick_sort_alg(lst, low, high, slicer):
    if low < high:
        partition_idx = partition(lst, low, high, slicer)
        quick_sort_alg(lst, low, partition_idx - 1, slicer)
        quick_sort_alg(lst, partition_idx + 1, high, slicer)

def partition(lst, low, high, slicer):
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j]<= pivot:
            i+=1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    draw(slicer)
    return i + 1

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
                print(exec_list)
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                burble_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                insertion_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                merge_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                quick_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                random.shuffle(col_order)
        draw(slicer)
    main()

if __name__=='__main__':
    main()