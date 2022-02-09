#1
평균점수 = (80 + 75 + 55)/3
print(평균점수)

#2
1 % 2
print(13%2)

#3 슬라이싱
pin = '881120-1068234'
print(pin[0:6])
print(pin[7:])

#4
print(pin[7])

#5
a = "a:b:c:d"
print(a.replace(':','#'))

#6
a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7 ★★
a = ['Life','is','too','short']
result =" ".join(a)
print(result)     #print(type(result))

#8 ★★
a = (1,2,3)
a = a + (4,) # 1개 요소 튜플은 컴마 붙여야됨.
print(a)

#9
a = dict()
print(a)
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'
a[250] = 'python'
#오류발생 이유: dictionary의 key로 변하는 값을 사용할 수 없기 때문.
# [1]은 리스트이므로 변할 수 있는 값.

#10
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B')) #출력 후 B는 삭제.

#11
a = [1,1,1,2,2,3,3,3,4,4,5]
a = set(a)
a = list(a)
print(a)

#12
a = b = [1,2,3]
a[1] = 4
print(b)
# a가 수정되면 b도 수정된다. 이유: b에게 a의 주소값을 입력했기 때문. 
# a의 값만 띡 복사X. 

odd = [1,2,36,2,6]
print(odd.sort(reverse=1))

#복사 배우기~

#1)
a = [1,2,3]
b = a[:]

# 2) 
from copy import copy
b = copy(a)
