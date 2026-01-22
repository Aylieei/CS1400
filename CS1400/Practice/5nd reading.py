import turtle # allows us to use the turtles library
wn = turtle.Screen()  # creates a graphics window
wn.bgcolor("black") # set background color

alex = turtle.Turtle() # create a turtle named alex, making new obj
alex.color("green") # turtle;s color
alex.pensize(3) # set the width of pen

alex.forward(150)
alex.left(90)
alex.forward(75)
#turtle은 처음에 right side를 보고있으므로!!!!
#오른쪽을 보고있는 상태에서 앞으로 150전진
#전진하고나서 90도 왼쪽을 바라봐
#그상태에서 앞으로 75 전진

wn.exitonclick() # wait for a user click on the canvas
# 다 완료해도 창을 바로 닫지말고, 사용자가 마우스클릭할때까지 기다려라.

for aColor in ['yellow','red','green']: #for loop는 list안에있는 아이템의 "개수" 만큼 반복.
    alex.forward(50)
    alex.left(90)
#따라서 이걸 실행해봤자 저 단어들과 연관된 색깔X, 아이템의 개수 (3개)만 반복됨 3번반복!

    alex.color(aColor) #<<< 이걸 넣는다면 노랑,빨강,그린 순으로 선에 색이 들어감

print(list(range(4))) # [0,1,2,3]
print(list(range(1,5))) # [1,2,3,4]
print(list(range(0, 19, 2))) #0부터 19 전 까지 2씩더해 [0,2,4,6,8,10,12,14,16,18]
