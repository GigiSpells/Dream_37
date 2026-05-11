import pygame
import pytmx
import spritesheet
import sys



# TODO: Animate player character
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
        #self.rect = pygame.Rect(self.spawnpoint[0], self.spawnpoint[1], )
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

    def update(self):
        self.saved_x_pos = self.rect.x
        self.saved_y_pos = self.rect.y
        self.move_player()
        print(self.rect)
        # self.animate_player()
        # print(self.rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Create Furniture Sprite Class?
# Add instances of Furniture to Group
    # Each instance will have start and end image stored in list
# Check if player is colliding with an instance of furniture
# If yes, check for which. If player clicks or presses enter while colliding, initiate interaction

# Create Object Sprite Class/Group
    # Import Object Image/s
    # Simulate Player-Object Collisions/Use User Input for object interaction
        # Check for user interaction each tick
    # Animate objects when they're found?
class Furniture(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        spritesheet_1 = pygame.image.load('assets/Top-Down_Retro_Interior/TopDownHouse_FurnitureState1.png').convert_alpha()
        spritesheet_2 = pygame.image.load('assets/Top-Down_Retro_Interior/TopDownHouse_FurnitureState2.png').convert_alpha()
        self.object_params = (16, 2, 12, 2, 4, 26, 55, 3)
        self.object = spritesheet.SpriteSheet(spritesheet_1)

    def update(self):
        self.image = self.object.get_object(*self.object_params)
        self.rect = self.image.get_bounding_rect()
        self.rect.topleft = (1089,214)

# Create Wall Sprite Class
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, width, height):
        super().__init__()

        self.pos = pos
        self.size = (width, height)
        self.image = pygame.Surface(self.size)
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft = self.pos)

    def draw(self, surface):
        surface.blit(self.surf, self.pos)


def is_colliding(player, group):
    if pygame.sprite.spritecollide(player, group, False):
        #print('collision')
        return True
    return False


def load_map(image, surf, surf_res,):
    map_img = pygame.image.load(image)
    map_rect = map_img.get_rect(center = (surf_res[0]//2, surf_res[1]//2))
    surf.blit(map_img, map_rect)   


def load_collisions():
    print("loading collisions")



def main():
    pygame.init
    pygame.display.set_caption("Dream 37")
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution, pygame.RESIZABLE)
    clock = pygame.time.Clock()
    dt = 0
    BG = (50, 50, 50)

    
    player = Player()
    wall = pygame.sprite.Group()
    wall.add(Wall((1177,587),333,389))

    furniture = pygame.sprite.Group()
    furniture.add(Furniture())

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

#Event Loop
    running = True
    while running:

        # Process player inputs.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
        furniture.update()
        player.check_collisions(wall)
        player.check_collisions(furniture)

        # Render the graphics here.
        # ...
        load_map('graphics/environment/Dream_37_Map_State1.png', screen, resolution)
        player.draw(screen)
        wall.draw(screen)
        furniture.draw(screen)
        
        #draw_map(screen)
        # screen.blit(walk_list[action][frame], (0,0))
        

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