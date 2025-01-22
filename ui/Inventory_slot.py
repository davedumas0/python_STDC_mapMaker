# inventory_slot.py

import pygame

class InventorySlot:
    def __init__(
        self, x, y, slot_size, sprite_sheet, sprite_index, sprite_size,
        border_color=(200, 200, 200), bg_color=(50, 50, 50)
    ):
        self.rect = pygame.Rect(x, y, slot_size, slot_size)
        self.slot_size = slot_size
        self.sprite_sheet = sprite_sheet
        self.sprite_index = sprite_index
        self.sprite_size = sprite_size
        self.border_color = border_color
        self.bg_color = bg_color
        self.sprite = None
        self.extract_sprite()

    def extract_sprite(self):
        row, col = self.sprite_index
        x = col * self.sprite_size
        y = row * self.sprite_size
        self.sprite = self.sprite_sheet.subsurface(pygame.Rect(x, y, self.sprite_size, self.sprite_size))
        self.sprite = pygame.transform.scale(self.sprite, (self.slot_size, self.slot_size))

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)
        if self.sprite:
            surface.blit(self.sprite, self.rect.topleft)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def update_sprite(self, sprite_index):
        self.sprite_index = sprite_index
        self.extract_sprite()
