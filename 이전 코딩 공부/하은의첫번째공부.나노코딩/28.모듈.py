# 필요한 것들끼리 부품처럼 잘 만들어진 파일
# 자동차를 이용하다 타이어가 펑크나면 타이어만 교체하면 된다. 
# 소프트웨어도 부품만 교체, 추가할 수 있다. 코드의 재사용이 쉬워짐.
# 모듈 확장자: .py

# 예를들어 극장에서 현금만 받는다고 가정.
# 또 거스름돈을 안줌. 정확한 가격을 줘야되는 상황.


# 방법 1
# import theater_module

# theater_module.price(3) #3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) #4명이서 조조 영화 보러 갔을 때 가격
# theater_module.price_soldier(5) #군인 5명이 영화 보러 갔을 때 가격



# 방법 2. 별명 붙이기
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)



# # 방법 3.
# from theater_module import *
# # 앞에서 배운 from random import * 이랑 비슷하다!

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# # price_soldier(5) -> error뜸

from theater_module import price_soldier as price   #별명을 price로 붙인다
price(5)