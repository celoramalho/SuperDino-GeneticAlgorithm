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
        self.refresh(0)
  
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_fps(self, average_fps):
        if average_fps < 10: #Check critical fps value
            fps_color = self.text_colors["RED"] 
        elif average_fps >= 10 and average_fps < 19:
            fps_color = self.text_colors["YELLOW"]
        else:
            fps_color = self.text_colors["GREEN"]
                 
        print(f"{fps_color}Average FPS: {average_fps}{self.text_colors["RESET"]}")
    
    def print_obstacle_distance(self, obstacle_distance=0):
        print(f"Obstacle Distance: {obstacle_distance}")
        
    def print_obstacle_lenght(self, obstacle_lenght=0):
        print(f"Obstacle Lenght: {obstacle_lenght}")
    
    def print_dino_speed(self, dino_speed=0):
        print(f"Dino Speed: {dino_speed}")
    
    def refresh(self, average_fps=0):
        self.clear_terminal()
        self.show_fps(average_fps)
        self.print_obstacle_distance()
        self.print_obstacle_lenght()
        self.print_dino_speed()
    
    def finish(self):
        self.clear_terminal()
        