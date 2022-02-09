#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
""" 
print(sentence3) #줄바꿈

#슬라이싱 #필요한 만큼만 잘라 추출

jumin = "980603-2037011"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0부터 2 직전까지 (0~1)
print("월 : " + jumin[2:4])
print("일 : " +jumin[4:6])

print("생년월일 : " + jumin[:6]) #처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) #7부터 끝까지
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) #맨 뒤에서 7번째부터 끝까지

#문자열 처리
python = "Python is Amazing"
print(python.lower()) #소문자
print(python.upper()) #대문자
print(python[0].isupper())
print(len(python)) #길이
print(python.replace("Python", "Java"))

index = python.index("n") #n이 몇번째에 위치해있는지
print(index)
index = python.index("n", index + 1) # 두번째 인자?(index + 1)는 start 위치. 한마디로 두번째로 n이 나오는 위치를 반환.
print(index)

print(python.find("n"))
print(python.find("Java")) #java라는 글자가 없으면 -1이 뜸. (오류 안 뜸)
#print(python.index("Java")) 없는 글자라 오류가 뜬다.

print(python.count("n")) #n이 총 몇번 나오나

#문자열 포맷
print("a" + "b")
print("a" + "b")

# 방법 1
print("나는 %d살입니다." % 24) #d는 정수형
print("나는 %s을 좋아해요." % "파이썬") # s는 문자열(string)형
print("Apple은 %c로 시작해요" %"A") #c:character(한 글자만 받음)

# %s를 쓰면 어떤 형식이든 상관없이 쓸 수 있다
print("나는 %s살입니다." % 24) #d는 정수형
print("나는 %s을 좋아해요." % "파이썬") # s는 문자열(string)형
print("Apple은 %s로 시작해요" %"A") #c:character(한 글자만 받음)

print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(24))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=24, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=24))

# 방법 4
age = 24
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") #f를 선언함

#탈출문자
print("백문이 불여일견!\n백견이 불여일타!")  #줄바꿈

#저는 "이주하은"입니다. 입력해보기 (큰따옴표 그대로 출력)
print('저는 "이주하은"입니다.')
print("저는 \"이주하은\"입니다.")

#\\ : 문장 내에서 \(하나의 역슬래쉬)
print("C:\\Users\\heana\\Desktop\\Python Workplace>")

#\r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #\r이 나오면 다시 처음으로 커서를 이동시켜서 그 다음 글자를 입력

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

#\t : 탭
print("Red\tApple")


#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# http://naver.com
# 규칙1 : httpL:// 부분은 제외 =>naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'의 갯수 + "!"로 구성
#                    (nav)          (5)          (1)               (!)
url = "http://naver.com"
url = "http://youtube.com"
url = "http://skku.com"
url_str = url.replace("http://","")  #규칙1
url_str = url_str[:url_str.index(".")] #처음부터 처음 점이 나오기 직전까지 출력 #규칙2
password = url_str[:3] + str(len(url_str)) + str(url_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(url, password))

