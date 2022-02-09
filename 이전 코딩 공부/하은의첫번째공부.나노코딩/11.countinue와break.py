absent = [2,5] #결석
no_book = [7] #책을 깜빡했음
for student in range(1, 11): #1부터 10까지
    if student in absent:
        continue #그냥 다음 반복으로 넘어감
    elif student in no_book:
        print("{0}새끼 때문에 오늘 수업 마치고 빠따 한 대씩.".format(student))
        break
    print("{0}야, 책 읽어봐".format(student))

