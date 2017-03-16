#!/usr/bin/python
import pygame
import sys

class WaterJet:
    """ A WaterJet game """

    def __init__(self, width=640, height=640):
        pygame.init()
        self.width = width
        self.height = height
        self.clicked = []
        pygame.display.set_caption("Hi, Michael!")
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.draw_background()
        pygame.display.update()

    def draw_background(self):
        tile1 = pygame.image.load('one.png').convert()
        for x in range(0, 16):
            for y in range(0, 16):
                self.screen.blit(tile1, (x * 40, y * 40))

        tile2 = pygame.image.load('two.png').convert()
        for pos in self.clicked:
            self.screen.blit(tile2, pos)

    def start(self):
        tile = pygame.image.load('two.png').convert()
        while 1:
            for event in pygame.event.get():
                print event
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked += [(event.pos[0] - 20, event.pos[1] - 20)]
                    self.draw_background()
                elif event.type == pygame.MOUSEMOTION:
                    self.draw_background()
                    position = (event.pos[0] - 20, event.pos[1] - 20)
                    self.screen.blit(tile, position)
                pygame.display.update()

if __name__ == "__main__":
    game = WaterJet()
    game.start()
