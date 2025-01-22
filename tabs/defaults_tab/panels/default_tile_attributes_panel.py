# room_canvas_panel.py

import pygame
from ui.base_panel import BasePanel

class DefaultTileAttributes(BasePanel):
    def __init__(self, x, y, width, height):
        # Initialize the panel using the BasePanel class
        super().__init__(x, y, width, height, bg_color=(70, 70, 100), border_color=(120, 120, 160), border_width=1)
        
        # Add placeholder buttons
        self.add_button(10,10,50,30,"testing", self.on_action1_click)
        pass

    def on_action1_click(self):
        # Placeholder logic for Action 1 button
        print("Action 1 triggered!")

    def on_action2_click(self):
        # Placeholder logic for Action 2 button
        print("Action 2 triggered!")

    def on_action3_click(self):
        # Placeholder logic for Action 3 button
        print("Action 3 triggered!")

    def draw(self, surface):
        # Call the parent draw method to render the panel and its children
        super().draw(surface)

    def handle_event(self, event):
        # Call the parent handle_event method to propagate events to child elements
        super().handle_event(event)

# Usage Example (Would be integrated into the RoomRootPanel or similar structure)
# room_canvas_panel = RoomCanvasPanel(0, 0, 800, 600)
# room_canvas_panel.draw(surface)
# room_canvas_panel.handle_event(event)
