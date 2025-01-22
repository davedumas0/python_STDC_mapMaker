import pygame

class SpriteSheetManager:
    def __init__(self, sprite_sheet_path, sprite_width, sprite_height):
        # Load the sprite sheet
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.sprite_width = sprite_width  # Width of each sprite
        self.sprite_height = sprite_height  # Height of each sprite
        self.sprites = []  # List to store individual sprites
        self._extract_sprites()  # Extract sprites from the sprite sheet

    def _extract_sprites(self):
        # Extract individual sprites from the sprite sheet
        sheet_width = self.sprite_sheet.get_width()
        sheet_height = self.sprite_sheet.get_height()

        for y in range(0, sheet_height, self.sprite_height):
            for x in range(0, sheet_width, self.sprite_width):
                sprite = self.sprite_sheet.subsurface((x, y, self.sprite_width, self.sprite_height))
                self.sprites.append(sprite)

    def get_sprite(self, index):
        # Get a specific sprite by index
        if 0 <= index < len(self.sprites):
            return self.sprites[index]
        else:
            raise IndexError(f"Sprite index {index} out of range.")

    def draw_sprite(self, surface, index, x, y):
        # Draw a specific sprite on a surface
        sprite = self.get_sprite(index)
        surface.blit(sprite, (x, y))

    def get_total_sprites(self):
        # Get the total number of sprites extracted
        return len(self.sprites)
