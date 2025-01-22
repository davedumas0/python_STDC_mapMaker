
#file: tabs.map_tab.root.map_root_panel.py

import pygame
from ui.base_root_panel import BaseRootPanel

from tabs.map_tab.panels.available_maps_panel import AvailableMapsPanel
from ui.jsonManager import JSONManager
from ui.popup_panel import BasePopup

class MapRootPanel(BaseRootPanel):
    def __init__(self, x, y, width, height, metadata):
        super().__init__(x, y, width, height, bg_color=(205, 133, 63), border_color=(139, 69, 19), border_width=0)

        self.metadata = metadata  # Shared metadata for all tabs
        self.json_manager = JSONManager()  # JSON manager for file handling
        self.popup = None  # Placeholder for active popup
        self.initialize_ui()  # Initialize UI components

    def initialize_ui(self):
        # Panel for available maps
        #self.availMaps = AvailableMapsPanel(10, 154, 300, 300)
        #self.availMaps.load_maps()  # Load existing maps into the panel
        #self.add_existing_panel(self.availMaps)
        self.availMaps = self.add_panel(10, 100, 200, 300,(25,25,25),(50,50,50),1)
        self.availMaps.add_button(10,10,150, 30, "new map", self.show_create_map_popup)

        

       
        

        # Add "Create Map" button
        #self.availMaps.add_button(150 - 125 / 2, 0, 125, 30, "Create Map", self.show_create_map_popup)
    def testFunc(self):
        print("test function")

    def show_create_map_popup(self):
        # Display a popup for entering the map name
        self.popup = BasePopup(
            x=self.rect.width // 2 - 200,
            y=self.rect.height // 2 - 100,
            min_width=200,
            min_height=100,
            message="Set new map attributes:",
            on_accept=self.create_map,
            on_cancel=self.close_popup
        )
        self.popup.add_text(300, 10, "map name: ", 28)
        self.popup.add_text_input(430, 10, 200,30,24,(255,255,255),(120,120,120),(0,0,0),0)
        
        self.popup.add_text(20, 75, "turn based combat: ", 24)
        self.popup.add_checkbox(185, 75, 19, False, (122,150,130), (50,255,50))

        self.popup.add_text(20, 75+65, "crafting: ", 24)
        self.popup.add_checkbox(185, 75+65, 19, False, (122,150,130), (50,255,50))

        self.popup.add_text(20, 75+65*2, "multi-party: ", 24)
        self.popup.add_checkbox(185, 75+65*2, 19, False, (122,150,130), (50,255,50))

        self.popup.add_text(20, 75+65*3, "day-night cycle: ", 24)
        self.popup.add_checkbox(185, 75+65*3, 19, False, (122,150,130), (50,255,50))

        self.popup.add_text(20, 75+65*4, "economy: ", 24)
        self.popup.add_checkbox(185, 75+65*4, 19, False, (122,150,130), (50,255,50))

        self.popup.add_text(300, 75+65*0, "wheather: ", 24)
        self.popup.add_checkbox(300+185, 75+65*0, 19, False, (122,150,130), (50,255,50))

        self.popup.add_text(300, 75+65*1, "seasons: ", 24)
        self.popup.add_checkbox(300+185, 75+65*1, 19, False, (122,150,130), (50,255,50))

        self.popup.add_text(300, 75+65*2, "perma-death: ", 24)
        self.popup.add_checkbox(300+185, 75+65*2, 19, False, (122,150,130), (50,255,50))

        self.popup.add_text(300, 75+65*3, "fog of war: ", 24)
        self.popup.add_checkbox(300+185, 75+65*3, 19, False, (122,150,130), (50,255,50))

        self.popup.add_text(300, 75+65*4, "side scroller: ", 24)
        self.popup.add_checkbox(300+185, 75+65*4, 19, False, (122,150,130), (50,255,50))
        
        



    def create_map(self, map_name="new_map"):
        # Ensure the map name is valid
        if not map_name.strip():
            print("Map name cannot be empty.")
            return

        # Default map structure
        new_map_data = {
            "map_data": {
                "room_data": {
                    "startRoom": {
                        "roomData": {"size_X": 10, "size_Y": 10},
                        "tileData": []  # Empty tile data for the start room
                    }
                }
            }
        }

        # Save the new map using a unique filename
        unique_filename = self.json_manager.generate_unique_filename(map_name)
        self.json_manager.save(new_map_data, unique_filename)

        # Load the new map into metadata for sharing between tabs
        self.metadata.clear()
        self.metadata.update(new_map_data)
        print(f"New map '{map_name}' created and loaded into metadata.")
        print(self.metadata)

        # Refresh available maps panel
        self.availMaps.load_maps()

        # Close the popup
        self.close_popup()

    def close_popup(self):
        # Close the active popup
        self.popup = None

    def draw(self, surface):
        # Draw the root panel and its child elements
        super().draw(surface)
        if self.popup:
            self.popup.draw(surface)

    def handle_event(self, events):
        # Handle events for the root panel and the popup
        super().handle_event(events)
        if self.popup:
            self.popup.handle_event(events)
