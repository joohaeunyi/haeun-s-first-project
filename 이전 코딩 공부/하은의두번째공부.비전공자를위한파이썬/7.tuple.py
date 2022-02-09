#tuple
#리스트와 비슷하지만 더 빨리 만들 수 있음. 삭제x 추가x

bts = ("jin", "rm", "v", "suga")
print(bts)

txt = "태현", "휴닝", "수빈" #괄호 안 써도 된다.
print(txt)

number1 = tuple(range(10))
print(number1)

#range(시작, 끝)
number2 = tuple(range(1,5)) 
print(number2)

#range(시작, 끝, 증가량)
number3 = tuple(range(1,15, 3)) 
print(number3)

#range(시작, 끝, 감소량)
number4 = tuple(range(15, 1, -2)) 
print(number4)

#tuple → list 변환
a = [1,2,34]
b = tuple(a)
print(b) #완전 간단하지?

#list → tuple 변환
c = 3,6,7
d = list(c)
print(d)



