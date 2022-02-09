print("휴닝카이", "연준", "태현", "수빈")
print("범규", "휴닝카이", "연준", "태현", "수빈", sep=" or ", end = "? ")
print("당신의 최애는?")


scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    #ljust: 왼쪽 정렬, rjust: 오른쪽 정렬


#은행 대기순번표
#001, 002, 003, ... 
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))
    #zfill: 빈공간을 0(zero)로 채우기

print("---------------")

# answer = input("아무 값이나 입력 : ")
# print("입력하신 값은 " + answer + "입니다.")
# print(type(answer)) #입력값은 문자열(str)형태로 받아들임.

#다양한  출력 포맷
#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보.
#부호는 오른쪽 정렬을 의미.
print("{0: >10}".format(500)) 
#양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(-500)) 
print("{0: >+10}".format(500)) 
#왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
#3자리 마다 콤마를 찍기
print("{0:,}".format(1000000000000000))
#3자리 마다 콤마를 찍기, +- 부호도 붙이기
print("{0:+,}".format(1000000000000000))
print("{0:+,}".format(-1000000000000000))
#3자리 마다 콤마를 찍기, +- 부호도 붙이기, 자릿수 확보하기
#빈자리는 ^로 채우기
print("{0:^<+30,}".format(10000000000000))
#소수점
print("{0:f}".format(5/3))
#소수점 특정 자리까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))
