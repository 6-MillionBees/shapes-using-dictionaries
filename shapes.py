# Arden Boettcher
# 3/5/25
# Shapes

from random import randint
import pygame as pg
import config





class Randcircle:
  def __init__(self):
    self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
    self.pos = [randint(0, config.WIDTH), randint(0, config.HEIGHT)]
    self.radius = randint(40, 50)

  def draw(self, surface):
    pg.draw.circle(surface, self.color, self.pos, self.radius)


class Randrect:
  def __init__(self):
    self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
    self.pos = [randint(0, config.WIDTH), randint(0, config.HEIGHT)]
    self.size = randint(80, 100)
    self.rect = pg.Rect(self.pos, (self.size, self.size))

  def draw(self, surface):
    pg.draw.rect(surface, self.color, self.rect)


class Randline:
  def __init__(self):
    self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
    self.startpos = [randint(0, config.WIDTH), randint(0, config.HEIGHT)]
    self.endpos = [randint(0, config.WIDTH), randint(0, config.HEIGHT)]

  def draw(self, surface):
    pg.draw.line(surface, self.color, self.startpos, self.endpos, 5)