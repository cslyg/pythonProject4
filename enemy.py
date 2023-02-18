import random

import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen,settings):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        # 载入图片并获取其外接矩形
        self.image = pygame.image.load(r"E:\桌面\enemy1.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.move_status = random.choice([-1,1])




    def draw_enemy(self):
        # 显示飞船图像
        self.screen.blit(self.image,self.rect)

    def enemy_randomx(self):
        # 让飞船位置随机
        self.x = random.uniform(0,self.screen_rect.right)
        self.rect.centerx = self.x


    def enemy_y(self):
        # 控制向下移动
        self.y += self.settings.enemy_speedy
        self.rect.y = self.y

    def enemy_x(self):
        # 控制左右移动
        if self.move_status != 0:
            self.x+= self.settings.enemy_speedx * self.move_status
            self.rect.centerx = self.x

    def direction_x(self):
        if self.rect.right == self.screen_rect.right:
            self.move_status = -1

        if self.rect.centerx == 0:
            self.move_status = 1


