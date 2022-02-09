# # class JSS:
# #     def __init__(self):
# #         self.name = input('이름: ')
# #         self.age = input('나이: ')
# #     def show(self):
# #         print('내 이름은 {}, 나이는 {}세입니다.' .format(self.name, self.age))

# # class JSS2(JSS):
# #     pass


# class HASS:
#     def __init__(self):
#         self.name = input('이름:')
#         self.age = input('skdl')
#     def show(self):
#         print("내 이름은 {} 나이는 {}이다~" .format(self.name, self.age))

# class HASS2(HASS):
#     pass

# # a = JSS()
# # a.name
# # a.show()

# a = HASS2()


# a.show()

# result = 0

# def add(num):
#     global result
#     result += num
#     return result

# print(add(3))
# print(add(4))

# class Cal():
#     def __init__(self):
#         self.result = 0

#     def add(self, num):     # 더하기 기능
#         self.result += num
#         return self.result
#     def sub(self, num):
#         self.result -= num
#         return self.result

# a = Cal()
# b = Cal()

# print(a.add(1))
# print(a.add(2))
# print(a.add(5))
# print(a.add(8))
# print(a.sub(1))   

# 클래스는 객체마다 고유한 성격을 가진다!
# 마치 과자틀로 과자를 만드는 것처럼 class로 객체를 형성한다.

# 객체가 없는 class
class cookie: # 괄호 안해도 상관ㄴ?
    pass
a = cookie()
b = cookie()

class calcu():
    def __init__(self,first, second):
        self.first = first
        self.second = second
        # self.first = input("첫번째 수:")
        # self.second = input("두번째 수:")
        # self말고 다른 것도 가능
        
    def add(self):                # method: 클래스 안에 구현된 함수
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = calcu(4,2)
b = calcu(3,6)
print(type(a))

# a.setdata(4,2)
# print(a.second)

# b.setdata(7,8)
# print(b.first)

# print(id(a.first))
# print(id(b.first))

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

# class 상속
class Morecal(calcu):    # 괄호 안에 적으면 상속 완료
    def pow(self):
        result = self.first ** self.second   # 제곱하기: **
        return result

a = Morecal(4,2)
print(a.add())
print(a.pow())

# method overriding (덮어쓰기)
class Safecal(calcu):
    def div(self):
        if self.second == 0:
            return 0
        else:
            reseult = self.first / self.second

a = Safecal(4,0)
print(a.div())

class Family:
    lastname = '이'

print(Family.lastname)

# module

# 1
import mod1
print(mod1.add(3,3))
print(mod1.sub(2,1))

# 2
from mod1 import add, sub
# from mod1 import *
print(add(3,3))
print(sub(2,1))

import sys
sys.path.append("C:\\python workplace\\이전 코딩 공부")
print(sys.path)

import mod2   # 오류뜸
print(mod2.PI)   # 파일 안의 변수 값 사용할 때: . 사용
a = mod2.Math()
print(a.solv(2)) # 항상 a 를 이용해서 사용해야 할까
print(mod2.add(mod2.PI,2))


# C:\python workplace\점프투파이썬>set PYTHONPATH=C:/python workplace/이전 코딩 공부
# C:\python workplace\점프투파이썬>python
# 모르겠음


# 연습문제
# Q.1
class Caculator():
    def __init__(self):
        self.value = 0
# value는 계산할 값

    
    def add(self,val):
        self.value += val

class UpgradeCalculator(Caculator):
    def minus(self,val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)

# Q.2
class MaxLimitCalculator():
    def __init__(self):
        self.value = 0
        
    def add(self,val):
        self.value += val
        if self.value >=100:
            self.value = 100
            return self.value
        else:
            return self.value

cal = MaxLimitCalculator()
cal.add(50)
print(cal.value)
cal.add(60)
print(cal.value)


# public, protect, private
# protect를 사용하여 직접접근을 방지하자. 실무에서는 그렇게 많이 씀.
