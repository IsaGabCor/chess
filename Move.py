class Move:

    def __init__(self, piece, start_pos, end_pos, capture=False, promotion=None, castling=False, en_passant=False):
        self.piece = piece
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.capture = capture
        self.promotion = promotion
        self.castling = castling
        self.en_passant = en_passant

    def __str__(self):
        move_str = self.end_pos
        if self.capture:
            move_str += "x"
        if self.promotion:
            move_str += f"={self.promotion}"
        if self.castling:
            if self.end_pos[0] == 'g':
                move_str = "O-O"
            else:
                move_str = "O-O-O"
        if self.en_passant:
            move_str += " (en passant)"
        return move_str