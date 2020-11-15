#! /usr/bin/env python

import os
import random
import pygame
import math
import sys

os.environ["SDL_VIDEO_CENTERED"] = "1"

screen = pygame.display.set_mode((192, 192))
pygame.display.set_caption("LEVEL 2 = Find the Correct Square!")

clock = pygame.time.Clock()

class Player(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((2, 2, 20, 20))
        self.gridSize = 24

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_a]:
           self.rect.move_ip(-self.gridSize, 0)
        if key[pygame.K_d]:
           self.rect.move_ip(self.gridSize, 0)
        if key[pygame.K_w]:
           self.rect.move_ip(0, -self.gridSize)
        if key[pygame.K_s]:
           self.rect.move_ip(0, self.gridSize)
        if key[pygame.K_q]:
           pygame.quit()
           sys.exit()
    def draw(self, surface):
        pygame.draw.rect(screen, (0, 0, 128), self.rect)

def main():
    pygame.init()

    player = Player()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
                running = False
            if event.type == pygame.KEYDOWN:
                player.handle_keys()

        screen.fill((255, 255, 255))

        player.draw(screen)
        pygame.display.update()

        clock.tick(40)
main()
