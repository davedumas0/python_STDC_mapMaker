# PlayerRootPanel Implementation
import pygame
from ui.base_root_panel import BaseRootPanel
from tabs.player_tab.panels.player_starting_stats_panel import PlayerStartStats


class PlayerRootPanel(BaseRootPanel):
    def __init__(self, x, y, width, height):
        # Initialize the root panel for the player tab
        super().__init__(x, y, width, height, bg_color=(46, 139, 87), border_color=(34, 139, 34), border_width=1)
        self.initialize_ui()  # Set up the UI components

    def initialize_ui(self):
        # Add a sub-panel for player controls
        self.playerStatsPanel = PlayerStartStats(500, 150, 400, 300)
        #self.player_palette_pnel = PalettePanel(5,150, 475, 610, "X:/MY_GAME/my_playground/map_editor/sprites/MASTER_spritesheet.png", 32, 32)
        self.playerStatsPanel.add_multiline_text(10,10,"", (255,255,255), (10,55,120), 390, 290)
        self.add_existing_panel(self.playerStatsPanel)
        #self.add_existing_panel(self.player_palette_pnel)
        

    def draw(self, surface):
        # Draw the root panel and its child elements
        super().draw(surface)
        

    def on_add_player_click(self):
        # Placeholder logic for adding a player
        print("Add Player button clicked!")

    def on_remove_player_click(self):
        # Placeholder logic for removing a player
        print("Remove Player button clicked!")

    def on_player_settings_click(self):
        # Placeholder logic for player settings
        print("Player Settings button clicked!")
