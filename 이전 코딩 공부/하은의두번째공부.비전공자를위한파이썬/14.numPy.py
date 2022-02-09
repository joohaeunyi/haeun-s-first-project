# # np는 다차원의 배열. 2차원차트가 아닌 정육면체!를 생각하자. 
import numpy as np

# # print(np.__version__) # 1.19.5


# list_data1 = [1,2,3,4,5]
# print(list_data1)

# list_data2 = [1,2.4, 3.3, 3, 5.2]
# print(list_data2)

# list_data3 = ([1,2,3],[4,5,6])  #2x3인 모양이 그려진다.
# print(list_data3)

# # 두 데이터의 NumPy array로 변환
# np_ar1 = np.array(list_data1)
# print(np_ar1.shape) # 축의 길이

# np_ar2 = np.array(list_data2)
# print(np_ar2.dtype) 


# np_ar3 = np.array(list_data3)
# print(np_ar3.shape) #2차원으로 저장됨.

# print(np.zeros(5))
# print(np.zeros((6,7)))
# print(np.zeros((3,4,2)))

# print(np.ones((5)))
# print(np.ones((6,7)))
# print(np.ones((3,4,2)))

# print(np.full((5)))
# print(np.zeros((6,7)))

# print(np.eye(6, k=-2)) # 단위 행렬. 오 첨 배워~ 언제 쓰는거지?
# print(np.arange(0,10,2)) # 0부터 10까지 2씩 증가 하면서 숫자 생성
# print(np.linspace(0,10,13)) # 0부터 10까지 일정한 간격으로 13개의 숫자 생성
# print(np.logspace(0,10,13))

# list1 = ([1,2,4],[2,6,89])
# ar1 = np.array(list1)
# list2 = ([1,5,7],[67,4,2])
# ar2 = np.array(list2)
# print(ar1.shape)
# print(ar1 + ar2) # 각 원소끼리 더해진다
# print(ar1 - ar2)
# print(ar1 * ar2)
# print(ar1 / ar2)

# 벡터는 더 빠르다. for를 이용할 때와 vector를 이용할 때의 시간
# import time
# startTime = time.time()
# test = np.arange(100000)

# print(test)
# result = 0

# for v in test:
#     result += v

# endTime = time.time() - startTime
# print(endTime) 

# test = np.arange(100000)
# result = 0
# start_time = time.time()

# for v in test:
#     result += v
# end_time = time.time()
# print("WorkingTime: {0}".format(end_time - start_time))

# start_time = time.time()
# result = np.sum(test)
# end_time = time.time()
# print("WorkingTime: {0}".format(end_time - start_time))

# test = np.arange(20)
# print(test)

#14.7 배열 불리언 인덱싱

# 배열 생성
arr = np.arange(1,13)
print(arr)

# 24개의 1차원 배열을 보기 쉽게 2차원으로 전환
# reshape(행, 열) 함수를 이요해서 3행 4열의 2차원 행렬 생성
reshaped = arr.reshape(3,4)
print(reshaped)
print(type(reshaped))

# 짝수만 True로 마스킹
even_arr = (reshaped%2 == 0)
print(even_arr)

# even_arr와 reshaped 배열 연산을 통해 True인 원소만 추출
masked = reshaped[even_arr]
print(masked)

print(np.sum(masked))

# 5 미만 값 마스킹
print(arr < 5)
less5 = reshaped < 5
print(less5)
masked = reshaped[less5]
print(masked)

print(np.sum(masked))
