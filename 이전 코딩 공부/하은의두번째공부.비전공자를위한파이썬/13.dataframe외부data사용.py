# df -> excel or csv

import pandas as pd
# data_list = {'날짜' : ['2015-12-28','2016-11-03','2016-12-08','2017-01-05'],\
#     '지역' : ['인천','서울','청주','제주'],\
#         '시작시간' : ['10:00','15:00','19:00','16:00'],\
#             '종료시간' : ['14:00','16:00','21:00','20:00']}

# df = pd.DataFrame(data_list)
# print(df)

# # df.to_excel('From the first to the end.xlsx','sheet1')


# txt_data = {'멤버' : ['연준','수빈','범규','태현','휴닝'],\
#     '포지션' : ['oldest','leader','visual','vocal','cutest'],
#     'age' : ['23','22','21','20','20']}


# txt_df = pd.DataFrame(txt_data)
# # print(txt_df)

# # txt_df.to_excel('투바투 간단 정보.xlsx','sheet1')

# txt_csv = txt_df.to_csv('투바투 정보를 csv로!.csv', encoding='euc-kr')
# # encoding = 'euc-kr'로 해야 안깨진다


# excel or csv -> df

read_xlsxfile = pd.read_excel('투바투 간단 정보.xlsx', index_col='Unnamed: 0')
print(read_xlsxfile)

read_csvfile = pd.read_csv('투바투 정보를 csv로!.csv', encoding = 'euc-kr', index_col='Unnamed: 0')
print(read_csvfile)





