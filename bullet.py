import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,ship,settings):
        pygame.sprite.Sprite.__init__(self)
        self.settings = settings
        self.rect = pygame.Rect(0,0,15,30)
        self.color = settings.bullet_color
        self.move = False


        # 子弹从飞机内发射
        self.rect.centerx = ship.rect.centerx
        self.rect.centery = ship.rect.centery

        self.y = float(self.rect.y)



    def update(self):
        # if self.move:
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y

    def draw_bullet(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)

