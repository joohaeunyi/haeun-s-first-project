#리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

환불원정대 = ['엄정화', '화사', '이효리', '제시']

# 화사는 몇번째?
print(환불원정대.index('화사'))

# 유재석 합류
환불원정대.append("유재석")
print(환불원정대)

#김종민을 엄정화, 화사 사이에 합류
환불원정대.insert(1, "김종민")
print(환불원정대)

# #한 명씩 하차
# print(환불원정대.pop())
# print(환불원정대)
# print(환불원정대.pop())
# print(환불원정대)
# print(환불원정대.pop())
# print(환불원정대)

#같은 이름의 사람이 몇 명 있는지 확인
환불원정대.append("유재석")
print(환불원정대)
print(환불원정대.count("유재석"))

num_list = [5,7,2,8,1]
num_list.sort()
print(num_list)

#순서 뒤집기도 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#e다양한 자료형 함께 사용
num_list = [1, 65, 3,9]
mix_list = ["화사", 20, True]
num_list.extend(mix_list)
print(num_list)
