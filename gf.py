import pygame,sys
from bullet import Bullet
from enemy import Enemy
from ship import Ship

def check_event(ship,bullets,settings):
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
                if len(bullets) <2:
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
def update_screen(ship,bullets,screen,enemies):
    enemies.draw(screen)
    enemies.update()
    ship.update()
    ship.draw_ship()

    for bullet in bullets.sprites():
        bullet.draw_bullet(screen)
        bullet.update()




def del_bullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)





def create_enemy(enemies, screen, settings):
    if len(enemies) == 0:

        for serial in range(get_nums(screen, settings)):
            enemy = Enemy(screen, settings)
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
def ship_hit(ship,enemies,settings):
    """响应飞船碰撞"""
    if pygame.sprite.spritecollideany(ship,enemies):
        print("飞船被击中！！！")
        #被击中时复位飞船

        ship.move_down = True
        ship.x = ship.screen_rect.centerx
        ship.y = ship.screen_rect.bottom - 100
        settings.ship_num -= 1
        print(settings.ship_num)





















