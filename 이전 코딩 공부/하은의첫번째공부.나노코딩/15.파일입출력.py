#파일 생성
score_file = open("score.txt", "w", encoding="utf8") #w:write 쓰기 위한 목적
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()
#txt파일 생성 완료!

score_file = open("score.txt", "a", encoding="utf8") #a: append 이어쓰기
score_file.write("과학 : 85")
score_file.write("\n코딩 : 100")
score_file.close()

#파일 읽어오기
score_file = open("score.txt", "r", encoding="utf8") #r:read 읽기위한 목적
print(score_file.read()) #모든 내용 읽기
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") #r:read 읽기위한 목적
print(score_file.readline(), end="") #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동 
print(score_file.readline())         #end="":줄바꿈 안하기
print(score_file.readline())
print(score_file.readline())
score_file.close()

#몇줄인지 모를때 한줄씩 파일 읽기
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line: #해당 줄에 내용이 없을 때
        break
    print(line)
score_file.close()

#list에 값을 다 넣어서 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() #모든 line을 가져와서 list 형태로 저장
for line in lines: #list에서 한 줄 씩 불러와서 출력
    print(line, end="")
score_file.close()
