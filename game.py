#!/usr/bin/env python3

"""
Created by: D. Jeffrey
Created on: June 2025
This module is a duck hunt clone
"""

import stage
import ugame
import time
import random
import supervisor

import constants

 
def menu_scene() -> None:
    """ This function is the main menu  """
    
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(20,10)
    text1.text("MT Game Studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40,110)
    text2.text("PRESS START")
    text.append(text2)
    
    
    # putting background on screen
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)

    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white
    

    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()
    
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            bug_hunt_menu_scene()

        # redraw sprites
        game.tick()

def bug_hunt_menu_scene() -> None:
    """ This function is the second menu screen for bug hunt """
    
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    

    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.WHITE_BLACK_PALETTE, buffer=None)
    text1.move(50,10)
    text1.text("BUG HUNT")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.WHITE_BLACK_PALETTE, buffer=None)
    text2.move(35,30)
    text2.text("PRESS SELECT")
    text.append(text2)
    
    
    text3 = stage.Text(width=29, height=12, font=None, palette=constants.WHITE_BLACK_PALETTE, buffer=None)
    text3.move(45,95)
    text3.text("PRESS 'A'")
    text.append(text3)
    
    
    text4 = stage.Text(width=29, height=12, font=None, palette=constants.WHITE_BLACK_PALETTE, buffer=None)
    text4.move(35,105)
    text4.text("FOR CREDITS")
    text.append(text4)
    
    # putting background on screen
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)
   
    image_bank_sprites = stage.Bank.from_bmp16("bug_hunt_sprites.bmp")
    
    scope = stage.Sprite(image_bank_sprites, 2, 72, 74)
    bug = stage.Sprite(image_bank_sprites, 6, 72, 54)
    
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [scope] + [bug] + [background]
    game.render_block()
    
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_SELECT != 0:
            sound.play(pew_sound)
            game_scene()
            
        if keys & ugame.K_O != 0:
            credits()

        # redraw sprites
        game.tick()


def credits() -> None:
    """this function prints the credits"""

    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    background = stage.Grid(image_bank_mt_background, constants.SCREEN_X,
                            constants.SCREEN_Y)
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.WHITE_BLACK_PALETTE, buffer=None)
    text1.move(5,10)
    text1.text("Created by: D.J")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.WHITE_BLACK_PALETTE, buffer=None)
    text2.move(5,30)
    text2.text("Created 08/25")
    text.append(text2)
    
    
    text3 = stage.Text(width=29, height=12, font=None, palette=constants.WHITE_BLACK_PALETTE, buffer=None)
    text3.move(5,50)
    text3.text("Shoot the bugs!")
    text.append(text3)
    
    text4 = stage.Text(width=29, height=12, font=None, palette=constants.WHITE_BLACK_PALETTE, buffer=None)
    text4.move(5,90)
    text4.text("PRESS SELECT")
    text.append(text4)
    
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()


        game.tick()

def game_scene() -> None:
    """ This function is the main game game_scene """
    
    # score keeping/display
    score = 0
    
    score_text = stage.Text(width=29, height=14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text("Score: {0}".format(score))
    

    def show_bug():
        """ This function places an bug on the screen """
        for bug_number in range(len(bugs)):
            if bugs[bug_number].x < 0:
                bugs[bug_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                        constants.SCREEN_X - constants.SPRITE_SIZE), 100)
            
                break
            
    def show_good_bug():
        """ This function places an alien on the screen """
        for bug_number in range(len(good_bugs)):
            if good_bugs[bug_number].x < 0:
                good_bugs[bug_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                        constants.SCREEN_X - constants.SPRITE_SIZE), 100)
            
                break
            
    def show_bomb():
        """ This function places an alien on the screen """
        for bomb_number in range(len(bombs)):
            if bombs[bomb_number].x < 0:
                bombs[bomb_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                        constants.SCREEN_X - constants.SPRITE_SIZE), 100)
            
                break

    score = 0

    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("bug_hunt_sprites.bmp")
    
    # buttons to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]
    boom_sound = open("boom.wav", 'rb')
    pew_sound = open("pew.wav", 'rb')
    gun_sound = open("crash.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    
    # putting background on screen
    background = stage.Grid(image_bank_sprites, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    
    """ for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(1,3)
            background.tile(x_location, y_locaiton, tile_picked)"""
    
    scope = stage.Sprite(image_bank_sprites, 2, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))
    explosion = stage.Sprite(image_bank_sprites, 3, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
    
    # create list of aliens
    bugs = []
    for bug_number in range(constants.TOTAL_NUMBER_OF_BUGS):
        a_single_bug = stage.Sprite(image_bank_sprites, 1,
                                    constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y)
        bugs.append(a_single_bug)
    
    show_bug()
    
    bombs = []
    for bomb_number in range(constants.TOTAL_NUMBER_OF_BOMBS):
        a_single_bomb = stage.Sprite(image_bank_sprites, 4,
                                    constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y)
        bombs.append(a_single_bomb)
    
    show_bomb()
    
    good_bugs = []
    for bug_number in range(1):
        a_single_bug = stage.Sprite(image_bank_sprites, 7,
                                    constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y)
        good_bugs.append(a_single_bug)
    
    shots = []
    for shot_number in range(constants.TOTAL_NUMBER_OF_SHOTS):
        a_single_shot = stage.Sprite(image_bank_sprites, 5,
                                    constants.OFF_SCREEN_X,
                                    constants.OFF_SCREEN_Y)
        shots.append(a_single_shot)

    # create stage background, load layers
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = [explosion] + [score_text] + shots + [scope] + bombs + good_bugs + bugs + [background]
    game.render_block()
    
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        
        # B button
        if keys & ugame.K_X:
            pass
        
        # A button
        if keys & ugame.K_O:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
            else:
                if a_button == constants.button_state["button_still_pressed"]:
                    a_button = constants.button_state["button_released"]
                else:
                    a_button = constants.button_state["button_up"]
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        
        if keys & ugame.K_RIGHT:
            if scope.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                scope.move(scope.x + constants.SCOPE_SPEED, scope.y)
            else:
                scope.move(constants.SCREEN_X - constants.SPRITE_SIZE, scope.y)
        
        if keys & ugame.K_LEFT:
            if scope.x >= 0: 
                scope.move(scope.x - constants.SCOPE_SPEED, scope.y)
            else:
                scope.move(0, scope.y)
                
        if keys & ugame.K_UP:
            if scope.y > 0: 
                scope.move(scope.x, scope.y - constants.SCOPE_SPEED)
            else:
                scope.move(scope.x, 0)
            
        if keys & ugame.K_DOWN:
            if scope.y < constants.SCREEN_Y - constants.SPRITE_SIZE:
                scope.move(scope.x, scope.y + constants.SCOPE_SPEED)
            else:
                scope.move(scope.x, constants.SCREEN_Y - constants.SPRITE_SIZE)
        
        # update game logic
        if a_button == constants.button_state["button_just_pressed"]:
            shots[1].move(scope.x, scope.y)
            sound.play(boom_sound)

                                            
        for bug_number in range(len(bugs)):
                bugs[bug_number].move(bugs[bug_number].x - random.choice(constants.HORIZONTAL_SPEED_LIST),
                                        bugs[bug_number].y - random.choice(constants.VERICAL_SPEED_LIST))

                # if alien not on screen, move to offscreen location
                if bugs[bug_number].y < 0:
                    bugs[bug_number].move(constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
                    show_bug()
                    show_bug()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text("Score: {0}".format(score))

        for bug_number in range(len(good_bugs)):
                good_bugs[bug_number].move(good_bugs[bug_number].x - random.choice(constants.HORIZONTAL_SPEED_LIST),
                                        good_bugs[bug_number].y - random.choice(constants.VERICAL_SPEED_LIST))

                # if bug not on screen, move to offscreen location
                if good_bugs[bug_number].y < 0:
                    good_bugs[bug_number].move(constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
                    show_good_bug()

        for bomb_number in range(len(bombs)):
            bombs[bomb_number].move(bombs[bomb_number].x - random.choice(constants.HORIZONTAL_SPEED_LIST),
                                        bombs[bomb_number].y - random.choice(constants.VERICAL_SPEED_LIST))
            if bombs[bomb_number].y < 0:
                bombs[bomb_number].move(constants.OFF_SCREEN_X,constants.OFF_SCREEN_Y)
                show_bomb()
        
        # bug collision
        for shot_number in range(len(shots)):
            if shots[shot_number].x > 0:
                for bug_number in range(len(bugs)):
                    if bugs[bug_number].x > 0:
                        if stage.collide(shots[shot_number].x, shots[shot_number].y,
                                        shots[shot_number].x + 16, shots[shot_number].y + 16,
                                        bugs[bug_number].x + 1, bugs[bug_number].y,
                                        bugs[bug_number].x + 15, bugs[bug_number].y + 15):
                            bugs[bug_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            shots[shot_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            show_bug()
                            show_bug()
                            score += 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text("Score: {0}".format(score))

        # bomb collision
        for shot_number in range(len(shots)):
            if shots[shot_number].x > 0:
                for bomb_number in range(len(bombs)):
                    if bombs[bomb_number].x > 0:
                        if stage.collide(shots[shot_number].x, shots[shot_number].y,
                                        shots[shot_number].x + 16, shots[shot_number].y + 16,
                                        bombs[bomb_number].x + 1, bombs[bomb_number].y,
                                        bombs[bomb_number].x + 15, bombs[bomb_number].y + 15):
                            bombs[bomb_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            shots[shot_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            explosion.move(scope.x, scope.y)
                            sound.stop()
                            sound.play(gun_sound)
                            time.sleep(2)
                            game_over_scene(score)

        # good bug collision
        for shot_number in range(len(shots)):
            if shots[shot_number].x > 0:
                for bug_number in range(len(good_bugs)):
                    if good_bugs[bug_number].x > 0:
                        if stage.collide(shots[shot_number].x, shots[shot_number].y,
                                        shots[shot_number].x + 16, shots[shot_number].y + 16,
                                        good_bugs[bug_number].x + 1, good_bugs[bug_number].y,
                                        good_bugs[bug_number].x + 15, good_bugs[bug_number].y + 15):
                            good_bugs[bug_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            shots[shot_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(pew_sound)
                            show_good_bug()
                            score -= 1
                            if score < 0:
                                score = 0
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text("Score: {0}".format(score))
                            
        
        # redraw sprites
        game.render_sprites([explosion] + shots + [scope] + bombs + bugs + good_bugs)
        game.tick()

def game_over_scene(final_score):
    """ this function prints the game over scene """
    
    sound = ugame.audio
    sound.stop()
    
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
                            
    
    text = []
    text1 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text1.move(22,20)
    text1.text("Final Score: {:0>2d}".format(final_score))
    text.append(text1)
    
    text2 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text2.move(43,60)
    text2.text("GAME OVER")
    text.append(text2)
    
    text3 = stage.Text(width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None)
    text3.move(32,110)
    text3.text("PRESS SELECT")
    text.append(text3)
    
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = text + [background]
    game.render_block()
    
    while True:
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_SELECT != 0:
            supervisor.reload()


        game.tick()


if __name__ == "__main__":
    menu_scene()
    
