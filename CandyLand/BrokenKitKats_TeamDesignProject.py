#By submitting this assignment, I agree to the following:
#"Aggies do not lie, cheat, or steal, or tolerate those who do."
#"I have not given or received any unauthorized aid on this assignment."
#
# Name: Celine Moumouris, Adittya Patil, Kevin Rivera, Charlie Hendon
# Section: 535
# Assignment: Lab 12a Act 1
# Date: 11-24-2020


# Module pygame is imported for the use of its user interface when presenting the board, pieces,
# buttons to choose from and visuals. Module random is imported solely for the use of randomizing
# the card chosen when getting a card from the deck during the game.

import pygame
import random

# starts the pygame gui

pygame.init()

# Title of game and set to be the window's title when it opens up

pygame.display.set_caption("Candy Land")

# Variable icon is set equal to the candies icon image. Program then sets the display icon to be as the variable
# icon

icon = pygame.image.load('candies_icon.png')
pygame.display.set_icon(icon)

# Variable board is set equal to the CandyLand board image.

board = pygame.image.load("Candyland_complex.png")

# creating global variables in order to use them all across several functions

global player_one
global gummy_bear_red
global gummy_bear_purple
global gummy_bear_pink
global gummy_bear_blue
global gummy_bear_green
global gummy_bear_yellow
global player_two
global computer
global colored_spots
global list_of_cards
global list_of_cards_used
global cards
global screen
global single_yellow
global single_green
global single_blue
global single_orange
global single_red
global single_purple
global double_yellow
global double_green
global double_blue
global double_orange
global double_red
global double_purple
global candy_cane_card
global gingerbread_card
global peanut_card
global gum_drop_card
global ice_cream_card
global lollipop_card
global card_deck, deck_highlight
global card_image
global starting_spot, winner

# setting image calls equal to global variables

candies = 'candies_icon.png'
gummy_bear_red = 'gummy-bear-red.png'
gummy_bear_purple = 'gummy-bear-purple.png'
gummy_bear_pink = 'gummy-bear-pink.png'
gummy_bear_yellow = 'gummy-bear-yellow.png'
gummy_bear_green = 'gummy-bear-green.png'
gummy_bear_blue = 'gummy-bear-blue.png'
computer = 'gummy-bear-orange.png'
single_red = 'Single-red-card.png'
single_yellow = 'Single-yellow-card.png'
single_green = 'Single-green-card.png'
single_purple = 'Single-purple-card.png'
single_blue = 'Single-blue-card.png'
single_orange = 'Single-orange-card.png'
double_blue = "Double-blue-card.png"
double_red = 'Double-red-card.png'
double_green = 'Double-green-card.png'
double_orange = 'Double-orange-card.png'
double_purple = 'Double-purple-card.png'
double_yellow = 'Double-yellow-card.png'
gumdrop_card = 'Gumdrop-card.png'
ice_cream_card = 'Ice-cream-card.png'
lollipop_card = "Lollipop-card.png"
peanut_card = 'Peanut-card.png'
gingerbread_card = 'Gingerbread-card.png'
candy_cane_card = 'Candy-cane-card.png'
card_deck = 'Deck-of-cards.png'
deck_highlight = 'Deck-of-cards-highlighted.png'

# Variable screen is set equal to the display window screen size, length and height
# hardcode to 1280 and 800

screen = pygame.display.set_mode((1280, 800))

# Variable called starting_spot set equal to True in order for the program to properly position the player chosen
# character/icons, gummy bears, to their starting spot on the board when the game first starts

starting_spot = True

# Setting up the lists and dictionaries to find and generate the cards

# The dictionary below called colored_spots contains each spot able to be moved too on the board.
# The keys are integer values that represent the numbering of the board if one was to count each spot starting from the
# beginning and the values the keys are set to are the colors or special characters of that specific spot.

colored_spots = {1: 'red', 2: 'purple', 3: 'yellow', 4: 'blue', 5: 'orange', 6: 'green', 7: 'red', 8: 'purple',
                 9: 'gingerbread', 10: 'yellow', 11: 'blue', 12: 'orange', 13: 'green', 14: 'red', 15: 'purple',
                 16: 'yellow', 17: 'blue', 18: 'orange', 19: 'green', 20: 'candy-cane', 21: 'red', 22: 'purple',
                 23: 'yellow', 24: 'blue', 25: 'orange', 26: 'green', 27: 'red', 28: 'purple', 29: 'yellow',
                 30: 'blue', 31: 'orange', 32: 'green', 33: 'red', 34: 'purple', 35: 'yellow', 36: 'blue',
                 37: 'orange', 38: 'green', 39: 'red', 40: 'purple', 41: 'yellow', 42: 'gumdrop', 43: 'blue',
                 44: 'orange', 45: 'green', 46: 'orange', 47: 'purple', 48: 'yellow', 49: 'blue', 50: 'orange',
                 51: 'green', 52: 'red', 53: 'purple', 54: 'yellow', 55: 'blue', 56: 'orange', 57: 'green',
                 58: 'red', 59: 'purple', 60: 'yellow', 61: 'blue', 62: 'orange', 63: 'green', 64: 'red',
                 65: 'purple', 66: 'yellow', 67: 'blue', 68: 'orange', 69: 'peanut', 70: 'green', 71: 'red',
                 72: 'purple', 73: 'yellow', 74: 'blue', 75: 'orange', 76: 'green', 77: 'red', 78: 'purple',
                 79: 'yellow', 80: 'blue', 81: 'orange', 82: 'green', 83: 'red', 84: 'purple', 85: 'yellow',
                 86: 'blue', 87: 'orange', 88: 'green', 89: 'red', 90: 'purple', 91: 'yellow', 92: 'lollipop',
                 93: 'blue', 94: 'orange', 95: 'green', 96: 'red', 97: 'purple', 98: 'yellow', 99: 'blue',
                 100: 'orange', 101: 'green', 102: 'ice cream', 103: 'red', 104: 'purple', 105: 'yellow',
                 106: 'blue', 107: 'orange', 108: 'green', 109: 'red', 110: 'purple', 111: 'yellow', 112: 'blue',
                 113: 'orange', 114: 'green', 115: 'red', 116: 'purple', 117: 'yellow', 118: 'blue', 119: 'orange',
                 120: 'green', 121: 'red', 122: 'purple', 123: 'yellow', 124: 'blue', 125: 'orange', 126: 'green',
                 127: 'red', 128: 'purple', 129: 'yellow', 130: 'blue', 131: 'orange', 132: 'green', 133: 'red',
                 134: 'rainbow'}

# List called list_of_cards contains a list of integers that would be associated with the following dictionary
# called cards where whatever random number is pulled from list_of_cards will be used to find and locate
# the integer's associated card color or character from the dictionary.

list_of_cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]

# List called list_of_used_cards is made and set to be empty at first. The list will insert any removed special
# character cards from list_of_cards such as a gingerbread card or lollipop card in order for them
# not to be pulled again.

list_of_used_cards = []

# Dictionary called cards is made to hold all the values of each integer and its relation to what card it would
# represent. The keys are the integers and their values are strings representing the card.

cards = {0: 'single-yellow', 1: 'single-red', 2: 'single-purple', 3: 'single-green', 4: 'single-blue',
         5: 'single-orange', 6: 'ice cream', 7: 'double-red', 8: 'double-green', 9: 'double-yellow',
         10: 'double-purple', 11: 'double-blue', 12: 'double-orange', 13: 'candy-cane', 14: 'single-red',
         15: 'single-green', 16: 'single-yellow', 17: 'single-blue', 18: 'single-orange', 19: 'single-purple',
         20: 'gingerbread', 21: 'double-red', 22: 'double-green', 23: 'double-orange', 24: 'double-blue',
         25: 'double-yellow', 26: 'double-purple', 27: 'lollipop', 28: 'single-red', 29: 'single-blue',
         30: 'single-green', 31: 'single-orange', 32: 'single-yellow', 33: 'single-purple', 34: 'double-red',
         35: 'double-green', 36: 'double-orange', 37: 'double-blue', 38: 'double-yellow', 39: 'double-purple',
         40: 'gumdrop', 41: 'single-red', 42: 'single-green', 43: 'single-orange', 44: 'single-blue',
         45: 'single-yellow', 46: 'single-purple', 47: 'peanut', 48: 'double-red', 49: 'double-blue',
         50: 'double-yellow', 51: 'double-purple', 52: 'single-red', 53: 'single-green', 54: 'single-blue',
         55: 'single-orange', 56: 'single-yellow', 57: 'single-purple', 58: 'single-red', 59: 'single-green',
         60: 'single-orange', 61: 'single-blue', 62: 'single-yellow', 63: 'single-purple'}

# In order to associate where the player's chosen character will go to, several dictionaries are created to
# associate the board spot to its x and y value within the created window.

# The two dictionaries, board_locations_player1_x_coordinates and board_locations_player1_y_coordinates are created
# for the coordinates for player1's character/icon to go to; x and y respectively.

board_locations_player1_x_coordinates = {0: 280, 1: 380, 2: 420, 3: 460, 4: 475, 5: 495, 6: 520, 7: 560, 8: 605, 9: 655,
                                         10: 705, 11: 730, 12: 765, 13: 795, 14: 825, 15: 860, 16: 905, 17: 945,
                                         18: 980, 19: 1000, 20: 1015, 21: 1000, 22: 970, 23: 930, 24: 888, 25: 845,
                                         26: 800, 27: 755, 28: 720, 29: 720, 30: 760, 31: 810, 32: 855, 33: 898,
                                         34: 938, 35: 976, 36: 1016, 37: 1051, 38: 1082, 39: 1111, 40: 1110, 41: 1085,
                                         42: 1065, 43: 1020, 44: 981, 45: 941, 46: 898, 47: 869, 48: 833, 49: 797,
                                         50: 758, 51: 713, 52: 668, 53: 632, 54: 586, 55: 553, 56: 526, 57: 501,
                                         58: 477, 59: 447, 60: 414, 61: 378, 62: 342, 63: 303, 64: 272, 65: 250,
                                         66: 256, 67: 269, 68: 312, 69: 352, 70: 387, 71: 426, 72: 464, 73: 500,
                                         74: 498, 75: 462, 76: 431, 77: 415, 78: 410, 79: 448, 80: 489, 81: 535,
                                         82: 571, 83: 611, 84: 648, 85: 686, 86: 721, 87: 763, 88: 802, 89: 843,
                                         90: 889, 91: 927, 92: 970, 93: 1009, 94: 1047, 95: 1079, 96: 1118, 97: 1120,
                                         98: 1097, 99: 1079, 100: 1049, 101: 1025, 102: 994, 103: 975, 104: 929,
                                         105: 891, 106: 870, 107: 851, 108: 830, 109: 799, 110: 763, 111: 725,
                                         112: 689, 113: 656, 114: 620, 115: 577, 116: 537, 117: 491, 118: 450,
                                         119: 410, 120: 355, 121: 336, 122: 306, 123: 281, 124: 278, 125: 287,
                                         126: 320, 127: 358, 128: 401, 129: 442, 130: 480, 131: 509, 132: 545,
                                         133: 576, 134: 616}

board_locations_player1_y_coordinates = {0: 730, 1: 725, 2: 725, 3: 715, 4: 695, 5: 660, 6: 625, 7: 610, 8: 605, 9: 605,
                                         10: 620, 11: 650, 12: 680, 13: 700, 14: 725, 15: 735, 16: 740, 17: 740,
                                         18: 735, 19: 715, 20: 695, 21: 670, 22: 670, 23: 660, 24: 666, 25: 666,
                                         26: 660, 27: 640, 28: 600, 29: 550, 30: 510, 31: 510, 32: 525, 33: 556,
                                         34: 580, 35: 594, 36: 601, 37: 594, 38: 577, 39: 545, 40: 499, 41: 462,
                                         42: 449, 43: 443, 44: 457, 45: 473, 46: 476, 47: 463, 48: 439, 49: 415,
                                         50: 394, 51: 387, 52: 387, 53: 399, 54: 424, 55: 454, 56: 486, 57: 521,
                                         58: 550, 59: 570, 60: 583, 61: 576, 62: 584, 63: 573, 64: 552, 65: 509,
                                         66: 474, 67: 433, 68: 434, 69: 429, 70: 441, 71: 452, 72: 453, 73: 456,
                                         74: 388, 75: 363, 76: 343, 77: 314, 78: 271, 79: 243, 80: 236, 81: 241,
                                         82: 256, 83: 274, 84: 296, 85: 317, 86: 334, 87: 352, 88: 360, 89: 371,
                                         90: 378, 91: 380, 92: 381, 93: 376, 94: 366, 95: 349, 96: 323, 97: 277,
                                         98: 235, 99: 222, 100: 200, 101: 150, 102: 109, 103: 105, 104: 110,
                                         105: 138, 106: 173, 107: 213, 108: 248, 109: 275, 110: 283, 111: 274,
                                         112: 254, 113: 232, 114: 210, 115: 191, 116: 187, 117: 188, 118: 194,
                                         119: 199, 120: 219, 121: 195, 122: 178, 123: 138, 124: 105, 125: 59,
                                         126: 32, 127: 23, 128: 21, 129: 34, 130: 55, 131: 76, 132: 100,
                                         133: 117, 134: 132}

# The two dictionaries, board_locations_player2_x_coordinates and board_locations_player2_y_coordinates are created
# for the coordinates for player2's character/icon to go to; x and y respectively.

board_locations_player2_x_coordinates = {0: 320, 1: 400, 2: 440, 3: 480, 4: 505, 5: 525, 6: 545, 7: 580, 8: 620, 9: 655,
                                         10: 685, 11: 710, 12: 740, 13: 770, 14: 815, 15: 850, 16: 890, 17: 930,
                                         18: 980, 19: 1020, 20: 1045, 21: 1025, 22: 970, 23: 930, 24: 888, 25: 845,
                                         26: 810, 27: 775, 28: 755, 29: 750, 30: 775, 31: 805, 32: 840, 33: 874,
                                         34: 910, 35: 952, 36: 996, 37: 1035, 38: 1075, 39: 1089, 40: 1096, 41: 1085,
                                         42: 1045, 43: 1003, 44: 962, 45: 919, 46: 875, 47: 836, 48: 808, 49: 768,
                                         50: 730, 51: 690, 52: 649, 53: 613, 54: 580, 55: 553, 56: 530, 57: 504,
                                         58: 474, 59: 437, 60: 398, 61: 355, 62: 318, 63: 284, 64: 265, 65: 241,
                                         66: 233, 67: 263, 68: 290, 69: 325, 70: 367, 71: 401, 72: 442, 73: 486,
                                         74: 490, 75: 473, 76: 421, 77: 406, 78: 414, 79: 435, 80: 470, 81: 505,
                                         82: 546, 83: 585, 84: 620, 85: 657, 86: 695, 87: 736, 88: 776, 89: 818,
                                         90: 861, 91: 901, 92: 946, 93: 990, 94: 1031, 95: 1072, 96: 1105, 97: 1104,
                                         98: 1097, 99: 1072, 100: 1037, 101: 1013, 102: 998, 103: 952, 104: 918,
                                         105: 893, 106: 877, 107: 855, 108: 826, 109: 783, 110: 740, 111: 690,
                                         112: 661, 113: 628, 114: 590, 115: 551, 116: 511, 117: 470, 118: 433,
                                         119: 390, 120: 353, 121: 311, 122: 280, 123: 270, 124: 259, 125: 286,
                                         126: 310, 127: 346, 128: 379, 129: 414, 130: 450, 131: 479, 132: 516,
                                         133: 550, 134: 590}
board_locations_player2_y_coordinates = {0: 730, 1: 760, 2: 760, 3: 745, 4: 715, 5: 675, 6: 650, 7: 635, 8: 640, 9: 640,
                                         10: 655, 11: 680, 12: 700, 13: 730, 14: 755, 15: 770, 16: 770, 17: 770,
                                         18: 765, 19: 745, 20: 695, 21: 650, 22: 640, 23: 630, 24: 635, 25: 635,
                                         26: 625, 27: 615, 28: 590, 29: 560, 30: 540, 31: 540, 32: 560, 33: 575,
                                         34: 590, 35: 610, 36: 615, 37: 616, 38: 597, 39: 557, 40: 521, 41: 488,
                                         42: 460, 43: 473, 44: 484, 45: 494, 46: 489, 47: 466, 48: 441, 49: 420,
                                         50: 409, 51: 404, 52: 412, 53: 429, 54: 455, 55: 480, 56: 514, 57: 548,
                                         58: 575, 59: 597, 60: 602, 61: 608, 62: 596, 63: 577, 64: 566, 65: 539,
                                         66: 486, 67: 456, 68: 443, 69: 445, 70: 452, 71: 465, 72: 472, 73: 460,
                                         74: 418, 75: 386, 76: 359, 77: 340, 78: 297, 79: 271, 80: 254, 81: 255,
                                         82: 265, 83: 281, 84: 299, 85: 322, 86: 341, 87: 360, 88: 370, 89: 382,
                                         90: 391, 91: 398, 92: 399, 93: 396, 94: 390, 95: 372, 96: 345, 97: 299,
                                         98: 263, 99: 236, 100: 216, 101: 177, 102: 140, 103: 124, 104: 137,
                                         105: 167, 106: 204, 107: 245, 108: 278, 109: 295, 110: 295, 111: 282,
                                         112: 256, 113: 236, 114: 214, 115: 205, 116: 204, 117: 208, 118: 215,
                                         119: 222, 120: 217, 121: 206, 122: 179, 123: 162, 124: 119, 125: 82,
                                         126: 55, 127: 39, 128: 34, 129: 44, 130: 58, 131: 80, 132: 103,
                                         133: 124, 134: 142}

# Variable font is created and set equal to the Font Constantia and has a size of 30 using the pygame font SysFont
# function.

font = pygame.font.SysFont('Constantia', 30)

# Defining all needed colors and naming them into their respective variable association for later use in the program
# to call back to.

pink = (255, 182, 193)
purple = (102, 0, 102)
buttonPinkDark = (204, 0, 102)
buttonPinkLight = (255, 0, 127)
buttonBlueDark = (76, 0, 153)
buttonBlueLight = (102, 0, 204)
grey = (0, 0, 0)
bg = (204, 102, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# In order to utilize the clock function for how fast the frame of the windows should go, variable clock
# is set to the pygame time clock function.

clock = pygame.time.Clock()

# Variables menu_width and menu_height define the menu's window size in terms of width and height respectively. Both
# variables are set equal to 500. Variable menu_screen is set equal to the function pygame display set_mode
# with parameters of variables menu_width and menu_height to be called back to frequently throughout the program.

menu_width = 500
menu_height = 500
menu_screen = pygame.display.set_mode((menu_width, menu_height))

# Variables piece_menu_width and piece_menu_height define the piece selection menu window size in terms of width and
# height respectively; piece_menu_width is set to 900 and piece_menu_height is set to 600. Variable piece_menu is set
# equal to the function pygame display set_mode with parameters of variables piece_menu_width and piece_menu_height
# to be called back to frequently throughout the program.

piece_menu_width = 900
piece_menu_height = 600
piece_menu = pygame.display.set_mode((piece_menu_width, piece_menu_height))


# Function below called text_display has parameters text and font. The function simply sets text preferences and
# returns them


def text_display(text, font):
    ''''Displays text within a text boxl. Has parameters text and font.'''
    # The variable textSurface is set equal to the result of the function font render with parameters
    # text, True and purple. Afterwards the program returns textSurface while calling the function
    # textSurface.get_rect.

    textSurface = font.render(text, True, purple)
    return textSurface, textSurface.get_rect()


# Function below called text_button has parameters text and font. The function simply sets text preferences and
# returns them


def text_button(text, font):
    ''''Displays text within a button. Has parameters text and font.'''
    # The variable textSurface is set equal to the result of the function font render with parameters
    # text, True and grey. Afterwards the program returns textSurface while calling the function
    # textSurface.get_rect.

    textSurface = font.render(text, True, grey)
    return textSurface, textSurface.get_rect()


# Function below called player1 has parameters img, x and y. The function simply displays the player's character image
# onto the screen.


def player1(img, x, y):
    '''Function to put player 1 candy on screen. Has parameters img, x and y.'''
    # Selecting the candy for player one and displaying it on the game board

    player1_Img = pygame.image.load(img)
    screen.blit(player1_Img, (x, y))


# Function below called player2 has parameters img, x and y. The function simply displays the player's character image
# onto the screen.


def player2(img, X, Y):
    '''Function to put player 2 candy on screen. Has parameters img, X and Y.'''
    # Selecting the candy for player two and displaying it on the game board

    player2_Img = pygame.image.load(img)
    screen.blit(player2_Img, (X, Y))


# The function below called starting_spot_player1 has parameter img. The function simply sets the player coordinates
# to be designated at the starting spot of the board and display it onto the board.


def starting_spot_player1(img):
    '''Function to display player 1 candy on starting spot of board. Has parameter img'''
    # Loading the candy of player one onto the gameboard

    player1_Img = pygame.image.load(img)

    # Setting the initial x and y coordinates of the player on the board

    x_coord = board_locations_player1_x_coordinates.get(0)
    y_coord = board_locations_player1_y_coordinates.get(0)

    # Displaying player's candy onto the board with designated coordinates.

    screen.blit(player1_Img, (x_coord, y_coord))


# The function below called starting_spot_player2 has parameter img. The function simply sets the player coordinates
# to be designated at the starting spot of the board and display it onto the board.


def starting_spot_player2(img):
    '''Function to display player 2 candy on starting spot of board'''
    # Loading the candy of player two onto the gameboard

    player2_Img = pygame.image.load(img)

    # Setting the initial x and y coordinates of the player on the board

    x_coord = board_locations_player2_x_coordinates.get(0)
    y_coord = board_locations_player2_y_coordinates.get(0)

    # Displaying player's candy onto the board with designated coordinates.

    screen.blit(player2_Img, (x_coord, y_coord))


# The function below called start_buttons has parameters txt, x_pos, y_pos, width, height, light, dark and choice.
# The function creates buttons for the start menu


def start_buttons(txt, x_pos, y_pos, width, height, light, dark, choice=None):
    '''Function to help make buttons on start menu. Has parameters txt, x_pos, y_pos, width, height, light, dark and
    choice.'''

    # finds the mouse position

    mouse_pos = pygame.mouse.get_pos()

    # finds if the mouse buttons have been pressed or not

    when_clicked = pygame.mouse.get_pressed()

    # sees where the mouse is so that it can change the color of the box

    if x_pos + width > mouse_pos[0] > x_pos and y_pos + height > mouse_pos[1] > y_pos:
        pygame.draw.rect(menu_screen, light, (x_pos, y_pos, width, height))

        # when the mouse is clicked, it goes to the function that it has been told to go to

        if when_clicked[0] == 1 and choice != None:
            choice()
    else:
        pygame.draw.rect(menu_screen, dark, (x_pos, y_pos, width, height))

    # this block of code prints the message on the button in the chosen font and size

    buttonText = pygame.font.SysFont("Curlz", 21)
    textSurf, textRect = text_button(txt, buttonText)
    textRect.center = ((x_pos + (width / 2)), (y_pos + (height / 2)))
    menu_screen.blit(textSurf, textRect)


# The function below called player_piece_button_one_player has parameters piece, x_pos and y_pos. The function
# makes icons buttons for the player to choose from.


def player_piece_button_one_player(piece, x_pos, y_pos):
    '''Function to ask and retrieve candy selection from player in one player mode. Has parameters piece, x_pos and
    y_pos.'''
    # gets the mouse position

    mouse_pos = pygame.mouse.get_pos()

    # gets if the mouse has clicked

    when_clicked = pygame.mouse.get_pressed()

    # loads the icon image

    icon = pygame.image.load(piece)
    piece_menu.blit(icon, (x_pos, y_pos))

    # locates where the mouse is

    if x_pos + 50 > mouse_pos[0] > x_pos and y_pos + 50 > mouse_pos[1] > y_pos:

        # if the mouse gets clicked

        if when_clicked[0] == 1:
            # this block of if-elif statements will assign what icon was chosen to the player for the rest of the game.
            # After the icon is assigned, it will run the player one function which holds that main game loop

            if x_pos == 301 and y_pos == 100:
                player_one = gummy_bear_red
                one_player(player_one)
            elif x_pos == 351 and y_pos == 100:
                player_one = gummy_bear_purple
                one_player(player_one)
            elif x_pos == 301 and y_pos == 175:
                player_one = gummy_bear_pink
                one_player(player_one)
            elif x_pos == 351 and y_pos == 175:
                player_one = gummy_bear_yellow
                one_player(player_one)
            elif x_pos == 301 and y_pos == 250:
                player_one = gummy_bear_green
                one_player(player_one)
            elif x_pos == 351 and y_pos == 250:
                player_one = gummy_bear_blue
                one_player(player_one)

    else:
        None


# Function below called player_piece_button_two has parameters piece, x_pos, y_pos, and choice. The function
# allows the player to choose their icon out of six choices to be used for the rest of the game.


def player_piece_button_one(piece, x_pos, y_pos, choice=None):
    '''Function to ask and retrieve candy selection from player one in two player mode. Has parameters piece, x_pos,
    y_pos, and choice.'''
    # gets the mouse position

    mouse_pos = pygame.mouse.get_pos()

    # gets if the mouse has clicked

    when_clicked = pygame.mouse.get_pressed()

    # loads the icon image

    icon = pygame.image.load(piece)
    piece_menu.blit(icon, (x_pos, y_pos))
    if x_pos + 50 > mouse_pos[0] > x_pos and y_pos + 50 > mouse_pos[1] > y_pos:
        # if the mouse gets clicked

        if when_clicked[0] == 1 and choice != None:
            # this block of if-elif statements will assign what icon was chosen to the player for the rest of the game
            # after the icon is assigned, it will run the player one function which holds that main game loop

            global player_one
            if x_pos == 100 and y_pos == 100:
                player_one = gummy_bear_red
                choice()
            elif x_pos == 150 and y_pos == 100:
                player_one = gummy_bear_purple
                choice()
            elif x_pos == 100 and y_pos == 200:
                player_one = gummy_bear_pink
                choice()
            elif x_pos == 150 and y_pos == 200:
                player_one = gummy_bear_yellow
                choice()
            elif x_pos == 100 and y_pos == 299:
                player_one = gummy_bear_green
                choice()
            elif x_pos == 150 and y_pos == 299:
                player_one = gummy_bear_blue
                choice()

    else:
        None


# Function below called player_piece_button_two has parameters piece, x_pos and y_pos. The function
# allows the player to choose their icon out of six choices to be used for the rest of the game.


def player_piece_button_two(piece, x_pos, y_pos):
    '''Function to ask and retrieve candy selection from player two in two player mode. Has parameters piece, x_pos and
    y_pos.'''
    # gets the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # gets if the mouse has clicked

    when_clicked = pygame.mouse.get_pressed()

    # loads the icon image

    icon = pygame.image.load(piece)
    piece_menu.blit(icon, (x_pos, y_pos))

    if x_pos + 50 > mouse_pos[0] > x_pos and y_pos + 50 > mouse_pos[1] > y_pos:
        # if the mouse gets clicked

        if when_clicked[0] == 1:
            # this block of if-elif statements will assign what icon was chosen to the player for the rest of the game
            # after the icon is assigned, it will run the player one function which holds that main game loop

            if x_pos == 301 and y_pos == 100 and player_one != gummy_bear_red:
                player_two = gummy_bear_red
                two_player(player_one, player_two)
            elif x_pos == 351 and y_pos == 100 and player_one != gummy_bear_purple:
                player_two = gummy_bear_purple
                two_player(player_one, player_two)
            elif x_pos == 301 and y_pos == 200 and player_one != gummy_bear_pink:
                player_two = gummy_bear_pink
                two_player(player_one, player_two)
            elif x_pos == 351 and y_pos == 200 and player_one != gummy_bear_yellow:
                player_two = gummy_bear_yellow
                two_player(player_one, player_two)
            elif x_pos == 301 and y_pos == 299 and player_one != gummy_bear_green:
                player_two = gummy_bear_green
                two_player(player_one, player_two)
            elif x_pos == 351 and y_pos == 299 and player_one != gummy_bear_blue:
                player_two = gummy_bear_blue
                two_player(player_one, player_two)

    else:
        None


# Function below called one_player_selection has no parameters. The function creates a menu designed for
# one player mode where the buttons are set to represent the icons for the player to choose as their character.


def one_player_selection():
    '''Function to create the menu for the one player mode. No parameters are needed.'''
    # Setting the dimensions of the menu on the display

    piece_menu_width = 900
    piece_menu_height = 600

    # Assigning the dimensions to the menu

    piece_menu = pygame.display.set_mode((piece_menu_width, piece_menu_height))
    intro = True

    # Checking to see if the player will quit the game when this menu is given and
    # Accounting for it

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Setting the color of the menu, establishing and positioning text to
        # display on the menu, and showing character choices.

        piece_menu.fill(pink)
        startText = pygame.font.SysFont("Curlz", 28)
        TextSurf, TextRect = text_display("Please select your flavor.", startText)
        TextRect.center = ((piece_menu_width / 1.5), (piece_menu_height / 6))
        menu_screen.blit(TextSurf, TextRect)
        player_piece_button_one_player(gummy_bear_red, 301, 100)
        player_piece_button_one_player(gummy_bear_purple, 351, 100)
        player_piece_button_one_player(gummy_bear_pink, 301, 175)
        player_piece_button_one_player(gummy_bear_yellow, 351, 175)
        player_piece_button_one_player(gummy_bear_green, 301, 250)
        player_piece_button_one_player(gummy_bear_blue, 351, 250)

        pygame.display.update()
        clock.tick(15)


# Function below called two_player_selection_player_one has no parameters. The function displays a menu
# for two player mode allowing the first player, player one, to select their candy of choice.


def two_player_selection_player_one():
    '''Function to create the menu for the two player mode allowing player one to select their candy of choice. No
    parameters are needed.'''
    # Setting the dimensions of the menu on the display

    piece_menu_width = 900
    piece_menu_height = 600

    # Assigning the dimensions to the menu

    piece_menu = pygame.display.set_mode((piece_menu_width, piece_menu_height))
    intro = True

    # Checking to see if the player will quit the game when this menu is given and accounting for it

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Setting the color of the menu, establishing and positioning text to display on the menu, and showing
        # character choices

        piece_menu.fill(pink)
        startText = pygame.font.SysFont("Curlz", 28)
        TextSurf, TextRect = text_display("Player 1, please select your flavor.", startText)
        TextRect.center = ((piece_menu_width / 1.5), (piece_menu_height / 6))
        menu_screen.blit(TextSurf, TextRect)

        player_piece_button_one(gummy_bear_red, 100, 100, two_player_selection_player_two)
        player_piece_button_one(gummy_bear_purple, 150, 100, two_player_selection_player_two)
        player_piece_button_one(gummy_bear_pink, 100, 200, two_player_selection_player_two)
        player_piece_button_one(gummy_bear_yellow, 150, 200, two_player_selection_player_two)
        player_piece_button_one(gummy_bear_green, 100, 299, two_player_selection_player_two)
        player_piece_button_one(gummy_bear_blue, 150, 299, two_player_selection_player_two)

        pygame.display.update()
        clock.tick(15)


# Function below called two_player_selection_player_two has no parameters. The function displays a menu
# # for two player mode allowing the second player, player two, to select their candy of choice.


def two_player_selection_player_two():
    '''Function to create the menu for the two player mode allowing player two to select their candy of choice. No
    parameters are needed.'''
    # Setting the dimensions of the menu on the display

    piece_menu_width = 900
    piece_menu_height = 600

    # Assigning the dimensions to the menu

    piece_menu = pygame.display.set_mode((piece_menu_width, piece_menu_height))
    intro = True

    # Checking to see if the player will quit the game when this menu is given and accounting for it

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Setting the color of the menu, establishing and positioning text to display on the menu, and showing
        # character choices

        piece_menu.fill(pink)
        startText = pygame.font.SysFont("Curlz", 28)
        TextSurf, TextRect = text_display("Player 2, please select your flavor.", startText)
        TextRect.center = ((piece_menu_width / 1.5), (piece_menu_height / 6))
        menu_screen.blit(TextSurf, TextRect)

        player_piece_button_two(gummy_bear_red, 301, 100)
        player_piece_button_two(gummy_bear_purple, 351, 100)
        player_piece_button_two(gummy_bear_pink, 301, 200)
        player_piece_button_two(gummy_bear_yellow, 351, 200)
        player_piece_button_two(gummy_bear_green, 301, 299)
        player_piece_button_two(gummy_bear_blue, 351, 299)

        pygame.display.update()
        clock.tick(15)


# The function below called one_player has parameters player_one. The function contains the entire logic process
# of one_player mode; Displays the screen with the board, deck of cards, and player icons added onto it. Calls on
# multiple functions to let the user click on the deck of cards, randomly get a card, display the gotten card on screen,
# and move the user's candy piece to its designated location on the board. Same is done for the computer piece.
# Once at the end of the board, the function endgame_menu is called upon with the parameter winner depending on
# which candy character reached the end, the player or the computer.


def one_player(player_one):
    '''Game logic in its entirety for the one player mode. Has parameter player_one. Has parameter player_one'''

    # Program will use the global variable starting_spot and defines it as such.

    global starting_spot

    # Variable csreen is set equal to the display mode function from pygame with resolution 1480 x 800 (window size).

    screen = pygame.display.set_mode((1480, 800))

    # Creates list of variables that the function will utilize for the board logic

    player1_pos = 0
    player2_pos = 0
    ongoing = True
    player1_turn = True
    player2_turn = True
    player1_lose_turn = 0
    player2_lose_turn = 0
    startText = pygame.font.SysFont("Curlz", 22)
    movespot = False
    x_1 = 1
    y_1 = 1
    y_2 = 730
    x_2 = 320

    while ongoing:

        # If the user decides to quit the game while it is still running

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((255, 182, 193))
        screen.blit(board, (200, 0))
        if starting_spot == True:
            starting_spot_player1(player_one)
            starting_spot_player2(computer)
        if movespot == True:
            player1(player_one, x_1, y_1)
            player2(computer, x_2, y_2)

        go_on, git_on = deck_clicked_on(0, 100, change_git_on_to_clicked, change_go_on_to_clicked)
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(10)
        if go_on == 1:
            print('success')
            while player1_turn:
                # during player 1s turn
                if player1_lose_turn == 1:  # checks if player 1 is supposed to lose this turn
                    player1_lose_turn = 0  # makes the player not lose the next turn
                    #  print("Player 1 lost a turn successfully")
                    player1_turn = False  # changes the turn to the other player
                    player2_turn = True
                    go_on = 1
                elif player1_pos == 5:  # checks if the player has landed on the first bridge spot and moves them
                    TextSurf, TextRect = text_display("You used a Shortcut!", startText)
                    TextRect.center = ((1000), (850))
                    screen.blit(TextSurf, TextRect)
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(.8)
                    player1_pos = 59
                    x_1, y_1 = player1_new_movement(player_one, player1_pos)
                    ongoing = True  # keeps the game going
                    player1_turn = False  # changes who's turn it is
                    player2_turn = True
                    go_on = 1

                elif player1_pos == 35:  # checks if the player has landed on the second bridge spot and moves them
                    player1_pos = 45
                    x_1, y_1 = player1_new_movement(player_one, player1_pos)
                    TextSurf, TextRect = text_display("You used a Shortcut!", startText)
                    TextRect.center = ((1000), (850))
                    screen.blit(TextSurf, TextRect)
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(.8)
                    ongoing = True  # keeps the game going
                    player1_turn = False  # changes who's turn it is
                    player2_turn = True
                    go_on = 1
                else:
                    spot, match, card_image = next_spot(get_card())  # gets player 1s card
                    print("Player 1s card is", match)
                    try:
                        chosen = pygame.image.load(card_image)
                    except:
                        print("You are missing a card image!")
                    screen.blit(chosen, (1280, 100))
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(.8)
                    new_player1_pos = player_move(spot, match,
                                                  player1_pos)  # finds where player 1 will land with the new card
                    print("player ones position", new_player1_pos)
                    x_1, y_1 = player1_new_movement(player_one, new_player1_pos)
                    # if player 1 landed on a licorice spot
                    if new_player1_pos == 46 or new_player1_pos == 86 or new_player1_pos == 117:
                        TextSurf, TextRect = text_display("Lord Licorice Took your Turn!", startText)
                        TextRect.center = ((800), (550))
                        screen.blit(TextSurf, TextRect)
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(.8)
                        player1_pos = new_player1_pos  # moves player to drawn position
                        player1_lose_turn = 1  # makes player 1 lose their next turn
                        ongoing = True  # keeps the game going
                        player1_turn = False  # changes who's turn it is
                        player2_turn = True
                        go_on = 1

                    elif new_player1_pos == 134:  # checks if player 1 is on the last space
                        print("Player 1 wins")  # prints player 1s victory
                        player1_turn = False
                        player2_turn = False
                        ongoing = False  # ends the game
                        winner = "Human"
                        endgame_menu(winner)

                    else:
                        player1_pos = new_player1_pos  # player moves to drawn spot
                        x_1, y_1 = player1_new_movement(player_one, player1_pos)
                        ongoing = True  # keeps the game going
                        player1_turn = False  # changes who's turn it is
                        player2_turn = True
                        starting_spot = False
                        movespot = True
                        go_on = 1
                        mouse = pygame.mouse.get_pos()  # gets the mouse position
            if go_on == 1:
                while player2_turn:  # during player 2s turn
                    if player2_lose_turn == 1:  # checks if player 2 is supposed to lose this turn
                        player2_lose_turn = 0  # makes player 2 lose this turn
                        #  print("Player 2 lost a turn successfully")
                        player1_turn = True  # changes who's turn it is
                        player2_turn = False
                        git_on = 0
                    elif player2_pos == 5:  # checks if the player has landed on the first bridge spot and moves them
                        player2_pos = 59
                        x_2, y_2 = player2_new_movement(computer, player2_pos)
                        TextSurf, TextRect = text_display("Computer used a Shortcut!", startText)
                        TextRect.center = ((1000), (850))
                        screen.blit(TextSurf, TextRect)
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(.8)
                        ongoing = True  # keeps the game going
                        player1_turn = True  # changes who's turn it is
                        player2_turn = False
                        git_on = 0

                    elif player2_pos == 35:  # checks if the player has landed on the second bridge spot and moves them
                        player2_pos = 45
                        x_2, y_2 = player2_new_movement(computer, player2_pos)
                        TextSurf, TextRect = text_display("Computer used a Shortcut!", startText)
                        TextRect.center = ((1000), (850))
                        screen.blit(TextSurf, TextRect)
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(.8)
                        ongoing = True  # keeps the game going
                        player1_turn = True  # changes who's turn it is
                        player2_turn = False
                        git_on = 0
                    else:
                        spot, match, card_image = next_spot(get_card())  # gets player 2s new card
                        print("Player 2s card is", match)
                        try:
                            chosen = pygame.image.load(card_image)
                        except:
                            print("You are missing a card image!")
                        screen.blit(chosen, (1280, 100))
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(.8)
                        new_player2_pos = player_move(spot, match,
                                                      player2_pos)  # finds where player 2 will land with the new card
                        x_2, y_2 = player2_new_movement(computer, new_player2_pos)
                        print("player 2s position", new_player2_pos)
                        # if player 2 landed on a licorice spot
                        if new_player2_pos == 46 or new_player2_pos == 86 or new_player2_pos == 117:
                            TextSurf, TextRect = text_display("Lord Licorice Took the computer's Turn!", startText)
                            TextRect.center = ((1000), (850))
                            screen.blit(TextSurf, TextRect)
                            pygame.display.update()
                            clock = pygame.time.Clock()
                            clock.tick(.8)
                            player2_pos = new_player2_pos  # moves player to drawn location
                            player2_lose_turn = 1  # makes player 2 lose their next turn
                            ongoing = True  # keeps the gaming going
                            player1_turn = True  # changes who's turn it is
                            player2_turn = False
                            git_on = 0
                        elif new_player2_pos == 134:  # checks if player 2 has landed on the last spot
                            print("Player 2 wins")  # prints player 2s victory
                            player1_turn = False
                            player2_turn = False
                            ongoing = False  # ends the game
                            winner = 'Computer'
                            endgame_menu(winner)
                        else:
                            player2_pos = new_player2_pos  # moves player 2 two the drawn position
                            x_2, y_2 = player2_new_movement(computer, player2_pos)
                            ongoing = True  # keeps the game going
                            player1_turn = True  # changes who's turn it is
                            player2_turn = False
                            git_on = 0


# Function below called deck_clicked_on has parameters x_pos, y_pos, choice1 and choice2. The function allows the player
# to click on the deck of cards if they want to pull a card.


def deck_clicked_on(x_pos, y_pos, choice1=None, choice2=None):
    '''A function which allows a player to select a card from the deck of cards. Has parameters x_pos, y_pos,
    choice1 and choice2.'''
    # Checking to see if the player clicked on the deck of cards
    # And to display a selected card when the deck is clicked on

    mouse_pos = pygame.mouse.get_pos()
    when_clicked = pygame.mouse.get_pressed()
    icon = pygame.image.load(card_deck)
    screen.blit(icon, (x_pos, y_pos))
    icon2 = pygame.image.load(deck_highlight)

    # Initialize variables to conduct next move on board

    git = 0
    go = 0

    # This code helps to make the card deck clickable and displays a card
    # once it is clicked.

    if x_pos + 200 > mouse_pos[0] > x_pos and y_pos + 400 > mouse_pos[1] > y_pos:
        screen.blit(icon2, (x_pos, y_pos))
        if when_clicked[2] == 1:
            print('works for player2')
            git = choice1(git)
        elif when_clicked[0] == 1:
            print('works for player1')
            go = choice2(go)
    else:
        screen.blit(icon, (x_pos, y_pos))

    # Returns move variables

    return go, git


# Function below called change_git_on_to_clicked with parameter git. Simply changes the value of git to 1 and returns
# it.


def change_git_on_to_clicked(git):
    '''A Function which determines which plaeyr's turn it is. Has parameter git.'''
    git = 1
    return git


# Function below called change_go_on_to_clicked with parameter go. Simply changes the value of go to 1 and returns
# it.

def change_go_on_to_clicked(go):
    '''A Function which determines which plaeyr's turn it is. Has parameter go.'''
    go = 1
    return go


# The function below called two_player has parameters playerOne and playerTwo. The function contains the entire logic
# process of two_player mode; Displays the screen with the board, deck of cards, and player icons added onto it. Calls
# on multiple functions to let the user click on the deck of cards, randomly get a card, display the gotten card on
# screen, and move the user's candy piece to its designated location on the board. Same is done for second player.
# Once at the end of the board, the function endgame_menu is called upon with the parameter winner depending on
# which player reached the end.


def two_player(playerOne, playerTwo):
    '''Game logic in its entirety for the two player mode. Has parameters playerOne and playerTwo.'''
    global starting_spot
    screen = pygame.display.set_mode((1480, 800))
    player1_pos = 0
    player2_pos = 0
    ongoing = True
    player1_turn = True
    player2_turn = True
    player1_lose_turn = 0
    player2_lose_turn = 0
    startText = pygame.font.SysFont("Curlz", 22)
    movespot = False
    x_1 = 1
    y_1 = 1
    y_2 = 730
    x_2 = 320

    while ongoing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((255, 182, 193))
        screen.blit(board, (200, 0))
        if starting_spot == True:
            starting_spot_player1(playerOne)
            starting_spot_player2(playerTwo)
        if movespot == True:
            player1(playerOne, x_1, y_1)
            player2(playerTwo, x_2, y_2)

        TextSurf, TextRect = text_display("Left-click for Player 1,", startText)
        TextRect.center = ((100), (550))
        screen.blit(TextSurf, TextRect)
        TextSurf2, TextRect2 = text_display("Right-click for Player 2", startText)
        TextRect2.center = ((100), (600))
        screen.blit(TextSurf2, TextRect2)
        go_on, git_on = deck_clicked_on(0, 100, change_git_on_to_clicked, change_go_on_to_clicked)
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(10)
        if go_on == 1:
            print('success')
            while player1_turn:
                # during player 1s turn
                if player1_lose_turn == 1:  # checks if player 1 is supposed to lose this turn
                    player1_lose_turn = 0  # makes the player not lose the next turn
                    #  print("Player 1 lost a turn successfully")
                    player1_turn = False  # changes the turn to the other player
                    player2_turn = True
                    go_on = 0
                elif player1_pos == 5:  # checks if the player has landed on the first bridge spot and moves them
                    TextSurf, TextRect = text_display("Player 1 used a Shortcut!", startText)
                    TextRect.center = ((1000), (850))
                    screen.blit(TextSurf, TextRect)
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(.8)
                    player1_pos = 59
                    x_1, y_1 = player1_new_movement(playerOne, player1_pos)
                    ongoing = True  # keeps the game going
                    player1_turn = False  # changes who's turn it is
                    player2_turn = True
                    go_on = 0

                elif player1_pos == 35:  # checks if the player has landed on the second bridge spot and moves them
                    player1_pos = 45
                    x_1, y_1 = player1_new_movement(playerOne, player1_pos)
                    TextSurf, TextRect = text_display("Player 1 used a Shortcut!", startText)
                    TextRect.center = ((1000), (850))
                    screen.blit(TextSurf, TextRect)
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(.8)
                    ongoing = True  # keeps the game going
                    player1_turn = False  # changes who's turn it is
                    player2_turn = True
                    go_on = 0
                else:
                    spot, match, card_image = next_spot(get_card())  # gets player 1s card
                    print("Player 1s card is", match)
                    try:
                        chosen = pygame.image.load(card_image)
                    except:
                        print("You are missing a card image!")
                    screen.blit(chosen, (1280, 100))
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(.8)
                    new_player1_pos = player_move(spot, match,
                                                  player1_pos)  # finds where player 1 will land with the new card
                    print("player ones position", new_player1_pos)
                    x_1, y_1 = player1_new_movement(playerOne, new_player1_pos)
                    # if player 1 landed on a licorice spot
                    if new_player1_pos == 46 or new_player1_pos == 86 or new_player1_pos == 117:
                        TextSurf, TextRect = text_display("Lord Licorice Took Player 1's Turn!", startText)
                        TextRect.center = ((1000), (850))
                        screen.blit(TextSurf, TextRect)
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(.8)
                        player1_pos = new_player1_pos  # moves player to drawn position
                        player1_lose_turn = 1  # makes player 1 lose their next turn
                        ongoing = True  # keeps the game going
                        player1_turn = False  # changes who's turn it is
                        player2_turn = True
                        go_on = 0

                    elif new_player1_pos == 134:  # checks if player 1 is on the last space
                        print("Player 1 wins")  # prints player 1s victory
                        player1_turn = False
                        player2_turn = False
                        ongoing = False  # ends the game
                        winner = "Player 1"
                        endgame_menu(winner)

                    else:
                        player1_pos = new_player1_pos  # player moves to drawn spot
                        x_1, y_1 = player1_new_movement(playerOne, player1_pos)
                        ongoing = True  # keeps the game going
                        player1_turn = False  # changes who's turn it is
                        player2_turn = True
                        starting_spot = False
                        movespot = True
                        go_on = 0
                        mouse = pygame.mouse.get_pos()  # gets the mouse position
        if git_on == 1:
            while player2_turn:  # during player 2s turn
                if player2_lose_turn == 1:  # checks if player 2 is supposed to lose this turn
                    player2_lose_turn = 0  # makes player 2 lose this turn
                    #  print("Player 2 lost a turn successfully")
                    player1_turn = True  # changes who's turn it is
                    player2_turn = False
                    git_on = 0
                elif player2_pos == 5:  # checks if the player has landed on the first bridge spot and moves them
                    player2_pos = 59
                    x_2, y_2 = player2_new_movement(playerTwo, player2_pos)
                    TextSurf, TextRect = text_display("Player 2 used a Shortcut!", startText)
                    TextRect.center = ((1000), (850))
                    screen.blit(TextSurf, TextRect)
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(.8)
                    ongoing = True  # keeps the game going
                    player1_turn = True  # changes who's turn it is
                    player2_turn = False
                    git_on = 0

                elif player2_pos == 35:  # checks if the player has landed on the second bridge spot and moves them
                    player2_pos = 45
                    x_2, y_2 = player2_new_movement(playerTwo, player2_pos)
                    TextSurf, TextRect = text_display("Player 2 used a Shortcut!", startText)
                    TextRect.center = ((1000), (850))
                    screen.blit(TextSurf, TextRect)
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(.8)
                    ongoing = True  # keeps the game going
                    player1_turn = True  # changes who's turn it is
                    player2_turn = False
                    git_on = 0
                else:
                    spot, match, card_image = next_spot(get_card())  # gets player 2s new card
                    print("Player 2s card is", match)
                    try:
                        chosen = pygame.image.load(card_image)
                    except:
                        print("You are missing a card image!")
                    screen.blit(chosen, (1280, 100))
                    pygame.display.update()
                    clock = pygame.time.Clock()
                    clock.tick(.8)
                    new_player2_pos = player_move(spot, match,
                                                  player2_pos)  # finds where player 2 will land with the new card
                    x_2, y_2 = player2_new_movement(playerTwo, new_player2_pos)
                    print("player 2s position", new_player2_pos)
                    # if player 2 landed on a licorice spot
                    if new_player2_pos == 46 or new_player2_pos == 86 or new_player2_pos == 117:
                        TextSurf, TextRect = text_display("Lord Licorice Took Player 2's Turn!", startText)
                        TextRect.center = ((1000), (850))
                        screen.blit(TextSurf, TextRect)
                        pygame.display.update()
                        clock = pygame.time.Clock()
                        clock.tick(.8)
                        player2_pos = new_player2_pos  # moves player to drawn location
                        player2_lose_turn = 1  # makes player 2 lose their next turn
                        ongoing = True  # keeps the gaming going
                        player1_turn = True  # changes who's turn it is
                        player2_turn = False
                        git_on = 0
                    elif new_player2_pos == 134:  # checks if player 2 has landed on the last spot
                        print("Player 2 wins")  # prints player 2s victory
                        player1_turn = False
                        player2_turn = False
                        ongoing = False  # ends the game
                        winner = 'Player 2'
                        endgame_menu(winner)
                    else:
                        player2_pos = new_player2_pos  # moves player 2 two the drawn position
                        x_2, y_2 = player2_new_movement(playerTwo, player2_pos)
                        ongoing = True  # keeps the game going
                        player1_turn = True  # changes who's turn it is
                        player2_turn = False
                        git_on = 0


# Function below called start_menu has no parameters. The function creates a menu when the game first runs.


def start_menu():  # making a menu function
    '''A Function to help create and display the start menu. Has no parameters.'''
    # Setting the width and height of the start menu and assigning them to a new window

    menu_width = 500
    menu_height = 500
    menu_screen = pygame.display.set_mode((menu_width, menu_height))
    intro = True

    # Checking to see if the user wants exits out of the program at this menu, and exiting
    # if the user wants to exit out

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Setting appearance options for the menu and setting the buttons for the
        # One player and Two player options

        menu_screen.fill(pink)
        startText = pygame.font.SysFont("Curlz", 32)
        TextSurf, TextRect = text_display("Are you ready to play Candyland?", startText)
        TextSurf2, TextRect2 = text_display("Please choose a playing mode.", startText)
        TextRect.center = ((menu_width / 2), (menu_height / 3))
        TextRect2.center = ((menu_width / 2), (menu_height / 2))
        menu_screen.blit(TextSurf, TextRect)
        menu_screen.blit(TextSurf2, TextRect2)
        start_buttons("One Player", 70, 300, 150, 80, buttonPinkLight, buttonPinkDark, one_player_selection)
        start_buttons("Two Player", 270, 300, 150, 80, buttonBlueLight, buttonBlueDark, two_player_selection_player_one)
        pygame.display.update()
        clock.tick(15)


# The function below called get_card has no parameters. The function randomly selects a card from the
# list of available cards.


def get_card():
    '''A Function to select cards from a randomly shuffled deck (list). No parameters needed.'''
    card = random.choice(list_of_cards)

    # Checking to see if the card is a special card, if it is, it gets removed

    if card == 6 or card == 20 or card == 13 or card == 40 or card == 27 or card == 47:
        list_of_cards.remove(card)
        list_of_used_cards.append(card)

    # Gets the randomly chosen card and returns it

    card = cards.get(card)
    return card


# The function below called next_spot has parameter card. The function determines what type of card was drawn, such as
# if it was a special card like candy cane or if it was a double green card. The function also determines what image
# needs to be displayed and how many times will the player move depending if the card was a double.


def next_spot(card):
    '''A Function to determine which spot corresponds to the card selected. Has parameter card.'''
    spots = 0
    if card == 'single-yellow':

        # Checking to see if each of the cards are preloaded into the system environment upon being picked,
        # if they aren't throw an exception

        try:
            match = "yellow"
            spots = 1
            card_image = single_yellow
        except:
            print("You need a single yellow card image")

    elif card == 'single-red':
        try:
            match = 'red'
            spots = 1
            card_image = single_red
        except:
            print("You need a single red card image")

    elif card == 'single-blue':
        try:
            match = "blue"
            spots = 1
            card_image = single_blue
        except:
            print("You need a single blue card image")

    elif card == 'single-orange':
        try:
            match = "orange"
            spots = 1
            card_image = single_orange
        except:
            print("You need a single orange card image")

    elif card == 'single-green':
        try:
            match = "green"
            spots = 1
            card_image = single_green
        except:
            print("You need a single green card image")
    elif card == 'single-purple':
        try:
            match = "purple"
            spots = 1
            card_image = single_purple
        except:
            print("You need a single purple card image")
    elif card == 'double-purple':
        try:
            match = "purple"
            spots = 2
            card_image = double_purple
        except:
            print("You need a double purple card image")
    elif card == 'double-green':
        try:
            match = "green"
            spots = 2
            card_image = double_green
        except:
            print("You need a double green card image")
    elif card == 'double-orange':
        try:
            match = "orange"
            spots = 2
            card_image = double_orange
        except:
            print("You need a double orange card image")
    elif card == 'double-blue':
        try:
            match = "blue"
            spots = 2
            card_image = double_blue
        except:
            print("You need a double blue card image")
    elif card == 'double-red':
        try:
            match = 'red'
            spots = 2
            card_image = double_red
        except:
            print("You need a double red card image")
    elif card == 'double-yellow':
        try:
            match = 'yellow'
            spots = 2
            card_image = double_yellow
        except:
            print("You need a double yellow card image")
    elif card == 'ice cream':
        try:
            match = 'ice cream'
            spots = 1
            card_image = ice_cream_card
        except:
            print("You need an ice cream card image")
    elif card == 'gingerbread':
        try:
            match = 'gingerbread'
            spots = 1
            card_image = gingerbread_card
        except:
            print("You need a gingerbread card image")
    elif card == 'candy-cane':
        try:
            match = 'candy-cane'
            spots = 1
            card_image = candy_cane_card
        except:
            print("You need a candy cane card image")
    elif card == 'gumdrop':
        try:
            match = 'gumdrop'
            spots = 1
            card_image = gumdrop_card
        except:
            print("you need a gumdrop card")
    elif card == 'lollipop':
        try:
            match = 'lollipop'
            spots = 1
            card_image = lollipop_card
        except:
            print("You need a lollipop card image")
    elif card == 'peanut':
        try:
            match = "peanut"
            spots = 1
            card_image = peanut_card
        except:
            print("You need a peanut card image")
    return spots, match, card_image


# The function below called player1_new_movement has parameters img and position. The function determines the new
# coordinates of where the player's candy character should be and will determine that by looking through
# the dictionaries made previously and finding the value of position.


def player1_new_movement(img, position):
    '''Finds new x and y coordinates for player one to make his/her next move. Has parameters img and position.'''

    # Loads the image of the candy for player one in two player mode

    player1_Img = pygame.image.load(img)

    # Gets the x and y coordinates of the new location

    player1_X = int(board_locations_player1_x_coordinates.get(position))
    player1_Y = int(board_locations_player1_y_coordinates.get(position))

    # Assigns them to the new position for the specific candy

    screen.blit(player1_Img, (player1_X, player1_Y))

    # Updates the board

    pygame.display.update()
    return player1_X, player1_Y


# The function below called player2_new_movement has parameters img and position. The function determines the new
# coordinates of where the player's candy character should be and will determine that by looking through
# the dictionaries made previously and finding the value of position.


def player2_new_movement(img, position):
    '''Finds new x and y coordinates for player two to make his/her next move. Has parameters img and position.'''
    # Loads the image of the candy for player two in two player mode

    player2_Img = pygame.image.load(img)

    # Gets the x and y coordinates of the new location

    player2_X = int(board_locations_player2_x_coordinates.get(position))
    player2_Y = int(board_locations_player2_y_coordinates.get(position))

    # Assigns them to the new position for the specific candy

    screen.blit(player2_Img, (player2_X, player2_Y))

    # Updates the board

    pygame.display.update()
    return player2_X, player2_Y


# The function player_move has parameters spot, match and position. The function determines where the player's character
# should go depending on how many times it should move based on the card, the current spot of the character, and
# if the spot it moves to next matches the correct corresponding card pulled. Afterwards, the function returns
# the new position the character has on the board.


def player_move(spot, match, position):
    '''A Function to determine the exact location of the next spot which a player will move to. Has parameters spot,
    match and position.'''
    candy_forest = True
    # key_spot = position + 1

    # Handles if the position is more han 127 and one player is near the end of the game

    if position > 133:
        end_game = colored_spots.get(position)

        # Handling all the specialty cards and their respective positions

        if end_game == 'gingerbread':
            position = 9
        elif end_game == 'lollipop':
            position = 92
        elif end_game == 'candy-cane':
            position = 20
        elif end_game == 'peanut':
            position = 69
        elif end_game == 'ice cream':
            position = 102
        elif end_game == 'gumdrop':
            position = 42

        # Dealing with all other card types

        else:
            position = 134
            print('Game should end here')

    # Handles if the position is between 121 and 128 and if a player is near the end of the game

    elif 121 < position < 134 and spot == 2:
        end_game = colored_spots.get(position)

        # Handling all the specialty cards and their respective positions

        if end_game == 'gingerbread':
            position = 9
        elif end_game == 'lollipop':
            position = 92
        elif end_game == 'candy-cane':
            position = 20
        elif end_game == 'peanut':
            position = 69
        elif end_game == 'ice cream':
            position = 102
        elif end_game == 'gumdrop':
            position = 42

        # Dealing with all other card types

        else:
            position = 134
    elif 127 < position < 134:
        end_game = colored_spots.get(position)

        # Handling all the specialty cards and their respective positions

        if end_game == 'gingerbread':
            position = 9
        elif end_game == 'lollipop':
            position = 92
        elif end_game == 'candy-cane':
            position = 20
        elif end_game == 'peanut':
            position = 69
        elif end_game == 'ice cream':
            position = 102
        elif end_game == 'gumdrop':
            position = 42

        # Dealing with all other card types

        else:
            position = 134
    else:
        # Handles if the player is anywhere else on the board

        for i in range(spot):
            key_spot = position + 1
            while candy_forest:
                spot_check = colored_spots.get(key_spot)

                # Handling specialty cards and their respective spots

                if match == spot_check:
                    position = key_spot
                    candy_forest = False
                elif match == 'gingerbread':
                    position = 9
                    candy_forest = False
                elif match == 'lollipop':
                    position = 92
                    candy_forest = False
                elif match == 'candy-cane':
                    position = 20
                    candy_forest = False
                elif match == 'peanut':
                    position = 69
                    candy_forest = False
                elif match == 'ice cream':
                    position = 102
                    candy_forest = False
                elif match == 'gumdrop':
                    position = 42
                    candy_forest = False
                else:
                    # Handling for all other card types

                    key_spot += 1

            candy_forest = True

    return position


# font changed to a different font

font = pygame.font.SysFont('comicsans', 30, True)


# The function below called endgame_buttons has parameters txt, x_pos, y_pos, width, height, light, dark and choice.
# The function makes buttons to be seen and clicked on in the endgame screen once either a player or computer has
# won the game.


def endgame_buttons(txt, x_pos, y_pos, width, height, light, dark, choice=None):
    '''Function which makes the buttons for the endgame screen. Has parameters txt, x_pos, y_pos, width, height, light,
    dark and choice.'''
    mouse_pos = pygame.mouse.get_pos()  # finds the mouse position
    when_clicked = pygame.mouse.get_pressed()  # finds if the mouse buttons have been pressed or not

    # sees where the mouse is so that it can change the color of the box
    if x_pos + width > mouse_pos[0] > x_pos and y_pos + height > mouse_pos[1] > y_pos:
        pygame.draw.rect(menu_screen, light, (x_pos, y_pos, width, height))

        # when the mouse is clicked, it goes to the function that it has been told to go to
        if when_clicked[0] == 1 and choice != None:
            choice()
    else:
        pygame.draw.rect(menu_screen, dark, (x_pos, y_pos, width, height))
        # this block of code prints the message on the button in the chosen font and size
    buttonText = pygame.font.SysFont("Curlz", 21)
    textSurf, textRect = text_button(txt, buttonText)
    textRect.center = ((x_pos + (width / 2)), (y_pos + (height / 2)))
    menu_screen.blit(textSurf, textRect)


# The function below called endgame_menu has parameter winner. The function creates the endgame menu, window, once
# the game has been decided. In addition to displaying buttons, the window also displays who won the game.


def endgame_menu(winner):
    '''Function which makes the endgame menu. Has parameter winner.'''

    # Setting the height and width of the endgame menu and assigning it to the
    # Menu screen

    menu_width = 800
    menu_height = 800
    menu_screen = pygame.display.set_mode((menu_width, menu_height))

    # Checking and handling to see if the user wants to quit the game at this point

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Appearance preferences for the menu and the endgame buttons

        menu_screen.fill(pink)
        startText = pygame.font.SysFont("Curlz", 32)
        TextSurf, TextRect = text_display(("The winner of CandyLand is: " + winner), startText)
        TextSurf2, TextRect2 = text_display("Please click a button on what you would like to do next.", startText)
        TextRect.center = ((menu_width / 2), (menu_height / 15))
        TextRect2.center = ((menu_width / 2), (menu_height / 2))
        menu_screen.blit(TextSurf, TextRect)
        menu_screen.blit(TextSurf2, TextRect2)
        endgame_buttons("1 Player Mode", 100, 300, 150, 80, buttonPinkLight, buttonPinkDark, one_player_selection)
        endgame_buttons("Quit", 300, 300, 150, 80, buttonPinkLight, buttonPinkDark, pygame.quit)
        endgame_buttons("2 player Mode", 500, 300, 150, 80, buttonPinkLight, buttonPinkDark,
                        two_player_selection_player_one)
        pygame.display.update()
        clock.tick(15)


# endgame_menu()


start_menu()
