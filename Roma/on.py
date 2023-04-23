import turtle


window = turtle.Screen()
window.bgcolor('yellow')

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(5)
border.up()



ball = turtle.Turtle(shape='circle')
ball.up()
ball.y = 0

while True:
    ball.y = ball.y - 0.1
    ball.goto(0, ball.ycor()+ball.y)

    if ball.ycor() <= -400:
        ball.y = -ball.y 




