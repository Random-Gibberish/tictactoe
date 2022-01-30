# A single player tictactoe game player, the bot make random moves


import pygame
from sys import exit


def draw_board():
    """
        Input: list of ints
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

    player_text = game_font.render('X', True, 'Black')
    bot_text = game_font.render('O', True, 'Black')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.blit(board, (0, HEIGHT/3))
        screen.blit(board, (HEIGHT/3, 0))
        screen.blit(board, (HEIGHT/3, 2*HEIGHT/3))
        screen.blit(board, (2*HEIGHT/3, HEIGHT/3))

        screen.blit(player_text, (HEIGHT/6 - 25, HEIGHT/6 - 25))
        screen.blit(bot_text, (2*HEIGHT/3 - 75, 2*HEIGHT/3 - 75))

        # Draw and update elements
        pygame.display.update()
        clock.tick(24)

    return 0


def player_move(board):
    """
        Input: list of ints
        Output:
        Asks for the players move and places it on the board.
    """

    return 0


def switch_player(is_players_move):
    """
        Input: boolean
        Output: boolean
        Switches boolean value.
    """

    return is_players_move


def full_board(board):
    """
        Input: list of ints
        Output: boolean
        If False the game continues, if True, the board is full. It is a tie.
    """

    return is_full


def three_in_a_row(board):
    """
        Input: list of ints
        Output: (boolean, int)
        Checks if there are 3 symbols in a row and returns either:
            True, int representing row, column or diagonal
            False, None
    """

    return are_three_in_a_row, case


def display_winner(player_symbol, case):
    """
        Input: string, int
        Output:
        Prints a string to stdout announcing the outcome of the game.
    """

    return 0


def main():
    """
        Initialises and determines the flow the game
    """

    draw_board()

    return 0


if __name__ == '__main__':
    main()
