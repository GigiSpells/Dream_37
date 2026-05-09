import pygame
import pytmx
import spritesheet



    
def load_map(file, group):
    for layer in file.visible_layers:
        if hasattr(layer,'data'):
            for x, y, surf, in layer.tiles():
                pos = (x * 16, y * 16)
                Tile(pos = pos, surf = surf, groups= group)

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)   

# TODO: Animate player character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.action_list = [2, 4]
        self.action = 0
        self.frame = 0
        self.frame_counter = 0

        self.spawn_point = (985, 920)
        self.speed = 1

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
                temp_down_list.append(player_down.get_image(self.frame_counter, 24, 24, 5, (0,0,0)))
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
        self.rect = self.image.get_rect(midbottom = self.spawn_point)


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

    def update(self):
        self.move_player()
        # self.animate_player()
        # print(self.rect)
        

# Collsions:
    #Use Rect1.colliderect(Rect2)
    #First check for any collision
    # If any collision, check for which side is collding to limit movement in single direction
    #Caclulate the position of the colission for each side
    # bottom - top = ~ 0 -> top collision, y cannot increase

# Create Furniture Sprite Class
# Add instances of Furniture to Group
    # Each instance will have start and end image stored in list
# Check if player is colliding with an instance of furniture
# If yes, check for which. If player clicks or presses enter while colliding, initiate interaction

# Create Wall Sprite Class
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__()

        self.pos = pos
        self.size = (width, height)

    def update(self):
        self.surf = pygame.Surface(self.size)
        self.surf.fill((255, 0, 0))

    def draw(self, surface):
        surface.blit(self.surf, self.pos)


def main():
    pygame.init
    pygame.display.set_caption("Dream 37")
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    clock = pygame.time.Clock()
    dt = 0

    map_image = pygame.image.load('graphics/environment/Dream_37_Map_State1.png')
    map_rect = map_image.get_rect(center = (resolution[0]//2, resolution[1]//2))
    # map_data = pytmx.load_pygame('graphics/environment/Dream_37_Map.tmx')
    # tile_sprite_group = pygame.sprite.Group()
    # load_map(map_data, tile_sprite_group)

    player = pygame.sprite.GroupSingle()
    player.add(Player())
    wall_1 = Wall((1177,587),333,389)

    # player_down_sheet = pygame.image.load('graphics/player/down.png').convert_alpha()
    # player_down = spritesheet.SpriteSheet(player_down_sheet)

    BG = (50, 50, 50)

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

#Event Loop
    running = True
    while running:

        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)


        # current_time = pygame.time.get_ticks()
        # if current_time - last_update >= cooldown:
        #     frame += 1
        #     last_update = current_time
        #     if frame >= len(walk_list[action]):
        #         frame = 0


        # Do logical updates here.
        # ...
        screen.fill(BG)
        player.update()
        wall_1.update()

        # Render the graphics here.
        # ...

        #tile_sprite_group.draw(screen)
        screen.blit(map_image, map_rect)
        player.draw(screen)
        wall_1.draw(screen)
        

        #draw_map(screen)
        # screen.blit(walk_list[action][frame], (0,0))
        

        pygame.display.flip()
        dt = clock.tick(60)

    pygame.quit()

# TODO:

# Create Object Sprite Class/Group
    # Import Object Image/s
    # Simulate Player-Object Collisions/Use User Input for object interaction
        # Check for user interaction each tick
    # Animate objects when they're found?

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