import pygame
class Button:
    """创建按钮类"""
    def __init__(self,settings,screen,msg):
        pygame.init()
        self.settings = settings
        self.screen = screen

        # 按钮的尺寸和颜色
        self.width, self.height = 200, 50
        self.button_color = (100,200,250)
        self.text_color = (50,250,50)
        self.font = pygame.font.SysFont(None,48)

        # 创建按钮的rect对象，并居中
        screen_rect = self.screen.get_rect()
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = screen_rect.center

        #创建实例的时候贴上按钮的标签
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """把字符串渲染为图像，并在按钮上居中"""
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)

        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_button(self):
        """绘制按钮"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_rect)








