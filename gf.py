import pygame,sys
def check_event(ship,bullet):
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
                bullet.move = True

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







