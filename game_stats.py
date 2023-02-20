import pygame,time
class GameStats:
    def __init__(self,settings):
        self.settings = settings
        self.game_active = True
        # 创建实例时，初始化飞机数量。


    def reset_stats(self,ship,enemies):
        """c初始化必要信息"""
        if self.settings.ship_num <= 0:
            self.game_active = False
            confirm = input("游戏结束，是否重新开始? ,输入Y/N\n\t：")
            if confirm == "y":
                self.game_active = True
            # self.game_active = False
                self.settings.ship_num = self.settings.ship_limit
                print("飞船用完了，已经补充了新的飞船")

        # # 被击中时复位飞船
        # if pygame.sprite.spritecollideany(ship, enemies):
        #     print("飞船被击中！！！")
        #     print("还剩余" + str(self.settings.ship_num) + "艘飞船")
        #     enemies.empty()
        #     ship.move_down = True
        #     ship.x = ship.screen_rect.centerx
        #     ship.y = ship.screen_rect.bottom - 100
        #     time.sleep(0.5)


