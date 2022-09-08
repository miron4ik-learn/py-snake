import pygame
from colors import black

class Snake:
  def __init__(self, width, height, segment_size, snake_speed):
    self.width = width
    self.height = height
    
    self.segment_size = segment_size
    self.snake_speed = snake_speed
    
    self.head_x = width // 2 // segment_size * segment_size
    self.head_y = height // 2 // segment_size * segment_size
    
    self.list = []
    self.length = 1
    
    self.vx = 0
    self.vy = 0
    
  def outside_window(self):
    outside_x = self.head_x < 0 or self.head_x > self.width - self.segment_size
    outside_y = self.head_y < 0 or self.head_y > self.height - self.segment_size
    return outside_x or outside_y
  
  # Set vx, vy
  def set_v(self, vx, vy):
    self.vx, self.vy = vx, vy
    
  # Set direction
  def set_d(self):
    self.head_x += self.vx
    self.head_y += self.vy
    
  def move(self, key):
    if key == pygame.K_DOWN:
      self.set_v(0, self.segment_size)
    elif key == pygame.K_UP:
      self.set_v(0, -self.segment_size)
    elif key == pygame.K_LEFT:
      self.set_v(-self.segment_size, 0)
    elif key == pygame.K_RIGHT:
      self.set_v(self.segment_size, 0)
      
  def show(self, display):
    for x in self.list:
      pygame.draw.rect(display, black, [ x[0], x[1], self.segment_size, self.segment_size ])