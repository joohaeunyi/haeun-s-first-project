txt = {"연준", "휴닝", "태현"}
print(txt, type(txt))

txt = list(txt)
print(txt, type(txt))

txt = tuple(txt)
print(txt, type(txt))
#괄호 차이를 보시라!

txt = set(txt)
print(txt, type(txt))



#Quiz
from random import *
lst = [1,2,3,4,5]
print(type(lst))
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1)) #1개를 무작위로 뽑기

print("-----------")
rist = range(1,21) #1부터 20까지 생성
rist = list(rist)
print(rist)
shuffle(rist)
print(rist)

#4명 무작위 추출
winners = sample(rist, 4)
print(winners)


print("-- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:4]))
print("축하합니다 ^0^")

