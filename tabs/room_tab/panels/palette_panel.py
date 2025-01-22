#palette_panel.py

import pygame
from ui.base_panel import BasePanel
from ui.sprite_sheet_manager import SpriteSheetManager

class PalettePanel(BasePanel):
    def __init__(self, x, y, width, height, tile_sheet_path, tile_width, tile_height, room_canvas):
        # Initialize the palette panel
        super().__init__(x, y, width, height, bg_color=(50, 50, 50), border_color=(200, 200, 200), border_width=2)
        self.tile_sheet_manager = SpriteSheetManager(tile_sheet_path, tile_width, tile_height)
        self.tiles = self.tile_sheet_manager.sprites  # Extracted tiles from the sprite sheet
        self.room_canvas_panel = room_canvas
        self.tiles_per_page = 96  # Number of tiles to show per page
        self.current_page = 0  # Current page index
        self.selected_tile_index = 0  # Index of the selected tile
        self.selected_sprite = None  # Actual selected sprite
        self.hovered_tile_index = None  # Index of the hovered tile
        self.tile_size = 40  # Size of each tile display
        self.tile_padding = 10  # Space between tiles
        self._setup_navigation_panel()  # Setup navigation buttons for paging

    def _setup_navigation_panel(self):
        """Set up navigation buttons for paging."""
        nav_panel_height = 50
        # create nav panel for the pages 
        self.nav_panel = BasePanel(
            self.rect.x + 10,
            self.rect.y + self.rect.height - nav_panel_height - 5,
            self.rect.width - 20,
            nav_panel_height,
            bg_color=(30, 30, 30),
            border_color=(100, 100, 100),
            border_width=1
        )

        # add nav panel to itself
        self.add_existing_panel(self.nav_panel)

        # Add navigation buttons for pages
        self.nav_panel.add_button(10, 10 - 54 - 5, 50, 30, "<", self.prev_page)
        self.nav_panel.add_button(self.rect.width - 60 - 20, 10 - 54 - 5, 50, 30, ">", self.next_page)

    def prev_page(self):
        """Navigate to the previous page."""
        if self.current_page > 0:
            self.current_page -= 1
            self._clear_highlights()

    def next_page(self):
        """Navigate to the next page."""
        max_pages = (len(self.tiles) + self.tiles_per_page - 1) // self.tiles_per_page
        if self.current_page < max_pages - 1:
            self.current_page += 1
            self._clear_highlights()

    def _clear_highlights(self):
        """Clear highlights when changing pages."""
        self.hovered_tile_index = None
        self.selected_tile_index = None
        self.selected_sprite = None

    def handle_event(self, event):
        """Handle user input events."""
        super().handle_event(event)
        if event.type == pygame.MOUSEMOTION:
            self.hovered_tile_index = self._get_tile_index_at(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
            self.selected_tile_index = self._get_tile_index_at(event.pos)
            self.room_canvas_panel.selectedTileIndex = self._get_tile_index_at(event.pos)

            self.selected_sprite = self._get_sprite_at(self.selected_tile_index)
            self.room_canvas_panel.selectedTilesprite = self._get_sprite_at(self.selected_tile_index)

    def _get_tile_index_at(self, pos):
        """Get the tile index at the mouse position."""
        mouse_x, mouse_y = pos
        if not self.rect.collidepoint(mouse_x, mouse_y):
            return None
        
        cols = (self.rect.width - self.tile_padding) // (self.tile_size + self.tile_padding)
        rows = self.tiles_per_page // cols

        for i in range(self.tiles_per_page):
            row = i // cols
            col = i % cols

            tile_x = self.rect.x + col * (self.tile_size + self.tile_padding) + self.tile_padding
            tile_y = self.rect.y + row * (self.tile_size + self.tile_padding) + self.tile_padding

            tile_rect = pygame.Rect(tile_x, tile_y, self.tile_size, self.tile_size)
            if tile_rect.collidepoint(mouse_x, mouse_y):
                return self.current_page * self.tiles_per_page + i
        return None

    def _get_sprite_at(self, index):
        """Get the sprite at the given index."""
        if index is not None and 0 <= index < len(self.tiles):
            return self.tiles[index]
        return None

    def get_selected_sprite(self):
        """Retrieve the currently selected sprite and its index."""
        return self.selected_sprite, self.selected_tile_index

    def draw(self, surface):
        """Draw the palette panel and its child elements."""
        super().draw(surface)

        # Draw tiles in a grid for the current page
        cols = (self.rect.width - self.tile_padding) // (self.tile_size + self.tile_padding)
        rows = self.tiles_per_page // cols

        start_index = self.current_page * self.tiles_per_page
        end_index = min(start_index + self.tiles_per_page, len(self.tiles))
        current_tiles = self.tiles[start_index:end_index]

        for i, tile in enumerate(current_tiles):
            row = i // cols
            col = i % cols

            tile_x = self.rect.x + col * (self.tile_size + self.tile_padding) + self.tile_padding
            tile_y = self.rect.y + row * (self.tile_size + self.tile_padding) + self.tile_padding

            # Scale the tile to fit within the display size
            scaled_tile = pygame.transform.scale(tile, (self.tile_size, self.tile_size))
            surface.blit(scaled_tile, (tile_x, tile_y))

            tile_index = start_index + i
            if tile_index == self.hovered_tile_index:
                pygame.draw.rect(surface, (255, 255, 0), (tile_x, tile_y, self.tile_size, self.tile_size), 2)  # Hover highlight
            if tile_index == self.selected_tile_index:
                pygame.draw.rect(surface, (0, 255, 0), (tile_x, tile_y, self.tile_size, self.tile_size), 2)  # Selection highlight

        # Draw navigation buttons
        self.nav_panel.draw(surface)
