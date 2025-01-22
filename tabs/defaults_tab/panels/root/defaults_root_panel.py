# DefaultsRootPanel Implementation
import pygame
from ui.base_root_panel import BaseRootPanel
from tabs.defaults_tab.panels.default_tile_attributes_panel import DefaultTileAttributes

class DefaultsRootPanel(BaseRootPanel):
    def __init__(self, x, y, width, height):
        # Initialize the root panel for the defaults tab
        super().__init__(x, y, width, height, bg_color=(128, 128, 128), border_color=(128, 128, 128), border_width=1)
        self.initialize_ui()  # Set up the UI components

    def initialize_ui(self):
        # Add a sub-panel for default controls
        self.defaultTileAttributes = DefaultTileAttributes(55, 150, 200, 500)
        

    def handle_events(self, events):
        super().handle_events(events)  # Ensure parent event handling
        self.defaultTileAttributes.handle_event(events)

    def draw(self, surface):
        # Draw the root panel and its child elements
        super().draw(surface)
        self.defaultTileAttributes.draw(surface)

    def on_set_default_room_click(self):
        # Placeholder logic for setting the default room
        print("Set Default Room button clicked!")

    def on_set_default_map_click(self):
        # Placeholder logic for setting the default map
        print("Set Default Map button clicked!")

    def on_reset_defaults_click(self):
        # Placeholder logic for resetting defaults
        print("Reset Defaults button clicked!")
