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

    def start(self):
        while 1:
            for event in pygame.event.get():
                print event
                if event.type == pygame.QUIT:
                    sys.exit()

if __name__ == "__main__":
    game = WaterJet()
    game.start()
