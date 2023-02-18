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

            elif event.key == pygame.K_LEFT:
                ship.move_left = True

            elif event.key == pygame.K_UP:

                ship.move_up = True
            elif event.key == pygame.K_DOWN:

                ship.move_down = True
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
def update_screen(bullets,screen,enemies):
    enemies.draw(screen)
    enemies.update()

    for bullet in bullets.sprites():
        bullet.draw_bullet(screen)
        bullet.update()




def del_bullet(bullets,screen,settings,enemies):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    for enemy in enemies.copy():
        if enemy.rect.bottom <= 0:
            enemies.remove(enemy)



def create_enemy(enemies,screen,settings):
    for serial in range(get_nums(screen,settings)):
        enemy = Enemy(screen,settings)
        enemy.x =3 * settings.enemy_width*serial
        enemy.rect.x = enemy.x
        enemies.add(enemy)



def get_nums(screen,settings):
    screen_rect = screen.get_rect()
    x_length = screen_rect.right
    distance = 3*settings.enemy_width
    nums = int(x_length/distance)
    return nums-5

















