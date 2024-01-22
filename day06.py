# Assignment Pokemon Game

class Pokemon:
    def __init__(self, name):
        self.name = name

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

c1 = Charmander("파이리", "불꽃")
s1 = Squirtle("꼬부기", "물")
b1 = Bulbasaur("이상해씨", "풀")
p1 = Pikachu("피카츄", "전기")

# 스타팅 포켓몬 선택
while True:
    try:
        user_pokemon = int(input("스타팅 포켓몬을 선택하세요\n1)파이리 2)꼬부기 3)이상해씨 4)피카츄 : "))
        if user_pokemon == 1:
            a = input(f"정말로 {c1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {c1.name}입니다.")
                break
            elif a == 'N':
                print()
                continue
            else:
                print()
        elif user_pokemon == 2:
            a = input(f"정말로 {s1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {s1.name}입니다.")
                break
            elif a == 'N':
                print()
                continue
            else:
                print()
        elif user_pokemon == 3:
            a = input(f"정말로 {b1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {b1.name}입니다.")
                break
            elif a == 'N':
                print()
                continue
            else:
                print()
        elif user_pokemon == 4:
            a = input(f"정말로 {p1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {p1.name}입니다.")
                break
            elif a == 'N':
                print()
                continue
            else:
                print()
        else:
            print("다시 입력해주세요\n")

    except ValueError:
        print("다시 입력해주세요\n")

