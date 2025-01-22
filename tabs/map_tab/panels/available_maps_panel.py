# tabs.map_tab.panels.available_maps_panel.py

import pygame
from ui.base_panel import BasePanel


class AvailableMapsPanel(BasePanel):
    def __init__(self, x, y, width, height):
        # Initialize the panel using the BasePanel class
        super().__init__(x, y, width, height, bg_color=(70, 70, 100), border_color=(120, 120, 160), border_width=0)
        
        # Add placeholder buttons
        pass

    def load_maps(self):
        
        pass

    def draw(self, surface):
        # Call the parent draw method to render the panel and its children
        super().draw(surface)

    def handle_event(self, event):
        # Call the parent handle_event method to propagate events to child elements
        super().handle_event(event)

