import pygame
from colors import red
from utils import get_random_point

class Food:
  def __init__(self, width, height, segment_size):
    self.width = width
    self.height = height
    self.segment_size = segment_size
    
    self.update()
    
  def update(self):
    self.x, self.y = get_random_point(self.width, self.height, self.segment_size)
    
  def show(self, display):
    pygame.draw.rect(display, red, [ self.x, self.y, self.segment_size, self.segment_size ])
    
  def eaten(self, snake):
    return snake.head_x == self.x and snake.head_y == self.y