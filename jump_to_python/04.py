# def say():
#     return 'Hi'

# a = say()
# print(a)

# def add(a,b):
#     print("%d과%d의 합은 %d입니다." %(a,b, a+b))

# a = 1
# b = 245

# add(a, b)

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# print(add_many(1,6,7,13,4567))

# def add_mul(choice, *args):
#     if choice == "add":
#         resul = 0 
#         for i in args:
#             resul = resul +i
#     elif choice == "mul":
#         resul = 1
#         for i in args:
#             resul = resul * i
#     return resul 

# rere = add_mul('add',2,3,4,5)
# print(rere)

# def add_and_mul(a,b):
#     return a+b, a*b
# result = add_and_mul(2,3)
# print(result) #튜플 값으로 반환

# def say_nick(nick):
#     if nick == "바보":
#         return
#     print("나의 별명은 %s 입니다." % nick)
    
# re = say_nick('항')
# print(re)

# ree = say_nick('바보')
# print(ree) # 그냥 return 만 써서 바보의 값이 반환되지 않는다. 

# def say_myself(name, old, man=True): 
#     print('내 이름은 %s입니다.' % name)
#     print('나이는 %d입니다' % old)
#     if man :
#         print('남자입니다')
#     else:
#         print('여자입ㄴ다')

# say_myself('하은' 24) #####왜 안됨??????

# a = 1
# def vartest():
#     global a
#     a = a+3

# vartest()
# print(a)

# add = lambda a, b: a+b
# result = add(3, 4)
# print(result)


# print("I" "like" "cat")
# print("I" + "like" + "cat")
# print("I","like","cat")

# for i in range(10):
#     print(i, end = " ")


#####################################

# 파일 생성하기

f = open("newfile.txt", 'w')  #w는 쓰기모드: 파일에 내용을 쓸 때 사용. 
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i    # \n은 다음 줄에 입력하게 해줌 
    f.write(data)
f.close()

# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     print(data)


# # 첫번째 줄만 읽기
# f = open("C:/Users/heana/Desktop/Python Workplace/newfile.txt", 'r')
# line = f.readline()    
# print(line)
# f.close()

# # 모든 줄 읽기
# f = open("C:/Users/heana/Desktop/Python Workplace/newfile.txt", 'r')
# while True:
#     line = f.readline()    
#     if not line: break     # 더 이상 읽을 줄이 없으면 break.
#     print(line)
# f.close()


# while 1:
#     data = input()
#     if not data: break
#     print(data)

f = open("C:/Users/heana/Desktop/Python Workplace/newfile.txt", 'r')
lines = f.readlines()   #리스트 만들기.
for line in lines:
    print(line)
f.close()

f = open("C:/Users/heana/Desktop/Python Workplace/newfile.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("C:/Users/heana/Desktop/Python Workplace/newfile.txt",'a') 
                             # a: 추가모드, 파일 마지막에 새로운 내용 추가 시킬때 사용.
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

# 추가로 적은 내용(11~20) 포함하여 다시 읽기. 
# f = open("C:/Users/heana/Desktop/Python Workplace/newfile.txt",'r') 
# data = f.read()
# print(data)
# f.close()

f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

# # 위에거 짧게 표현하기
# with open("foo.txt", "w") as f:
#     f.write("Life is too short, you need python")

# 확인차 읽어보기
f = open("C:/Users/heana/Desktop/Python Workplace/foo.txt",'r')
data = f.read()
print(data)
f.close()


######################################

#연습문제
# 1.
def is_odd(a):
    if a % 2 == 0:
        print('%d는 짝수입니다.' % a)
    elif a % 2 == 1:
        print('%d는 홀수입니다.' % a)
    else:
        print('잘못된 수를 입력하셨습니다')

is_odd(4)
is_odd(7)


# 2.
# def avg_num(*args):
#     result = 0
#     result_avg = 0
#     for i in args:
#         result = result + i
        
#     return result / len(args) = result_avg

# 3.
input1 = input("첫 번째 숫자:")
input2 = input("두 번째 숫자:")

total = int(input1) + int(input2)
print("두 수의 합은 %s임." %total)

# 4.
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

# 5.
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()
f2 = open("test.txt", 'r')