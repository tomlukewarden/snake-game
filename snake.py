import pygame
import time
import random

pygame.init()

background_colour = (0, 0, 0)

# Set up the display
game_window = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Snake')

game_window.fill(background_colour)
pygame.display.update()

# Think about snake logic - size, speed, space etc

# Game loop (to keep the window open)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()
