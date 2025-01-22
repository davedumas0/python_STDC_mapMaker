import pygame

class Button:
    def __init__(
        self, x, y, width, height, text, callback=None,
        bg_color=(70, 70, 70), text_color=(255, 255, 255),
        active_line_color=(255, 255, 255), button_type="tab"
    ):
        self.rect = pygame.Rect(x, y + 4, width, height)  # Offset button down for the top indicator
        self.text = text  # Button label
        self.callback = callback  # Function to call when clicked
        self.font = pygame.font.SysFont(None, 24)  # Font for the button text
        self.bg_color = bg_color  # Default background color
        self.hover_color = self._calculate_hover_color(bg_color)  # Hover color dynamically calculated
        self.text_color = text_color  # Text color
        self.active_line_color = active_line_color  # Color for the active line
        self.is_hovered = False  # Track hover state
        self.type = button_type  # Button type: "tab" or "normal"

    def _calculate_hover_color(self, color):
      
        lighten_factor = 40  # Adjust this value to control how much lighter the hover color is
        return tuple(min(c + lighten_factor, 255) for c in color)  # Ensure values stay within 0-255

    def draw(self, surface, is_active=False):
        color = self.hover_color if self.is_hovered else self.bg_color  # Use hover or default color
        pygame.draw.rect(surface, color, self.rect)  # Draw the button rectangle

        # Render the button text and center it
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

        # For tab buttons, draw the indicator line at the top if active
        if self.type == "tab" and is_active:
            pygame.draw.line(
                surface,
                self.active_line_color,
                (self.rect.left, self.rect.top),  # Line is drawn above the button
                (self.rect.right, self.rect.top),
                4  # Line thickness
            )

    def handle_event(self, events):
        """Handle a list of user input events."""
        if not isinstance(events, (list, tuple)):
            events = [events]  # Ensure events is always a list
    
        for event in events:  # Process each event
            if event.type == pygame.MOUSEMOTION:
                self.is_hovered = self.rect.collidepoint(event.pos)  # Check if the mouse is over the button
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.is_hovered and self.callback:
                    self.callback()  # Call the button's callback when clicked
