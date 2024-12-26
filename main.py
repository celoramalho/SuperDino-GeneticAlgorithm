from screen_capture.screen_capture import DinoGameWithScreenCapture
# Usar a classe
# Example usage
if __name__ == "__main__":
    game = DinoGameWithScreenCapture()
    game.open_game()
    
    game.start_screen_capture()
    
    #game.keep_open()  # Keep the browser open is crashing esse trem