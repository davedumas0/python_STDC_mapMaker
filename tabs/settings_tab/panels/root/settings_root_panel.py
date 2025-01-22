import pygame
from ui.base_root_panel import BaseRootPanel
from tabs.settings_tab.panels.settings_autoSave import SettingsAutoSave


class SettingsRootPanel(BaseRootPanel):
    def __init__(self, x, y, width, height):
        # Initialize the root panel for the settings tab
        super().__init__(x, y, width, height, bg_color=(100, 100, 100), border_color=(200, 200, 200), border_width=0)
        self.initialize_ui()  # Set up the UI components

    def initialize_ui(self):
        # Add a sub-panel for placeholder buttons
        self.autoSavePanel = SettingsAutoSave(20,50, 600, 200)
        self.autoSavePanel.add_checkbox(25,50,20,False)
        self.add_existing_panel(self.autoSavePanel)
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
