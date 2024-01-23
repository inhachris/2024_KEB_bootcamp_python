import random

normal_attack_list = ["몸통박치기", "할퀴기", "베어가르기", "막치기"]
fire_attack_list = ["불꽃세례", "화염방사", "불대문자"]
water_attack_list = ["거품광선", "물대포", "하이드로펌프"]
grass_attack_list = ["덩굴채찍", "잎날가르기", "리프스톰"]
electric_attack_list = ["10만볼트", "번개", "볼트태클"]

class Pokemon:
    def __init__(self, name):
        self.name = name

    def normal_attack(self, target):
        damage = random.randrange(3, 7)    # 3 ~ 6
        print(f"{self.name}가 {target.name}에게 {random.choice(normal_attack_list)}!     (-{damage})")
        target.hp = target.hp - damage
        if target.hp < 0:
            target.hp = 0

    def type_attack(self, target):
        damage = random.randrange(6, 12)    # 6 ~ 11
        if self.type == "불꽃":
            print(f"{self.name}가 {target.name}에게 {random.choice(fire_attack_list)}!     (-{damage})")
        elif self.type == "물":
            print(f"{self.name}가 {target.name}에게 {random.choice(water_attack_list)}!     (-{damage})")
        elif self.type == "풀":
            print(f"{self.name}가 {target.name}에게 {random.choice(grass_attack_list)}!     (-{damage})")
        elif self.type == "전기":
            print(f"{self.name}가 {target.name}에게 {random.choice(electric_attack_list)}!     (-{damage})")
        target.hp = target.hp - damage
        if target.hp < 0:
            target.hp = 0

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
