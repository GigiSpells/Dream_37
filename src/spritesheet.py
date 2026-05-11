import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, frame_width, frame_height, sprite_width, sprite_height, scale, color):
        image = pygame.Surface((sprite_width, sprite_height)).convert_alpha()
        left_edge = (frame_width - sprite_width) / 2
        top_edge = frame_height - sprite_height
        image.blit(self.sheet, (0, 0, sprite_width, sprite_height), ((frame*frame_width)+left_edge, top_edge, sprite_width, sprite_height))
        image = pygame.transform.scale(image, (sprite_width*scale, sprite_height*scale))
        image.set_colorkey(color)

        return image
    
    def get_object(self, tile_size, col, row, w_in_tiles, h_in_tiles, obj_w, obj_h, scale):
        full_width = w_in_tiles * tile_size
        full_height = h_in_tiles * tile_size
        image = pygame.Surface((full_width, full_height), pygame.SRCALPHA)
        image.blit(self.sheet, (0, 0, obj_w, obj_h), ((col*tile_size), (row*tile_size), full_width, full_height))
        image = pygame.transform.scale(image, (full_width*scale, full_height*scale))

        return image
    
# class FurnitureSheet():
#     def __init__(self, image):
#         self.sheet = image

#     def get_object(self, tile_size, col, row, w_in_tiles, h_in_tiles, obj_w, obj_h):
#         full_width = w_in_tiles * tile_size
#         full_height = h_in_tiles * tile_size
#         image = pygame.Surface((full_width, full_height), pygame.SRCALPHA)
#         image.blit(self.sheet, (0, 0, obj_w, obj_h), ((col*tile_size), (row*tile_size), full_width, full_height))

#         return image

# Furniture and parameter input to retrieve them with get_object()
fridge = (16, 2, 12, 2, 4, 26, 55, 3)
stove = (16, 4, 12, 2, 3, 30, 43, 3)
utensils = (16, 4, 15, 2, 1, 24, 25, 3)
sink = (16, 6, 12, 2, 3, 32, 43, 3)
counter = (16, 8, 12, 3, 3, 48,43, 3)
cupboard = (16, 3, 0, 1, 2, 16, 23, 3)
big_couch = (16, 0, 12, 2, 4, 22, 55, 3)
little_couch = (16, 9, 10, 2, 2, 32, 32, 3)
lamp = (16, 6, 7, 1, 3, 15, 46, 3)
side_table = (16, 2, 0, 1, 2, 13, 27, 3)
fireplace = (16, 9, 8, 2, 2, 24, 25, 3)
record_player = (16, 12, 16, 2, 2, 30, 25, 3)