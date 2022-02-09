# 조건문
# if

x = 10
if x == 10:
    print("x = ", x)

#숫자 맞추기~
# ip = input("제가 무슨 숫자를 생각하고 있게요~? (1~10) :")
# ip_int = int(ip)
# if ip_int == 5 :
#     print("입력한 값은 제가 생각한 5가 맞습니다~")
# else:
#     print("제 마음을 읽지 못하셨군요!")


#에너지바 자판기 프로그램
store = input("구매하고 싶은 제품 번호를 입력해주세요 (a1,a2,a3) :")
if store == "a1":
    print("트윅스는 500원입니다")
    a1_notint = input("해당 금액을 넣어주세요")
    print(a1_notint + "원 입금받았습니다")
    money = int(a1_notint)
    if store == "a1" and money < 500:
        money_lack = 500-money
        money2_notint = input("금액이 {0}원 부족합니다.{0}원을 더 넣어주세요.".format(money_lack))
        money2 = int(money2_notint)
        if money2 == money_lack:
            print("금액을 정확하게 입력하셨네요! 상품을 드릴게요!")
            print("[트윅스]를 획득했다!")
        elif money2 <money_lack:
            print("흥! 당신같은 돈 없는 손님은 안받아요!")
            print("[거래가 종료되었습니다.]")
        elif money2 > money_lack:
            print("상품을 드리겠습니다!")
            print("거스름돈은 {0}원 입니다.".format(money2-money_lack))
            print("[트윅스]와 거스름돈을 획득했다!")  
        else:
            print("잘못된 값을 입력하셨습니다.")

    elif store == "a1" and money == 500:
        print("금액을 정확하게 입력하셨네요! 상품을 드릴게요!")
        print("[트윅스]를 획득했다!")
    elif store == "a1" and money > 500:
        print("상품을 드리겠습니다!")
        print("거스름돈은 {0}원 입니다.".format(money-500))
        print("[트윅스]와 거스름돈을 획득했다!")
    else:
        print("해당 상품은 재고가 없슴다 ㅠ0ㅠ 다음주에 재방문해주세요!")
        print("{0}원을 다시 돌려받았다!".format(money))
elif store == "a2":
    print("스니커즈는 600원입니다")
    a1_notint = input("해당 금액을 넣어주세요")
    print(a1_notint + "원 입금받았습니다")
    money = int(a1_notint)
    if store == "a2" and money < 600:
        money_lack = 600-money
        money2_notint = input("금액이 {0}원 부족합니다.{0}원을 더 넣어주세요.".format(money_lack))
        money2 = int(money2_notint)
        if money2 == money_lack:
            print("금액을 정확하게 입력하셨네요! 상품을 드릴게요!")
            print("[스니커즈]를 획득했다!")
        elif money2 <money_lack:
            print("흥! 당신같은 돈 없는 손님은 안받아요!")
            print("[거래가 종료되었습니다.]")
        elif money2 > money_lack:
            print("상품을 드리겠습니다!")
            print("거스름돈은 {0}원 입니다.".format(money2-money_lack))
            print("[스니커즈]와 거스름돈을 획득했다!")  
        else:
            print("잘못된 값을 입력하셨습니다.")

    elif store == "a2" and money == 600:
        print("금액을 정확하게 입력하셨네요! 상품을 드릴게요!")
        print("[스니커즈]를 획득했다!")
    elif store == "a2" and money > 600:
        print("상품을 드리겠습니다!")
        print("거스름돈은 {0}원 입니다.".format(money-600))
        print("[스니커즈]와 거스름돈을 획득했다!")
    else:
        print("해당 상품은 재고가 없슴다 ㅠ0ㅠ 다음주에 재방문해주세요!")
        print("{0}원을 다시 돌려받았다!".format(money))
elif store == "a3":
    print("자유시간은 300원입니다")
    a3_notint = input("해당 금액을 넣어주세요")
    print(a3_notint + "원 입금받았습니다")
    money = int(a3_notint)
    if store == "a3" and money < 300:
        money_lack = 300-money
        money2_notint = input("금액이 {0}원 부족합니다.{0}원을 더 넣어주세요.".format(money_lack))
        money2 = int(money2_notint)
        if money2 == money_lack:
            print("금액을 정확하게 입력하셨네요! 상품을 드릴게요!")
            print("[자유시간]을 획득했다!")
        elif money2 <money_lack:
            print("흥! 당신같은 돈 없는 손님은 안받아요!")
            print("[거래가 종료되었습니다.]")
        elif money2 > money_lack:
            print("상품을 드리겠습니다!")
            print("거스름돈은 {0}원 입니다.".format(money2-money_lack))
            print("[자유시간]와 거스름돈을 획득했다!")  
        else:
            print("잘못된 값을 입력하셨습니다.")

    elif store == "a3" and money == 300:
        print("금액을 정확하게 입력하셨네요! 상품을 드릴게요!")
        print("[자유시간]를 획득했다!")
    elif store == "a3" and money > 300:
        print("상품을 드리겠습니다!")
        print("거스름돈은 {0}원 입니다.".format(money-300))
        print("[자유시간]과 거스름돈을 획득했다!")
    else:
        print("잘못된 값을 입력하셨습니다.")
else:
    print("그런 상품 번호는 없습니다")


#유닛같은 걸 써보면 더 간단하게 작성할 수 있지 않을까?

    
