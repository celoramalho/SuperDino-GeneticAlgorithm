from OpenDinoGame.DinoGame import DinoGame
from ScreenReading.DinoGameWithCapture import DinoGameWithCapture
# Usar a classe
# Example usage
if __name__ == "__main__":
    game = DinoGame()
    game.open_game()
    
    game.start_screen_capture()
    
    game.keep_open()  # Keep the browser open