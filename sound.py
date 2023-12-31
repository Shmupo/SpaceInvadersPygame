import pygame as pg
import time


class Sound:
    def __init__(self, bg_music):
        pg.mixer.init()
        pg.mixer.music.load(bg_music)
        pg.mixer.music.set_volume(0.1)
        laser_sound = pg.mixer.Sound('sounds/laser.wav')
        laser_sound.set_volume(.5)
        gameover_sound = pg.mixer.Sound('sounds/gameover.wav')
        self.sounds = {'laser': laser_sound, 'gameover': gameover_sound}

    def play_bg(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_bg(self):
        pg.mixer.music.stop()

    def shoot_laser(self): pg.mixer.Sound.play(self.sounds['laser'])
    def gameover(self): 
        self.stop_bg() 
        pg.mixer.music.load('sounds/gameover.wav')
        self.play_bg()
        time.sleep(1.5)
        self.stop_bg()
