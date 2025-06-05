#!/usr/bin/env python3

"""
Created by: D. Jeffrey
Created on: June 2025
This module converts a string into hex unicode
"""

import stage
import ugame


def game_scene() -> None:
    """ This function is the main game game_scene """
    
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()
    
    while True:
        # to make code repeat forever
        pass


if __name__ = "__main__":
    game_scene()
