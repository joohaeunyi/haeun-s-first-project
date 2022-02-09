def open_account():
    print("새로운 계좌가 생성되었습니다.")
#여기까지만 적으면 함수가 실행되지 않는다.
# 그저 정의만 한 것이고, 따로 호출을 해야 실행시킬 수 있다.

open_account()

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else: 
        print("출금 실패. 잔액: {0}원.".format(balance))
        return balance

def withdraw_night(balance, money): #밤에 출금
    commission = 500 #수수료 500원
    return commission, balance - money - commission


balance = 0 #잔액
balance = deposit(balance, 1000)

balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 1000)
#왜 커미션을 입력했는지 이해가 안된다.
print("수수료 {0} 원이며, 잔액은 {1}원입니다.".format(commission, balance))


# # 함수의 기본값 설정
# def profile(name, age, main_lang):      #\t: tab
#     print("이름 : {0}\t나이: {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))

# profile("최연준", 23, "파이썬")

#같은 학교 같은 학년 같은 반 같은 수업.

def profile(name, age=23, main_lang="파이썬"):      #\t: tab 
    print("이름 : {0}\t나이: {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))
        
profile("최연준")

#키워드 값

def profile2(name, age, main_lang):
    print(name, age, main_lang)


profile2(name = "휴닝카이", main_lang="파이썬", age=20)
profile2(main_lang="자바", age=23, name="최연준")
#이렇게 키워드를 지정하면 순서가 뒤바뀌어도 호출가능.

#가변인자를 이용한 함수 호출

# def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이르미 {0}\t나이 : {1}".format(name, age), end=" ") 
#     #end:줄바꿈 없이 다음문장이 출력될 수 있음
#     print(lang1, lang2, lang3, lang4, lang5)


def profile3(name, age, *language):   #*로 시작되는 '매개 변수'를 입력해서 뒤에 몇개가 오던 상관없이 할 수 있다.
    print("이름 : {0}\t나이 : {1}".format(name, age), end=" ") 
    for lang in language:
        print(lang, end=" ")
    print()
profile3("휴닝카이", 20, "Pytyhon", "Java", "C", "C++", "C#", " Javascript")
profile3("범규", 21, "Kotlin", "Swift")


print("-------------")

#지역변수:함수 내에서만 사용. 함수가 호출될 때 만들어지고 함수 호출이 끝나면 사라짐
#전역변수: 프로그램 어디서든지 부를 수 있는 변수

mic = 7

def performance(mic_sayong): #공연하는 날
    global mic #전역 공간에 있는 mic 사용
    mic = mic - mic_sayong
    print("[함수 내] 남은 마이크 : {0}".format(mic))


def perform_ret(mic, mic_sayong):
    mic = mic - mic_sayong
    print("[함수 내] 남은 마이크 : {0}".format(mic))
    return mic


print("전체 마이크 수 : {0}".format(mic))
# performance(2) #2명이 공연을 함

mic = perform_ret(mic, 2)
print("남은 마이크 : {0}".format(mic))


#Quiz: 표준 체중을 구하는 프로그램

def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height, gender, weight))




