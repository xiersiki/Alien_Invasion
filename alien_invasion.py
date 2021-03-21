import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏以及创建游戏资源。"""
        pygame.init()
        self.settings = Settings()
        # 这里设置全屏模式
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.scree_width = self.screen.get_rect().width
        # self.settings.scree_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.scree_width, self.settings.scree_height)
        )
        pygame.display.set_caption("Alien Invasion")
        # 这里的self是这个class的对象是指这个游戏AlienInvasion
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events_()
            self.ship.update()
            self.bullets.update()
            # 每次循环时都重新绘制屏幕
            self._update_screen_()

    def _check_events_(self):
        """响应鼠标和键盘事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 事件是按下按键时
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 事件是松开按键时
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # 响应按下按键
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # 如果检测到的事件是向右移动
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.type == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        # 松开的是右方向键
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一个子弹，并把它加入到编组中去"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)  # bullets属性是一个管理发射子弹的编组

    def _update_screen_(self):
        """更新频幕上的图像和切换到新的屏幕上"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 让绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并且运行
    ai = AlienInvasion()
    ai.run_game()
