import pygame
from ui.base_root_panel import BaseRootPanel
from tabs.room_tab.panels.room_canvas_panel import RoomCanvasPanel
from tabs.room_tab.panels.sprite_navigator_panel import SpriteNavigatorPanel

tabButtonOffset = 54

class RoomRootPanel(BaseRootPanel):
    def __init__(self, x, y, width, height):
        # Initialize the root panel for the room tab
        super().__init__(x, y, width, height, bg_color=(80, 80, 120), border_color=(150, 150, 200), border_width=0)
        self.initialize_ui()  # Set up the UI components

    def initialize_ui(self):
        
        # create palette panel for sprite selection
        self.palettePanel = SpriteNavigatorPanel(1150, 150, 675, 700,"X:/MY_GAME/my_playground/map_editor/sprites", (50,50,50), (10,25,200),0)
        
        # create room canvas panel
        self.room_canvas_panel = RoomCanvasPanel(325, 130, 800, 500, 32, self.palettePanel)
        self.add_existing_panel(self.room_canvas_panel)
        
        self.room_canvas_panel.grid_width = 10
        self.room_canvas_panel.grid_height = 10

        # LAYER CONTROL
        # add panel for fill and clear canvas buttons 
        self.basic_tools_panel = self.add_panel(200, 0, 120, 100, (25,50,25), (50,25,50), 1)
        # add the fill button
        self.basic_tools_panel.add_button(10,10,100, 30, "fill layer", self.testFunc_fill)
        # add the clear button
        self.basic_tools_panel.add_button(10,10+30+10,100, 30, "clear layer", self.testFunc_clear)


        # add panel for room size slider
        self.roomControlPanel = self.add_panel(75, 0, 95, 115, (30,40,30), (40,30,40), 1)

        self.roomControlPanel.add_text(5, 0+5, "x axis", 20, (255,255,255))
        self.roomSizeSliderXAxis = self.roomControlPanel.add_slider(10, 0, 75, 20, 4, 24, 4)

        self.roomControlPanel.add_text(5, 5+35+20, "y axis", 20, (255,255,255))
        self.roomSizeSliderYAxis = self.roomControlPanel.add_slider(10, 40, 75, 20, 4, 13, 4)


        # add room canvas panel to root panel
        self.add_existing_panel(self.room_canvas_panel)


    def handle_events(self, events):
        super().handle_events(events)  # Ensure parent event handling
        self.palettePanel.handle_event(events)
        self.room_canvas_panel.handle_event(events)
        self.room_canvas_panel.grid_width = self.roomSizeSliderXAxis.value
        self.room_canvas_panel.grid_height = self.roomSizeSliderYAxis.value
        
    def testFunc_fill(self):
        print("test function FILL")

    
    def testFunc_clear(self):
        print("test function CLEAR")

        
        

    def draw(self, surface):
        # Draw the root panel and its child elements
        super().draw(surface)
        #self.room_canvas_panel.draw(surface)
        self.palettePanel.draw(surface)

    def on_add_room_click(self):
        # Placeholder logic for adding a room
        print("Add Room button clicked!")

    def on_remove_room_click(self):
        # Placeholder logic for removing a room
        print("Remove Room button clicked!")

    def on_room_settings_click(self):
        # Placeholder logic for room settings
        print("Room Settings button clicked!")