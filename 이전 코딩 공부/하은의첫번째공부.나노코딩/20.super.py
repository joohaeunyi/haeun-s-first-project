class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):         
        # super().__init__()     #만약 12,13행 대신 11행 super()를 쓰면
        Unit.__init__(self)      #순서상 맨 처음 class(Unit)에 대해서
        Flyable.__init__(self)   #__init__함수가 호출된다.
#드랍쉽
dropship = FlyableUnit()
#다중상속할 때 명시적으로 
