import pygame



class astronaut:
    def __init__(self, ai_game):

        """Initialize the character and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loading the character image and get its rect
        self.image = pygame.image.load('images\Astronaut.png').convert_alpha()
        self.rect = self.image.get_rect()


        # Start each new character at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)