import pygame
import pytmx
import spritesheet


# BLIT Environment Onto Screen
    # Figure out how to resize tmx map (resize tiles individually?)
    # Figure out if possible to implement collisons through Tiled
    # If not, create custom rects for collision purposes
def draw_map(surface):
    tmx_data = pytmx.load_pygame('graphics/environment/Dream_37_Map.tmx')
    tile_width = tmx_data.tilewidth
    tile_height = tmx_data.tileheight
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    surface.blit(tile, (x * tile_width, y * tile_height))

# Create Character Sprite Class
        # Animate Character by iterating through images in list?
    # Allow Character movement through User Input
        # A/<-- key decreases y value, D/--> key increases y value
        #   def move_character(self):
        #       keys = pygame.key.get_pressed()
    # Simulate Collisions (Finish Ultimate Pygame Video)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.action_list = [2, 4]
        self.action = 0
        self.frame = 0
        self.frame_counter = 0

        player_up_sheet = pygame.image.load('graphics/player/up.png').convert_alpha()
        player_up = spritesheet.SpriteSheet(player_up_sheet)

        self.up_frames = []
        
        player_down_sheet = pygame.image.load('graphics/player/down.png').convert_alpha()
        player_down = spritesheet.SpriteSheet(player_down_sheet)

        self.down_frames = []

        for i in self.action_list:
            temp_img_list = []
            for _ in range(i):
                temp_img_list.append(player_down.get_image(self.frame_counter, 24, 24, 3, (0,0,0)))
                self.frame_counter += 1
            self.down_frames.append(temp_img_list)

        player_left_sheet = pygame.image.load('graphics/player/left.png').convert_alpha()
        player_left = spritesheet.SpriteSheet(player_left_sheet)

        self.left_frames = []

        player_right_sheet = pygame.image.load('graphics/player/right.png').convert_alpha()
        player_right = spritesheet.SpriteSheet(player_right_sheet)

        self.right_frames = []

        self.image = self.down_frames[self.action][self.frame]
        #self.image = player_down.get_image(1, 24, 24, 3, (0,0,0))
        self.rect = self.image.get_rect(midbottom = (100,100))

    # user input
        # find out key = pygame.key.get(pressed) vs event.type == pygame.KEYDOWN
        # if event.key == pygame.K_UP or K_w / K_DOWN or K_s / K_LEFT or K_a / K_RIGHT or K_d
        # self.rect.y -= 2 (try different speeds)
    # def receive_input(self):

    # player animation 
        
        # Increase index each tick a movement key is pressed
        # Or not pressed, for the idle animation
        # When index > the len(list) reset to 0 to reset walk cycle
        # self.image = self.player_walk_down[int(self.player_index)]
        # Access different list based on the key being pressed to change sprite direction
    # def animate_player(self):

    # def update(self):
        


def main():
    pygame.init
    pygame.display.set_caption("Dream 37")
    resolution = (640, 360)
    screen = pygame.display.set_mode(resolution)
    clock = pygame.time.Clock()
    dt = 0
    
    player = pygame.sprite.GroupSingle()
    player.add(Player())

    player_down_sheet = pygame.image.load('graphics/player/down.png').convert_alpha()
    player_down = spritesheet.SpriteSheet(player_down_sheet)

    BG = (50, 50, 50)

    walk_list = []
    walk_index = [2, 4]
    action = 0
    last_update = pygame.time.get_ticks()
    cooldown = 200
    frame = 0
    step_counter = 0

    for i in walk_index:
        temp_img_list = []
        for _ in range(i):
            temp_img_list.append(player_down.get_image(step_counter, 24, 24, 3, (0,0,0)))
            step_counter += 1
        walk_list.append(temp_img_list)

#Event Loop
    running = True
    while running:

        screen.fill(BG)

        current_time = pygame.time.get_ticks()
        if current_time - last_update >= cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(walk_list[action]):
                frame = 0

        
        draw_map(screen)
        screen.blit(walk_list[action][frame], (0,0))

        #Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Game Logic

        #Render & Display

        player.draw(screen)
        player.update()

        pygame.display.flip()
        dt = clock.tick(40)

    pygame.quit()

# TODO:

# Create Object Sprite Class/Group
    # Import Object Image/s
    # Simulate Player-Object Collisions/Use User Input for object interaction
        # Check for user interaction each tick
    # Potentially animate objects when they're found?

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