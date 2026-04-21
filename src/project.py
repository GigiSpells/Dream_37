import pygame
import spritesheet

def main():
    pygame.init
    pygame.display.set_caption("Dream 37")
    resolution = (640, 360)
    screen = pygame.display.set_mode(resolution)

    sprite_sheet_image = pygame.image.load('assets/CharacterSheets/Player/Right.png').convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

    BG = (50, 50, 50)
    BLACK = (0, 0, 0)

    frame_0 = sprite_sheet.get_image(0, 24, 24, 3, BLACK)
    frame_1 = sprite_sheet.get_image(1, 24, 24, 3, BLACK)

#Event Loop
    running = True
    while running:

        screen.fill(BG)

        screen.blit(frame_0, (0,0))
        screen.blit(frame_1, (100,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

# TODO:

# Initalize Pygame
# Initalize Window Screen
    # pygame.init()
    # screen = pygame.display.set_mode((800,400))
    # pygame.display.set_caption
# Create Game Loop (for closing window)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

# BLIT Environment Assets Onto Screen
    # Have Environment background larger than screen, 
    # background moves when character reaches edge of screen?

# Create Character Sprite Class
    # Import Character Image/s
        # Animate Character by iterating through images in list?
    # Allow Character movement through User Input
        # A/<-- key decreases y value, D/--> key increases y value
        #   def move_character(self):
        #       keys = pygame.key.get_pressed()
    # Simulate Collisions (Finish Ultimate Pygame Video)

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