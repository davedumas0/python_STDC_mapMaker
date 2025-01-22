# sprite_navigator_panel.py
import os
import pygame
from ui.base_panel import BasePanel
from ui.button import Button


class SpriteNavigatorPanel(BasePanel):
    def __init__(self, x, y, width, height, root_dir, bg_color=(50, 50, 50), border_color=(200, 200, 200), border_width=2):
        super().__init__(x, y, width, height, bg_color, border_color, border_width)
        self.root_dir = root_dir  # Root directory containing sprite folders
        self.current_path = root_dir  # Current directory being browsed
        self.sprite_thumbnails = []  # List of loaded sprite thumbnails
        self.sprite_file_names = []  # List of sprite file names
        self.folder_panel = None  # Panel for folder navigation
        self.folder_panel_scroll_offset = 0  # Scroll offset for dynamic folder panel
        self.items_per_page = 72  # Limit sprites per page to 72
        self.current_page = 0
        self.selected_sprite = None  # Store the selected sprite
        self.selected_sprite_name = None  # Store the name of the selected sprite

        self.item_size = 50
        self.item_padding = 10

        self._setup_folder_panel()
        self._setup_selected_sprite_panel()
        self._load_directory_contents()  # Load the contents of the root directory
        self._setup_navigation_panel()


    
    def _setup_folder_panel(self):
        """Set up the folder navigation panel at the top."""
        folder_panel_height = 75
        self.folder_panel = BasePanel(
            self.rect.x,
            self.rect.y,
            self.rect.width,
            folder_panel_height,
            bg_color=(40, 40, 40),
            border_color=(100, 100, 100),
            border_width=1,
        )
        # Add permanent "Back" button
        self.backButton = self.folder_panel.add_button(
            10,
            10 - 54,
            50,
            30,
            "Back",
            callback=self.navigate_to_parent_folder
        )
        self.backButton.bg_color = (85, 75, 255)
        self.add_existing_panel(self.folder_panel)


    def _setup_selected_sprite_panel(self):
        """Set up the panel to display the selected sprite."""
        selected_panel_height = 200  # Restore to the previous position and size
        self.selected_panel = BasePanel(
            self.rect.x,
            self.rect.y + self.rect.height - 54+1,
            self.rect.width,
            selected_panel_height,
            bg_color=(30, 30, 30),
            border_color=(100, 100, 100),
            border_width=1,
        )
        self.add_existing_panel(self.selected_panel)

        
    def _updatePageIndicator(self):
        # Add current/max page text in the center
        total_pages = max(1, (len(self.sprite_thumbnails) + self.items_per_page - 1) // self.items_per_page)
        self.nav_panel.pageText.set_text(f"{self.current_page + 1}/{total_pages}")
        #self.nav_panel.pageText.set_text("")
        

    def _setup_navigation_panel(self):
        """Set up navigation buttons for folders and paging."""
        nav_panel_height = 50
        self.nav_panel = BasePanel(
            self.rect.x + 10,
            self.rect.y + self.rect.height - nav_panel_height - 5 - 54,
            self.rect.width - 20,
            nav_panel_height,
            bg_color=(30, 30, 30),
            border_color=(100, 100, 100),
            border_width=1,
        )
        total_pages = max(1, (len(self.sprite_thumbnails) + self.items_per_page - 1) // self.items_per_page)
        self.add_existing_panel(self.nav_panel)

        self.nav_panel.add_button(10, 5 - 54, 50, 30, "<", self.prev_page)
        self.nav_panel.add_button(self.rect.width - 70 - 10, 5 - 54, 50, 30, ">", self.next_page)
        self.nav_panel.pageText = self.nav_panel.add_text((self.rect.width // 2) - 25, 5 - 40, f"{self.current_page + 1}/{total_pages}", font_size=24, color=(255, 255, 255))
        
        # Add current/max page text in the center
        self._updatePageIndicator()
        
    


    def _load_directory_contents(self):
        """Load the contents of the current directory."""
        self.sprite_thumbnails = []
        self.sprite_file_names = []
        self.folder_panel.children.clear()  # Clear previous folder buttons

        # Add permanent "Back" button
        self._setup_folder_panel()

        try:
            items = os.listdir(self.current_path)
            folder_index = 1  # Start after the "Back" button
            for item in items:
                full_path = os.path.join(self.current_path, item)
                if os.path.isdir(full_path):
                    # Dynamically add folder buttons
                    button_x = 10 + (folder_index - 1) * (self.item_size + self.item_padding) - self.folder_panel_scroll_offset
                    if 0 <= button_x <= self.rect.width - self.item_size:  # Only draw buttons within visible area
                        self.temp = self.folder_panel.add_button(
                            button_x,
                            10 - 54,
                            self.item_size,
                            self.item_size,
                            item,
                            callback=lambda p=full_path: self._navigate_to_folder(p)
                        )
                        self.temp.font = pygame.font.SysFont(None, 20)
                    folder_index += 1
                elif item.endswith((".png", ".jpg")):  # Filter for image files
                    self.sprite_thumbnails.append((pygame.image.load(full_path), "sprite"))
                    self.sprite_file_names.append(os.path.splitext(item)[0])  # Store name without extension
        except Exception as e:
            print(f"Failed to load directory contents: {e}")

    def _navigate_to_folder(self, path):
        """Navigate to a selected folder."""
        self.current_path = path
        self._load_directory_contents()
        self._updatePageIndicator()

    def handle_event(self, events):
        """Handle user input for navigation."""
        # Ensure events is iterable (wrap a single event in a list if necessary)
        if not isinstance(events, (list, tuple)):
            events = [events]
    
        super().handle_event(events)
    
        # Process each event in the list
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # Scroll up
                self.folder_panel_scroll_offset = max(0, self.folder_panel_scroll_offset - 20)
                self._load_directory_contents()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:  # Scroll down
                self.folder_panel_scroll_offset += 20
                self._load_directory_contents()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
                cols = (self.rect.width - self.item_padding) // (self.item_size + self.item_padding)
                rows = (self.rect.height - self.item_padding) // (self.item_size + self.item_padding)
                max_items = cols * rows
                start_index = self.current_page * self.items_per_page
    
                for i in range(len(self.sprite_thumbnails[start_index:start_index + max_items])):
                    row = i // cols
                    col = i % cols
                    item_x = self.rect.x + col * (self.item_size + self.item_padding) + self.item_padding
                    item_y = self.folder_panel.rect.bottom + row * (self.item_size + self.item_padding) + self.item_padding
                    item_rect = pygame.Rect(item_x, item_y, self.item_size, self.item_size)
    
                    if item_rect.collidepoint(event.pos):
                        # Adjust index to account for current page
                        actual_index = start_index + i
                        self.selected_sprite = self.sprite_thumbnails[actual_index][0]
                        self.selected_sprite_name = self.sprite_file_names[actual_index]
                        self._update_selected_sprite_panel(self.selected_sprite, self.selected_sprite_name)
                        break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:  # Navigate back to the parent folder
                    self.navigate_to_parent_folder()


    def _update_selected_sprite_panel(self, sprite, sprite_name):
        """Update the selected sprite panel with the new sprite."""
        self.selected_panel.children.clear()
    
        # Display the sprite name without extension
        self.selected_panel.add_text(
            10, 10,
            f"Selected Sprite: {sprite_name}",
            font_size=20,
            color=(255, 255, 255)
        )
    
        # Add the scaled-up sprite image directly to the selected panel
        if isinstance(sprite, pygame.Surface):
            scaled_sprite = pygame.transform.scale(sprite, (self.item_size * 2, self.item_size * 2))
            self.selected_panel.children.append({
                "type": "sprite",
                "surface": scaled_sprite,
                "position": (self.selected_panel.rect.x + self.selected_panel.rect.width-128, self.selected_panel.rect.y + 30),
            })
    

    def navigate_to_parent_folder(self):
        """Navigate to the parent folder."""
        if self.current_path != self.root_dir:  # Ensure we don’t navigate above the root directory
            self.current_path = os.path.dirname(self.current_path)
            self._load_directory_contents()

    def prev_page(self):
        """Navigate to the previous page."""
        if self.current_page > 0:
            self.current_page -= 1
            self._updatePageIndicator()

    def next_page(self):
        """Navigate to the next page."""
        total_pages = (len(self.sprite_thumbnails) + self.items_per_page - 1) // self.items_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self._updatePageIndicator()

    def draw(self, surface):
        """Draw the folder and sprite thumbnails."""
        super().draw(surface)
        cols = (self.rect.width - self.item_padding) // (self.item_size + self.item_padding)
        rows = (self.rect.height - self.item_padding) // (self.item_size + self.item_padding)
        max_items = cols * rows

        start_index = self.current_page * self.items_per_page
        end_index = min(start_index + self.items_per_page, len(self.sprite_thumbnails))
        current_items = self.sprite_thumbnails[start_index:end_index]

        # Draw sprites in the selected sprite panel
        for child in self.selected_panel.children:
            if isinstance(child, dict) and child.get("type") == "sprite":
                sprite_surface = child["surface"]
                sprite_position = child["position"]
                surface.blit(sprite_surface, sprite_position)



        # Draw sprites in the main panel
        for i, (item, item_type) in enumerate(current_items):
            row = i // cols
            col = i % cols
            item_x = self.rect.x + col * (self.item_size + self.item_padding) + self.item_padding
            item_y = self.folder_panel.rect.bottom + row * (self.item_size + self.item_padding) + self.item_padding

            sprite_rect = pygame.Rect(item_x, item_y, self.item_size, self.item_size)
            if self.selected_sprite == item:
                pygame.draw.rect(surface, (255, 255, 0), sprite_rect, 3)  # Highlight selected sprite

            surface.blit(pygame.transform.scale(item, (self.item_size, self.item_size)), (item_x, item_y))

        # Optionally, draw breadcrumbs at the top
        breadcrumb_text = " > ".join(os.path.basename(path) for path in self.current_path.split(os.sep) if path)
        font = pygame.font.SysFont(None, 24)
        text_surface = font.render(breadcrumb_text, True, (255, 255, 255))
        surface.blit(text_surface, (self.rect.x + 10, self.folder_panel.rect.bottom + 10))
