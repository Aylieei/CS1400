#turtle의 other methods

import turtle
ms = turtle.Screen()
ms.bgcolor("lightgreen")
alex = turtle.Turtle()
alex.color("blue")
alex.shape("turtle") #거북이 모양 knob
alex.speed(10) #edit speed

print(list(range(5,60,2)))
alex.up() #펜 종이에서 떼고 움직이삼
for size in range(5,60,2):
    alex.stamp() #penup 이든 down이든 명령을받은 그순간 바로 거북이모양 남김
    alex.forward(size)
    alex.right(24)

#don't draw any lines, 그냥 아무것도 없는 상태에서 감
#alex.up() # = alex.penup()
#alex.forward(100)
#alex.down() # = alex.pendown()

#other methods
print(alex.heading()) #지금 바라보고있는 위치
print(alex.position()) #지금 있는 위치
alex.goto(30,50) #좌표로 순간이동 기본은 정중앙(0,0)
alex.begin_fill() #지금부터 그리는 도형 안을 색칠할 준비를 해
alex.end_fill() #도형 그리기 끝났으니까 색칠해 begin-end
alex.dot() # 점(동그라미) 찍음
alex.stamp() #도장 찍음

ms.exitonclick()