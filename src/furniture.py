import pygame
import spritesheet

pygame.init

class Furniture(pygame.sprite.Sprite):
    def __init__(self, object, pos):
        super().__init__()

        spritesheet_1 = pygame.image.load('assets/Top-Down_Retro_Interior/TopDownHouse_FurnitureState1.png').convert_alpha()
        spritesheet_2 = pygame.image.load('assets/Top-Down_Retro_Interior/TopDownHouse_FurnitureState2.png').convert_alpha()

        self.states = [spritesheet_1,spritesheet_2]
        self.state_index = 0
        self.current_state = self.states[self.state_index]
    
        self.objects = spritesheet.SpriteSheet(self.current_state)
        self.object_params = object
        self.pos = pos

    def update(self):
        self.image = self.objects.get_object(*self.object_params)
        self.rect = self.image.get_bounding_rect(1)
        self.rect.topleft = self.pos

fridge = Furniture(spritesheet.fridge_info, (1080-200,203-50))
sink = Furniture(spritesheet.sink_info, (1176-200,250-50))
counter = Furniture(spritesheet.counter_info, (1272-200,250-50))
stove = Furniture(spritesheet.stove_info, (1415-200,251-50))
utensils = Furniture(spritesheet.utensils_info, (1175-200,202-50))
cupboard = Furniture(spritesheet.cupboard_info, (1272-200,155-50))
#Furniture(spritesheet.big_couch, (408-200,683-50))
#Furniture(spritesheet.little_couch, (504-200, 634-50))
side_table = Furniture(spritesheet.side_table_info, (408-200,827-50))
fireplace = Furniture(spritesheet.fireplace_info, (600-200,635-50))
record_player = Furniture(spritesheet.record_player_info, (648-200,827-50))

furniture = pygame.sprite.Group(fridge, sink, counter, stove, utensils,
                                cupboard, side_table, fireplace, record_player)