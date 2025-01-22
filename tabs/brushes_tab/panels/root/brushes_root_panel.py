# BrushesRootPanel Implementation
import pygame
from ui.base_root_panel import BaseRootPanel
from tabs.brushes_tab.panels.user_brushes_panel import UserBrushesPanel
from tabs.brushes_tab.panels.brush_canvas_panel import BrushesCanvasPanel
from tabs.room_tab.panels.palette_panel import PalettePanel

class BrushesRootPanel(BaseRootPanel):
    def __init__(self, x, y, width, height):
        # Initialize the root panel for the brushes tab
        super().__init__(x, y, width, height, bg_color=(92, 92, 92), border_color=(105, 105, 105), border_width=0)
        self.initialize_ui()  # Set up the UI components

    def initialize_ui(self):
        # Add a sub-panel for brush controls
        self.userBrushesPanel = UserBrushesPanel(50,60, 400, 700)
        self.brusheCanvasPanel = BrushesCanvasPanel(460, 60, 800, 600)
        #self.palette_panel = PalettePanel(200+1210, 180, 475, 610, "X:/MY_GAME/my_playground/map_editor/sprites/huge_spritesheet.png", 32, 32, room_canvas=self.room_canvas_panel)
        

        self.add_existing_panel(self.userBrushesPanel)
        self.add_existing_panel(self.brusheCanvasPanel)
        #self.add_existing_panel(self.palette_panel)
        

    def handle_events(self, events):
        super().handle_events(events)  # Ensure parent event handling

    def draw(self, surface):
        # Draw the root panel and its child elements
        super().draw(surface)
        
    def on_select_brush_click(self):
        # Placeholder logic for selecting a brush
        print("Select Brush button clicked!")

    def on_add_brush_click(self):
        # Placeholder logic for adding a brush
        print("Add Brush button clicked!")

    def on_remove_brush_click(self):
        # Placeholder logic for removing a brush
        print("Remove Brush button clicked!")
