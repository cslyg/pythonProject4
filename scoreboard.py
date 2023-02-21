import pygame
class Scoreboard:
    def __init__(self, settings, screen):
        pygame.init()
        self.settings = settings
        self.screen = screen

        # 计分板的尺寸和颜色
        self.width, self.height = 150, 50
        self.score_color = (100, 20, 250)
        self.text_color = (150, 250, 150)
        self.font = pygame.font.SysFont(None, 30)

        # 创建计分板的rect对象，并放在右上角
        screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = screen_rect.right - 20
        self.rect.top = 20

        self.msg_image = self.font.render(settings.score, True, self.text_color, self.score_color)
        self.msg_rect = self.msg_image.get_rect()



        # 创建实例的时候贴上按钮的标签


    # def prep_score(self, score):
    #     """文字在图像中央"""
        # self.msg_image = self.font.render(score, True, self.text_color, self.score_color)

        # self.msg_rect = self.msg_image.get_rect()


    def draw_score(self,settings):
        """绘制按钮"""
        self.msg_image = self.font.render(settings.score, True, self.text_color, self.score_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

        self.screen.fill(self.score_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)