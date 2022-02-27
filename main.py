import pygame
from datetime import datetime
import random
from slicer import Slicer

pygame.display.set_caption('Sorting Algorithms')
pygame.font.init()
WIDTH, HEIGHT = 1000, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont('meslolgsnf', 20, bold=True, italic=False)
TITLE_FONT = pygame.font.SysFont('meslolgsnf', 40, bold=True, italic=False)
FPS = 60
image = pygame.image.load('img/messi.png')

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
    SCREEN.fill('#090810')
    pygame.draw.circle(SCREEN , '#4431FF', (30,60), 100)
    pygame.draw.circle(SCREEN , '#4431FF', (130,30), 50)
    pygame.draw.circle(SCREEN , '#4431FF', (970,640), 120)
    pygame.draw.circle(SCREEN , '#4431FF', (870,670), 75)
    pygame.draw.circle(SCREEN , '#4431FF', (25,300), 15)
    pygame.draw.circle(SCREEN , '#4431FF', (400,600), 25)
    SCREEN.blit(image,(50,100))
    SCREEN.blit(TITLE_FONT.render('Sorting Algorithms', 1,(255,255,255)),(280, 20))
    SCREEN.blit(FONT.render('Original', 1,(255,255,255)),(200, 500))
    SCREEN.blit(FONT.render('Unsorted', 1,(255,255,255)),(700, 500))
    SCREEN.blit(FONT.render('Burble sort (B) | Insertion sort(I) | Merge sort(M) | Quick sort(Q)', 1,(255,255,255)),(100, 600))
    SCREEN.blit(FONT.render('| Unsort(S) |', 1,(255,255,255)),(420, 630))
    pygame.draw.rect(SCREEN, (255,255,255), pygame.Rect(950, 100, 50, 400))
    pygame.display.update()

def draw(slicer):
    slicer.draw_slices(SCREEN)
    pygame.draw.rect(SCREEN, '#090810', pygame.Rect(950, 100, 50, 400))
    pygame.display.update()

def draw_algo_info(algorithm):
    pygame.draw.rect(SCREEN, '#090810', pygame.Rect(430, 520, 200, 25))
    SCREEN.blit(FONT.render(algorithm, 1,'#F85989'),(430, 520))
    pygame.display.update()

def main():
    pygame.init()
    running = True
    clock = pygame.time.Clock()
    algorithm = 'Wait Please...'
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
                algorithm = 'Burble Sort'
                draw_algo_info(algorithm)
                burble_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                algorithm = 'Insertion Sort'
                draw_algo_info(algorithm)
                insertion_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                algorithm = 'Merge Sort'
                draw_algo_info(algorithm)
                merge_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                algorithm = 'Quick Sort'
                draw_algo_info(algorithm)
                quick_sort(col_order, slicer)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                algorithm = 'Unsort'
                draw_algo_info(algorithm)
                random.shuffle(col_order)
            else:
                algorithm = 'Wait Please...'
        draw_algo_info(algorithm)
        draw(slicer)
    main()

if __name__=='__main__':
    main()