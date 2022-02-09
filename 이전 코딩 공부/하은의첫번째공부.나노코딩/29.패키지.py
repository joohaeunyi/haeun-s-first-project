#클래스 : 모듈을 모아놓은 집합
#신규 여행사 프로젝트를 담당.
#태국, 베트남에 패키지 여행 상품을 제공.
# 이 패키지 내용을 만들어 누구나 사용할 수 있기로 하자

# import travel.thailand  #점 뒤에는 모듈, 패키지만 가능. 클래스, 함수는 불가능.
# # import travel.thailand.ThailandPackage()    <- 이렇게 쓰면 안된단 말임.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()  
from travel import *
import inspect #현재 파일 위치
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))