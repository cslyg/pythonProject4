import random

import pygame
class Enemy:
    def __init__(self,screen,settings):
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

    def draw_enemy(self):
        # 显示飞船图像
        self.screen.blit(self.image,self.rect)

    def enemy_move(self):
        self.x = random.uniform(0,self.screen_rect.right)
        self.rect.x = self.x