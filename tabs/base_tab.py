import pygame
from ui.button import Button

class BaseTab:
    def __init__(self, metadata, name, bg_color, button_x, button_callback, y_offset=50):
        self.metadata = metadata  # Shared metadata or state
        self.name = name  # Name of the tab
        self.bg_color = bg_color  # Background color for the tab
        self.y_offset = y_offset  # Offset to leave room for buttons

        # Create the tab's button with type "tab"
        self.button = Button(
            button_x, 6, 150, y_offset - 6,  # Position button lower for the indicator
            name, button_callback, bg_color=bg_color, active_line_color=(255, 255, 255), button_type="tab"
        )

    def handle_events(self, events):
        pass  # Tabs can handle their own events

    def update(self, dt):
        pass  # Tabs can update their own state

    def draw(self, surface):
        # Fill the tab's background, leaving space for buttons
        #surface.fill(self.bg_color, pygame.Rect(0, self.y_offset, surface.get_width(), surface.get_height() - self.y_offset))
        pass
    def draw_button(self, surface, is_active):
        # Draw the button and add a line if the tab is active
        self.button.draw(surface, is_active=is_active)
