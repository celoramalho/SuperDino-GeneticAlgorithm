import os

class DinoTerminalGui:
    def __init__(self, config):
        self.config = config
        self.refresh_gui(0)
  
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else clear)
    
    def show_fps(self, average_fps):
        print(f"Average FPS: {average_fps}")
    
    def refresh_gui(self, average_fps):
        self.clear_terminal()
        self.show_fps(average_fps)
        