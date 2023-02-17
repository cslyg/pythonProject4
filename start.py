# import sys
#
import pygame,os,random,sys,gf
from settings import Settings
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group
from enemy import Enemy
bullets = Group()


settings = Settings()

screen = pygame.display.set_mode(settings.screen_size)
ship = Ship(screen,settings)
bullet = Bullet(ship,settings)
enemy = Enemy(screen,settings)

pygame.display.set_caption("飞机大战")
enemy.enemy_move()

while True:
    gf.check_event(ship,bullet,bullets,settings)
    screen.fill(settings.bg_color)
    gf.update_screen(bullets,screen)
    gf.del_bullet(bullets)
    enemy.draw_enemy()

    ship.update()
    ship.draw_ship()


    pygame.display.update()
    pygame.display.flip()


