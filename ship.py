import pygame
class Ship(pygame.sprite.Sprite):
    def __init__(self,screen,settings):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.settings = settings
        # 载入图片并获取其外接矩形
        self.image = pygame.image.load(r"E:\桌面\feiji.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False


        # 设定飞机的初始位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom

        self.x = float(self.rect.centerx)
        self.y = float(self.rect.y)




    def draw_ship(self):
        # 显示飞船图像
        self.screen.blit(self.image,self.rect)

    
            
        
        
        
        # 向左移动


    def right(self):

        if self.move_right and self.rect.right <= self.screen_rect.right:

            self.x += self.settings.ship_speed
            self.rect.x = self.x
    def left(self):
        if self.move_left and self.rect.left >= self.screen_rect.left:

            self.x -= self.settings.ship_speed
            self.rect.x = self.x
    def up(self):
        if self.move_up and self.rect.top >= self.screen_rect.left:
            self.y -= self.settings.ship_speed
            self.rect.y = self.y

    def down(self):
        if self.move_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.ship_speed
            self.rect.y = self.y
    def update(self):
        self.up()
        self.down()
        self.left()
        self.right()













