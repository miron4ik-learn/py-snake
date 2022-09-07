import pygame

pygame.init()

width = 800
height = 600

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

while True:
  events = pygame.event.get()
  for event in events:
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        vy = segment_size
        vx = 0
      elif event.key == pygame.K_UP:
        vy = -segment_size
        vx = 0
      elif event.key == pygame.K_LEFT:
        vy = 0
        vx = -segment_size
      elif event.key == pygame.K_RIGHT:
        vy = 0
        vx = segment_size
        
  head_x += vx
  head_y += vy

  display.fill(green)
  pygame.draw.rect(display, black, [ head_x, head_y, segment_size, segment_size ])
  
  pygame.display.flip()
  clock.tick(snake_speed)