# Configuartion for Squish
# ------------------------
import random
import pygame, config, os
from os import path

img_dir = path.join(path.dirname(__file__), 'img_dir')
snd_dir = path.join(path.dirname(__file__), 'snd_dir')
clock = pygame.time.Clock()

background_image = path.join(img_dir, 'background_image.png')
alien_image = path.join(img_dir, 'alien.png')
fighter_1_image = path.join(img_dir, 'fighter_1.png')
fighter_2_image = path.join(img_dir, 'fighter_2.png')
fighter_3_image = path.join(img_dir, 'fighter_3.png')
fighter_4_image = path.join(img_dir, 'fighter_4.png')
fighter_5_image = path.join(img_dir, 'fighter_5.png')
fighter_6_image = path.join(img_dir, 'fighter_6.png')
fighter_7_image = path.join(img_dir, 'fighter_7.png')
astronaut_1_image = path.join(img_dir, 'astronaut_1.png')
astronaut_2_image = path.join(img_dir, 'astronaut_2.png')
astronaut_3_image = path.join(img_dir, 'astronaut_3.png')
astronaut_4_image = path.join(img_dir, 'astronaut_4.png')
astronaut_5_image = path.join(img_dir, 'astronaut_5.png')
alien_lg_image = path.join(img_dir, 'alien_lg.png')
life_image = path.join(img_dir, 'heart.png')
bullet_image = path.join(img_dir, 'laserRed16.png')

pygame.mixer.init()
picked_up_sound = pygame.mixer.Sound(path.join(snd_dir, 'pow4.wav'))
extra_life_sound = pygame.mixer.Sound(path.join(snd_dir, 'health_pack.wav'))
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))

explosion_sound = []
for expl in ['expl3.wav', 'expl6.wav']:
    explosion_sound.append(pygame.mixer.Sound(path.join(snd_dir, expl)))

pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.3)

explosion_anim = []

for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename))
    img_large = pygame.transform.scale(img, (100, 100))
    explosion_anim.append(img_large)



# General appearance
screen_size = 1440, 900
FPS = 60
background_color = 255, 255, 255
margin = 30
full_screen = 1
font_size = 48

# Game behavior
drop_speed_1 = 3#round(random.uniform(2, 5), 1)
drop_speed_2 = 3.5#round(random.uniform(2, 5), 1)
drop_speed_3 = 4#round(random.uniform(2, 5), 1)
drop_speed_4 = 4.5#round(random.uniform(5, 9), 1)
drop_speed_5 = 5#round(random.uniform(5, 9), 1)
drop_speed_6 = 5.5#round(random.uniform(5, 9), 1)
drop_speed_7 = 6
speed_increase = 2
fighter_per_level = 100
lives_per_level = 0
alien_pad_top = 40
alien_pad_side = 20
fighter_pad_top = 40
fighter_pad_side = 20
bullet_pad_top = 1
bullet_pad_side = 1
