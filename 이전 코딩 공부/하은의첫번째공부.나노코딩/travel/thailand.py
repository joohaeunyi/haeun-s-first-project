class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else: #main이 아닌 경우
    print("Thailand 외부에서 모듈 호출")

#29.패키지 파일에서 위 구문을 가져다 쓸 때에는 
# else다음의 구문이 실행될 것이고, print("Thailand 외부에서 모듈 호출")

# 현재 thailand.py 파일에서 직접 이 내용을 실행할 때에는 
# if밑의 구문 6~9행이 실행된다.