""" Main module for the Space Invasion game. """

try:
    import pygame
    import sys
    import os

except ImportError as error:
    sys.exit("Couldn't loading module.  {}".format(error))

def main():
    """ Set up screen and display """
    
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((550, 550))
    pygame.display.set_caption("Space Invaders!")

    # Create background
    background = pygame.image.load("space.jpg")

    # Display text
    font = pygame.font.Font(None, 36)
    text = font.render("Space Invaders!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    # Display everything on screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
