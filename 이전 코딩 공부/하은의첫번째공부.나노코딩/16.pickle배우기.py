#pickle: 프로그램에서 사용하고 있는 데이터를 파일형태로 저장.
#외부에 전달 가능

import pickle
# profile_file = open("profile.pickle", "wb")
# #wb:write binary. 피클을 쓰기 위해 항상 이 입력을 해야됨. 
# #pickle에서는 따로 encoding처리 필요x
# profile = {"이름":"최범규", "나이":21, "취미":["노래", "춤", "방탈출"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()
# #profile.pickle이라는 파일이 생김

profile_file = open("profile.pickle", "rb") #rb: read binary
profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불어오기
print(profile)
profile_file.close()