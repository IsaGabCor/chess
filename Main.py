import pygame
from Board import Board
from Piece import Piece
from UI import UI

pygame.init()

# Define constants for the game window
SQUARE_SIZE = 80
BOARD_SIZE = 8
LEFT_PADDING = 40
RIGHT_PADDING = 250
TOP_PADDING = 40
BOTTOM_PADDING = 40

WINDOW_WIDTH  = (LEFT_PADDING + 8 * SQUARE_SIZE) + RIGHT_PADDING
WINDOW_HEIGHT = TOP_PADDING + 8 * SQUARE_SIZE + BOTTOM_PADDING

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Chess Game")

#create an instance of board class and display the board
piece_images = Piece.load_image(SQUARE_SIZE)
board = Board(piece_images)
board.FEN_setup(Board.starting_fen)
ui = UI(screen)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle other events like mouse clicks here
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            board.handle_click(mouse_x, mouse_y)
    screen.fill((10, 10, 10))  # Fill the screen with black
    board.display_Board(screen)
    ui.draw_notation_panel(board)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()

