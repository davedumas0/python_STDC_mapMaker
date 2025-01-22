# StoryRootPanel Implementation
import pygame
from ui.base_root_panel import BaseRootPanel
from tabs.story_tab.panels.story_panel import StoryPanel
from ui.ScrollablePanel import ScrollablePanel



class StoryRootPanel(BaseRootPanel):
    def __init__(self, x, y, width, height):
        # Initialize the root panel for the story tab
        super().__init__(x, y, width, height, bg_color=(160, 82, 45), border_color=(139, 69, 19), border_width=0)
        self.initialize_ui()  # Set up the UI components

    def initialize_ui(self):
        # Add a sub-panel for story controls
        #self.storyPanel = StoryPanel(150,150,200,80)

        self.roomsPanel = self.add_panel(20,5, 200, 600,(25,25,25), (200,175,80), 1)
        self.roomsPanel.add_text(75, 10-54,"rooms", 30, (255,255,255), (25,25,25))
        self.test =  ScrollablePanel(300, 150, 400, 300, layout_mode="grid", expand_direction="vertical")

        #self.test.add_button(0,5, 200-10,65,"df_1", self.on_load_room_click)
        self.test.add_button(0,0+65, 200-10,65,"df_2", self.on_load_room_click)
        self.test.add_button(0,0+65*2, 200-10,65,"df_3", self.on_load_room_click)
        self.test.add_button(0,0+65*3, 200-10,65,"df_4", self.on_load_room_click)
        self.test.add_button(0,0+65*4, 200-10,65,"df_5", self.on_load_room_click)
        self.test.add_button(0,0+65*5, 200-10,65,"df_6", self.on_load_room_click)
        self.test.add_button(0,0+65*6, 200-10,65,"df_7", self.on_load_room_click)
        self.test.add_button(0,0+65*7, 200-10,65,"df_8", self.on_load_room_click)
        self.test.add_button(0,0+65*8, 200-10,65,"df_9", self.on_load_room_click)
        self.test.add_button(0,0+65*9, 200-10,65,"df_10", self.on_load_room_click)
        self.add_existing_panel(self.test)

        self.roomsPanel.add_button(10, 45-54, 120, 30, "room_1", self.on_load_room_click) # this is a placeholder for the rooms data

    def draw(self, surface):
        # Draw the root panel and its child elements
        super().draw(surface)
        #self.storyPanel.draw(surface)

    def on_load_room_click(self):
        # Placeholder logic for adding a scene
        print("load room 1 button clicked!")

    def on_remove_scene_click(self):
        # Placeholder logic for removing a scene
        print("Remove Scene button clicked!")

    def on_story_settings_click(self):
        # Placeholder logic for story settings
        print("Story Settings button clicked!")
