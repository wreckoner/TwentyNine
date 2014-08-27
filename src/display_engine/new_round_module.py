'''
Created on Aug 26, 2014
@author: Dibyendu
'''
import pygame
import display_engine

def new_round():
    screen = pygame.display.get_surface()
    screen_backup = pygame.Surface.copy(screen)
    message_src = display_engine.methods.load_image('messages.png', ['images'], 1)
    
    question = pygame.Surface((729, 57), pygame.SRCALPHA, 32).convert_alpha()
    question.blit(message_src, (0, 0), (5, 306, 729, 57))
    rect = question.get_rect()
    rect.center = screen.get_rect().center
    
    yes = pygame.Surface((115, 49), pygame.SRCALPHA, 32).convert_alpha()
    yes.blit(message_src, (0, 0), (6, 368, 115, 49))
    rect_yes = yes.get_rect()
    rect_yes.topleft = rect.bottomleft
    
    no = pygame.Surface((91, 49), pygame.SRCALPHA, 32).convert_alpha()
    no.blit(message_src, (0, 0), (150, 368, 91, 49))
    rect_no = no.get_rect()
    rect_no.topleft = rect_yes.bottomleft
    
    screen.blit(question, rect)
    screen.blit(yes, rect_yes)
    screen.blit(no, rect_no)
    
    pygame.display.update([rect, rect_yes, rect_no])
    
    running, flag = True, True
    key_table = {pygame.K_RETURN : True, pygame.K_ESCAPE : False}
    
    while running:
        for event in pygame.event.get():
            if event.type is pygame.KEYDOWN:
                flag, running = key_table[event.key], False
            elif event.type is pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if rect_yes.collidepoint(pos):
                    flag, running = True, False
                elif rect_no.collidepoint(pos):
                    flag, running = False, False
            elif event.type is pygame.QUIT:
                flag, running = False, False
    pygame.display.update(screen.blit(screen_backup, (0, 0)))
    return flag
    
    