import pygame
from Piece import Piece

pygame.mixer.init()

class Board:
    starting_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    move_list = []

    square_size = 80
    board_size = 8
    left_margin = 40
    top_margin = 40

    #store sounds for moves and captures
    move_sound = pygame.mixer.Sound("chess/assets/sfx/move1.wav")
    move_sound2 = pygame.mixer.Sound("chess/assets/sfx/move2.wav")
    move_sound3 = pygame.mixer.Sound("chess/assets/sfx/move3.wav")
    capture_sound = pygame.mixer.Sound("chess/assets/sfx/capture.wav")
    move_sounds = [move_sound, move_sound2, move_sound3]
    start_sound = pygame.mixer.Sound("chess/assets/sfx/board_start.wav")

    #initialize the chess board
    def __init__(self, piece_images):
        self.board = self.create_board()
        self.piece_images = piece_images
        self.font = pygame.font.SysFont(None, 24)
        self.start_sound.play()
    
    #create an 8x8 board
    def create_board(self):
         # 8x8 board initialized to None
        return [[None for _ in range(8)] for _ in range(8)]
        
    #create a method to print the board
    def print_board(self):
        for row in self.board:
            for square in row:
                if square is None:
                    print("..", end=" ")
                else:
                    print(square.color + square.type, end=" ")
            print()

    #create a method that interperets FEN strings and sets up the board accordingly
    def FEN_setup(self, fen):
        rows = fen.split()[0].split('/')
        self.board = self.create_board()

        for row_idx, fen_row in enumerate(rows):
            col_idx = 0
            for char in fen_row:
                if char.isdigit():
                    col_idx += int(char)
                else:
                    color  = 'w' if char.isupper() else 'b'
                    piece_type = char.lower()

                    image_key = color + piece_type
                    image = self.piece_images[image_key]

                    self.board[row_idx][col_idx] = Piece(piece_type, color, image, (row_idx, col_idx))
                    col_idx += 1
        
    #draw pieces on the board
    def draw_pieces(self, screen):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    x = self.left_margin + col * self.square_size
                    y = self.top_margin + row * self.square_size
                    screen.blit(piece.image, (x, y))

    #create a method that draws the board
    def display_Board(self, screen):
        light = (238, 240, 218)
        dark = (37, 84, 125)
        
        for row in range(8):
            for col in range(8):
                color = light if (row + col) % 2 == 0 else dark
                x = self.left_margin + col * self.square_size
                y = self.top_margin + row * self.square_size

                pygame.draw.rect(screen, 
                                 color, 
                                 pygame.Rect(x, y, self.square_size, self.square_size)
                )
                
        self.draw_pieces(screen)
        self.draw_notation(screen)

    #draw files on the sides of the board
    def draw_files(self, screen):
        files = 'abcdefgh'
        for col in range(8):
            label = self.font.render(files[col], True, (238, 240, 218))
            x = self.left_margin + col * self.square_size + self.square_size // 2
            y = self.top_margin // 2
            rect = label.get_rect(center=(x, y))
            screen.blit(label, rect)

    #draw ranks on the sides of the board
    def draw_ranks(self, screen):
        for row in range(8):
            label = self.font.render(str(8 - row), True, (238, 240, 218))
            x = self.left_margin // 2
            y = self.top_margin + row * self.square_size + self.square_size // 2
            rect = label.get_rect(center=(x, y))
            screen.blit(label, rect)

    #draw notation around the board
    def draw_notation(self, screen):
        self.draw_files(screen)
        self.draw_ranks(screen)

    #handle mouse clicks on the board
    def handle_click(self, mouse_x, mouse_y):
        col = (mouse_x - self.left_margin) // self.square_size
        row = (mouse_y - self.top_margin) // self.square_size

        if 0 <= row < 8 and 0 <= col < 8:
            print(f"Clicked on square: {chr(col + ord('a'))}{8 - row}")
            #self.print_board()
            piece = self.board[row][col]
            print("piece: ", piece.color + piece.type if piece else "None")
            

    #this method adds a move to the move list
    @staticmethod
    def add_move(move):
        Board.move_list.append(move + " ")