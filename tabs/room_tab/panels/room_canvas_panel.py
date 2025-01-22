# room_canvas_panel.py

import pygame
from ui.base_panel import BasePanel
from ui.slider import Slider
from ui.TextElement import TextElement

class RoomCanvasPanel(BasePanel):
    def __init__(self, x, y, width, height, grid_size, palettePanel):
        # Initialize the panel using the BasePanel class
        super().__init__(x, y, width, height, bg_color=(70, 70, 100), border_color=(120, 120, 160), border_width=1)
        
        self.grid_size = grid_size
        self.grid_width = width // grid_size
        self.grid_height = height // grid_size
        self.palettePanel = palettePanel
        self.selected_sprite = palettePanel.selected_sprite

        # Layers: Base, Floor, Structure, Entity
        self.layers = {
            "Base": [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)],
            "Floor": [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)],
            "Structure": [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)],
            "Entity": [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        }
        self.active_layer = "Base"
        
        self.selected_tile_index = 0
        self.selected_tile_sprite = None
        
        # Keep track of the last placed tile for line painting
        self.last_placed_tile = None  

        self._setup_layer_buttons()

    def add_text(self, rel_x, rel_y, text, font_size=24, color=(255, 255, 255), bg_color=None):
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y 
        text_element = TextElement(abs_x, abs_y, text, font_size, color, bg_color)
        self.add_to_page(text_element)
        return text_element
    
    def add_slider(self, rel_x, rel_y, width, height, min_val=0, max_val=100, start_val=50):
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y 
        slider = Slider(abs_x, abs_y, width, height, min_val, max_val, start_val)
        self.add_to_page(slider)
        return slider


    def _setup_layer_buttons(self):
        """Set up buttons to switch between layers."""
        button_width = 80
        button_height = 30
        button_padding = 10
    
        layers = list(self.layers.keys())
        for i, layer_name in enumerate(layers):
            button = self.add_button(
                button_padding + i * (button_width + button_padding),
                -button_height - button_padding - 20 ,  # Adjusted position above the canvas
                button_width,
                button_height,
                layer_name,
                callback=lambda ln=layer_name: self.set_active_layer(ln)
            )
            button.type = "normal"  # Ensure buttons are standard, not tab-specific


    def set_active_layer(self, layer_name):
        """Set the active layer for painting."""
        if layer_name in self.layers:
            self.active_layer = layer_name
            print("active layer set")

    def set_tile(self, x, y, tile_index, tile_sprite):
        """Set a tile at the given grid coordinates in the active layer."""
        if 0 <= x < self.grid_width and 0 <= y < self.grid_height:
            self.layers[self.active_layer][y][x] = (tile_index, tile_sprite)

    def draw(self, surface):
        """Draw the panel and the grid."""
        super().draw(surface)

        # Draw all layers in order
        for layer_name, layer in self.layers.items():
            for y in range(self.grid_height):
                for x in range(self.grid_width):
                    tile = layer[y][x]
                    if tile and tile[1]:
                        tile_rect = pygame.Rect(
                            self.rect.x + x * self.grid_size,
                            self.rect.y + y * self.grid_size,
                            self.grid_size,
                            self.grid_size
                        )
                        surface.blit(pygame.transform.scale(tile[1], (self.grid_size, self.grid_size)), tile_rect.topleft)

        # Draw grid lines
        for x in range(self.grid_width + 1):
            pygame.draw.line(surface, (100, 100, 100),
                             (self.rect.x + x * self.grid_size, self.rect.y),
                             (self.rect.x + x * self.grid_size, self.rect.y + self.grid_height * self.grid_size))
        for y in range(self.grid_height + 1):
            pygame.draw.line(surface, (100, 100, 100),
                             (self.rect.x, self.rect.y + y * self.grid_size),
                             (self.rect.x + self.grid_width * self.grid_size, self.rect.y + y * self.grid_size))

    def handle_event(self, events):
        """Handle a list of user input events."""
        if not isinstance(events, (list, tuple)):
            events = [events]  # Ensure events is always a list

        # First, process events for child elements
        for child in self.children:
            if hasattr(child, 'handle_event'):
                child.handle_event(events)

        # Then, process events specific to RoomCanvasPanel
        for event in events:
            if hasattr(self.palettePanel, "selected_sprite"):
                self.selected_tile_sprite = self.palettePanel.selected_sprite

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                mouse_x, mouse_y = event.pos
                grid_x = (mouse_x - self.rect.x) // self.grid_size
                grid_y = (mouse_y - self.rect.y) // self.grid_size

                if 0 <= grid_x < self.grid_width and 0 <= grid_y < self.grid_height:
                    self.set_tile(grid_x, grid_y, self.selected_tile_index, self.selected_tile_sprite)

                    if pygame.key.get_mods() & pygame.KMOD_SHIFT and self.last_placed_tile:
                        self._paint_line(self.last_placed_tile, (grid_x, grid_y))

                    self.last_placed_tile = (grid_x, grid_y)


    
    def _process_single_event(self, event):
        """Process a single input event."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            mouse_x, mouse_y = event.pos
            grid_x = (mouse_x - self.rect.x) // self.grid_size
            grid_y = (mouse_y - self.rect.y) // self.grid_size
    
            if 0 <= grid_x < self.grid_width and 0 <= grid_y < self.grid_height:
                self.set_tile(grid_x, grid_y, self.selected_tile_index, self.selected_tile_sprite)
    
                if pygame.key.get_mods() & pygame.KMOD_SHIFT and self.last_placed_tile:
                    self._paint_line(self.last_placed_tile, (grid_x, grid_y))
    
                self.last_placed_tile = (grid_x, grid_y)
    

    def _paint_line(self, start, end):
        """Paint a line of tiles from start to end in the active layer."""
        x1, y1 = start
        x2, y2 = end

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        err = dx - dy

        while True:
            self.set_tile(x1, y1, self.selected_tile_index, self.selected_tile_sprite)
            if (x1, y1) == (x2, y2):
                break
            e2 = err * 2
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

                

    def set_selected_tile(self, tile_index, tile_sprite):
        """Set the currently selected tile."""
        self.selected_tile_index = tile_index
        self.selected_tile_sprite = self.selected_sprite
