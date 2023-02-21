
import pygame,gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

msg = "PLAY"



bullets = Group()
enemies = Group()
settings = Settings()
stats = GameStats(settings)

screen = pygame.display.set_mode(settings.screen_size)
ship = Ship(screen,settings)

play_button = Button(settings,screen,msg)
scoreboard = Scoreboard(settings,screen)



pygame.display.set_caption("飞机大战")



while True:
    gf.check_event(ship,bullets,settings,stats,play_button)
    screen.fill(settings.bg_color)



    gf.update_screen(ship,bullets, screen, enemies,stats,play_button,scoreboard,settings)
    gf.del_bullet(bullets,stats)
    # print(len(enemies))
    gf.create_enemy(enemies, screen, settings,stats)


    gf.ship_hit(ship,enemies,settings,stats)
    gf.hit_screen(screen,enemies)
    gf.score_stats(settings,enemies,bullets)
    stats.reset_stats(ship,enemies,settings)

    pygame.display.update()



