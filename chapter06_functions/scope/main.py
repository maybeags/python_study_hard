'''
Scope : 범위

지역 변수 : 함수 내부에 정의된 변수
전역 변수 : 함수 외부(main단계)에 정의된 변수
'''

# enemies = 1         # 전역 변수
#
# def increase_enemies():     # 함수 정의 시작
#     enemies = 2             # 같은 이름이긴 하지만 얘는 지역 변수에 해당
#     print(f"함수 내부의 적의 숫자는 {enemies}입니다.")
#
# increase_enemies()          # 함수 호출
# print(f"함수 외부의 적의 숫자는 {enemies}입니다.")

# 지역 변수 =/= 전역 변수 -> 그렇다보니까 변수명을 서로 다르게 짓는게 혼란을 피하는 방식

# 함수 정의
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# print(potion_strength)    # 오류 발생합니다.
# drink_potion()              # 함수 호출
# print(potion_strength)    # 오류가 발생
# 지역 변수가 선언되고, 이를 호출한다고 해서, 함수 내에 있는 변수가 전역에서(main에서)
# 참조하는 것은 불가능합니다.

'''
Global Scope
'''

# player_health = 10          # 전역 변수

# 함수 정의
# def game():
#     # 함수 내부에 함수 정의 -> jump 내에 turn_right 함수 사용했었습니다.
#     # 얘는 정의된 함수를 함수 내에서 호출했는데, 여기서는 함수 내에 정의를 새로 함.
#     # 자주 일어나지는 않습니다 -> 가독성 문제로
#     def drink_potion():
#         # player_health += 2    # 마찬가지로 전역에서 선언되고 초기화된 변수를
#                                 # 함수 내에서 조작하는 것은 불가능합니다.
#
#         # 근데 무조건 불가능하냐면 그건 아닙니다.
#         global player_health   # global을 선언하고,
#         player_health += 2      # 값을 바꿀 전역 변수 명을 쓰게 되면
#                                 # 함수 내에서 전역 변수의 값을 바꿀 수 있음.
#         #이상의 코드에서 생겨날 수 있는 잠재적인 문제점은 :
#         #   함수의 호출 횟수에 따라 전역 변수의 값이 바뀌기 때문에
#         #   전역 변수의 값을 정확히 알기 위해서는
#         #   함수의 호출 횟수를 알아야 한다는 점입니다.
#         #   이상을 이유로 함수가 전역 변수의 값을 바꾸는 이러한 코딩 방식은
#         #   선호되지 않습니다.
#     drink_potion()
# game()
# print(f"체력은 {player_health}입니다.")        # 전역변수 값을 확인

game_level = 3
def create_enemy():
    enemies = ["좀비", "스켈레톤", "에일리언"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()
'''
이상의 코드에서 생기는 문제점
1. game_level 이라는 전역변수를 create_enemy()라는 함수의 정의 부분에서 사용하고 있음에도 오류 발생하지 않음
2. 함수 정의 내부의 if절에서 new_enemy라는 변수를 선언 및 초기화 했음에도,
    if절 바깥에서(들여쓰기 참조) new_enemy를 참조했음에도 오류가 발생하지 않음.
    
    1.의 이유 : game_level이라는 전역변수의 값을 바꾸는게 아니라, 참조만 해서 True/False만 반환하기때문에
        오류 발생하지 않음.
    2.의 이유 : if / while / for와 같이 콜론을 기준으로 들여쓰기가 있는 모든 코드 블록들은
        지역 변수를 만드는 것으로 간주되지 않음 -> 지역 변수의 용어 정의에 주목할 필요가 있습니다.
        
    chapter07_collections 패키지 생성 -> main.py 생성
'''