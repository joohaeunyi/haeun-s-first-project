# def love_yourself(i):
#     print("{0}는 {0}를 사랑한다".format(i))
# love_yourself("나")
# # # def deposit(balance, money):
# # #     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance,money))

# # i = "나"
# # you = "너"


# # # def withdraw(balance, money):
# # #     print("출금이 완료되었습니다.")



# # def my_add(x1, x2):
# #     sum = x1 + x2
# #     print("입력된 첫번째 수:", x1, '-----', '입력된 두 번째 수 :', x2)
# #     result = '두 수의 합 %d' %sum           %d는 정수형

# #     return result

# # my_add(1,4)
# # print(my_add(1,4))

# # 하은이의 코딩 일지...
# # 보았는가? my_add(1,4) 와 print(my_add(1,4)) 의 값이 다르다! 

# # print(my_add(1,4))는 result 값을 반환한다!

# def my_add(x1,x2):
#     sum = x1 + x2
#     print("입력된 첫번째 수:", x1, '(그리고) 입력된 두 번째 수:', x2)
#     result = '두 수의 합 %d' %sum
    
#     return result    #print(my_add())하면 위에 result값이 뜬다. 

# my_add(4,11)
# print(my_add(2,6))

def my_multiple(a, b):
    sum = a+ b
    sub = a- b
    multi = a * b
    div = a / b

    return sum, sub, multi, div


my_multiple(2,8)
f_s, f_sub, f_mul, f_div = my_multiple(2, 8)

print('더하기:', f_s, '빼기:', f_sub, '곱하기:', f_mul, '나누기:', f_div)

a = 1
b = 2
(lambda z1, z2: z1+z2)(a,b)

print((lambda z1, z2: z1+z2)(a,b))