# from game.sound import *
# echo.echo_test()
# echo

# import game.sound.echo
# game.sound.echo.echo_test()


# 기본1
try:
    4 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없음')

# 기본2
try: 
    f = open("나없는파일", 'r')
except FileNotFoundError:
    print('없는 파일이래요')


# finally
f = open('foo.txt', 'w')
try:
    f.write('hello')
finally:
    f.close()
    print('hello')

# except가 여러개
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print('0으로 못 나눠요')
except IndexError:
    print('인덱싱 안 돼요')

# except 한 개로 함께 처리할 수도 있다.
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

# try 문에 else 사용하기
try:
    age=int(input('나이를 입력하세요: '))    # int(정수)로 받음.
except:
    print('입력이 정확하지 않습니다.')       # 정수가 아닐 경우.
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')

# 예외 처리를 하기 위해 예외를 일부러 만듬.
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()  # 오류 일부러 발생시키기
    print(nick)

say_nick("천재")
# say_nick("바보")

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명"
try:
    say_nick("천재")
    say_nick("바보")
except MyError as e:
    print(e)



# 내장 함수
divmod(4,2) # 몫과 나머지

for i, name in enumerate(['aabc', 'dfg', 'qwer']):
    print(i, name)
