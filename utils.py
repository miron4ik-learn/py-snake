import random
import pygame

def get_random_point(width, height, segment_size):
  x = random.randint(0, width - segment_size) // segment_size * segment_size
  y = random.randint(0, height - segment_size) // segment_size * segment_size
  return x, y

def exit():
  pygame.quit()
  quit()