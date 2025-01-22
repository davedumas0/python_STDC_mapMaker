import pygame
from ui.TextElement import TextElement

class MultiLineTextElement:
    def __init__(self, x, y, text, color=(255, 255, 255), bg_color=None, width=None, height=None):
        if width is None or height is None:  # Ensure width and height are provided
            raise ValueError("Both width and height must be specified for MultiLineTextElement.")

        self.x = x  # X-coordinate for the text block
        self.y = y  # Y-coordinate for the text block
        self.text = text  # The text content
        self.color = color  # Text color
        self.bg_color = bg_color  # Optional background color
        self.width = width  # Width for wrapping text
        self.height = height  # Height for text block
        self.font_size = 20  # Fixed font size
        self.text_elements = []  # List of TextElement instances
        self._wrap_text_to_fit()  # Wrap text to fit within the given dimensions

    def _wrap_text_to_fit(self):
        font = pygame.font.SysFont(None, self.font_size)  # Use the fixed font size
        words = self.text.split(' ')  # Split the text into words
        lines = []  # List to store the calculated lines
        current_line = ""  # Temporary holder for the current line

        for word in words:
            test_line = f"{current_line} {word}".strip()  # Test adding the word to the current line
            text_width, _ = font.size(test_line)  # Measure the width of the test line

            if text_width <= self.width:  # If the line fits, update the current line
                current_line = test_line
            else:
                if current_line:  # If the current line has content, finalize it
                    lines.append(current_line)
                current_line = word  # Start a new line with the current word

        if current_line:  # Append the last line if any
            lines.append(current_line)

        max_lines = self.height // font.get_linesize()  # Calculate the maximum number of lines that fit
        self._create_text_elements(lines[:max_lines])  # Truncate lines to fit height

    def _create_text_elements(self, lines):
        self.text_elements = []  # Reset the list of text elements
        font = pygame.font.SysFont(None, self.font_size)  # Recreate the font with the fixed size
        y_offset = 0  # Initialize the vertical offset

        for line in lines:
            text_element = TextElement(
                x=self.x, y=self.y + y_offset, text=line, font_size=self.font_size,
                color=self.color, bg_color=self.bg_color
            )
            self.text_elements.append(text_element)  # Add the new TextElement
            y_offset += font.get_linesize()  # Increment the offset by the font's line size

    def set_text(self, new_text):
        self.text = new_text  # Update the text content
        self._wrap_text_to_fit()  # Recalculate the text wrapping

    def draw(self, surface):
        for text_element in self.text_elements:  # Draw each TextElement instance
            text_element.draw(surface)
