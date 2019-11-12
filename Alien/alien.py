# Main logic for the alien game
# ------------------------------

import os, sys, pygame
from pygame.locals import *
import objects, config
from time import sleep
import random

class State:

    '''
    A generic game state class that can handle events and display
    istelf on a given surface.
    '''

    def handle(self, event):
        '''
        Default event handling only deals with quitting.
        '''
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    def first_display(self, screen):
        '''
        Used to display the State for the first time. Fills the screen
        with the background color.
        '''
        screen.fill(config.background_color)
        # calling flip to make the changes visible
        pygame.display.flip()


    def display(self, screen):
        '''
        Used to display the Sate after it has already been displayed
        once. The deafult behavior is to do nothing.
        '''
        pass


class Level(State):

    '''
    A game level. Takes care of counting how many fighters have been dropped,
    moving the sprites around, and other tasks relating to game logic.
    '''

    def __init__(self, number=1, life=0):
        self.number = number
        self.lives = life
        # how many fighters remain to dodge in this level?

        self.fighter_remaining = (config.fighter_per_level + self.number ** 2)

        # how many lives remaining in this level?
        self.lives_remaining = config.lives_per_level

        speed_1 = config.drop_speed_1
        speed_2 = config.drop_speed_2
        speed_3 = config.drop_speed_3
        speed_4 = config.drop_speed_4
        speed_5 = config.drop_speed_5
        speed_6 = config.drop_speed_6
        speed_7 = config.drop_speed_7

        # one speed_increase added for each level above 1:
        speed_1 += (self.number-1) * config.speed_increase
        speed_2 += (self.number-1) * config.speed_increase
        speed_3 += (self.number-1) * config.speed_increase
        speed_4 += (self.number-1) * config.speed_increase
        speed_5 += (self.number-1) * config.speed_increase
        speed_6 += (self.number-1) * config.speed_increase
        speed_7 += (self.number-1) * config.speed_increase
        # create all sprites
        self.fighter_1 = objects.Fighter_1(speed_1)
        self.fighter_2 = objects.Fighter_2(speed_2)
        self.fighter_3 = objects.Fighter_3(speed_3)
        self.fighter_4 = objects.Fighter_4(speed_4)
        self.fighter_5 = objects.Fighter_5(speed_5)
        self.fighter_6 = objects.Fighter_6(speed_6)
        self.fighter_7 = objects.Fighter_7(speed_7)
        self.alien = objects.Alien()
        self.food_1 = objects.Food_1()
        self.food_2 = objects.Food_2()
        self.food_3 = objects.Food_3()
        self.life_1 = objects.Life_1()
        self.life_2 = objects.Life_2()
        self.life_3 = objects.Life_3()
        fighter_sprite = (self.fighter_1, self.fighter_2, self.fighter_3,
        self.fighter_4, self.fighter_5, self.fighter_6, self.fighter_7)
        alien_sprite = self.alien
        food_sprite = self.food_1, self.food_2, self.food_3
        life_sprite = self.life_1, self.life_2, self.life_3
        self.sprites = pygame.sprite.RenderUpdates(fighter_sprite, alien_sprite, food_sprite, life_sprite)


    def update(self, game):
        'Updates the game state from previous frame'
        # update all sprites
        self.sprites.update()
        # Sprites grouped in lists, ready to iterate through
        foods = self.food_1, self.food_2, self.food_3
        fighters = (self.fighter_1, self.fighter_2, self.fighter_3,
        self.fighter_4, self.fighter_5, self.fighter_6, self.fighter_7)
        lives = self.life_1, self.life_2, self.life_3

        self.bullet_1 = objects.Bullet(self.fighter_7.rect.left + 12, self.fighter_7.rect.centery + 63)
        self.bullet_2 = objects.Bullet(self.fighter_7.rect.right - 12, self.fighter_7.rect.centery + 63)

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_SPACE]:
            self.sprites.add(self.bullet_1)
            self.sprites.add(self.bullet_2)
            config.shoot_sound.play()

        bullets = self.bullet_1, self.bullet_2

        for bullet in bullets:
            if self.alien.touches(bullet):
                print('bullet on alien')
                self.explosion = objects.Explosion(self.alien.rect.center)
                self.sprites.add(self.explosion)
                random.choice(config.explosion_sound).play()

        for food in foods:
            for fighter in fighters:
                if fighter.touches(food):
                    food.hide()
                if fighter.landed:
                    fighter.reset()
                    self.fighter_remaining -= 1
                    if self.fighter_remaining == 0:
                        game.next_state = LevelCleared(self.number)

                if self.alien.touches(food):
                    food.hide()
                    self.lives_remaining += 1
                    config.extra_life_sound.play()
                    if self.lives_remaining == 1:
                        self.life_1.show()
                    if self.lives_remaining == 2:
                        self.life_2.show()
                    if self.lives_remaining == 3:
                        self.life_3.show()

                if fighter.touches(self.alien):
                    self.explosion = objects.Explosion(self.alien.rect.center)
                    self.sprites.add(self.explosion)
                    random.choice(config.explosion_sound).play()
                    fighter.reset()
                    self.lives_remaining -= 1
                    if self.lives_remaining == 2:
                        self.life_3.hide()
                    if self.lives_remaining == 1:
                        self.life_2.hide()
                    if self.lives_remaining == 0:
                        self.life_1.hide()
                    if self.lives_remaining < 0:
                        game.next_state = GameOver()

        # if the fighter has landed, reset it. If all the fighters
        # of this level have been dodged before the lives have been
        # exhausted, tell the game to switch to a LevelCleared state



    def display(self, screen):
        '''
        Displays the state after the first display (which siply wipes the
        screen). As opposed to first_display, this method uses
        pygame.display.update with a list of rectangles that need to be
        updated, suplied from self.sprites.draw.
        '''
        screen.fill(config.background_color)
        updates = self.sprites.draw(screen)
        pygame.display.update(updates)

        '''bg_image = pygame.image.load(config.background_image).convert_alpha()
        screen.blit(bg_image, (0,0))
        updates = self.sprites.draw(screen)
        pygame.display.update(updates)'''



class Paused(State):

    '''
    A simple, paused game state, which may be broken out by pressing either
    a keyboard key or the mouse button.
    '''

    finished = 0 # has the user ended the pasue?
    image = None # no image shown in this case
    text = '' # inform the used the game is paused

    def handle(self, event):
        '''
        Handles events by delegating to State (which handles quitting
        in general) and by reacting to key presses and mouse clicks.
        If a key is pressed or the mouse is clicked, self.finish is set to true.
        '''
        State.handle(self, event)
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.finished = 1

    def update(self, game):
        '''
        Update the level. If a key has been pressed or the mouse has been
        clicked (i.e., self.finished is true), tell the game to move to
        the state represented by self.next_state().
        '''
        if self.finished:
            game.next_state = self.next_state()

    def first_display(self, screen):
        '''
        The first time the Paused state is displayed, draw the image (if any)
        and render the text.
        '''
        # first, clear the screen by filling it with the background color
        screen.fill(config.background_color)

        # create a Font object with the deafult appearance, and specified size
        font = pygame.font.Font(None, config.font_size)

        # get the lines of text om self.text, ignoring empty lines at the top
        # or bottom
        lines = self.text.strip().splitlines()

        # calculate the height of the text(using font.get_linesize() to get
        # the height of each line of text)
        height = len(lines) * font.get_linesize()

        # calculate the placement of the text (centered on the screen)
        center, top = screen.get_rect().center
        top -= height // 2

        # if there is an image to display
        if self.image:
            # load it
            image = pygame.image.load(self.image).convert()
            # get its rect
            r = image.get_rect()
            # move the text down by half the image height
            top += r.height // 2
            # place the image 20 pixels above the text
            r.midbottom = center, top - 20
            # blit the image to the screen
            screen.blit(image, r)

        antialias = 1 # smooth text
        black = 0, 0, 0 # render it as black

        # render all lines, starting at the calculated top, and move down
        # font.get_linesize() pixels for each line
        for line in lines:
            text = font.render(line.strip(), antialias, black)
            r = text.get_rect()
            r.midtop = center, top
            screen.blit(text, r)
            top += font.get_linesize()

        # display all the changes
        pygame.display.flip()


class Info(Paused):

    '''
    A simple paused state that displays some information about the game.
    It is followed by a Level state (the first level).
    '''
    next_state = Level
    text = '''
    In this game you are an alien in outer space,
    trying to survive the fighter planes coming from planet Earth wanting
    to rescue their astronauts (your food) and kill you.
    '''


class StartUp(Paused):

    '''
    A paused state that displays an Alien image and a welcome message.
    It is followed by an Info state.
    '''
    next_state = Info
    image = config.alien_lg_image
    text = '''
    Welcome to Alian Survival
    '''


class LevelCleared(Paused):

    '''
    A paused state that informs the user that they have cleared a given level.
    It is followed by the next level state.
    '''

    def __init__(self, number):
        self.number = number
        self.text = '''
        Level {} cleared
        Click to start next level'''.format(self.number)

    def next_state(self):
        return Level(self.number + 1)


class GameOver(Paused):

    '''
    A State that infroms the user that they have lost the game.
    It is followed by the first level.
    '''

    next_state = Level
    text = '''
    Game Over
    Click to Restart, Esc to Quit
    '''


class Game:

    '''
    A game object that takes care of the main event loop, including changing
    between the different game states.
    '''

    def __init__(self, *args):
        # get the directory where the game and the images are locates
        path = os.path.abspath(args[0])
        dir = os.path.split(path)[0]
        # move to that directory (so that the image files may be
        # opened later on)
        os.chdir(dir)
        # start with no state
        self.state = None
        # move to StartUp in the first even loop iteration
        self.next_state = StartUp()

    def run(self):
        '''
        This method sets things in motion. It performs some vital
        initialisation tasks, and enters the main event loop.
        '''
        pygame.init()# this is needed to initialise all the pygame modules
        pygame.mixer.music.play(loops=-1)# this is looping the background music

        # decide whether to display the game in a window or to use full screen
        flag = 1 # default mode

        if config.full_screen:
            flag = FULLSCREEN # full screen mode
        screen_size = config.screen_size
        screen = pygame.display.set_mode(screen_size, flag)

        pygame.display.set_caption('Alian Survival')
        pygame.mouse.set_visible(False)

        # the main loop
        while True:
            config.clock.tick(config.FPS)
            # (1) if nextState has been changed, move to the new state
            # and display it (for the first time)
            if self.state != self.next_state:
                self.state = self.next_state
                self.state.first_display(screen)
            # (2) delegate the event handling to the current state
            for event in pygame.event.get():
                self.state.handle(event)
            # (3) update the current state
            self.state.update(self)
            # (4) display the current state
            self.state.display(screen)



if __name__ == '__main__':
    game = Game(*sys.argv)
    game.run()
