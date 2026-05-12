import pygame
import spritesheet

# TODO: 
# Blit Interaction Text to Screen
# Create Timer to Keep Text on Screen
# Change Furniture State upon Interaction
# Animate player character
# Add Music
# Add Found Items GUI
# Add Start Screen
# Add New End Screen

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.action_list = [2, 4]
        self.action = 1
        self.frame = 0
        self.frame_counter = 0

        self.spawn_point = (985, 920)
        self.speed = 5

        player_up_sheet = pygame.image.load('graphics/player/up.png').convert_alpha()
        player_up = spritesheet.SpriteSheet(player_up_sheet)

        self.up_frames = []

        # for i in self.action_list:
        #     temp_up_list = []
        #     for _ in range(i):
        #         temp_up_list.append(player_up.get_image(self.frame_counter, 24, 24, 3, (0,0,0)))
        #         self.frame_counter += 1
        #     self.up_frames.append(temp_up_list)
        
        player_down_sheet = pygame.image.load('graphics/player/down.png').convert_alpha()
        player_down = spritesheet.SpriteSheet(player_down_sheet)

        self.down_frames = []

        for i in self.action_list:
            temp_down_list = []
            for _ in range(i):
                temp_down_list.append(player_down.get_image(self.frame_counter, 24, 24, 10, 17, 5, (0,0,0)))
                self.frame_counter += 1
            self.down_frames.append(temp_down_list)

        player_left_sheet = pygame.image.load('graphics/player/left.png').convert_alpha()
        player_left = spritesheet.SpriteSheet(player_left_sheet)
        
        self.left_frames = []

        # for i in self.action_list:
        #     temp_left_list = []
        #     for _ in range(i):
        #         temp_left_list.append(player_left.get_image(self.frame_counter, 24, 24, 3, (0,0,0)))
        #         self.frame_counter += 1
        #     self.left_frames.append(temp_left_list)

        player_right_sheet = pygame.image.load('graphics/player/right.png').convert_alpha()
        player_right = spritesheet.SpriteSheet(player_right_sheet)

        self.right_frames = []

        # for i in self.action_list:
        #     temp_right_list = []
        #     for _ in range(i):
        #         temp_right_list.append(player_right.get_image(self.frame_counter, 24, 24, 3, (0,0,0)))
        #         self.frame_counter += 1
        #     self.right_frames.append(temp_right_list)


        self.image = self.down_frames[self.action][self.frame]
        #self.rect = pygame.Rect(960, 865, 50, 20)
        self.rect = self.image.get_bounding_rect()
        self.rect.midbottom = self.spawn_point


    def move_player(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        else:
            return False       

    # player animation 
        # Increase index each tick a movement key is pressed
        # Or not pressed, for the idle animation
        # When index > the len(list) reset to 0 to reset walk cycle
        # self.image = self.player_walk_down[int(self.player_index)]
        # Access different list based on the key being pressed to change sprite direction
    #def animate_player(self):
    #     keys = pygame.key.get_pressed()
    #     if self.move_player() == False:
    #         self.action = 0
    #     else:
    #         self.action = 1
    #         if keys[pygame.K_UP] or keys[pygame.K_w]:
    #             print("up")
    #             self.image = self.up_frames[self.action][self.frame]
    #         elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
    #             print("down")
    #             self.image = self.down_frames[self.action][self.frame]
    #         elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
    #             print("left")
    #             self.image = self.left_frames[self.action][self.frame]
    #             print(self.image)
    #             print(self.rect)
    #         elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
    #             print("right")
    #             self.image = self.right_frames[self.action][self.frame]
    #             print(self.image)
    #             print(self.rect)
                #iterate through list based on key pressed
                # iterate through idle animation

    def check_collisions(self, group):
        if is_colliding(self, group):
            self.rect.y = self.saved_y_pos
            self.rect.x = self.saved_x_pos

    # def check_item_collisions(self, group):
    #     if is_colliding(self, group):

    def update(self):
        self.saved_x_pos = self.rect.x
        self.saved_y_pos = self.rect.y
        self.move_player()
        # self.animate_player()
        # print(self.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


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


class Item(pygame.sprite.Sprite):
    def __init__(self, object, pos):
        super().__init__()

        sprite_sheet = pygame.image.load('assets/Top-Down_Retro_Interior/TopDownHouse_SmallItems.png').convert_alpha()

        self.objects = spritesheet.SpriteSheet(sprite_sheet)
        self.object_params = object
        self.pos = pos

    def update(self):
        self.image = self.objects.get_object(*self.object_params)
        self.rect = self.image.get_bounding_rect(1)
        self.rect.midbottom = self.pos


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__()

        self.pos = pos
        self.size = (width, height)
        self.image = pygame.Surface(self.size)
        self.image.fill((255, 0, 0))
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(topleft = self.pos)

    def draw(self, surface):
        surface.blit(self.surf, self.pos)
        

def is_colliding(player, group):
    collisions = pygame.sprite.spritecollide(player, group, False)
    if collisions:
        #print(collisions)
        return True
    return False


def is_interacting(player, group):
    keys = pygame.key.get_pressed()
    if is_colliding(player, group) and keys[pygame.K_RETURN]:
        return True
    return False


def answer_yes():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_y]:
        return True
    else:
        pass


def furniture_interaction(player, group):
    keys = pygame.key.get_pressed()
    collisions = pygame.sprite.spritecollide(player, group, False)
    sprite_list = pygame.sprite.Group.sprites(group)
    for sprite in collisions:
        if sprite == sprite_list[0]:
            print('You opened the fridge and fond an APPLE. How long has this been here?')
            #fridge.state_index = 1
            return True
        if sprite == sprite_list[1]:
            print('You looked under the sink and found a METAL CLOTHESHANGER. Fun to bend into various shapes!')
            return True
        if sprite == sprite_list[2]:
            print("You looked under the counter... There's not much")
        if sprite == sprite_list[3]:
            print('Turn on the stove? Y / N')
        if sprite == sprite_list[4]:
            print('Utensils')
        if sprite == sprite_list[5]:
            print('Cupboard')
        if sprite == sprite_list[6]:
            print('Turn on the lamp? Y / N')
        if sprite == sprite_list[7]:
            print("You checked the side table draw and found a RECIEPT for... something. (It's faded)")
            return True
        if sprite == sprite_list[8]:
            print("It's a little cold. Light a fire? Y / N")
        if sprite == sprite_list[9]:
            print("Play some music?")
            #pygame.mixer.music.play()

def complete_interaction(sprite):
    pygame.sprite.Sprite.kill(sprite)
    return True

def item_interaction(player, group):
    keys = pygame.key.get_pressed()
    collisions = pygame.sprite.spritecollide(player, group, False)
    sprite_list = pygame.sprite.Group.sprites(group)
    for sprite in collisions:
        if sprite == sprite_list[0]:
            complete_interaction(sprite)
            return "You found a RUBBER DUCK. It must have fallen down the stairs..."
        if sprite == sprite_list[1]:
            complete_interaction(sprite)
            return "There's a CHEW TOY. Who does this belong to? You don't have a dog."
        if sprite == sprite_list[2]:
            complete_interaction(sprite)
            return "There's a BOOK on the table. Its' usually on a shelf upstairs."
        else:
            pass


def show_interaction_text(message, font, surface):
    text = font.render(message, False, (250,200,200))
    text_rect = text.get_rect(topleft = (500,500))

    surface.blit(text, text_rect)


def load_map(image, surf, surf_res,):
    map_img = pygame.image.load(image)
    #map_img.set_alpha(70)
    map_rect = map_img.get_rect(center = (surf_res[0]//2, surf_res[1]//2))
    surf.blit(map_img, map_rect)   


#def render_text(font):
    

def main():
    pygame.init()
    pygame.display.set_caption("Dream 37")
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    clock = pygame.time.Clock()
    dt = 0
    game_font = pygame.font.Font('assets/font/Pixeltype.ttf', 50)
    BG = (70, 50, 50)

    found_items = 0
    interacting = False

    player = pygame.sprite.GroupSingle()
    player.add(Player())

    # Walls
    wall = pygame.sprite.Group()
    wall.add(Wall((1510,98),51,536),Wall((1177,587),333,389),
             Wall((396,925),780,54),Wall((690,256),51,428),
             Wall((746,40),342,245))

    # Furniture
    fridge = Furniture(spritesheet.fridge_info, (1080,203))
    sink = Furniture(spritesheet.sink_info, (1176,250))
    counter = Furniture(spritesheet.counter_info, (1272,250))
    stove = Furniture(spritesheet.stove_info, (1415,251))
    utensils = Furniture(spritesheet.utensils_info, (1175,202))
    cupboard = Furniture(spritesheet.cupboard_info, (1272,155))
    lamp = Furniture(spritesheet.lamp_info, (454,587))
    side_table = Furniture(spritesheet.side_table_info, (408,827))
    fireplace = Furniture(spritesheet.fireplace_info, (600,635))
    record_player = Furniture(spritesheet.record_player_info, (648,827))

    furniture = pygame.sprite.Group(fridge, sink, counter, stove, utensils,
                                    cupboard, lamp, side_table, fireplace, record_player)
    
    # Objects 
    rubber_duck = Item(spritesheet.rubber_duck_info, (600+200, 300+50))
    apple = Item(spritesheet.apple_info, (600+200, 300+50))
    chew_toy = Item(spritesheet.chew_toy_info, (900+200, 670+50))
    receipt = Item(spritesheet.receipt_info, (600+200, 300+50))
    clotheshanger = Item(spritesheet.clotheshanger_info, (600+200, 300+50))
    book = Item(spritesheet.book_info, (730+200, 380+50))

    visible_items = pygame.sprite.Group(rubber_duck, chew_toy, book)
    hidden_items = pygame.sprite.Group(apple, receipt, clotheshanger)

    # player_down_sheet = pygame.image.load('graphics/player/down.png').convert_alpha()
    # player_down = spritesheet.SpriteSheet(player_down_sheet)

    # walk_list = []
    # walk_index = [2, 4]
    # action = 0
    # last_update = pygame.time.get_ticks()
    # cooldown = 200
    # frame = 0
    # step_counter = 0

    # for i in walk_index:
    #     temp_img_list = []
    #     for _ in range(i):
    #         temp_img_list.append(player_down.get_image(step_counter, 24, 24, 3, (0,0,0)))
    #         step_counter += 1
    #     walk_list.append(temp_img_list)

    instructions = game_font.render(f'Press ENTER to interact.', False, (250,200,200))
    instructions_rect = instructions.get_rect(topleft = (20,20))

    end_text = game_font.render(f'You found 3 items', False, (250,200,200))
    end_text_rect = end_text.get_rect(center = (resolution[0]//2, resolution[1]//2))

#Event Loop
    running = True
    game_active = True
    while running:

        # Process player inputs.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                        #check_interaction(player, furniture_list)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_pos = pygame.mouse.get_pos()
            #     print(mouse_pos)


        # current_time = pygame.time.get_ticks()
        # if current_time - last_update >= cooldown:
        #     frame += 1
        #     last_update = current_time
        #     if frame >= len(walk_list[action]):
        #         frame = 0


        # Do logical updates here.
        # ...
        if game_active:
            player.sprite.update()
            furniture.update()
            if is_interacting(player.sprite, furniture):
                furniture_interaction(player.sprite, furniture)
            visible_items.update()
            if is_interacting(player.sprite, visible_items):
                if item_interaction(player.sprite, visible_items):       
                    found_items += 1
                    print(found_items)
                    show_interaction_text(item_interaction(player.sprite, visible_items), game_font, screen)
                if found_items >= 3:
                    game_active = False
            
            items_found_text = game_font.render(f"Items Found: {found_items}", False, (250,200,200))
            items_found_rect = items_found_text.get_rect(topright = (1900,20))

            player.sprite.check_collisions(wall)
            player.sprite.check_collisions(furniture)


            # Render the graphics here.
            # ...
            screen.fill(BG)
            screen.blit(instructions, instructions_rect)
            screen.blit(items_found_text, items_found_rect)
            load_map('graphics/environment/Dream_37_Map_MinusKeys.png', screen, resolution)
            wall.draw(screen)
            furniture.draw(screen)
            visible_items.draw(screen)
            #hidden_items.draw(screen)
            player.draw(screen)
            
            # screen.blit(walk_list[action][frame], (0,0))
        
        else:
            screen.fill(BG)
            end_image = pygame.image.load('graphics/Dream_37_Image.jpg')
            end_image = pygame.transform.scale_by(end_image, 0.58)
            end_image_rect = end_image.get_rect(center = (resolution[0]//2, 790))
            screen.blit(end_image, end_image_rect)
            screen.blit(end_text, end_text_rect)

        pygame.display.flip()
        dt = clock.tick(60)

    pygame.quit()

# TODO:

# Develop Points System/ Way for Game to End
    # Create Progress bar sprite? with new frame for each point of progress?
    # Import image/ use text 0/5
        # If (some object interaction) 
        #   points = points += 1
        #   increase number text/ iterate to next image

# Game State Development 
    # Run game within game_active loop
# else:
    # If progress/points == 0: screen.blit(start screen) *shows when game opens
    # If progress/points >= 5: screen.blit(temp end screen)

if __name__ == "__main__":
    main()