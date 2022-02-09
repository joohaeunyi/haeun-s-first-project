class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성됨.".format(self.name))
        print("체력  {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


#__init__ : 생성자. 마린, 탱커같은 객체 만들때 자동으로 호출됨. 클레스로 부터 만들어지는 녀석들 : 객체
# 마린과 탱크는 Unit의 instance

# 레이스
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))