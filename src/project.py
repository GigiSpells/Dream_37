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
