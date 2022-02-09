import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

#열었던 파일에 대해 close()해줄 필요 없이 with문을 탈출하면서 자동으로 종료해줌.
#두 문장이면 충분! 수월, 간편.

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
    #study라는 파일 생성

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


#Quiz x주차 주간보고서 50회 만들기

#내가한 것! 성공.
# for i in range(1,51):
#     weekfile = open("{0}주차.txt".format(i), "w", encoding="utf8")
#     print("-{0}주차 주간보고-".format(i), file = weekfile)
#     print("부서 : ", file = weekfile)
#     print("이름 : ", file = weekfile)
#     print("업무 요약 : ", file = weekfile)
#     weekfile.close()

#나도코딩의 정답
for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("-{0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")