
class ObjectDetected:
    def __init__(self, x, y, w, h, label):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.label = label
        self.aspect_ratio = w / float(h)
        
        
    def dimensions(self):
        return (self.x, self.y, self.w, self.h)
    
    def height(self):
        return self.h   
    def lenght(self):
        return self.w
    
    def width(self):
        return self.h
    
    def area(self):
        return self.w * self.h
    
    def location(self):
        return (self.x, self.y)
    
    def is_dino(self): #bidimensional (2D)        
        if 20 < self.w < 60 and 20 < self.h < 60 and 0.5 < self.aspect_ratio < 1.5:
            self.label = "dino"
            return True
        else:
            return False
    
    def is_cactus(self): #bidimensional (2D)
        if 20 < self.w < 60 and 20 < self.h < 60 and 0.5 < self.aspect_ratio < 1.5:
            self.label = "cactus"
            return True
        else:
            return False
    
    def is_fcking_prehistoric_birds(self): #bidimensional (2D)
        if 20 < self.w < 60 and 20 < self.h < 60 and 0.5 < self.aspect_ratio < 1.5:
            self.label = "fcking_prehistoric_birds"
            return True
        else:
            return False