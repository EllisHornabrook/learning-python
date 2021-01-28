class Planet:
    def __init__(self, name, life, gravity, radius):
        self.name = name
        self.life = life
        self.gravity = gravity
        self.radius = radius
        self.type = 'planet'

    def description(self):
        return f'{self.name} is a {self.type}'