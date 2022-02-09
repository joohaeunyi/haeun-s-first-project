# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}님, 커피가 준비되었습니다. {1}번 기회 드릴게요.".format(customer, index))
#     index -=1     #index를 1번씩 줄여나감
#     if index ==0:
#         print("언제오시냐구요, 커피 버렸습니다 ㅡㅡ")

# customer = "최연준"
# index = 1
# while True:
#     print("{0}님, 커피가 준비되었습니다. {1}번 불렀습니다.".format(customer, index))
#     index +=1     #index를 1번씩 줄여나감

 #무한루프에 빠짐. ctrl +c 누르면 강제 종료

customer = "휴닝카이"
person = "Unknown"

while person != customer : 
    print("{0}님, 커피가 준비되었습니다. ".format(customer))
    person = input("이름이 어떻게 되세요?")
    

