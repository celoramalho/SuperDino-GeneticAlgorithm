import os

class DinoTerminalGui:
    # Códigos ANSI
    text_colors = {
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "YELLOW": "\033[33m",
        "BLUE": "\033[34m",
        "RESET": "\033[0m"
    }
    
    def __init__(self, config):
        self.config = config
        self.refresh_gui(0)
  
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else clear)
    
    def show_fps(self, average_fps):
        if average_fps < 10: #Check critical fps value
            fps_color = self.text_colors["RED"] 
        elif average_fps >= 10 and average_fps < 19:
            fps_color = self.text_colors["YELLOW"] 
        else:
            fps_color = self.text_colors["GREEN"] 
                 
        print(f"{fps_color}Average FPS: {average_fps}{self.text_colors["RESET"]}")
    
    def refresh_gui(self, average_fps):
        self.clear_terminal()
        self.show_fps(average_fps)
        