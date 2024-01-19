# class Pokemon:
#     pass
#
# pikachu = Pokemon()
# squirtle = Pokemon()
# pikachu.name = "피카츄"
# pikachu.nemesis = squirtle
# print(pikachu.name)
# #print(pikachu.nemesis.name)
# #squirtle.name = "꼬부기"
# pikachu.nemesis.name = "꼬부기" #squirtle.name = "꼬부기"
# print(pikachu.nemesis.name)
# print(squirtle.name)

# class Pokemon():
class Pokemon:
    def __init__(self, name):
        self.name = name
        print(f"{name} 포켓몬스터 생성")

    def attack(self, target):
        print(f"{self.name}이(가) {target.name}을(를) 공격!")


charizard = Pokemon("리자몽")
pikachu = Pokemon("피카츄")
squirtle = Pokemon("꼬부기")
charizard.attack(squirtle)
# print(pikachu.name)
# print(squirtle.name)