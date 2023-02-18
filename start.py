# import sys
#
import pygame,os,random,sys,gf
from settings import Settings
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group
from enemy import Enemy
bullets = Group()
enemies = Group()


settings = Settings()

screen = pygame.display.set_mode(settings.screen_size)
ship = Ship(screen,settings)
bullet = Bullet(ship,settings)
enemy = Enemy(screen,settings)

pygame.display.set_caption("飞机大战")
enemy.enemy_randomx()
def collide():
    pygame.sprite.spritecollide(enemy,bullets,True)

while True:
    enemy.direction_x()
    gf.check_event(ship,bullets,settings)
    screen.fill(settings.bg_color)
    gf.update_screen(bullets,screen)
    gf.del_bullet(bullets)
    enemy.draw_enemy()

    enemy.enemy_y()
    enemy.enemy_x()

    ship.update()
    ship.draw_ship()
    collide()





    pygame.display.update()
    pygame.display.flip()


