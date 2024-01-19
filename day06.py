class FlyingMixin:
    def fly(self):
        return f"{self.hidden_name}이(가) 하늘을 훨훨 날아갑니다~"

class SwimmingMixin:
    def swim(self):
        return f"{self.hidden_name}이(가) 수영을 합니다."

class Pokemon:
    def __init__(self, name):
        self.hidden_name = name

    def attack(self):    # self는 반드시 객체 (클래스x)
        print("공격~")

    def get_name(self):
        return self.hidden_name

    def set_name(self, new_name):
        self.hidden_name = new_name

    name = property(get_name, set_name)

class Charizard(Pokemon, FlyingMixin):
    pass

class Gyarados(Pokemon, SwimmingMixin):
    pass


g1 = Gyarados("갸라도스")
c1 = Charizard("리자몽")

# print(g1.get_name())
# g1.set_name("잉어킹")
# print(g1.get_name())

# property
print(g1.name)
g1.name = "잉어킹"
print(g1.name)