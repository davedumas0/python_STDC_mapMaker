# BrushesTab Implementation
from tabs.base_tab import BaseTab
from tabs.brushes_tab.panels.root.brushes_root_panel import BrushesRootPanel

class BrushesTab(BaseTab):
    def __init__(self, metadata, button_callback, button_x):
        # Initialize the base tab with metadata and button details
        super().__init__(
            metadata,
            name="Brushes",
            bg_color=(92, 92, 92),  # Slate gray for brushes background
            button_x=button_x,  # X-coordinate for the button
            button_callback=button_callback,
        )
        # Initialize the root panel for the brushes tab
        self.root_panel = BrushesRootPanel(1, 54, 1918, 1080 - 55)  # Panel starts below the tab buttons

    def handle_events(self, events):
        # Forward events to the root panel
        self.root_panel.handle_events(events)

    def update(self, dt):
        # Update logic for the root panel
        self.root_panel.update(dt)

    def draw_button(self, surface, is_active):
        # Draw the button with an active/inactive state indicator
        self.button.draw(surface, is_active=is_active)

    def draw(self, surface):
        # Draw the background color for the tab
        super().draw(surface)
        # Draw the root panel and all its child elements
        self.root_panel.draw(surface)
