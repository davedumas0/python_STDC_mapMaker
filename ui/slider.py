# ui.slider.py

import pygame
from ui.button import Button

class Slider:
    def __init__(self, x, y, width, height, min_val=0, max_val=100, start_val=50, orientation="horizontal", direction="ltr"):
        self.rect = pygame.Rect(x, y + 54, width, height)  # Adjust slider position to compensate for tab buttons
        self.min_val = min_val  # Minimum slider value
        self.max_val = max_val  # Maximum slider value
        self.value = start_val  # Current slider value
        self.orientation = orientation  # Orientation: "horizontal" or "vertical"
        self.direction = direction  # Direction: "ltr", "rtl", "ttb", or "btt"

        # Create the slider handle as a Button
        self.handle = Button(
            x=self._calculate_handle_position(),
            y=self.rect.centery - (10 if orientation == "horizontal" else 0),
            width=10 if orientation == "horizontal" else 20,
            height=20 if orientation == "horizontal" else 10,
            text="",
            bg_color=(150, 25, 150),
            callback=None,  # No direct callback for the handle
        )
        self.dragging = False
        self.value_type = type(min_val)  # Store the type of the values (int or float)

    def _calculate_handle_position(self):
        range_val = max(1, self.max_val - self.min_val)  # Ensure range is at least 1
        if self.orientation == "horizontal":
            if self.direction == "ltr":
                return self.rect.x + (self.value - self.min_val) / range_val * self.rect.width - 5
            else:
                return self.rect.right - (self.value - self.min_val) / range_val * self.rect.width - 5
        else:
            if self.direction == "ttb":
                return self.rect.y + (self.value - self.min_val) / range_val * self.rect.height - 5
            else:
                return self.rect.bottom - (self.value - self.min_val) / range_val * self.rect.height - 5

    def draw(self, surface):
        pygame.draw.rect(surface, (150, 150, 150), self.rect)  # Draw slider track
        self.handle.draw(surface)  # Draw the slider handle using the Button class

    def handle_event(self, events):
        if not isinstance(events, (list, tuple)):  # Ensure events is iterable
            events = [events]

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.handle.rect.collidepoint(event.pos):  # Check if the click is on the handle
                    self.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.dragging = False
            elif event.type == pygame.MOUSEMOTION and self.dragging:
                range_val = max(1, self.max_val - self.min_val)  # Ensure range is at least 1

                if self.orientation == "horizontal":
                    rel_x = max(0, min(event.pos[0] - self.rect.x, self.rect.width))  # Clamp horizontal movement
                    ratio = rel_x / self.rect.width
                else:  # Vertical
                    rel_y = max(0, min(event.pos[1] - self.rect.y, self.rect.height))  # Clamp vertical movement
                    ratio = rel_y / self.rect.height

                # Adjust ratio for direction
                if (self.orientation == "horizontal" and self.direction == "rtl") or \
                   (self.orientation == "vertical" and self.direction == "btt"):
                    ratio = 1 - ratio

                new_value = self.min_val + ratio * range_val  # Calculate new slider value
                self.value = self.value_type(new_value)  # Cast to the original type (int or float)

                # Update handle position
                self.handle.rect.x = self._calculate_handle_position() if self.orientation == "horizontal" else self.handle.rect.x
                self.handle.rect.y = self._calculate_handle_position() if self.orientation == "vertical" else self.handle.rect.y
