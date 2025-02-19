from menu import Menu                # from 파일명(소문자 시작) import 클래스(대문자 시작)
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 외부 파일에서 import 해온 class들의 객체 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# 반복
is_on = True
while is_on:
    choice = input(f"어떤 음료를 드시겠습니까? {menu.get_items()} >>> ").lower()
    # todo - 1 : choice가 -> off / report / 오타났을 때 작성하는 부분을 완성하시오.
    if choice == "off":
        pass
    elif choice == "report":
        pass
