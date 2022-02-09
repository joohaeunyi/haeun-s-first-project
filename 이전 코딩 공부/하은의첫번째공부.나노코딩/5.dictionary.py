txt = {3:"연준", 100:"휴닝카이"}
#사전 사용할 땐 중괄호 {} 를 사용
#3번키는 연준이가 사용, 100번키는 휴닝이가 사용
print(txt[3])
print(txt.get(3))
#print(cabinet[5]) #값이 없는 걸 실행 -> 프로그램 종료 
#print(cabinet.get(5)) #값이 없는 걸 실행 -> None 뜨고 다음 문장을 실행

#값 없는 키 바로 뒤에서 값 지정 가능
print(txt.get(5, "태현")) 

#키 값이 있는지 확인
print(3 in txt)  #True
print(4 in txt)  #False

#문자형 키도 가능
cabinet = {"A-3":"연준", "B-100": "범규"}
print(["A-3"])


print(txt)

#새 손님
txt["A-3"] = "갑자기 김종국" #값 업데이트txtt["C-20"] = "수빈"
print(txt)

#값 지우기
del txt["A-3"]
print(txt)

#key만 출력
print(txt.keys())

#value만 출력
print(txt.values())

#키와 밸류 쌍으로 출력
print(txt.items())

# 목욕탕 폐점
txt.clear()
print(txt)