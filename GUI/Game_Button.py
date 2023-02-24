from datetime import datetime

import pygame
from pygame.color import Color
from pygame.math import Vector2
from pygame.rect import Rect
from pygame.surface import Surface

from GUI.Game_line import GameLine
from Interface.IDraw import IDraw
from Interface.IClick import IClick

class Game_Button(IDraw,IClick):

    MaxTextLength = 2

    def __init__(self, text:str, width, height, button_color:Color,
                 fontColor: Color, topLeftPoint : Vector2, fontType='Arial'):
        self.text = text
        self.width = width
        self.height = height
        self.button_color = button_color
        self.fontColor = fontColor
        self.topLeftPoint = topLeftPoint
        self.flliped = False
        self.finished = False
        self.AntiAlias = False
        self.rect = Rect(self.topLeftPoint.x, self.topLeftPoint.y, width, height)
        self.fontType = fontType
        self.fontSize = self.GetMaxFittingFonSize()
        self.font = pygame.font.SysFont(self.fontType, self.fontSize)
        self.last_click_time = None

    def draw(self,surface : Surface):
        pygame.draw.rect(surface , self.button_color , self.rect)
        if self.get_is_flliped():
            center = self.GetTextCenter()
            self.title = self.font.render(self.text, self.AntiAlias, self.fontColor)
            centerTitle = self.title.get_rect(center=center)
            surface.blit(self.title, centerTitle)

    def GetTextCenter(self):
        xCenter = self.width / 2 + self.topLeftPoint.x
        yCenter = self.height / 2 + self.topLeftPoint.y
        return (xCenter, yCenter)

    def GetMaxFittingFonSize(self):
        maxText = 'X'* Game_Button.MaxTextLength
        defaultFontSize = 16
        sysFont = pygame.font.SysFont(self.fontType, defaultFontSize)
        text_surface = sysFont.render(maxText, True, (0,0,0))
        size = text_surface.get_size()
        widthFontScaling =  self.width / size[0]
        hieghtFontScaling = self.height / size[1]
        minScalingByAxis = min(widthFontScaling, hieghtFontScaling)
        return int(defaultFontSize * minScalingByAxis)


    def is_clicked(self, coordinate: Vector2):
        return ( coordinate.x >= self.rect.left and coordinate.x <= self.rect.right) and\
               (coordinate.y >= self.rect.top and coordinate.y <= self.rect.bottom)

    def get_is_flliped(self):
        if self.finished:
            return True
        return self.flliped

    def handle_click(self, coordinate: Vector2):
        if not self.get_is_flliped():
            self.fllip()


    def undo_handle_click(self):
        if self.get_is_flliped():
            self.fllip()

    def fllip(self):
        self.flliped = not self.flliped

    def finish(self):
        self.finished = True

    def hide(self):
        self.flliped = False

    def is_equal(self,button2)->bool:
        return self.text == button2.text

    def get_button_mark(self):
        return self.text