class Animals:
    noise = "Rrrr"
    color = "Red"
    def make_noise(self):
        print(f"{self.noise}")
    def set_noise(self, new_noise):
        self.noise = new_noise
    def get_noise(self):
        return self.noise
    def set_noise(self, new_noise):
        self.new_noise = new_noise
        return self.noise        
    def get_color(self):
        return self.color
    def set_color (self, new_color):
        self.color = new_color
        return self.color

class Wolf(Animals):
    noise = "grrrr"

class BabyWolf(Wolf):
    color = "yellow"