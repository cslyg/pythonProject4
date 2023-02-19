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
# bullet = Bullet(ship,settings)
#



pygame.display.set_caption("飞机大战")
# enemy.enemy_randomx()


while True:
    gf.check_event(ship,bullets,settings)
    screen.fill(settings.bg_color)




    gf.update_screen(ship,bullets, screen, enemies)
    gf.del_bullet(bullets
                  )
    # print(len(enemies))
    gf.create_enemy(enemies, screen, settings)





    pygame.sprite.groupcollide(enemies,bullets,True,True)
    gf.ship_hit(ship,enemies,settings)



    pygame.display.update()
    # pygame.display.flip()


