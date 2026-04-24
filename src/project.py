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

    # init
        # Import Up, Down, Left, and Right Sprite sheet
        # Define Idle frames 1 and 2, and walking frames 1-4 from each sheet
        # Create Idle list, and a Walk List for each direction
        # Set index to 0 (self.player_index)
        # Define current player image surface (set default) self.image
        # Define player rect (self.rect = self.image.get_rect(point_on_rect = x,y))

    # user input
        # find out key = pygame.key.get(pressed) vs event.type == pygame.KEYDOWN
        # if event.key == pygame.K_UP or K_w / K_DOWN or K_s / K_LEFT or K_a / K_RIGHT or K_d
        # self.rect.y -= 2 (try different speeds)

    # player animation 
        # Increase index each tick a movement key is pressed
        # Or not pressed, for the idle animation
        # When index > the len(list) reset to 0 to reset walk cycle
        # self.image = self.player_walk_down[int(self.player_index)]
        # Access different list based on the key being pressed to change sprite direction

def main():
    pygame.init
    pygame.display.set_caption("Dream 37")
    resolution = (640, 360)
    screen = pygame.display.set_mode(resolution)
    
    #sprite_sheet_image = pygame.image.load('assets/CharacterSheets/Player/Right.png').convert_alpha()
    #sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

    BG = (50, 50, 50)

    #frame_0 = sprite_sheet.get_image(0, 24, 24, 1, BLACK)
    #frame_1 = sprite_sheet.get_image(1, 24, 24, 1, BLACK)

#Event Loop
    running = True
    while running:

        screen.fill(BG)

        #screen.blit(frame_0, (0,0))
        #screen.blit(frame_1, (100,0))
        #screen.blit(tile_0, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_map(screen)

        pygame.display.flip()

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