class Settings:
    """存储游戏中的所有设置的类"""

    def __init__(self):
        """初始化的游戏设置"""
        # 屏幕设置
        self.scree_width = 1200  # 宽
        self.scree_height = 800  # 长
        self.bg_color = (230, 230, 230)

        # 飞船速度设置
        self.shi_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
