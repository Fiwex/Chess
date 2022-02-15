"""
Personal Chess project, aiming to play vs an IA at the end
Base of project taken from 'Eddie Sharick' on YouTube with his 'Chess Engine in Python' series
Made by Adrien GIGET, starting 11/02/2022
"""

import pygame as p
from Chess import ChessEngine

# Global elements

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
Initialize our global dictionary of images
'''


def load_images():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bp", "wp", "wR", "wN", "wB", "wQ", "wK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("pieces/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


'''
Main for input and graphic loads
'''


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    game_state = ChessEngine.GameState()
    load_images()
    running = True
    sq_selected = ()  # Track last click of user (tuple)
    player_clicks = []  # keep track of player clicks (two tuple)
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // SQ_SIZE
                row = location[1] // SQ_SIZE
                if sq_selected == (row, col):  # select two time the same sq
                    sq_selected = ()  # deselect
                    player_clicks = []
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected)  # Append for 1st and 2cd click
                if len(player_clicks) == 2:  # After the 2cd click
                    move = ChessEngine.Move(player_clicks[0], player_clicks[1], game_state.board)
                    print(move.get_chess_notation())
                    game_state.make_move(move)
                    sq_selected = ()  # Deselect what user clicked
                    player_clicks = []

            elif e.type == p.KEYDOWN:
                if e.key == p.K_u:  # Undo on "U" key
                    game_state.undo_move()

        disp_game_state(screen, game_state)
        clock.tick(MAX_FPS)
        p.display.flip()


def disp_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def disp_pieces(screen, game_state):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = game_state[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def disp_game_state(screen, game_state):
    disp_board(screen)
    disp_pieces(screen, game_state.board)


if __name__ == "__main__":
    main()
