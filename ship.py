import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):  # 第一个参数是游戏的ship，第二个参数是传进来的游戏
        """初始化飞船并且设置其初始化位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # 移动的标志
        self.moving_right = False
        self.moving_left = False

        # 加载飞船图像并且获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每一艘飞船，都把他放在屏幕的正中央底部
        self.rect.midbottom = self.screen_rect.midbottom

        # 设置飞船移动的速度
        self.ship_speed = 1.5

        # 在属性x中存储小数值
        self.x = float(self.rect.x)

    def update(self):
        """根据标志来调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
