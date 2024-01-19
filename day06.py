class FlyingMixin:
    def fly(self):
        return f"{self.name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name):
        self.name = name

    def attack(self):    # self는 반드시 객체 (클래스x)
        print("공격~")

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass

g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")
# print(c1.fly())
# print(g1.swim())
# c1.attack()
# # Charizard.attack()    # TypeError    c1, g1과 같은 객체가 self
# Charizard.attack(c1)
print(g1.get_name())
g1.set_name("잉어킹")
print(g1.get_name())