class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        print(f"{self.name}가 {target.name}를 공격!")

class Charmander(Pokemon):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

class Squirtle(Pokemon):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

class Bulbasaur(Pokemon):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type

class Pikachu(Pokemon):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type