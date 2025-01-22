# ui.TextElement.py
import pygame

class TextElement:
    def __init__(self, x, y, text, font_size=24, color=(255, 255, 255), bg_color=None):
        self.x = x  # X-coordinate
        self.y = y  # Y-coordinate
        self.text = text  # Text content
        self.font = pygame.font.SysFont(None, font_size)  # Font for rendering the text
        self.color = color  # Text color
        self.bg_color = bg_color  # Optional background color for the text
        self.surface = self.font.render(self.text, True, self.color)  # Pre-render the text

    def set_text(self, new_text):
        self.text = new_text  # Update the text content
        self.surface = self.font.render(self.text, True, self.color)  # Re-render the text

    def draw(self, surface):
        # Draw the background if specified
        if self.bg_color:
            text_rect = self.surface.get_rect(topleft=(self.x, self.y))
            pygame.draw.rect(surface, self.bg_color, text_rect)
        # Draw the text
        surface.blit(self.surface, (self.x, self.y))
