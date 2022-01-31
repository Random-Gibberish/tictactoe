# A single player tictactoe game player, the bot make random moves


import pygame
import random
from sys import exit


def draw_board(player_symbol, bot_symbol, board):
    """
        Input: string, list of ints
        Output:
        Renders a window and siplays the board.
    """

    pygame.init()
    HEIGHT = 300
    WIDTH = 300

    screen = pygame.display.set_mode((HEIGHT, WIDTH))
    screen.fill('Dark grey')

    pygame.display.set_caption('Tictactoe')
    clock = pygame.time.Clock()
    game_font = pygame.font.Font(None, 100)

    board = pygame.Surface((HEIGHT/3, WIDTH/3))
    board.fill('Light grey')

    player_text = game_font.render(player_symbol, True, 'Black')
    bot_text = game_font.render(bot_symbol, True, 'Black')

    player_rect = player_text.get_rect(center = (HEIGHT/6, HEIGHT/6))
    bot_rect = player_text.get_rect(center = (3*HEIGHT/6, 3*HEIGHT/6))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Board format
        screen.blit(board, (0, HEIGHT/3))
        screen.blit(board, (HEIGHT/3, 0))
        screen.blit(board, (HEIGHT/3, 2*HEIGHT/3))
        screen.blit(board, (2*HEIGHT/3, HEIGHT/3))

        screen.blit(player_text, player_rect)
        screen.blit(bot_text, bot_rect)

        # Draw and update elements
        pygame.display.update()
        clock.tick(24)

    return 0


def pick_a_side():
    """
        Input:
        Output: string
        Prompts the player to select 'X' or 'O'
    """

    print("Please select 'X' or 'O* to start: ")

    while True:
        player_symbol = input().upper()
        bot_symbol = 'X'

        if player_symbol == 'X':
            bot_symbol == 'O'
            break

        print("Invalid selection! Try again.")

    return player_symbol, bot_symbol


def player_move(player_symbol, board):
    """
        Input: string, list of ints
        Output: list of ints
        Asks for the players move and places it on the board.
    """

    print("Your move! Pick 'row column' between 1 and 3: ")

    while True:
        player_move = input().split()

        move = 3 * (int(player_move[0]) - 1) + (int(player_move[1]) - 1)

        if board[move] == '':
            break

        print("Square taken, pick another one!")

    board[move] = player_symbol

    return board


def switch_player(is_players_move):
    """
        Input: boolean
        Output: boolean
        Switches boolean value.
    """

    is_players_move = isplayers_move + 1 % 2

    return is_players_move


def bot_move(bot_symbol, board):
    """
        Input: list of ints
        Output:
        Randomly selects the bot's move
    """

    while True:
        move = random.randint(0, 9)

        if board[move] == '':
            break

    board[move] = bot_symbol

    return board


def is_full(board):
    """
        Input: list of ints
        Output: boolean, int
        If False the game continues, if True, the board is full. It is a tie.
    """

    for square in board:
        if square == '':
            return False, -1

    return True, -1


def three_in_a_row(board):
    """
        Input: list of ints
        Output: (boolean, int)
        Checks if there are 3 symbols in a row and returns either:
            True, int
            False, int
        The int represents one of the squares of the winning line
    """

    return are_three_in_a_row, case


def is_winner(player_symbol, case):
    """
        Input: string, int
        Output:
        Prints a string to stdout announcing the outcome of the game.
    """

    if three_in_a_row():
        print("It's a tie!")
    elif board[case] == player_symbol:
        print("You won!")
    else:
        print("You lose!")

    return 0


def main():
    """
        Initialises and determines the flow the game
    """

    player_symbol = pick_a_side()
    board = ['' for _ in range(9)]
    print(board)
    draw_board(player_symbol, board)

    return 0


if __name__ == '__main__':
    main()
