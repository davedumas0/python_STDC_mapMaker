import pygame

class TextInput:
    def __init__(self, x, y, width, height, font_size=24, text_color=(0, 0, 0), bg_color=(255, 255, 255), border_color=(0, 0, 0), border_width=1, callback=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""  # The current text in the input box
        self.font = pygame.font.SysFont(None, font_size)
        self.text_color = text_color
        self.bg_color = bg_color
        self.border_color = border_color
        self.border_width = border_width
        self.callback = callback  # Callback to call when text changes
        self.active = False  # Whether the input box is active

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Toggle active state when clicked
                self.active = self.rect.collidepoint(event.pos)
            elif event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    if self.callback:
                        self.callback(self.text)  # Call the callback with the current text
                else:
                    self.text += event.unicode

    def draw(self, surface):
        # Draw the input box
        pygame.draw.rect(surface, self.bg_color, self.rect)
        if self.border_width > 0:
            pygame.draw.rect(surface, self.border_color, self.rect, self.border_width)

        # Render the text
        text_surface = self.font.render(self.text, True, self.text_color)
        surface.blit(text_surface, (self.rect.x + 5, self.rect.y + (self.rect.height - text_surface.get_height()) // 2))
