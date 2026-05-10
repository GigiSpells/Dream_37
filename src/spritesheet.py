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
    

    #furniture_object(tile_size=16, col, row, w_in_tiles, h_in_tiles, obj_w, obj_h)
    #full_width = w_in_tiles * tile size
    #full_height = h_in_tiles * tile size
    #pygame.Surface(furniture_sheet, (0, 0, sprite_width, sprite_height), (col*tile_size), (row*tile_size), obj_w, obj_h

    #fridge = Furniture(2, 4, 78, 165)