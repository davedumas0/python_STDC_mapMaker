import pygame

class ProgressBar:
    def __init__(self, x, y, width, height, max_value=100, start_value=0, bg_color=(50, 50, 50), bar_color=(0, 200, 0)):
        self.rect = pygame.Rect(x, y, width, height)  # Full progress bar rectangle
        self.max_value = max_value  # Maximum value of the progress bar
        self.value = start_value  # Current value of the progress bar
        self.bg_color = bg_color  # Background color of the bar
        self.bar_color = bar_color  # Color of the progress bar

    def set_value(self, value):
        # Set the current value of the progress bar, clamped between 0 and max_value
        self.value = max(0, min(value, self.max_value))

    def increment(self, amount):
        # Increment the current value of the progress bar
        self.set_value(self.value + amount)

    def draw(self, surface):
        # Draw the background of the progress bar
        pygame.draw.rect(surface, self.bg_color, self.rect)

        # Calculate the width of the filled portion
        fill_width = (self.value / self.max_value) * self.rect.width

        # Draw the filled portion of the progress bar
        fill_rect = pygame.Rect(self.rect.x, self.rect.y, fill_width, self.rect.height)
        pygame.draw.rect(surface, self.bar_color, fill_rect)

        # Optionally draw a border around the progress bar
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2)