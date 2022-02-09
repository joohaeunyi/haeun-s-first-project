class SoldOutError(Exception): #Exception을 상속받음
    pass

class Notdigit(Exception):
    pass


chicken = 10
waiting = 1

while(True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken : #남은 치킨보다 많이 주문할때
            print("재료가 부족합니다.")
        elif order <= 0 :                
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting+= 1
            chicken -= order
    
        if chicken == 0:
            raise SoldOutError
         

    except ValueError :
        print("잘못된 값을 입력하였습니돠")
    except SoldOutError:
        print("재료가 소진되어 더 이상 주문을 받지 않습니다")
        break


#설명: 
#치킨 몇 마리 주문하시겠습니까? ->2.2같은 소수 입력하면 ValueError
#가 떠서 (int함수에서 에러 발생) 잘못된 값을 입력하였습니돠가 뜨게 되는 것이다.
