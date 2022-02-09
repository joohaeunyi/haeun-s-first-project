# # 자식class에서 정의한 method를 쓰고싶을 때 method를 새롭게 정의하여 사용하는 것.
# #일반유닛: 부모, attackUnit: 자식
# class Unit: 
#     def __init__(self, name, hp, speed):  
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
#             .format(self.name, location, self.speed))

# class AttackUnit(Unit) : 
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"
#             .format(self.name, location, self.damage))    

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(\
#             name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable): #둘다 상속받음. 컴마를 써서 작성.
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 
#         Flyable.__init__(self, flying_speed)

#     # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# #배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")
# #지금 문제: 지상유닛이면 ->move
# # 공중유닛이면 ->fly를 써야되는 번거로움이 생김.


class Unit: 
    def __init__(self, name, hp, speed):  
        self.name = name
        self.hp = hp
        self.speed = 
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 공격 유닛       
class AttackUnit(Unit) : 
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"
            .format(self.name, location, self.damage))    

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    #스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp> 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
#탱크
class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가.
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False :
            return
        #현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False :
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else :
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = False
        

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(\
            name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable): #둘다 상속받음. 컴마를 써서 작성.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 
        Flyable.__init__(self, flying_speed)

    def move(self, location): #move의 재정의
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

##레이스 : 비행기 유닛. 클로킹(상대방에게 보이지 않음)
class Wrait(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True : #클로킹 모드 -> 모드 해제
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else :
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg") #good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


    # 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

#배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
       #Unit.__init__(self, name, hp, 0):
       super().__init__(name, hp, 0) 

#서플라이 디폿 : 건물, 1개 건물 = 8 유닛 생성.
suuply_depot = BuildingUnit("서플라이 디폿", 500, "7시")
#pass가 없었으면 오류가 뜨는데 정상적으로 작동된다. 아무것도 안 뜨긴 하지만 

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
    pass
def game_over():
    pass

game_start()
game_over() #오류가 안뜬다!


