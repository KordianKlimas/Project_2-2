
# def cordsT(x, y):
#     store = get_game_store()
    
#     # Actual screen size and play area size
#     screen_width, screen_height = store.screen_size()
#     play_area_width, play_area_height = store.play_area_size()

#     # Calculate the center of the screen
#     screen_center_x, screen_center_y = screen_width // 2, screen_height // 2

#     # Assuming the play area is centered in the middle of the screen, given coordinates
#     # will be transofrmed so they match the origin(top left) point of play area 
     
#     # Transform the coordinates relative to theplay area's center (middle of the screen)
#     transformed_x = screen_center_x + (x - play_area_width // 2)
#     transformed_y = screen_center_y + (y - play_area_height // 2)

#     return transformed_x, transformed_y