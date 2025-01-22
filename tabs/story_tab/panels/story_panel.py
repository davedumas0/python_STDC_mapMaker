import pygame
from ui.base_root_panel import BaseRootPanel

class StoryPanel(BaseRootPanel):
    def __init__(self, x, y, width, height):
        # Initialize the root panel for the settings tab
        super().__init__(x, y, width, height, bg_color=(160, 82, 45), border_color=(200, 200, 200), border_width=0)
        self.initialize_ui()  # Set up the UI components

    def initialize_ui(self):
        # Add a sub-panel for placeholder buttons
        

        # Add placeholder buttons to the sub-panel
        #self.full_tab_panel.add_button(10, 10, 150, 40, "Button 1", self.on_button1_click)
        #self.full_tab_panel.add_button(10, 60, 150, 40, "Button 2", self.on_button2_click)
        #self.full_tab_panel.add_button(10, 110, 150, 40, "Button 3", self.on_button3_click)
        pass


    def draw(self, surface):
        # Draw the root panel and its child elements
        super().draw(surface)
        

    def on_button1_click(self):
        # Placeholder logic for Button 1
        print("Button 1 clicked!")

    def on_button2_click(self):
        # Placeholder logic for Button 2
        print("Button 2 clicked!")

    def on_button3_click(self):
        # Placeholder logic for Button 3
        print("Button 3 clicked!")

    def toggle_auto_save(self):
        # Logic for toggling auto-save
        print("Auto-save toggled!")

    def save_settings(self):
        # Logic for saving settings
        print("Settings saved!")
