class FlyingBehavior:
    def fly(self):
        return f"하늘을 훨훨 날아갑니다~"


class JetPack(FlyingBehavior):
    def fly(self):
        return f"로켓추진기로 하늘을 날아갑니다!"


class NoFly(FlyingBehavior):
    def fly(self):
        return f"하늘을 날 수 없습니다."


class FlyWithWings(FlyingBehavior):
    def fly(self):
        return f"날개로 하늘을 훨훨 날아갑니다"



class Pikachu:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.fly_behavior = NoFly()  # composition


p1 = Pikachu("피카츄", 35)
print(p1.fly_behavior.fly())