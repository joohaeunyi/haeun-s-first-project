print(5)
print(-10)
print(2*8)
print(3*(3+1))

print('풍선')
print("나비")
#작은따옴표, 큰따옴표 똑같이 문자열 쓸때 사용.
print("ㅋ"*9)
#문자열과 곱하기를 섞어서 사용할 수 있다.

#참과거짓
print(5>10)
print(4 >=7) # False
print(True)
print(not True)

#변수 (애완동물을 소개해주세요~)
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3
print("우리집 " +animal+ "의 이름은 " + name + "에요")
print( name, "는 ", age, "살이고,", hobby ,"을 아주 좋아해요")
print(name+ "는 어른일까요? " + str(is_adult))
'''이렇게하면 여러문장이 주석처리 됨!!'''
# 여러문장 쓰는 주석 한번에 처리하기! 
# 바로바로~ ctrl + slash~ 한번 해보셈
# 주석 해제도 ctrl + slash입니다!

# quiz) 변수를 이용하여 다음 문장을 출력하시오.

station = "사당"
print(station,'행 열차가 들어오고 있습니다.')
station = "신도림"
print(station, "행 열차가 들어오고 있습니다.")
station = "인청공항"
print(station, "행 열차가 들어오고 있습니다.")

print(2**3) #2의 3제곱
print(5%3) #5나누기3의 나머지
print(10//3) #10나누기3의 몫

print(3==3) #True
print(3==7) #False
print(3+4 ==7) #True!!
print(1 != 3)

print((3 > 0) and (3 < 5 )) #둘다 만족시켜야지 True 나옴 #True
print((2+3)*4) #20
number = 2+3*4
print(number) #14
number = number+2
print(number) #16
number +=2
print(number)
number *=2
print(number)
number -=2
print(number)

number %= 2 #number를 2로 나누었을 때의 나머지 
print(number)

