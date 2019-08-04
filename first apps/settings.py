class Settings():

    #a class that will store the settings

    def __init__(self):
        """initialize the game's settings"""

        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230 ,230, 230)
        self.ship_speed_factor = 1.5

        #bullet settings

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 70, 60, 60



