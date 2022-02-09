#ValueErrorr같은 건 파이썬에서 원래 제공하는 에러처리다.
#새로운 에러를 정의할 수 있다.
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg #메세지

    def __str__(self):
        return self.msg

#raise: 에러를 발생시키는 것
try:
    print("한 자리 숫자 나누기 전용 계산기입니다")
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))  #int : 정수형으로 바꾸기
    num2 = int(input("두 번째 숫자를 입력하세요 :"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) 
    #if의 경우에 맞지 않다면 BigNumberError라는 에러를 발생시킴.
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요?")
except BigNumberError as err:
    print("잘못된 값을 입력했습니다. 한 자리 숫자만 입력하세요.")
    print(err)