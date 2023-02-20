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
from game_stats import GameStats
from button import Button
msg = "PLAY"




settings = Settings()
stats = GameStats(settings)

screen = pygame.display.set_mode(settings.screen_size)
ship = Ship(screen,settings)
play_button = Button(settings,screen,msg)



pygame.display.set_caption("飞机大战")
# enemy.enemy_randomx()


while True:
    gf.check_event(ship,bullets,settings,stats,play_button)
    screen.fill(settings.bg_color)



    gf.update_screen(ship,bullets, screen, enemies,stats,play_button)
    gf.del_bullet(bullets,stats)
    # print(len(enemies))
    gf.create_enemy(enemies, screen, settings,stats)





    pygame.sprite.groupcollide(enemies,bullets,True,True)
    gf.ship_hit(ship,enemies,settings,stats)
    stats.reset_stats(ship,enemies)



    pygame.display.update()
    # pygame.display.flip()


