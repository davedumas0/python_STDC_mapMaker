import pygame
from ui.button import Button
from ui.slider import Slider
from ui.drop_down_menu import DropdownMenu
from ui.progress_bar import ProgressBar
from ui.TextElement import TextElement
from ui.checkBox import Checkbox
from ui.Inventory_slot import InventorySlot
from ui.text_input import TextInput
from ui.MultiLineTextElement import MultiLineTextElement


class BasePanel:
    def __init__(self, x, y, width, height, bg_color=(50, 50, 50), border_color=(200, 200, 200), border_width=2):
        self.rect = pygame.Rect(x, y, width, height)  # Panel rectangle
        self.bg_color = bg_color  # Background color of the panel
        self.border_color = border_color  # Border color of the panel
        self.border_width = border_width  # Border thickness
        self.children = []  # List to hold child UI elements for the default page
        self.paginate = False  # Flag for pagination mode
        self.current_page = 0  # Index of the current page
        self.pages = [[]]  # Pages for paginated panels, start with one empty page

    def add_to_page(self, element, page_index=0):
        """
        Adds an element to a specific page or default page if paginate is False.
        Args:
            element: The UI element to add.
            page_index: The index of the page to add the element to (ignored if paginate is False).
        """
        if self.paginate:
            while len(self.pages) <= page_index:
                self.pages.append([])
            self.pages[page_index].append(element)
        else:
            self.children.append(element)

    def add_button(self, rel_x, rel_y, width, height, text, callback=None):
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y
        button = Button(abs_x, abs_y , width, height, text, callback)
        self.add_to_page(button)
        return button

    def add_slider(self, rel_x, rel_y, width, height, min_val=0, max_val=100, start_val=50):
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y
        slider = Slider(abs_x, abs_y, width, height, min_val, max_val, start_val)
        self.add_to_page(slider)
        return slider

    def add_panel(self, rel_x, rel_y, width, height, bg_color=(60, 60, 60), border_color=(180, 180, 180), border_width=1):
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y
        sub_panel = BasePanel(abs_x, abs_y, width, height, bg_color, border_color, border_width)
        self.add_to_page(sub_panel)
        return sub_panel

    def add_existing_panel(self, panel):
        self.add_to_page(panel)
        return panel

    def add_dropdown(self, rel_x, rel_y, width, height, options, callback=None, bg_color=(60, 60, 60), text_color=(255, 255, 255), border_color=(180, 180, 180)):
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y
        dropdown = DropdownMenu(abs_x, abs_y, width, height, options, callback, bg_color, text_color, border_color)
        self.add_to_page(dropdown)
        return dropdown

    def add_progress_bar(self, rel_x, rel_y, width, height, max_value=100, start_value=0, bg_color=(50, 50, 50), bar_color=(0, 200, 0)):
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y
        progress_bar = ProgressBar(abs_x, abs_y, width, height, max_value, start_value, bg_color, bar_color)
        self.add_to_page(progress_bar)
        return progress_bar

    def add_text(self, rel_x, rel_y, text, font_size=24, color=(255, 255, 255), bg_color=None):
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y
        text_element = TextElement(abs_x, abs_y, text, font_size, color, bg_color)
        self.add_to_page(text_element)
        return text_element
    
    
    
    def add_multiline_text(self, rel_x, rel_y, text, color=(255, 255, 255), bg_color=None, width=None, height=None):
        if width is None or height is None:  # Ensure width and height are provided
            raise ValueError("Both width and height must be specified for adding a multiline text element.")
    
        abs_x = self.rect.x + rel_x  # Calculate absolute X position
        abs_y = self.rect.y + rel_y  # Calculate absolute Y position
    
        multiline_text = MultiLineTextElement(  # Create a MultiLineTextElement instance
            x=abs_x, y=abs_y, text=text,
            color=color, bg_color=bg_color, width=width, height=height
        )
    
        self.add_to_page(multiline_text)  # Add to the current page or children
        return multiline_text
    
    

    def add_checkbox(self, rel_x, rel_y, size=20, checked=False, bg_color=(50, 50, 50), check_color=(0, 200, 0), callback=None):
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y
        checkbox = Checkbox(abs_x, abs_y, size, checked, bg_color, check_color, callback)
        self.add_to_page(checkbox)
        return checkbox

    def add_inventory_slot(self, rel_x, rel_y, slot_size, sprite_sheet, sprite_index, sprite_size, border_color=(200, 200, 200), bg_color=(50, 50, 50)):
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y
        inventory_slot = InventorySlot(
            abs_x, abs_y, slot_size, sprite_sheet, sprite_index, sprite_size,
            border_color, bg_color
        )
        self.add_to_page(inventory_slot)
        return inventory_slot
    
    def add_text_input(self, rel_x, rel_y, width, height, font_size=24, text_color=(0, 0, 0), bg_color=(255, 255, 255), border_color=(0, 0, 0), border_width=1, callback=None):
        """
        Adds a text input field to the panel.
        Args:
            rel_x: Relative X position within the panel.
            rel_y: Relative Y position within the panel.
            width: Width of the text input field.
            height: Height of the text input field.
            font_size: Font size for the text.
            text_color: Color of the text.
            bg_color: Background color of the input field.
            border_color: Border color of the input field.
            border_width: Border width of the input field.
            callback: Callback function called when the text changes.
        Returns:
            The created TextInput instance.
        """
        abs_x = self.rect.x + rel_x
        abs_y = self.rect.y + rel_y
        text_input = TextInput(
            abs_x, abs_y, width, height,
            font_size, text_color, bg_color, border_color, border_width, callback
        )
        self.add_to_page(text_input)
        return text_input




    def next_page(self):
        """Switch to the next page."""
        if self.paginate and self.current_page < len(self.pages) - 1:
            self.current_page += 1

    def previous_page(self):
        """Switch to the previous page."""
        if self.paginate and self.current_page > 0:
            self.current_page -= 1

    def handle_event(self, events):
        """Handle a list of user input events."""
        if not isinstance(events, (list, tuple)):
            events = [events]  # Ensure events is always a list

        for child in self.children:  # Propagate events to all children
            if hasattr(child, 'handle_event'):
                child.handle_event(events)

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        if self.border_width > 0:
            pygame.draw.rect(surface, self.border_color, self.rect, self.border_width)
        active_children = self.pages[self.current_page] if self.paginate else self.children
        for child in active_children:
            if hasattr(child, 'draw'):
                child.draw(surface)
