'''
Created on Jul 5, 2014
@author: Dibyendu
'''

import os, pygame

def load_image(_file, folders = None, colorkey = 1):
    # folders must be a list of folders
    if not folders: folders = []
    folders.append(_file)
    image = os.path.join(*folders)
    if colorkey is 0: image = pygame.image.load(image).convert()
    else: image = pygame.image.load(image).convert_alpha()
    return image