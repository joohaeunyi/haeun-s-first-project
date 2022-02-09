weather = input("오늘 날씨는?")
if weather == "비" :          #콜론! 꼭 찍기
    print("우산을 챙기세요")
elif weather =="미세먼지":
    print("마스크를 챙기세요")
else :
    print("준비물 없는 날이에용 ^^")


temp = int(input("기온은 어때요?"))
if 30<= temp:
    print("너무 더워요. 나가지 마세요")
elif 10<=temp and temp<30:
    print("무난한 날씨~")
else : 
    print("추워 뒤지겠네")