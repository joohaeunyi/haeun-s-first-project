print(abs(-5))
print(pow(4,2)) #4^2=16
print(max(5,12)) #12
print(min(5,12,8))
print(round(3.14))

#from math import * 
#math안에 있는 모든 것을 사용하겠다.
from math import *
print(floor(4.88)) #내림.4
print(ceil(3.14)) #올림.4 
print(sqrt(16)) #제곱근.4

#랜덤함수 #무작위로 숫자 뽑기
from random import *
print(random()) #0.0~1.0(미만의) 임의의 값 생성
print(random()*10) #0.0~10.0미만 임의의 값 생성
print(int(random() * 10)) #소수자리를 없애버림
#만약 0은 나오지 않게 한다면?
print(int(random()*10)+1) #1~10이하의 임의의 값 생성

#로또값을 추출하자
# 1)
print(int(random() * 45)+1) #1~45이하 임의의 값 생성
print(int(random() * 45)+1) 
print(int(random() * 45)+1) 

# 2) randrange
print(randrange(1,46)) #1~46 미만 임의의 값 생성
print(randrange(1,46)) 
print(randrange(1,46)) 

# 3) randint
print(randint(1,45)) #1 ~ 45 이하 임의의 값 생성
print(randint(1,45)) 
print(randint(1,45))


#Quiz 4~28일 중 하루 랜덤으로 정하기
from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" + str(date)+ "일로 선정되었습니다.")
