# A single player tictactoe game player, the bot make random moves


import pygame
import random
from sys import exit


def draw_board(player_symbol, bot_symbol, board):
    """
        Input: string, string, list of strings
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

    board_display = pygame.Surface((HEIGHT/3, WIDTH/3))
    board_display.fill('Light grey')

    is_players_move = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if is_full(board):
                print("It's a tie!")
                exit()

        # Board format
        screen.blit(board_display, (0, HEIGHT/3))
        screen.blit(board_display, (HEIGHT/3, 0))
        screen.blit(board_display, (HEIGHT/3, 2*HEIGHT/3))
        screen.blit(board_display, (2*HEIGHT/3, HEIGHT/3))

        if is_players_move:
            board = player_move(player_symbol, board)
        else:
            board = bot_move(bot_symbol, board)

        is_players_move = (is_players_move + 1) % 2
        print(is_players_move, board)

        for square, symbol in enumerate(board):
            if symbol == '':
                continue

            coordinates = get_coordinates(square)
            square_text = game_font.render(symbol, True, 'Black')
            square_rect = square_text.get_rect(center = coordinates)
            screen.blit(square_text, square_rect)

        # Draw and update elements
        pygame.display.update()
        clock.tick(24)

    return 0


def get_coordinates(square):
    """
        Input: int, list of strings
    """

    board_coordinates = (square//3 + 50, square%2 + 50)

    return board_coordinates


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

        if player_symbol == 'O':
            break
        if player_symbol == 'X':
            bot_symbol = 'O'
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


def bot_move(bot_symbol, board):
    """
        Input: list of ints
        Output:
        Randomly selects the bot's move
    """

    while True:
        move = random.randint(0, 8)

        if board[move] == '':
            board[move] = bot_symbol
            print(move, board)
            break

    return board


def is_full(board):
    """
        Input: list of ints
        Output: boolean
        If False the game continues, if True, the board is full, it's a tie.
    """

    for square in board:
        if square == '':
            return False

    return True


def three_in_a_row(board):
    """
        Input: list of ints
        Output: boolean
        Checks if there are 3 symbols in a row.
        The int represents one of the squares of the winning line
    """

    return are_three_in_a_row


def is_winner(player_symbol, case):
    """
        Input: string, int
        Output:
        Prints a string to stdout announcing the outcome of the game.
    """

    if board[case] == player_symbol:
        print("You won!")
    else:
        print("You lose!")

    return 0


def main():
    """
        Initialises and determines the flow the game
    """

    player_symbol, bot_symbol = pick_a_side()
    board = ['' for _ in range(9)]
    draw_board(player_symbol, bot_symbol, board)

    return 0


if __name__ == '__main__':
    main()
