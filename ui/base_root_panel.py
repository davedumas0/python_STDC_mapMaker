import pygame
from ui.base_panel import BasePanel


class BaseRootPanel(BasePanel):
    def __init__(self, x, y, width, height, bg_color=(30, 30, 30), border_color=(255, 255, 255), border_width=0, tab_button_height=50):
        # Initialize the root panel with position, size, and appearance
        super().__init__(x, y, width, height, bg_color, border_color, border_width)
        self.tab_button_height = 54
        # Create a full-tab panel slightly darker than the background color
        #darker_bg_color = tuple(max(c - 20, 0) for c in bg_color)  # Darken the background color
        #self.full_tab_panel = self.add_panel(0, tab_button_height, width, height - tab_button_height, bg_color=darker_bg_color, border_color=(200, 200, 200), border_width=0)

    
    def add_button(self, rel_x, rel_y, width, height, text, callback=None):
        # Override to compensate for the tab button height
        adjusted_y = rel_y + self.tab_button_height  # Shift down by the tab button height
        return super().add_button(rel_x, adjusted_y, width, height, text, callback)

    def add_panel(self, rel_x, rel_y, width, height, bg_color=(60, 60, 60), border_color=(180, 180, 180), border_width=1):
        # Override to compensate for the tab button height
        adjusted_y = rel_y + self.tab_button_height  # Shift down by the tab button height
        return super().add_panel(rel_x, adjusted_y, width, height, bg_color, border_color, border_width)

    def add_slider(self, rel_x, rel_y, width, height, min_val=0, max_val=100, start_val=50):
        # Override to compensate for the tab button height
        adjusted_y = rel_y + self.tab_button_height  # Shift down by the tab button height
        return super().add_slider(rel_x, adjusted_y, width, height, min_val, max_val, start_val)

    def add_dropdown(self, rel_x, rel_y, width, height, options, callback=None, bg_color=(60, 60, 60), text_color=(255, 255, 255), border_color=(180, 180, 180)):
        # Override to compensate for the tab button height
        adjusted_y = rel_y + self.tab_button_height  # Shift down by the tab button height
        return super().add_dropdown(rel_x, adjusted_y, width, height, options, callback, bg_color, text_color, border_color)

    def add_text(self, rel_x, rel_y, text, font_size=24, color=(255, 255, 255), bg_color=None):
        # Override to compensate for the tab button height
        adjusted_y = rel_y + self.tab_button_height  # Shift down by the tab button height
        return super().add_text(rel_x, adjusted_y, text, font_size, color, bg_color)

    def add_checkbox(self, rel_x, rel_y, size=20, checked=False, bg_color=(50, 50, 50), check_color=(0, 200, 0), callback=None):
        # Override to compensate for the tab button height
        adjusted_y = rel_y + self.tab_button_height  # Shift down by the tab button height
        return super().add_checkbox(rel_x, adjusted_y, size, checked, bg_color, check_color, callback)
    
    def add_existing_panel(self, panel):
        """
        Adjust the y-coordinate of the existing panel to account for the tab button height
        and add it to the children list.
        """
        panel.rect.y += 54  # Shift the panel's position down
        self.children.append(panel)  # Add the panel to the children list
        return panel  # Return the panel instance for reference

    def handle_events(self, events):
        """Handle events for the root panel and its children."""
        if not isinstance(events, (list, tuple)):
            events = [events]

        for event in events:
            super().handle_event(event)  # Pass single event to the parent class

    def handle_events(self, events):
        """Handle a list of events for the root panel and its children."""
        if not isinstance(events, (list, tuple)):
            events = [events]  # Ensure events is always a list

        super().handle_event(events)  # Pass the list to the parent class


    def update(self, dt):
        # Update logic for the root panel
        pass

    def draw(self, surface):
        # Draw the root panel background and border
        super().draw(surface)
        
        # Ensure the full-tab panel and its children are drawn
        #if hasattr(self.full_tab_panel, 'draw'):
        #    self.full_tab_panel.draw(surface)
