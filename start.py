# import sys
#
import pygame,os,random,sys,gf
from settings import Settings
from ship import Ship
from bullet import Bullet

settings = Settings()

screen = pygame.display.set_mode(settings.screen_size)
ship = Ship(screen,settings)
bullet = Bullet(ship,settings)

pygame.display.set_caption("飞机大战")

while True:
    gf.check_event(ship,bullet)
    screen.fill(settings.bg_color)

    ship.update()
    ship.draw_ship()
    bullet.draw_bullet(screen)
    bullet.emit()

    pygame.display.update()
    pygame.display.flip()


