import pygame 
from store import GameStore

# The coordinate system is transformed in order to match (0,0) origin to the playare top-left corner
# (0, 0) - top left corner (without transformation)
# - The X-coordinate represents the horizontal position and increases to the right.
# - The Y-coordinate represents the vertical position and increases downward.




# Subclassing pygame.Rect to add support for relative positioning for rectangles along with image support
class RelativeRect(pygame.Rect):
    def __init__(self, x, y, width, height, outer_rect=None):
        # If outer_rect is provided, adjust the position of the rectangle relative to it
        if outer_rect:
            x += outer_rect.x
            y += outer_rect.y
    
        super().__init__(x, y, width, height)
        

# Initialize Pygame
pygame.init()

# Initialize game state
store = GameStore.get_game_store() 


screen = pygame.display.set_mode((store.screen_size()))
pygame.display.set_caption("Boss fight")

# Setup 

# play area setup
player_rect = pygame.Rect(store.player_position(),store.player_size())
play_area_sizes = store.play_area_size()
play_area = pygame.Rect(store.position_center()[0] - play_area_sizes[0]//2,
                        store.position_center()[1] - play_area_sizes[1]//2, 
                        play_area_sizes[0], play_area_sizes[1])


# adding object to the game realtive to the play area
square1_rect = RelativeRect(50,50, 50,50,play_area)



# Game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    
    # Fill screen with black
    screen.fill((0,0,0))

    # Draw the play area (background rectangle)
    pygame.draw.rect(screen, (255, 255, 255), play_area)
    pygame.draw.rect(screen, (4, 4, 77) ,square1_rect)
    pygame.display.flip()
    clock.tick(60) # Limit to 60 FPS
pygame.quit()