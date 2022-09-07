import time
import pygame

pygame.init()

width = 800
height = 600

red = (213, 50, 80)
green = (0, 255, 0)
black = (0, 0, 0)

segment_size = 20
snake_speed = 12

head_x = width // 2
head_y = height // 2

vx = 0
vy = 0

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()
font = pygame.font.SysFont('None', 35)

def exit():
  pygame.quit()
  quit()
  
def head_move(key):
  if key == pygame.K_DOWN:
    vy = segment_size
    vx = 0
  elif key == pygame.K_UP:
    vy = -segment_size
    vx = 0
  elif key == pygame.K_LEFT:
    vy = 0
    vx = -segment_size
  elif key == pygame.K_RIGHT:
    vy = 0
    vx = segment_size
    
  return vx, vy

def game_over():
  message = font.render('Вы проиграли', True, red)
  display.blit(message, [ width / 2, height / 2 ])
  pygame.display.flip()
  
  time.sleep(2)
  exit()

while True:
  if head_x < 0 or head_x > width - segment_size or head_y < 0 or head_y > height - segment_size:
    game_over()
  
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      exit()
    elif event.type == pygame.KEYDOWN:
      vx, vy = head_move(event.key)
        
  head_x += vx
  head_y += vy

  display.fill(green)
  pygame.draw.rect(display, black, [ head_x, head_y, segment_size, segment_size ])
  
  pygame.display.flip()
  clock.tick(snake_speed)