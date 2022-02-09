class JSS:
    def __init__(self):
        self.name = input("이름은? :")
        print("{0}이라는 이름을 생성!".format(self.name))
        self.age = input("나이는? :")
        
    def show(self):
        print("내 이름은 {0}, 나이는 {1}살!".format(self.name,self.age))

# a = JSS()   # self 가 a가 된 것이다.
# print(a.name)
# a.show()


class JSS2(JSS):
    def __init__(self):
        super().__init__()
        self.gender = input("성별은? :")
    def show(self):
        print("내 이름은 {0}, 나이는 {1}살! 그리고 {2}지."\
            .format(self.name,self.age, self.gender))


a = JSS2()
a.show()