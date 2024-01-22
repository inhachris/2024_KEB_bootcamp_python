# Assignment Pokemon Game

from pokemon_module import *
import random

c1 = Charmander("파이리", "불꽃")
s1 = Squirtle("꼬부기", "물")
b1 = Bulbasaur("이상해씨", "풀")
p1 = Pikachu("피카츄", "전기")

pokelist = [c1, s1, b1, p1]

# 스타팅 포켓몬 선택
while True:
    try:
        user_pokemon = int(input("스타팅 포켓몬을 선택하세요\n1)파이리 2)꼬부기 3)이상해씨 4)피카츄 : "))
        if user_pokemon == 1:
            a = input(f"정말로 {c1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {c1.name}입니다. {c1.name}는 {c1.type}타입 포켓몬입니다.\n")
                starting_pokemon = Charmander("파이리", "불꽃")
                break
            elif a == 'N':
                print()
                continue
            else:
                print()
        elif user_pokemon == 2:
            a = input(f"정말로 {s1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {s1.name}입니다. {s1.name}는 {s1.type}타입 포켓몬입니다.\n")
                starting_pokemon = Squirtle("꼬부기", "물")
                break
            elif a == 'N':
                print()
                continue
            else:
                print()
        elif user_pokemon == 3:
            a = input(f"정말로 {b1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {b1.name}입니다. {b1.name}는 {b1.type}타입 포켓몬입니다.\n")
                starting_pokemon = Bulbasaur("이상해씨", "풀")
                break
            elif a == 'N':
                print()
                continue
            else:
                print()
        elif user_pokemon == 4:
            a = input(f"정말로 {p1.name}를 선택하시겠습니까? Y / N : ")
            if a == 'Y':
                print(f"\n당신의 포켓몬은 {p1.name}입니다. {p1.name}는 {p1.type}타입 포켓몬입니다.\n")
                starting_pokemon = Pikachu("피카츄", "전기")
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

while True:
    try:
        target = random.choice(pokelist)
        behavior = int(input(f"야생의 {target.name}를 만났다!\n1)일반공격  2)타입공격  3)도망  4)게임종료 : "))
        if behavior == 1:
            print(f"{starting_pokemon.name}가 {target.name}에게 몸통박치기 공격!\n")
        elif behavior == 2:
            print(f"{starting_pokemon.name}가 {target.name}에게 {starting_pokemon.type}타입 공격!\n")
        elif behavior == 3:
            print(f"{starting_pokemon.name}와 무사히 도망쳤다\n")
        elif behavior == 4:
            print(f"게임을 종료합니다\n")
            break
    except ValueError:
        print("다시 입력해주세요\n")