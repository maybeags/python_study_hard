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

# for _ in range(3):
#     t.forward(100)
#     t.left(120)


screen.exitonclick()