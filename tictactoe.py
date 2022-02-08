import pygame
import random
from sys import exit


def pick_a_side():
    """
        Prompts the player to select 'X' or 'O'
    """

    print("Please select 'X' or 'O* to start: ")

    while True:
        player_symbol = input().upper()

        if player_symbol == 'O':
            bot_symbol = 'X'
            return player_symbol, bot_symbol

        if player_symbol == 'X':
            bot_symbol = 'O'
            return player_symbol, bot_symbol

        print("Invalid selection! Try again.")


def player_move(player_symbol, board):
    """
        Asks for the players move and places it on the board.
    """

    print("Enter 'row column' to make your move.")
    while True:
        player_move = input().split()
        move = 3 * (int(player_move[0]) - 1) + (int(player_move[1]) - 1)

        if board[move] == '':
            board[move] = player_symbol
            return board
        else:
            print("Square taken, pick another one!")


def bot_move(bot_symbol, board):
    """
        Randomly selects the bot's move
    """

    while True:
        move = random.randint(0, 8)

        if board[move] == '':
            board[move] = bot_symbol
            return board


def is_full(board):
    """
        If False the game continues. If True, the board is full and it's a tie.
    """

    for square in board:
        if square == '':
            return False

    return True


def three_in_a_row(board):
    """
        If False the game continues. If True calls is_winner().
    """

    cases = [board[0] == board[1] == board[2] != '',
            board[3] == board[4] == board[5] != '',
            board[6] == board[7] == board[8] != '',
            board[0] == board[3] == board[6] != '',
            board[1] == board[4] == board[7] != '',
            board[2] == board[5] == board[8] != '',
            board[0] == board[4] == board[8] != '',
            board[2] == board[4] == board[6] != '']

    for case_number, case in enumerate(cases):
        if case:
            is_winner(player_symbol, case_number, board)
            return True

    return False


def is_winner(player_symbol, case_number, board):
    """
        If True prints 'You won!'. If False printa 'You lost!'..
    """

    victor_cases = [case_number in [0, 3, 6] and board[0] == player_symbol,
            case_number in [5, 7] and board[2] == player_symbol,
            case_number == 1 and board[3] == player_symbol,
            case_number in [2, 4] and board[7] == player_symbol]

    for victor_case in victor_cases:
        if victor_case:
            print("You won!")
            return True

    print("You lost!")

    return True


if __name__ == '__main__':
    player_symbol, bot_symbol = pick_a_side()

    board = ['' for _ in range(9)]
    pygame.init()

    # Window and board dimensions
    HEIGHT = 300
    height = HEIGHT/3

    pygame.display.set_caption('Tictactoe')
    clock = pygame.time.Clock()
    game_font = pygame.font.Font(None, 100)

    screen = pygame.display.set_mode((HEIGHT, HEIGHT))
    screen.fill('Dark grey')

    board_display = pygame.Surface((height, height))
    board_display.fill('Light grey')

    is_players_move = True

    while True:
        # Draw and update elements
        pygame.display.update()
        clock.tick(24)

        # Quit game in case of interuption
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Board format
        for i in range(1, 8, 2):
            square = (height * (i // 3), height * (i % 3))
            screen.blit(board_display, square)

        if not three_in_a_row(board) and not is_full(board):
            board = player_move(player_symbol, board)

        if not three_in_a_row(board) and not is_full(board):
            board = bot_move(bot_symbol, board)

        if three_in_a_row(board):
            pygame.quit()
            exit()

        if is_full(board):
            print("It's a tie!")
            pygame.quit()
            exit()

        print(board[:3])
        print(board[3:6])
        print(board[6:])

        for num, symbol in enumerate(board):
            if symbol == '':
                continue

            coords = (height * (num%3 + 1/2), height * (num//3 + 1/2))
            square_text = game_font.render(symbol, True, 'Black')
            square_rect = square_text.get_rect(center = coords)
            screen.blit(square_text, square_rect)
