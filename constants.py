#!/usr/bin/env python3

"""
Created by: D. Jeffrey
Created on: June 2025
This constants file is for the Tron game
"""

# PyBadge screen size is 160 x 128 and sprites are 16 x 16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_BUGS = 3
TOTAL_NUMBER_OF_BOMBS = 1
TOTAL_NUMBER_OF_SHOTS = 5
FPS = 60
SCOPE_SPEED = 1.5
BUG_SPEED_MIN = 0.8
BUG_SPEED_MAX = 1.2
HORIZONTAL_SPEED_LIST = [-1, 1]
VERICAL_SPEED_LIST = [0.5, 0.6, 0.7, 0.8]

BOMB_SPEED_MIN = 0.8
BOMB_SPEED_MAX = 1.2
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
SPRITE_MOVEMENT_SPEED = 1

# button state
button_state = {"button_up": "up",
"button_just_pressed": "just pressed",
"button_still_pressed": "stil pressed",
"button_released": "released"
}

WHITE_BLACK_PALETTE = (
    b"\xf8\x1f\x00\x00\xcey\xff\xff\xf8\x1f\x00\x19\xfc\xe0\xfd\xe0"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
RED_PALETTE = (
    b"\xff\xff\x00\x00\xcey\x66\xff\xff\xff\xff\xff\xff\xff\xfd\xe0"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
)
BLUE_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
