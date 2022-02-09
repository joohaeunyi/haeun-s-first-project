# # 진수 변환


# print(" 16의 10진수 :",16)
# print(" 16의 2진수 :", bin(16))
# print(" 16의 8진수 :", oct(16))
# print(" 16의 16진수 :",hex(16))

# a = 8
# b = 3

# # 나머지 : %
# print(a % 3)

# # 제곱 : **
# print(3 ** 3)

# # 나누기의 몫 : //
# print(10 // 3)


# print(10 <= 8)

#문자열 붙이기
print("안녕,", "L!")
print("안녕,"+ "L!")

# maketrans : 문자 바꾸기
# str = "hello txt"
# print(str)
# rep_str = str.maketrans('et', 'op')
# print(str.translate(rep_str))

hi_hu = "bye HUENINGKAI?"
print(hi_hu)
hiL_low = hi_hu.lower()
print(hiL_low)
rep_hiL = hiL_low.maketrans("bh", "iw") #어디를 바꿀지 찾아주는 지표 만들기
tran_hiL = hiL_low.translate(rep_hiL)
print(tran_hiL)

# #split : 문자 자르기
# spl = hi_hu.split() #list
# print(spl)
# print(type(spl))
# print(len(hi_hu))
# print(len(hi_hu[4:]))
# print("hello" + "HUENINGKAI")

# #maketrans : 문자열 바꾸기 연습2
# hi_yeon = "hi, yeonjun?"
# rep_yeon = hi_yeon.maketrans("hn","nm") 
#                         #.maketrans:어디를 바꿀지 찾아주는 지표
# tran_yeon = hi_yeon.translate(rep_yeon) #.translate : 바꾸기
# print(tran_yeon)

# txt = "yeonjun subin beomgyu huening taeyeon"
# txt_split = txt.split()
# print(txt_split)
# txt_join = ", ".join(txt_split)
# print(txt_join)
# print(type(txt_join))
# print(txt.upper())

jam = "    잠이 안 오면 공부나 하자 !! ^^    "
print(jam)
print(type(jam))
print(len(jam))
print(jam.strip())
print(len(jam.strip()))
print(jam.lstrip())
print(len(jam.lstrip()))
print(jam.rstrip())
print(len(jam.rstrip()))
bts = ["jin", "suga", "rm", "j-hope","v"]
# bighits = join(txt, bts)
# join(tran_hiL, tran_yeon)

#zfill : 문자열을 맞추기 위해 왼쪽에 0을 채우기
print('34'.zfill(4))
print("잠이 안 오면 공부나 하자 !! ^^".zfill(28))

#문자열 찾기 : find, index
print(jam.find("잠"))
print(jam.index("잠"))

#없는 글자를 find에서는 -1, index에서는 에러가 뜬다
print(jam.find("존"))
# print(jam.index("존"))

#문자열 개수 새기 : count

ap = "pen pineapple applepen"
print(ap.count("apple"))
print(ap.count("e"))



