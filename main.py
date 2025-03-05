# Arden Boettcher
# 3/5/25
# Shapes Using Dictionaries

import pygame
import sys
from random import choice, randint

import shapes
import config

pygame.init()

# Setting up the window
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("PLACEHOLDER")

# Setting up the clock
clock = pygame.time.Clock()

# Event handling
def main_events():
  for event in pygame.event.get():
    # Quits the game when you press the x
    if event.type == pygame.QUIT:
      return False
  return True


# Chooses one of three random shapes
def make_shape():
  return choice([
      shapes.Randrect(),
      shapes.Randcircle(),
      shapes.Randline()
    ])


# Main loop
def main():
  # The bool for the main loop
  running = True

  shapes_list = []

  while running:

    # Call events / update running
    running = main_events()

    # Adds another shape
    shapes_list.append(make_shape())

    # Fills window
    screen.fill(config.WHITE)

    # Draws Shapes
    for shape in shapes_list:
      shape.draw(screen)

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate
    clock.tick(config.FPS)

  # Close the pygame modules
  pygame.quit()


# Calls the code
if __name__ == "__main__":
  main()
