import pygame
import threading


class Player(object):
    def __init__(self):
        pygame.mixer.init()
        self.lock = threading.Lock()

    def play(self, song):
        self.lock.acquire()
        pygame.mixer.music.load(song.file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        self.lock.release()

    def stop(self):
        pygame.mixer.music.stop()
