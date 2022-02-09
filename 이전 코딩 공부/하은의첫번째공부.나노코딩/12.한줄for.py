#출석번호가 1,2,3,4 앞에 100을 붙이기로 함. -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i + 100 for i in students]
print(students)

bts = ["RM","Suga", "V", "Jin"]
bts = [len(i) for i in bts]
print(bts)


#학생 이름을 대문자로 변환
bts = ["RM","Suga", "V", "Jin"]
bts = [i.upper() for i in bts]
print(bts)

#Quiz
from random import *
cnt = 0
for i in range(1,51):
    e = randrange(5,51)
    if 5<= e <= 16:
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, e))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)". format(i, e))
print("총 탑승 승객 : {}분".format(cnt))