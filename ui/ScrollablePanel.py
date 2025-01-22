# ui.scrollable_panel.py

import pygame
from ui.base_panel import BasePanel

class ScrollablePanel(BasePanel):
    def __init__(
        self, x, y, width, height, layout_mode="free", expand_direction="vertical",
        bg_color=(50, 50, 50), border_color=(200, 200, 200), border_width=2
    ):
        super().__init__(x, y, width, height, bg_color, border_color, border_width)
        self.scroll_offset = 0  # Tracks scroll offset
        self.layout_mode = layout_mode  # "grid" or "free" layout mode
        self.expand_direction = expand_direction  # Expansion direction for grid mode
        self.grid_spacing = 10  # Spacing between grid items
        self.grid_position = [0, 0]  # Current grid placement position (x, y)

        # Scroll handling
        self.total_content_size = 0  # Total size of the content (height or width based on direction)
        self.visible_area_size = height if expand_direction == "vertical" else width

        # Scrollbar properties
        self.scrollbar_thickness = 20
        self.scrollbar_color = (70, 70, 70)  # Background of the scrollbar
        self.scrollbar_handle_color = (150, 150, 150)  # Handle color

    def _update_scroll_area(self):
        if self.expand_direction == "vertical":
            self.total_content_size = sum(child.rect.height for child in self.children) + len(self.children) * self.grid_spacing
        else:
            self.total_content_size = sum(child.rect.width for child in self.children) + len(self.children) * self.grid_spacing
    

    def _draw_scrollbar(self, surface):
        if self.total_content_size <= self.visible_area_size:
            return  # No need to draw scrollbar if content fits within the visible area
    
        if self.expand_direction == "vertical":
            scrollbar_rect = pygame.Rect(
                self.rect.right - self.scrollbar_thickness, self.rect.top, self.scrollbar_thickness, self.rect.height
            )
            handle_height = max(int((self.visible_area_size / self.total_content_size) * scrollbar_rect.height), 20)
            handle_position = int((self.scroll_offset / max(1, self.total_content_size - self.visible_area_size)) * (scrollbar_rect.height - handle_height))
            handle_rect = pygame.Rect(
                scrollbar_rect.left, scrollbar_rect.top + handle_position, self.scrollbar_thickness, handle_height
            )
        else:
            scrollbar_rect = pygame.Rect(
                self.rect.left, self.rect.bottom - self.scrollbar_thickness, self.rect.width, self.scrollbar_thickness
            )
            handle_width = max(int((self.visible_area_size / self.total_content_size) * scrollbar_rect.width), 20)
            handle_position = int((self.scroll_offset / max(1, self.total_content_size - self.visible_area_size)) * (scrollbar_rect.width - handle_width))
            handle_rect = pygame.Rect(
                scrollbar_rect.left + handle_position, scrollbar_rect.top, handle_width, self.scrollbar_thickness
            )
    
        # Draw the scrollbar background
        pygame.draw.rect(surface, self.scrollbar_color, scrollbar_rect)
    
        # Draw the scrollbar handle with a distinct color
        pygame.draw.rect(surface, self.scrollbar_handle_color, handle_rect)
    

    def add_child(self, child):
        if self.layout_mode == "grid":
            # Automatically place the child in the grid
            child.rect.x = self.rect.x + self.grid_position[0]
            child.rect.y = self.rect.y + self.grid_position[1]

            if self.expand_direction == "vertical":
                self.grid_position[1] += child.rect.height + self.grid_spacing  # Move down for vertical expansion
                if self.grid_position[1] + child.rect.height > self.rect.height:
                    self.grid_position[0] += child.rect.width + self.grid_spacing  # Move to the next column
                    self.grid_position[1] = 0  # Reset row position
            else:
                self.grid_position[0] += child.rect.width + self.grid_spacing  # Move right for horizontal expansion
                if self.grid_position[0] + child.rect.width > self.rect.width:
                    self.grid_position[1] += child.rect.height + self.grid_spacing  # Move to the next row
                    self.grid_position[0] = 0  # Reset column position

        self.children.append(child)  # Add the child element
        self._update_scroll_area()  # Recalculate scroll area requirements

    def handle_event(self, events):
        if not isinstance(events, (list, tuple)):
            events = [events]  # Ensure events is iterable

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # Scroll up
                self.scroll_offset = max(self.scroll_offset - 20, 0)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # Scroll down
                max_scroll = max(self.total_content_size - self.visible_area_size, 0)
                self.scroll_offset = min(self.scroll_offset + 20, max_scroll)

        for child in self.children:  # Propagate events to children
            if hasattr(child, 'handle_event'):
                child.handle_event(events)

    def draw(self, surface):
        # Draw the panel background and border
        pygame.draw.rect(surface, self.bg_color, self.rect)
        if self.border_width > 0:
            pygame.draw.rect(surface, self.border_color, self.rect, self.border_width)

        for child in self.children:
            if self.expand_direction == "vertical":
                # Ensure the child is fully visible within the vertical bounds
                child_top = child.rect.top + self.scroll_offset
                child_bottom = child.rect.bottom + self.scroll_offset
                if self.rect.top <= child_top and child_bottom <= self.rect.bottom:
                    offset_rect = child.rect.move(0, -self.scroll_offset)
                    if hasattr(child, 'draw'):
                        child.draw(surface, offset_rect)
            else:
                # Ensure the child is fully visible within the horizontal bounds
                child_left = child.rect.left + self.scroll_offset
                child_right = child.rect.right + self.scroll_offset
                if self.rect.left <= child_left and child_right <= self.rect.right:
                    offset_rect = child.rect.move(-self.scroll_offset, 0)
                    if hasattr(child, 'draw'):
                        child.draw(surface)

        # Draw the scrollbar
        self._draw_scrollbar(surface)
