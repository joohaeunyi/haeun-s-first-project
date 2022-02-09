# for i in range(100):
#     print("최연준은 잘생겼다 {0}번 외치기".format(i+1))


lst = [10,20,30,40,50]
for data in lst:
    print(data)

#꼭 숫자 아니여도 된다!!
bts = ['sunga',"v","rm","ji","jk","j-hope","jimin"]
for member in bts:
    print(member)







txt = ["연준","휴닝","태현","수빈","범규"]
for member in txt:
    print(member)

# 멤버 합류
연습생 = ("희진","현진","여진","츄","올리비아 혜")
girl_thismonth = []

for i in range(len(연습생)):
    print("연습생[{0}]: {1} -> 이달소[{0}]".format(i,연습생[i]))
    girl_thismonth.append(연습생[i])
print("합류된 이달소 멤버 :", girl_thismonth)

#1부터 10까지의 합 구하기

hap = 0
for i in range(10):
    hap += i+1
    print('{0}를 더한 지금까지의 합은 {1}입니다'.format(i+1,hap))
print("1부터 10까지의 합: {0}".format(hap))

#while
i=1
while i < 6:
    print("{0}번 말하는 중. 김석진은 잘생겼다!".format(i))
    i += 1

from random import *
die = 0
while die != 6:
    print("주사위를 굴렸다. \'{0}\'이 나왔다. 게임을 계속 진행한다.".format(die))
    die = randint(1,6)
print("주사위를 굴렸다. \'{0}\'이 나왔다. 게임을 종료한다.".format(die))

# from random import *와 import random의 차이점
# 47행에 import random쓰면 51행에 die = random.randint(1,6)를 써야된다.
# from random import *은 모든 함수를 불러오는 거임. 따라서 random.randint처럼 
# random을 불러오지 않아도 된다. 
# 하지만 전체 함수를 불러오기 때문에 메모리가 많이 낭비되서 되도록 지양하라고 한다. 

# # 무한 while 문 제어하기
# while True:
#     print("최연준님 안무 연습하실 시간입니다.")
# #ctrl + c 를 눌러 강제종료시키자.

count = 0
while True:
    number = input("값을 입력하세요")
    count += 1
    print("입력된 값 : {0} [{1}]".format(number,count))
    
    if number == 'esc':
        print("esc를 입력해서 강제 종료")
        break
print("총 반복 수 : ", count)


