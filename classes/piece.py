import pygame

class Piece(pygame.sprite.Sprite):

  def __init__(self, position, x, y, length):
    pygame.sprite.Sprite.__init__(self)
    self.queen = False
    self.position = position
    self.rect = pygame.Rect(x, y, length, length)

  def __str__(self):
    return f'{self.position}{"T" if self.queen else "F"}'

  def isQueen(self):
    return self.queen

  def getPosition(self):
    return self.position

  def getRect(self):
    return self.rect

  def setPosition(self, newPosition):
    self.position = newPosition