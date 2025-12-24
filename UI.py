import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 24)

    def draw_notation_panel(self, board):
        panel_width = 230
        panel_height = board.square_size * 8 - 100
        panel_x = board.left_margin + board.square_size * 8 + 10
        panel_y = board.top_margin

        # Draw panel background
        pygame.draw.rect(self.screen, (50, 50, 50), (panel_x, panel_y, panel_width, panel_height))

        # Draw notation text
        notation_text = []

        for i, text in enumerate(notation_text):
            img = self.font.render(text, True, (255, 255, 255))
            self.screen.blit(img, (panel_x + 10, panel_y + 10 + i * 30))