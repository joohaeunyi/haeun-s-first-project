#dictionary


haeun_dic = {"name" : "haeun", "age" : 24, "gender" : "female"}
print("하은이의 인적 정보 :", haeun_dic)

print(haeun_dic["name"])
print(haeun_dic["age"])

#키 값 조회하기
print("gender" in haeun_dic)
print("female" in haeun_dic) #키 값만 조회 가능하다

#키 개수 구하기
print(len(haeun_dic))
