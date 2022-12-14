class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        # 让游戏一开始处于非活动状态
        self.game_active = False
        # 在任何情况下都不应重置最高得分
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
