import pygame

pygame.init()

width = 800
height = 600

green = (0, 255, 0)
black = (0, 0, 0)

segment_size = 20

display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Змейка')

display.fill(green)

pygame.draw.rect(display, black, [ width // 2, height // 2, segment_size, segment_size ])
pygame.display.flip()