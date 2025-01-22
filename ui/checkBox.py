import pygame

class Checkbox:
    def __init__(self, x, y, size=20, checked=False, bg_color=(50, 50, 50), check_color=(0, 200, 0), callback=None):
        self.rect = pygame.Rect(x, y, size, size)  # The square representing the checkbox
        self.checked = checked  # Current state of the checkbox
        self.bg_color = bg_color  # Background color when unchecked
        self.check_color = check_color  # Color for the checkmark when checked
        self.callback = callback  # Function to call when toggled

    def toggle(self):
        self.checked = not self.checked  # Toggle the state
        if self.callback:  # Trigger the callback if provided
            self.callback(self.checked)

    def handle_event(self, events):
        # Ensure `events` is iterable (wrap a single event in a list if needed)
        if not isinstance(events, (list, tuple)):
            events = [events]

        # Process each event
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                if self.rect.collidepoint(event.pos):  # If the checkbox is clicked
                    self.toggle()
                    print(self.checked)

    def draw(self, surface):
        # Draw the checkbox background
        pygame.draw.rect(surface, self.bg_color, self.rect)
        # Draw the checkmark if checked
        if self.checked:
            pygame.draw.rect(surface, self.check_color, self.rect.inflate(-6, -6))  # Smaller rect inside
