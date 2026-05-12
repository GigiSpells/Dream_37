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
    

# Piece of furniture and parameter input to retrieve them with get_object()
fridge_info = (16, 2, 12, 2, 4, 26, 55, 3)
stove_info = (16, 4, 12, 2, 3, 30, 43, 3)
utensils_info = (16, 4, 15, 2, 1, 24, 25, 3)
sink_info = (16, 6, 12, 2, 3, 32, 43, 3)
counter_info = (16, 8, 12, 3, 3, 48,43, 3)
cupboard_info = (16, 3, 0, 1, 2, 16, 23, 3)
big_couch_info = (16, 0, 12, 2, 4, 22, 55, 3)
little_couch_info = (16, 9, 10, 2, 2, 32, 32, 3)
lamp_info = (16, 6, 7, 1, 3, 15, 46, 3)
side_table_info = (16, 2, 0, 1, 2, 13, 27, 3)
fireplace_info = (16, 9, 8, 2, 2, 24, 25, 3)
record_player_info = (16, 11, 16, 2, 2, 30, 25, 3)

rubber_duck_info = (16, 4, 0, 1, 1, 11, 9, 3)
apple_info = (16, 4, 7, 1, 1, 11, 9, 3)
chew_toy_info = (16, 0, 2, 1, 1, 11, 6, 3)
receipt_info = (16, 3, 1, 1, 1, 8, 8, 3)
clotheshanger_info = (16, 7, 3, 1, 1, 10, 9, 3)
book_info = (16, 1, 3, 1, 1, 8, 9, 3)

# class Interaction():
#     def __init__(self, player, type):
#         self.player = player
#         self.interaction_type = type
#         self.collisions = pygame.sprite.spritecollide(player, self.interaction_type, False)
#         self.sprite_list = pygame.sprite.Group.sprites(type)
    
#     def is_interacting(self):
#         keys = pygame.key.get_pressed()
#         if is_colliding(self.player, self.interaction_type) and keys[pygame.K_RETURN]:
#             return True
#         return False

#     def furniture_interaction(self):
#         for sprite in self.collisions:
#             if sprite == self.sprite_list[0]:
#                 print('Fridge')
#             if sprite == self.sprite_list[1]:
#                 print('Sink')
#             if sprite == self.sprite_list[2]:
#                 print('Counter')
#             if sprite == self.sprite_list[3]:
#                 print('Stove')
#             if sprite == self.sprite_list[4]:
#                 print('Utensils')
#             if sprite == self.sprite_list[5]:
#                 print('Cupboard')
#             if sprite == self.sprite_list[6]:
#                 print('Lamp')
#             if sprite == self.sprite_list[7]:
#                 print('Side Table')
#             if sprite == self.sprite_list[8]:
#                 print('Fireplace')
#             if sprite == self.sprite_list[9]:
#                 print('Record Player')

#     def item_interaction(self):
#         for sprite in self.collisions:
#             if sprite == self.sprite_list[0]:
#                 print('rubber duck')
#             if sprite == self.sprite_list[1]:
#                 print('Chew Toy')
#             if sprite == self.sprite_list[2]:
#                 print('Book')