import pygame

class DropdownMenu:
    def __init__(self, x, y, width, height, options, callback=None, bg_color=(50, 50, 50), text_color=(255, 255, 255), border_color=(200, 200, 200)):
        # Initialize the dropdown menu with position, dimensions, and styling
        self.rect = pygame.Rect(x, y, width, height)  # Main dropdown box rectangle
        self.options = options  # List of available options in the dropdown
        self.selected_option = options[0] if options else None  # Default to the first option, if any
        self.callback = callback  # Function to call when an option is selected
        self.bg_color = bg_color  # Background color of the dropdown box
        self.text_color = text_color  # Color of the option text
        self.border_color = border_color  # Color of the dropdown border
        self.font = pygame.font.SysFont(None, 24)  # Font used for text rendering
        self.is_open = False  # Dropdown is initially closed

        # Button for toggling dropdown (placed on the right side of the dropdown box)
        self.button_rect = pygame.Rect(x + width - height, y, height, height)  # Square button

    def toggle(self):
        # Toggle the dropdown's open/closed state
        self.is_open = not self.is_open

    def select_option(self, index):
        # Select an option by index and trigger the callback
        self.selected_option = self.options[index]  # Update the selected option
        self.is_open = False  # Close the dropdown menu
        if self.callback:  # Trigger the callback if one is defined
            self.callback(self.selected_option)

    def handle_event(self, event):
        # Handle mouse events for the dropdown and its toggle button
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Check for left mouse button click
            if self.button_rect.collidepoint(event.pos):  # Clicked on the toggle button
                self.toggle()  # Toggle the dropdown menu
            elif self.rect.collidepoint(event.pos):  # Clicked on the main dropdown box
                self.toggle()
            elif self.is_open:  # If the dropdown is open, check for option clicks
                for i, option in enumerate(self.options):
                    # Create a rectangle for each option below the main box
                    option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)
                    if option_rect.collidepoint(event.pos):  # Check if the click is on an option
                        self.select_option(i)  # Select the clicked option
                        break

    def draw(self, surface):
        # Draw the main dropdown box
        pygame.draw.rect(surface, self.bg_color, self.rect)  # Draw the background
        pygame.draw.rect(surface, self.border_color, self.rect, 1)  # Draw the border

        # Render the selected option text
        if self.selected_option:
            text_surface = self.font.render(self.selected_option, True, self.text_color)  # Render text
            surface.blit(text_surface, text_surface.get_rect(center=self.rect.center))  # Center the text

        # Draw the toggle button
        pygame.draw.rect(surface, (70, 70, 70), self.button_rect)  # Background for the button
        pygame.draw.rect(surface, self.border_color, self.button_rect, 1)  # Button border

        # Render a small triangle (down arrow) in the button
        triangle_color = self.text_color
        triangle_points = [
            (self.button_rect.centerx, self.button_rect.centery + 5),
            (self.button_rect.centerx - 5, self.button_rect.centery - 5),
            (self.button_rect.centerx + 5, self.button_rect.centery - 5)
        ]
        pygame.draw.polygon(surface, triangle_color, triangle_points)

        # If the dropdown is open, draw all options
        if self.is_open:
            for i, option in enumerate(self.options):
                # Calculate the rectangle for each option
                option_rect = pygame.Rect(self.rect.x, self.rect.y + (i + 1) * self.rect.height, self.rect.width, self.rect.height)

                # Highlight the hovered option
                if option_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(surface, (80, 80, 200), option_rect)  # Highlight background color
                else:
                    pygame.draw.rect(surface, self.bg_color, option_rect)  # Default background

                pygame.draw.rect(surface, self.border_color, option_rect, 1)  # Draw the border for each option

                # Render and position the option text
                option_surface = self.font.render(option, True, self.text_color)
                surface.blit(option_surface, option_surface.get_rect(center=option_rect.center))
