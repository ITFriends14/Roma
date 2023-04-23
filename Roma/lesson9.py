import turtle


window = turtle.Screen()
window.bgcolor('yellow')

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pensize(5)
border.up()
border.goto(-250, 250)
border.down()
border.goto(-250, -250)
border.goto(250, -250)
border.goto(250, 250)



ball = turtle.Turtle(shape='circle')
ball.up()
ball.goto(0, 200)
ball.y = 0
ball.x = 2

gravitation = 0.1

while True:
    ball.y = ball.y -gravitation
    ball.goto(ball.xcor()+ball.x, ball.ycor()+ball.y)

    if ball.ycor() <= -245:
        ball.y = -ball.y 

    if ball.xcor() >= 245 or ball.xcor() <= -245:
        ball.x = -ball.x





