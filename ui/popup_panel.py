# popup_panel.py
import pygame
from ui.base_panel import BasePanel


class BasePopup(BasePanel):
    def __init__(
        self, x, y, min_width, min_height, message, on_accept=None, on_cancel=None,
        bg_color=(40, 40, 40), border_color=(200, 200, 200), border_width=2
    ):
        # Initialize the base panel
        super().__init__(x, y, min_width, min_height, bg_color, border_color, border_width)

        # Store callbacks for the buttons
        self.on_accept = on_accept
        self.on_cancel = on_cancel

        # Add a label or message area
        self.message = message
        self.font = pygame.font.SysFont(None, 24)

        # Add Accept and Cancel buttons (initial positioning; will adjust dynamically)
        self.accept_button = self.add_button(
            0, 0, 80, 40, "Accept", self.on_accept
        )
        self.cancel_button = self.add_button(
            0, 0, 80, 40, "Cancel", self.on_cancel
        )

        self.dynamic_resize()

    def dynamic_resize(self):
        # Adjust the size of the popup based on its children
        max_width = max((child.rect.right for child in self.children), default=self.rect.width)
        max_height = max((child.rect.bottom for child in self.children), default=self.rect.height)

        self.rect.width = max(max_width + 20, self.rect.width)  # Padding
        self.rect.height = max(max_height + 60, self.rect.height)  # Padding + space for buttons

        # Reposition buttons to the bottom-right corner
        self.accept_button.rect.x = self.rect.x + self.rect.width - 180
        self.accept_button.rect.y = self.rect.y + self.rect.height - 50
        self.cancel_button.rect.x = self.rect.x + self.rect.width - 90
        self.cancel_button.rect.y = self.rect.y + self.rect.height - 50
        

    def draw(self, surface):
        # Draw the popup background and border
        super().draw(surface)

        # Draw the message text centered in the popup
        text_surface = self.font.render(self.message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(
            center=(self.rect.x + self.rect.width // 2, self.rect.y + 20)
        )
        surface.blit(text_surface, text_rect)

        # Draw child elements like buttons
        for child in self.children:
            if hasattr(child, 'draw'):
                child.draw(surface)

    def handle_event(self, events):
        # Pass events to child elements like buttons
        super().handle_event(events)
