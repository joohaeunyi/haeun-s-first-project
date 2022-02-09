# Bool 형식 (2장 복습)
# "python" = True
# ""       = False
# [1,2,3]  = True
# []       = False
# ()       = False
# {}       = False
# 1        = True
# 0        = False
# None     = False

#############################
# if문

a = 1
b = 2
if  a and b:
    print("돈있음")
else:
    print("돈없읔ㅁ")


# 1 = True
# 0 = False

if 2 in [1,2,3]:
    pass
else:
    print('없음')

#elif: 위에 조건문에 false가 나오면 실행


# 간결하게 적기
score = 70
message = 'success' if score >=60 else 'failure' 
print(message)

# 택시타기
money = 2000
card = True
if money >= 3000 or card: # 돈은 부족하지만 card가 있음
    print("택시를 타고 가라") 
else:
    print("걸어가라")


#___________________________

pocket = ['coin','paper']
card = True
if 'money' in pocket: # False 나와서 31행 elif로 넘어감
    print('택시타자') 
elif card:            # True
    print("택시타자")
else:
    print('뚜벅이')

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass 
else:
    print("ㅇㅎ")



############################################
#While문

hit = 0
while hit < 10:
    hit = hit +1
    print('%d번 침' % hit)
    if hit == 10:
        print('10대 다침')

# 무한 루프의 늪
# ctrl + c 로 빠져나가기
# while True:
#     print('ㅎㅇ')

prompt = '''
1. Add
2. Del
3. List
4. Quit

Enter number: '''
number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())


# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee -1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
#         coffee = coffee -1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break




############################################
#for문

# i = 임시변수 j, k 등등 다른 알파벳도 가능.
a_list = ['안녕', 'hi', 'ㅎㅇ']
for i in a_list:
    print(i)

# 리스트 안에 튜플이 3개 있는 형태
number_list = [(1,2), (3,4), (5,6)]
for first, last in number_list: # 괄호 안쳐도 제대로 작동 됨. 왜?
    print(first + last)

sum = 0
for i in range(1,11):  # range의 마지막 숫자(11)은 포함되지 않음.
    sum = sum + i
    print(sum, end = ' ') # 다음 줄로 넘어가지 않고 띄어쓰기됨.

#구구단
for i in range(2,10):
    print('%d단 :' % i , end = ' ')
    for j in range(1,10):
        print(i * j, end = " ")



###################################
#3장 연습문제

#Q1.
a = "Life is too short, you need python"

if "wife" in a: print("wife") #False
elif "python" in a and "you" not in a: print("python") # False
elif "shirt" not in a: print("shirt") # True
elif "need" in a: print("need") # True
else: print("none")
#답은 shirt  (먼저 참으로나온거)


#Q2.
sum = 0
while i in range(1,1001):
    if i%3 == 0:
        sum = sum + i
    i = i + 1
print(sum)

#Q3.
i = 0
while True:
    i = i + 1
    if i > 5:
        break
    print('*' * i)    # * i가 뭔뜻인지 

#Q.4
for i in range(1,101):
    print(i, end = " ")

#Q.5
sum = 0
a_score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for i in a_score:
    sum = sum + i
print(sum/len(a_score))

#Q.6
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)


