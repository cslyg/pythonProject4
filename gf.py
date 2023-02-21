import pygame,sys
from bullet import Bullet
from enemy import Enemy
from ship import Ship

def check_event(ship,bullets,settings,stats,play_button):
    # 检查输入并给出反馈
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.move_right = True
                ship.move_up = False
                ship.move_left =False
                ship.move_down = False

            elif event.key == pygame.K_LEFT:
                ship.move_right = False
                ship.move_up =False
                ship.move_left =True
                ship.move_down =False


            elif event.key == pygame.K_UP:
                ship.move_right = False
                ship.move_up =True
                ship.move_left =False
                ship.move_down =False


            elif event.key == pygame.K_DOWN:
                ship.move_right = False
                ship.move_up =False
                ship.move_left =False
                ship.move_down =True


            elif event.key == pygame.K_SPACE:
                if len(bullets) <4:
                    new_bullet = Bullet(ship,settings)
                    bullets.add(new_bullet)
                # print(len(bullets))


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.move_right = False

            elif event.key == pygame.K_LEFT:

                ship.move_left = False

            elif event.key == pygame.K_UP:

                ship.move_up = False
            elif event.key == pygame.K_DOWN:

                ship.move_down = False

            elif event.key == pygame.K_q:
                sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y)
def update_screen(ship,bullets,screen,enemies,stats,paly_button,scoreboard,settings):

    if stats.game_active:
        enemies.draw(screen)
        enemies.update()
        ship.update()
        ship.draw_ship()
        scoreboard.draw_score(settings)


        for bullet in bullets.sprites():
            bullet.draw_bullet(screen)
            bullet.update()
    else:
        paly_button.draw_button()




def del_bullet(bullets,stats):
    if stats.game_active:
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)





def create_enemy(enemies, screen, settings,stats):
    if stats.game_active:
        if len(enemies) == 0:
            for serial in range(get_nums(screen, settings)):
                enemy = Enemy(screen, settings)
                settings.increse_speed()
                enemy.x = 3 * settings.enemy_width*serial
                enemy.rect.x = enemy.x
                enemies.add(enemy)



def get_nums(screen,settings):
    screen_rect = screen.get_rect()
    x_length = screen_rect.right
    distance = 3*settings.enemy_width
    nums = int(x_length/distance)
    return nums-3




from time import sleep
def ship_hit(ship,enemies,settings,stats):
    """响应飞船碰撞"""
    if stats.game_active:
    # 碰撞后，复位飞船，同时飞船数量减1,与飞船碰撞的敌人也被消灭。
        if pygame.sprite.spritecollideany(ship,enemies):
            for enemy in enemies.sprites():
                if pygame.sprite.spritecollideany(ship, enemies):
                    enemies.remove(enemy)

            print("飞船被击中！！！")
            #被击中时复位飞船

            ship.move_down = True
            ship.x = ship.screen_rect.centerx
            ship.y = ship.screen_rect.bottom - 100
            settings.ship_num -= 1

            print("还剩余" + str(settings.ship_num) + "艘飞船")
            sleep(0.5)

def check_play_button(stats,play_button,mouse_x,mouse_y):
    """在玩家点击play的时候开始游戏"""
    if play_button.rect.collidepoint(mouse_x,mouse_y) :
        stats.game_active = True
        pygame.mouse.set_visible(False)

def hit_screen(screen,enemies):
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.top == screen_rect.bottom:
            enemies.remove(enemy)























