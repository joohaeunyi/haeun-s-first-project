# 내장 함수
divmod(4,2) # 몫과 나머지

for i, name in enumerate(['aabc', 'dfg', 'qwer']):
    print(i, name)

def positive(l):
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6])) 
# 양수만 출력하기


# 연습 문제
# Q.3
print('Q.3.1')
print(abs(-3)-3)
print(all([1, 2, abs(-3)-3])) # 하나라도 False 있으면 False. 0이 있으므로 False

print('Q.3.2')
print(chr(ord('a')) == 'a')
# ord: 문자의 유니코드 값을 돌려줌.
# chr: unicode 값을 입력받아 그 코드에 해당되는 문자를 출력.

# Q.4
# lambda는 인자 : 표현식 
a = list(filter(lambda x : x >= 0 , [1, -2, 3, -5, 8, -3]))
print(a)

# Q.5
print(int(0xea))
print(int('0xea', 16))

# Q.6
def three_times(x):
    return x*3

a = list(map(three_times, [1,2,3,4]))
print(a)

# Q.7
print('Q.7')
print(max([-8, 2, 7, 5, -3, 5, 0, 1]) + min([-8, 2, 7, 5, -3, 5, 0, 1]))

# Q.8
# round: 반올림 해주는 함수
print('Q.8')
print(round(17/3,4))

# Q.9

# Q.13++
import random

result = []
while len(result) < 6:
    num = random.randint(1,45) # 1~ 45 난수 발생
    if num not in result: 
        result.append(num)
a=sorted(result)
print(a)
        # 리스트 result의 개수가 6개가 안되면
def random_pop(data):
    number = random.randint(1, len(data)-1)