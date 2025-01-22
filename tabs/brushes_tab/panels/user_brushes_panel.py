# room_canvas_panel.py

import pygame
from ui.base_panel import BasePanel

class UserBrushesPanel(BasePanel):
    def __init__(self, x, y, width, height):
        # Initialize the panel using the BasePanel class
        super().__init__(x, y, width, height, bg_color=(112, 128, 144), border_color=(120, 120, 160), border_width=1)
        self.testList = ["test", "test 2"]
        
        # Add placeholder buttons
        self.add_button(10, 10, width-20, 40, "create brush", self.on_action1_click)
        
        self.add_button(10, height-50, 150, 40, "save brush", self.on_action1_click)
        self.add_button(10+150+10, height-50, 150, 40, "load brush", self.on_action1_click)
        #self.add_dropdown(15, 80, 150,50,self.testList, self.on_action1_click,(25, 50,60), (200,200,200), (0,0,0))
        #self.add_button(10, 60, 150, 40, "Action 2", self.on_action2_click)
        #self.add_button(10, 110, 150, 40, "Action 3", self.on_action3_click)
        #self.room_controls_panel = self.add_panel(20, 20, 400, 200, bg_color=(50, 50, 90), border_color=(100, 100, 150), border_width=1)
        #self.playerStatsPanel = PlayerStartStats(0, 54, 800, 600-54)

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
