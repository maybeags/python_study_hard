import random

'''
chapter12_turtle
main
'''
# turtle이라는 모듈을 사용할건데, Turtle, Screen 클래스를 import 할겁니다
from turtle import Turtle, Screen

t = Turtle()        # Turtle 클래스의 객체 생성, 이름은 t
screen = Screen()   # Screen 클래스의 객체 생성
t.shape("turtle")
t.color("white")
screen.bgcolor("black")
# t.penup()
# t.forward(100)
# t.pendown()
# t.forward(200)

# for _ in range(10):   # 그냥 반복을 10번 하는 거고 변수를 사용하지 않았기 때문에 _를 썼습니다(i나 n이 아니라)
#     t.penup()
#     t.forward(20)
#     t.pendown()
#     t.forward(20)

# t.left(90)
# t.forward(100)

# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# for _ in range(4):
#     t.forward(100)
#     t.left(90)
#
# for _ in range(3):
#     t.forward(100)
#     t.left(120)

# for _ in range(10):
#     t.forward(5)
#     t.penup()
#     t.forward(5)
#     t.pendown()

# 해당 부분까지 다 하신 분들은
# 오각형, 육각형 ... 십각형까지 그려볼 수 있도록 하고
# 이후 코드를 축약할 방법에 대해서 고민하도록 하겠습니다

# dotted_line을 그리는 함수를 하나 정의할겁니다

def dotted_line():
    for _ in range(10):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()

# 삼각형도 그려볼까요
# for _ in range(3):
#     dotted_line()
#     t.left(120)
#
# # 이상의 함수를 사용하여 사각형을 그린다고 가정했을 때
#
# for _ in range(4):
#     dotted_line()
#     t.left(90)
#
# for _ in range(5):
#     dotted_line()
#     t.left(72)

def draw_figures(num):
    for _ in range(num):
        dotted_line()
        t.left(360 / num)

# 랜덤 객체를 생성
random = random.Random()

colors = [
    "dodger blue",
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
]

t.speed(10)
for i in range(3, 11, 1):
    t.color(random.choice(colors))
    draw_figures(i)













#
#
# for _ in range(3):
#     for _ in range(10):
#         t.forward(5)
#         t.penup()
#         t.forward(5)
#         t.pendown()
#     t.left(120)
#
# for _ in range(4):
#     for _ in range(10):
#         t.forward(5)
#         t.penup()
#         t.forward(5)
#         t.pendown()
#     t.left(90)


screen.exitonclick()