#!/usr/bin/python
import pygame
import sys

class WaterJet:
    """ A WaterJet game """

    def __init__(self, width=640, height=640):
        pygame.init()
        self.width = width
        self.height = height
        pygame.display.set_caption("Hi, Michael!")
        self.screen = pygame.display.set_mode((self.width, self.height))

        tile = pygame.image.load('one.png').convert()
        for x in range(0, 16):
            for y in range(0, 16):
                self.screen.blit(tile, (x * 40, y * 40))
        pygame.display.update()

    def start(self):
        tile = pygame.image.load('two.png').convert()
        while 1:
            for event in pygame.event.get():
                print event
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    self.screen.blit(tile, event.pos)
                pygame.display.update()

if __name__ == "__main__":
    game = WaterJet()
    game.start()
