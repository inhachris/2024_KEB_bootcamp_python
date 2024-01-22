class Pokemon:
    def __init__(self, name):
        self.name = name

    def normal_attack(self, target):
        print(f"{self.name}가 {target.name}에게 몸통박치기 공격!")
        print(f"\n========================================================================\n")
        target.hp = target.hp - 4
        if target.hp < 0:
            target.hp = 0
            print(f"{self.name}의 체력 : {self.hp}     /     {target.name}의 체력 : {target.hp}")
        else:
            print(f"{self.name}의 체력 : {self.hp}     /     {target.name}의 체력 : {target.hp}")

    def type_attack(self, target):
        print(f"{self.name}가 {target.name}에게 {self.type}타입 공격!")
        print(f"\n========================================================================\n")
        target.hp = target.hp - 8
        if target.hp < 0:
            target.hp = 0
            print(f"{self.name}의 체력 : {self.hp}     /     {target.name}의 체력 : {target.hp}")
        else:
            print(f"{self.name}의 체력 : {self.hp}     /     {target.name}의 체력 : {target.hp}")

class Charmander(Pokemon):
    def __init__(self, name, type, hp):
        super().__init__(name)
        self.type = type
        self.hp = hp

class Squirtle(Pokemon):
    def __init__(self, name, type, hp):
        super().__init__(name)
        self.type = type
        self.hp = hp

class Bulbasaur(Pokemon):
    def __init__(self, name, type, hp):
        super().__init__(name)
        self.type = type
        self.hp = hp

class Pikachu(Pokemon):
    def __init__(self, name, type, hp):
        super().__init__(name)
        self.type = type
        self.hp = hp
