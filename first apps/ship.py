import pygame

class Ship():

    def __init__(self ,ai_settings ,screen):
        """ initialize ship"""
        self.screen = screen
        self.ai_settings = ai_settings

        #ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #ship possition
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for the ship's location
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.right > 0:#instead of 0 you could try with bigger numbers to get the ship to not disappear
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image ,self.rect)