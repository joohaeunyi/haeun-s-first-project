#변경되지 않는 리스트. 리스트보다 더 빠르다.
#리스트처럼 데이터를 저장하지만 추가, 삭제 불가.

txt = ("연준", "휴닝") 
print(txt[1])
print(type(txt)) #tuple

# txt.add("태현") 튜플은 add 못씀.

# name = "연준"
# age = 23
# hobby = "DISCO"

(name, age, hobby) = ("최연준", 23 , "DISCO")
print(name, age, hobby)


###########
#set
###########

#중복x, 순서x
my_set = {1,2,3,3,3}
print(my_set)

txt = {"연준", "태현", "휴닝"}
bighits = set(["태현", "Suga", "V"])

#교집합 구하기
print(txt & bighits)          
print(txt.intersection(bighits))

#합집합
print(txt | bighits)
print(txt.union(bighits))

#차집합
print(txt - bighits)
print(txt.difference(bighits))

#값 추가
bighits.add("정국")
print(bighits)

#값 사제
bighits.remove("Suga")
