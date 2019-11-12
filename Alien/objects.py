# Game objects for Squish
# -----------------------

import pygame, config, os
from pygame import time
from random import randrange
import random



class SurviveSprite(pygame.sprite.Sprite):

    '''
    Generic superclass for all sprites in the game. The constructor
    takes care of loading an image, setting up the sprite rect,
    and the area within which it is allowed to move.
    That is governed by the screen size and the margin.
    '''

    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        shrink = -config.margin * 2
        self.area = screen.get_rect().inflate(shrink, shrink)

class Fighter_1(SurviveSprite):

    '''
    A falling fighter. It uses the SurviveSprite constructor to set up
    its fighter image, and will fall with a speed given as a parameter
    to its constructor.
    '''

    def __init__(self, speed_1):
        super().__init__(config.fighter_1_image)
        self.pad_top = config.fighter_pad_top
        self.pad_side = config.fighter_pad_side
        self.speed_1 = speed_1
        self.reset()

    def reset(self):
        '''
        Move the fighter to the top of the screen (just out of sight)
        and place it in a random horizontal position.
        '''
        x = randrange(self.area.left + 10, self.area.right - 10)
        self.rect.midbottom = x, 0

    def update(self):
        '''
        Move the fighter vertically (downwards) at its corresponding speed.
        Also set the landed attribute according to whether
        it has reached the bottom of the screen.
        '''
        self.rect.top += self.speed_1
        self.landed = self.rect.top >= self.area.bottom + 10

    def touches(self, other):
        '''
        Determines whether the fighter touches another sprite (e.g.,
        alien). Instead of just using the rect method colliderect,
        a new rectangle is first calculated (using the rect method inflate
        with the side and top paddings) that does not include the 'empty'
        areas on the top and sides of the fighter
        '''
        # deflate the bounds with the proper padding
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        # move the bounds so they are placed at the bottom of the Fighter
        bounds.bottom = self.rect.bottom
        # check whether the bounds intersect with the other object's rect
        return bounds.colliderect(other.rect)


class Fighter_2(SurviveSprite):

    def __init__(self, speed_2):
        super().__init__(config.fighter_2_image)
        self.pad_top = config.fighter_pad_top
        self.pad_side = config.fighter_pad_side
        self.speed_2 = speed_2
        self.reset()

    def reset(self):
        x = randrange(self.area.left + 10, self.area.right - 10)
        self.rect.midbottom = x, 0

    def update(self):
        self.rect.top += self.speed_2
        self.landed = self.rect.top >= self.area.bottom + 10

    def touches(self, other):
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)


class Fighter_3(SurviveSprite):

    def __init__(self, speed_3):
        super().__init__(config.fighter_3_image)
        self.pad_top = config.fighter_pad_top
        self.pad_side = config.fighter_pad_side
        self.speed_3 = speed_3
        self.reset()

    def reset(self):
        x = randrange(self.area.left + 10, self.area.right - 10)
        self.rect.midbottom = x, 0

    def update(self):
        self.rect.top += self.speed_3
        self.landed = self.rect.top >= self.area.bottom + 10

    def touches(self, other):

        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)


class Fighter_4(SurviveSprite):

    def __init__(self, speed_4):
        super().__init__(config.fighter_4_image)
        self.pad_top = config.fighter_pad_top
        self.pad_side = config.fighter_pad_side
        self.speed_4 = speed_4
        self.reset()

    def reset(self):
        x = randrange(self.area.left + 10, self.area.right - 10)
        self.rect.midbottom = x, 0

    def update(self):
        self.rect.top += self.speed_4
        self.landed = self.rect.top >= self.area.bottom + 10

    def touches(self, other):
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)


class Fighter_5(SurviveSprite):

    def __init__(self, speed_5):
        super().__init__(config.fighter_5_image)
        self.pad_top = config.fighter_pad_top
        self.pad_side = config.fighter_pad_side
        self.speed_5 = speed_5
        self.reset()

    def reset(self):
        x = randrange(self.area.left + 10, self.area.right - 10)
        self.rect.midbottom = x, 0

    def update(self):
        self.rect.top += self.speed_5
        self.landed = self.rect.top >= self.area.bottom + 10

    def touches(self, other):
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)


class Fighter_6(SurviveSprite):

    def __init__(self, speed_6):
        super().__init__(config.fighter_6_image)
        self.pad_top = config.fighter_pad_top
        self.pad_side = config.fighter_pad_side
        self.speed_6 = speed_6
        self.reset()

    def reset(self):
        x = randrange(self.area.left + 10, self.area.right - 10)
        self.rect.midbottom = x, 0

    def update(self):
        self.rect.top += self.speed_6
        self.landed = self.rect.top >= self.area.bottom + 10

    def touches(self, other):
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)


class Fighter_7(SurviveSprite):

    def __init__(self, speed_7):
        super().__init__(config.fighter_7_image)
        self.pad_top = config.fighter_pad_top
        self.pad_side = config.fighter_pad_side
        self.speed_7 = speed_7
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.reset()

    def reset(self):
        x = randrange(self.area.left + 10, self.area.right - 10)
        self.rect.midbottom = x, 0

    def update(self):
        self.rect.top += self.speed_7
        self.landed = self.rect.top >= self.area.bottom + 10



    def touches(self, other):
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        bounds.bottom = self.rect.bottom
        return bounds.colliderect(other.rect)

    def shoot(self):
        bullet_1 = Bullet(self.rect.left, self.rect.centery)
        bullet_2 = Bullet(self.rect.right, self.rect.centery)



class Alien(SurviveSprite):

    '''
    It uses the SurvuveSprite constructor to set up its image,
    and will be able to move freely on screen. Its osition is governed by
    the current mouse position.
    '''

    def __init__(self):
        super().__init__(config.alien_image)
        self.rect.bottom = self.area.bottom
        # these paddings represent part of the image where there is no
        # alien. If a fighter moves into these areas, it doesn't
        # constitute a hit.
        self.pad_top = config.alien_pad_top
        self.pad_side = config.alien_pad_side

    def update(self):
        '''
        Set the Alien's center x and y coordinates to the current mouse
        x and y coordinates.
        '''
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos


    def touches(self, other):
        '''
        Determines whether the alien touches another sprite (e.g. food)
        Instead of just using the rect method colliderect, a new rectangle
        is first calculated (using the rect method inflate with the side and
        top paddings) that does not include the 'empty'
        areas on the top and sides of the alien
        '''
        # deflate the bounds with the proper padding
        bounds = self.rect.inflate(-self.pad_side, -self.pad_top)
        # move the bounds so they are placed at the bottom of the Alien
        bounds.bottom = self.rect.bottom
        # check whether the bounds intersect with the other object's rect
        return bounds.colliderect(other.rect)


class Food_1(SurviveSprite):

    '''
    It uses the SurvuveSprite constructor to set up its image.
    Food will randombly show on screen and , once the Alien 'eats' the food,
    it will disappear (just off screen) and a Life will be granted.
    '''

    def __init__(self):
        super().__init__(config.astronaut_1_image)
        self.reset()

    def reset(self):
        x = randrange(60,1350)
        y = randrange(60,800)
        self.rect.midbottom = x,y

    def hide(self):
        x = 0
        y = 0
        self.rect.midbottom = x,y


class Food_2(SurviveSprite):

    def __init__(self):
        super().__init__(config.astronaut_2_image)
        self.reset()

    def reset(self):
        x = randrange(60,1350)
        y = randrange(60,800)
        self.rect.midbottom = x,y

    def hide(self):
        x = 0
        y = 0
        self.rect.midbottom = x,y


class Food_3(SurviveSprite):

    def __init__(self):
        super().__init__(config.astronaut_3_image)
        self.reset()

    def reset(self):
        x = randrange(60,1350)
        y = randrange(60,800)
        self.rect.midbottom = x,y

    def hide(self):
        x = 0
        y = 0
        self.rect.midbottom = x,y


class Life_1(SurviveSprite):

    '''
    Lives start in a hidden state (just off screen), and they show in a
    specified x and y location once Food has been eaten by alien
    '''

    def __init__(self):
        super().__init__(config.life_image)
        self.hide()

    def show(self):
        x = 1400
        y = 100
        self.rect.midbottom = x,y

    def hide(self):
        x = 0
        y = 0
        self.rect.midbottom = x,y


class Life_2(SurviveSprite):


    def __init__(self):
        super().__init__(config.life_image)
        self.hide()

    def show(self):
        x = 1400
        y = 150
        self.rect.midbottom = x,y

    def hide(self):
        x = 0
        y = 0
        self.rect.midbottom = x,y


class Life_3(SurviveSprite):


    def __init__(self):
        super().__init__(config.life_image)
        self.hide()

    def show(self):
        x = 1400
        y = 200
        self.rect.midbottom = x,y

    def hide(self):
        x = 0
        y = 0
        self.rect.midbottom = x,y


class Explosion(SurviveSprite):

    '''
    Explosion is a list of 9 images that will spawn everytime a fighter
    crashes with Alien
    '''

    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = config.explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(config.explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = config.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Bullet(SurviveSprite):

    '''
    Bullets are bring shot from the right and left wing of the Fighter.
    Its constructor method takes x and y coordinates in order to determine
    the exact position from where are shot, relative to each fighter.
    '''

    def __init__(self, x, y):
        super().__init__(config.bullet_image)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 10

    def update(self):
        '''
        If the bullet has passed the bottom of the screen, it will dissapear
        '''
        self.rect.y += self.speedy
        if self.rect.top >= self.area.bottom + 10:
            self.kill()
