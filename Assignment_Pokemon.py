# Assignment Pokemon Game

from pokemon_module import *

c1 = Charmander("파이리", "불꽃", 20)
s1 = Squirtle("꼬부기", "물", 20)
b1 = Bulbasaur("이상해씨", "풀", 20)
p1 = Pikachu("피카츄", "전기", 20)

pokelist = [c1, s1, b1, p1]

# 스타팅 포켓몬 선택
while True:
    try:
        user_pokemon = int(input("스타팅 포켓몬을 선택하세요\n1)파이리 2)꼬부기 3)이상해씨 4)피카츄 : "))
        if user_pokemon == 1:
            a = input(f"정말로 {c1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {c1.name}입니다. {c1.name}는 {c1.type}타입 포켓몬입니다.\n\n")
                starting_pokemon = Charmander("파이리", "불꽃", 20)
                break
            elif a == 'N':
                print()
                continue
            else:
                print()
        elif user_pokemon == 2:
            a = input(f"정말로 {s1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {s1.name}입니다. {s1.name}는 {s1.type}타입 포켓몬입니다.\n\n")
                starting_pokemon = Squirtle("꼬부기", "물", 20)
                break
            elif a == 'N':
                print()
                continue
            else:
                print()
        elif user_pokemon == 3:
            a = input(f"정말로 {b1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {b1.name}입니다. {b1.name}는 {b1.type}타입 포켓몬입니다.\n\n")
                starting_pokemon = Bulbasaur("이상해씨", "풀", 20)
                break
            elif a == 'N':
                print()
                continue
            else:
                print()
        elif user_pokemon == 4:
            a = input(f"정말로 {p1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {p1.name}입니다. {p1.name}는 {p1.type}타입 포켓몬입니다.\n\n")
                starting_pokemon = Pikachu("피카츄", "전기", 20)
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

# 야생 포켓몬과 전투
i = 1
while i == True:
    try:
        target = random.choice(pokelist)
        target.name = f"야생의 {target.name}"
        print(f"==================================================================\n")
        print(f"{target.name}를 만났다!")
        print(f"{starting_pokemon.name}의 체력 : {starting_pokemon.hp}     /     {target.name}의 체력 : {target.hp}")
        while True:
            behavior = int(input(f"\n1)일반공격  2)타입공격  3)도망  4)게임종료 : "))
            if behavior == 1:
                starting_pokemon.normal_attack(target)
                print(f"{starting_pokemon.name}의 체력 : {starting_pokemon.hp}     /     {target.name}의 체력 : {target.hp}")

                if target.hp <= 0:
                    print(f"<<< {starting_pokemon.name}가 {target.name}와의 전투에서 승리했습니다! >>>")
                    print(f"\n\n\n\n")
                    starting_pokemon.hp = 20
                    target.hp = 20
                    break

                target.normal_attack(starting_pokemon)
                print(f"{starting_pokemon.name}의 체력 : {starting_pokemon.hp}     /     {target.name}의 체력 : {target.hp}")

                if starting_pokemon.hp <= 0:
                    print(f"<<< {starting_pokemon.name}가 {target.name}와의 전투에서 패배했습니다... >>>")
                    print(f"\n\n\n\n")
                    starting_pokemon.hp = 20
                    target.hp = 20
                    break
            elif behavior == 2:
                starting_pokemon.type_attack(target)
                print(f"{starting_pokemon.name}의 체력 : {starting_pokemon.hp}     /     {target.name}의 체력 : {target.hp}")

                if target.hp <= 0:
                    print(f"<<< {starting_pokemon.name}가 {target.name}와의 전투에서 승리했습니다! >>>")
                    print(f"\n\n\n\n")
                    starting_pokemon.hp = 20
                    target.hp = 20
                    break

                target.type_attack(starting_pokemon)
                print(f"{starting_pokemon.name}의 체력 : {starting_pokemon.hp}     /     {target.name}의 체력 : {target.hp}")

                if starting_pokemon.hp <= 0:
                    print(f"<<< {starting_pokemon.name}가 {target.name}와의 전투에서 패배했습니다... >>>")
                    print(f"\n\n\n\n")
                    starting_pokemon.hp = 20
                    target.hp = 20
                    break
            elif behavior == 3:
                print(f"{starting_pokemon.name}와 무사히 도망쳤다\n")
                print(f"\n\n\n\n")
                break
            elif behavior == 4:
                print(f"게임을 종료합니다\n")
                i = i-1
                break
    except ValueError:
        print("다시 입력해주세요\n")
