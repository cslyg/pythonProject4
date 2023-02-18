import pygame,sys
from bullet import Bullet
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
                new_bullet = Bullet(ship,settings)
                bullets.add(new_bullet)
                print(len(bullets))


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
def update_screen(bullets,screen):
    for bullet in bullets.sprites():
        bullet.draw_bullet(screen)
        bullet.update()

def del_bullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)












