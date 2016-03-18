import pygame


def play(song):
    pygame.mixer.init()
    pygame.mixer.music.load(song.file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
