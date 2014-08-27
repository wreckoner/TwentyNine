'''
Created on Jul 15, 2014
@author: Dibyendu

Menu module: A simple title screen with animation. Returns if Enter is pressed.
'''
import random, pygame
from display_engine.image_files import card_files
from display_engine.methods import load_image

def menu_screen(image_dict):
    screen = image_dict['screen']
    background = image_dict['background']
    
    #######
    cards = card_files()
    width, height = screen.get_rect().size
    image = load_image(cards['back - up'])
    x_limit, y_limit = xrange(width - int(image.get_rect().height * 1.2)), xrange(height - image.get_rect().height)
    #######
    
    title = load_image('menu.png', ['images'], 1)
    title = pygame.transform.smoothscale(title, (width, height))
    title_rect = title.get_rect()
    title_rect.center = screen.get_rect().center
    
    while True:
        
        key = random.choice(list(cards.keys()))

        image = load_image(cards[key], None, 1)
        image = pygame.transform.rotozoom(image, random.choice(xrange(0, 360)), 1)
        screen.blit(image, (random.choice(x_limit), random.choice(y_limit)))
        screen.blit(title, title_rect)
        pygame.time.delay(50)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type is pygame.KEYDOWN and event.key is pygame.K_RETURN: 
                screen.blit(background, screen.get_rect())
                return True
            elif event.type is pygame.KEYDOWN and event.key is pygame.K_ESCAPE: 
                return False
            elif event.type is pygame.QUIT:
                return False
