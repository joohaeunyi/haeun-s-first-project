#내장함수: 내장(기본 탑재)되어있어서 따로 import 필요없이 바로 사용 가능한 함수
#ex)
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# # print("{0}은 아주 좋은 언어입니다!".format(language))

# # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# # print(dir())
# import random # 외장 함수
# # print(dir()) # random이 추가되었다.
# # import pickle
# # print(dir())

# print(dir(random))
# lst = [1,2,3]
# print(dir(lst)) #현재 lst라는 리스트에 사용할 수 있는 함수들이 나옴.

name = "Haeun"
print(dir(name))


#list of python builtins <- 내장함수 dictionary같은 웹페이지.