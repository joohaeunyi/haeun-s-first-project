# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = '마린' 
# hp = 40
# damage = 5 #공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# #탱크 : 공격 유닛, 탱크. 포를 쏜다. 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n.".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
#         name, location, damage))

# # attack(name, "1시", damage)
# # attack(tank_name, "1시", tank_damage)
# # attack(tank2_name, "1시", tank2_damage)

# #일반 유닛
# class Unit: 
#     def __init__(self, name, hp, damage):    #__init__: 생성자. 마린이나 탱커와같이 어떤 클래스로 부터 만들어지는 클래스. 객체. unit클래스의 instance.  self제외하고 동일한 개수만큼 값을 지정해주어야함.
#         self.name = name          #self는 자기 자신을 의미하는 것.
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 40, 5)
# # marine2 = Unit("마린", 40, 5)
# # tank = Unit("탱크", 150, 35)

# #레이스 : 비행기 유닛. 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
# #멤버변수를 외부에서 사용가능.

# #마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
# wraith2 = Unit("빼앗은 레이스", 80,5)
# wraith2.clocking = True
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# #클래스 외부에서 원하는 변수 확장가능. 확장한 객체에만 적용./ 기존의 다른 객체에는 적용 안됨.

# class AttackUnit : 
#     def __init__(self, name, hp, damage):    #__init__: 생성자. 마린이나 탱커와같이 어떤 클래스로 부터 만들어지는 클래스. 객체. unit클래스의 instance.  self제외하고 동일한 개수만큼 값을 지정해주어야함.
#         self.name = name
#         self.hp = hp
#         self.damage = damage
        
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))    
#             #1,3번째 인자?는 self를 붙였다. 즉 56,58행에서 정의한 것을 사용
#             #2번째 인자 location은 self를 붙이지 않음. 즉 60행에서 언급한 것을 사용

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
        # print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))


#다중상속. 부모가 둘.,
#일반유닛: 부모, attackUnit: 자식
class Unit: 
    def __init__(self, name, hp):  
        self.name = name
        self.hp = hp

class AttackUnit(Unit) : #(Unit)을 통해 일반유닛의 속성을 상속받음.
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))    

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

#드랍쉽 : 수송기. 마린/ 파이어뱃 / 탱크 등을 수송. 공격x

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(" {0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(\
            name, location, self.flying_speed))

#공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): #둘다 상속받음. 컴마를 써서 작성.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)
        #attackunit과 flyable유닛으로부터 상속받아 초기화를 시켜준 유닛임.

#발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
#133행에 self를 제외한 4가지 속성을 입력
valkyrie.fly(valkyrie.name, "3시")  
#127행의 self을 제외한 2가지 속성(name, location)을 입력
#flyableattackunit은 flyable의 속성을 상속받으니 .fly를 사용할 수 있는 것으로 생각한다!




# #메딕: 힐러

# #파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시") #공격을 하기 위해 attack함수를 호출

# # #공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

