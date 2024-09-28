import pygame
import time
import random

pygame.init()

background_colour = (0, 0, 0)
x_position = (800)
y_position = (800)

# Set up the display
game_window = pygame.display.set_mode((x_position, y_position))
pygame.display.set_caption('Snake')

game_window.fill(background_colour)
pygame.display.update()

# Think about snake logic - size, speed, space etc
snake_position = [100, 50]

snake_body = [[100, 50],
            [90, 50],
            [80, 50],
            [70, 50]
]

fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# setting default snake direction 
# towards right
direction = 'RIGHT'
change_to = direction



# Game loop (to keep the window open)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()
