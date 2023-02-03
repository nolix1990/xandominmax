import pygame
from pygame import Surface, Color
from pygame.math import Vector2
from Interface.IDraw import IDraw


class GameLine(IDraw):

    def __init__(self, width, startPoint:Vector2, endPoint:Vector2, color:Color=Color(0,0,0)):
        self.width = width
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.color = color

    def draw(self,surface : Surface):
        pygame.draw.line(surface , self.color, self.startPoint, self.endPoint, self.width)