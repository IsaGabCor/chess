import pygame

class Piece:
    def __init__(self, piece_type, color, image, position):
        self.type = piece_type  # 'p', 'r', 'n', 'b', 'q', 'k'
        self.color = color  # 'w' or 'b'
        self.image = image  # path to image file
        self.position = position  # e.g., 'e4'

    def move(self, new_position, board):
        self.position = new_position
        board.add_move(new_position)

    def get_legal_moves(self, board):
        raise NotImplementedError("This method should be implemented by subclasses.")
    
    def load_image(square_size):
        pieces = {}
        for color in ['w', 'b']:
            for piece_type in ['p', 'r', 'n', 'b', 'q', 'k']:
                img = pygame.image.load(f"chess/assets/pieces/{color}{piece_type}.png")
                img = pygame.transform.scale(img, (square_size, square_size))
                pieces[color + piece_type] = img
        return pieces