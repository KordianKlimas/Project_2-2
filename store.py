import pygame

class GameStore:
    _instance = None  # Singleton instance

    def __new__(cls,*args,**kwargs):
        """Ensure only one instance of GameStore exists."""
        if cls._instance is None:
            cls._instance = super(GameStore, cls).__new__(cls)
            cls._instance._initialize_game_settings()
        return cls._instance    
    

    def _initialize_game_settings(self): 
        # Actual Screen size  
        info = pygame.display.Info()
        self._screen_width = info.current_w
        self._screen_height = info.current_h
        # Game settings 
        self.play_area_width = 1000
        self.play_area_height = 1000  
        self._position_center = get_middle_of_screen() 
        
        
        # Boss settings 
        self.boss_health = 1000

        # Player settings 
        self.player_health = 100
        self.player_width = 50 
        self.player_height = 50
        self.player_X = self._position_center[0]
        self.player_Y = self._position_center[1]

        # Metrics
        self.score = 0
    
    @classmethod
    def get_game_store(cls):
        """Returns the singleton instance of GameStore."""
        return cls()

    def play_area_size(self):
        """Returns the screen size as a tuple (width, height)."""
        return (self.play_area_width, self.play_area_height)
    def position_center(self):
        """Returns the screen size as a tuple (width, height)."""
        return (self._position_center)

    def player_position(self):
        """Returns the player's position as a tuple (X, Y)."""
        return (self.player_X, self.player_Y)

    def player_size(self):
        """Returns the player's size as a tuple (width, height)."""
        return (self.player_width, self.player_height)
    def screen_size(self):
        """Returns the actual screen size as a tuple (width, height)."""
        return (self._screen_width, self._screen_height)


# helper methods
def get_middle_of_screen():
    """
    Returns the (x, y) coordinates for the center of the screen.
    """
    info = pygame.display.Info()
    return (info.current_w // 2, info.current_h // 2)

