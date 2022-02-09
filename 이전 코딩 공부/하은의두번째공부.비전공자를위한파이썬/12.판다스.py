
import pandas as pd #pd는 별명 정해주는 것. 호출 할 때 pandas 대신 사용 가능
# mySeries = pd.Series([19000, 13000, 1000, 4000], index=["피자", "치킨", "콜라","맥주"])
# print("   <메뉴판>")
# print(mySeries)
# origin = pd.Series(["국내산","중국산","무설탕","only카스"], index=["김치","고추가루","콜라","맥주"])
# print("원산지 정보")
# print(origin)


# #series와 dictionary는 비슷하게 생겨서 변환이 가능하다.

# #series-> dictionary 변환하기
# dic_data = {"피자":19000,"치킨":18000,"콜라":1500,"맥주":4500}
# print(dic_data)
# seri_data = pd.Series(dic_data)
# print(seri_data)
# print(seri_data["피자"]) #19000

# list_data = ['bhc',"bbq","썬더치킨","페리카나"]
# list_series = (pd.Series(list_data, index=["뿌링클","황금올리브","기본프라이드","모름"]))
# print(list_series)
# print(list_series["모름"])
# #변환 즉시, 인덱스를 같이 부여할 수도 있는거야~


#12.4 dataframe
#txt데이터프레임 만들기
values = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]]
index = ["1행", '2행', '3행' ,'4행' ,'5행']
columns = ['A열', 'B열','C열']

df = pd.DataFrame(values, index = index, columns = columns)
print(df)

data = {'name': ['태현','수빈','연준','휴닝','범규'],\
    'age': [20,22,23,20,21],
    'position':['vocal','leader','dance','cute','vidual',]}

txt = pd.DataFrame(data)
print(txt)

#행과 열을 지정하면서 df만드는데 길이 다르면 NaN으로 처리된다.
txt2 = pd.DataFrame(data, columns = ['name','age','position','animal'],\
    index = ['No.1','No.2','No.3','No.4',"No.5"])
print(txt2)

#df 조회하기
print('처음 3명:',txt2.head(3))
print('마지막 2명:',txt2.tail(2))
#열 조회
print('첫 번째 방법:',txt2['name'])
print('두 번째 방법:', txt2.name)
#행 조회: 열 처럼 단순하지 않다!

# loc, lioc을 이용
# print(txt2['No.3']) #행을 이렇게 불러올 수 없다.
print(txt2.loc['No.2']) # 수빈의 정보
print(txt2.loc['No.4']) # 휴닝의 정보
print(txt2.loc['No.4',['name','age']]) #4번째 행 중, name, age 열의 데이터 추출

# iloc(가져올 행의 번호, 열 번호)
print(txt2.iloc[0]) # 첫번 째 행인 태현의 정보
print(txt2.iloc[-1]) # 마지막 행인 범규의 정보
print(txt2.iloc[0,2]) # 첫번 째 행의 태현의 정보 중, 세 번째 열인 position정보: vocal

# 일정 간격으로 행 추출
print(txt2.iloc[ : : 2]) # 모든 행에서 홀 수 행만 추출 (간격 = 2)
print(txt2.iloc[0:4:3]) #0부터 4행까지 중 3행마다 추출

# 행/열 추가, 삭제, 변경
txt2.animal = ['앵무새', '굼벵이', '사마귀', '도마뱀', '나비']
print(txt2)
# txt2.animal[2] ='도마뱀' 이렇게 변경하는 게 왜 안될까

# 추가
txt2['country'] = ['Kor','Kor','Kor','USA','kor'] # 열 추가
txt2.loc['No.6'] = ['설','마','있','나','?'] # 행 추가
print(txt2)

# 삭제
txt2 = txt2.drop('No.6') # 행 삭제
# 또는 txt2 = txt2.drop(['No.6'))
# 아마 디폴트가 axis = 0 이라서 행 삭제할 땐 굳이 axis 안 써도 될 듯.

# 행기준 : axis = 0
# 열기준 : axis = 1

txt2 = txt2.drop('country', axis = 1) # 열 삭제
# 또는 txt2 = txt2.drop(['country'], axis= 1)
print(txt2)

# # 변경
# txt2.loc['No.2','animal'] = '토끼'
# print(txt2)
