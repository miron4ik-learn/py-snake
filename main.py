import time
import pygame

from colors import red, green, black
from utils import get_random_point, exit

from snake import Snake
from food import Food

pygame.init()

width = 800
height = 600

segment_size = 20
snake_speed = 12

snake = Snake(width, height, segment_size, snake_speed)
food = Food(width, height, segment_size)

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()
font = pygame.font.SysFont('None', 35)

def game_over():
  message = font.render('Вы проиграли', True, red)
  display.blit(message, [ width / 2, height / 2 ])
  pygame.display.flip()
  
  time.sleep(2)
  exit()

def show_score(score):
  value = font.render('Очки: ' + str(score), True, black)
  display.blit(value, [ 0, 0 ])

while True:
  if snake.outside_window():
    game_over()
  
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      exit()
    elif event.type == pygame.KEYDOWN:
      snake.move(event.key)
        
  snake.set_d()

  display.fill(green)
  
  food.show(display)
  
  snake.list.append((snake.head_x, snake.head_y))
  if len(snake.list) > snake.length:
    del snake.list[0]
  
  snake.show(display)
  show_score(snake.length - 1)
  
  if food.eaten(snake):
    food.update()
    snake.length += 1
  
  pygame.display.flip()
  clock.tick(snake_speed)