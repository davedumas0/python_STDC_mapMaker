# base_palette_panel.py

import pygame
from ui.base_panel import BasePanel



class BasePalettePanel(BasePanel):
    def __init__(self, x, y, width, height, bg_color=(50, 50, 50), border_color=(200, 200, 200), border_width=2):
        # Initialize the base palette panel
        super().__init__(x, y, width, height, bg_color, border_color, border_width)
        
        self.items = []  # List to store palette items
        self.items_per_page = 96  # Number of items displayed per page
        self.current_page = 0  # Current page index
        self.selected_item_index = None  # Index of the selected item
        self.hovered_item_index = None  # Index of the hovered item
        self.item_size = 40  # Size of each palette item display
        self.item_padding = 10  # Space between items
        
        self._setup_navigation_panel()  # Setup navigation buttons for paging

    def _setup_navigation_panel(self):
        """Set up navigation buttons for paging."""
        nav_panel_height = 50
        self.nav_panel = BasePanel(
            self.rect.x + 10,
            self.rect.y + self.rect.height - nav_panel_height - 5,
            self.rect.width - 20,
            nav_panel_height,
            bg_color=(30, 30, 30),
            border_color=(100, 100, 100),
            border_width=1
        )
        self.add_existing_panel(self.nav_panel)

        # Add navigation buttons
        self.nav_panel.add_button(10, 10, 50, 30, "<", self.prev_page)
        self.nav_panel.add_button(self.rect.width - 70, 10, 50, 30, ">", self.next_page)

    def prev_page(self):
        """Navigate to the previous page."""
        if self.current_page > 0:
            self.current_page -= 1
            self._clear_highlights()

    def next_page(self):
        """Navigate to the next page."""
        max_pages = (len(self.items) + self.items_per_page - 1) // self.items_per_page
        if self.current_page < max_pages - 1:
            self.current_page += 1
            self._clear_highlights()

    def _clear_highlights(self):
        """Clear highlights when changing pages."""
        self.hovered_item_index = None
        self.selected_item_index = None

    def add_item(self, item):
        """Add an item to the palette."""
        self.items.append(item)

    def handle_event(self, event):
        """Handle user input events."""
        super().handle_event(event)
        if event.type == pygame.MOUSEMOTION:
            self.hovered_item_index = self._get_item_index_at(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            self.selected_item_index = self._get_item_index_at(event.pos)

    def _get_item_index_at(self, pos):
        """Get the item index at the mouse position."""
        mouse_x, mouse_y = pos
        if not self.rect.collidepoint(mouse_x, mouse_y):
            return None

        cols = (self.rect.width - self.item_padding) // (self.item_size + self.item_padding)
        rows = self.items_per_page // cols

        for i in range(self.items_per_page):
            row = i // cols
            col = i % cols

            item_x = self.rect.x + col * (self.item_size + self.item_padding) + self.item_padding
            item_y = self.rect.y + row * (self.item_size + self.item_padding) + self.item_padding

            item_rect = pygame.Rect(item_x, item_y, self.item_size, self.item_size)
            if item_rect.collidepoint(mouse_x, mouse_y):
                return self.current_page * self.items_per_page + i
        return None

    def get_selected_item(self):
        """Retrieve the currently selected item and its index."""
        if self.selected_item_index is not None and 0 <= self.selected_item_index < len(self.items):
            return self.items[self.selected_item_index], self.selected_item_index
        return None, None

    def draw(self, surface):
        """Draw the palette panel and its child elements."""
        super().draw(surface)

        # Draw items in a grid for the current page
        cols = (self.rect.width - self.item_padding) // (self.item_size + self.item_padding)
        rows = self.items_per_page // cols

        start_index = self.current_page * self.items_per_page
        end_index = min(start_index + self.items_per_page, len(self.items))
        current_items = self.items[start_index:end_index]

        for i, item in enumerate(current_items):
            row = i // cols
            col = i % cols

            item_x = self.rect.x + col * (self.item_size + self.item_padding) + self.item_padding
            item_y = self.rect.y + row * (self.item_size + self.item_padding) + self.item_padding

            # Scale the item if it's an image (optional for extensions)
            pygame.draw.rect(surface, item, (item_x, item_y, self.item_size, self.item_size))

            item_index = start_index + i
            if item_index == self.hovered_item_index:
                pygame.draw.rect(surface, (255, 255, 0), (item_x, item_y, self.item_size, self.item_size), 2)  # Hover highlight
            if item_index == self.selected_item_index:
                pygame.draw.rect(surface, (0, 255, 0), (item_x, item_y, self.item_size, self.item_size), 2)  # Selection highlight

        # Draw navigation buttons
        self.nav_panel.draw(surface)
