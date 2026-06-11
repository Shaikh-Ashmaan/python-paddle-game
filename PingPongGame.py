import turtle
import time
import random


sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
sc.tracer(0)

left_score = 0
right_score = 0


left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)



right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)



hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 2
hit_ball.dy = -2


score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Left Player: 0    Right Player: 0", align="center", font=("Courier", 20, "normal"))


def left_pad_up():
    y = left_pad.ycor()
    if y < 240:
        left_pad.sety(y + 20)


def left_pad_down():
    y = left_pad.ycor()
    if y > -240:
        left_pad.sety(y - 20)


def right_pad_up():
    y = right_pad.ycor()
    if y < 240:
        right_pad.sety(y + 20)


def right_pad_down():
    y = right_pad.ycor()
    if y > -240:
        right_pad.sety(y - 20)


def update_score():
    score_display.clear()
    score_display.write(
        f"Left Player: {left_score}    Right Player: {right_score}",
        align="center",
        font=("Courier", 20, "normal")
    )


def reset_ball():
    hit_ball.goto(0, 0)
    hit_ball.dx = random.choice([-2, 2])
    hit_ball.dy = random.choice([-2, 2])


reset_ball()


sc.listen()
sc.onkeypress(left_pad_up, "w")
sc.onkeypress(left_pad_down, "s")
sc.onkeypress(right_pad_up, "Up")
sc.onkeypress(right_pad_down, "Down")


while True:
    sc.update()
    time.sleep(0.01)

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    if hit_ball.ycor() > 290:
        hit_ball.sety(290)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -290:
        hit_ball.sety(-290)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 490:
        left_score += 1
        update_score()
        reset_ball()

    if hit_ball.xcor() < -490:
        right_score += 1
        update_score()
        reset_ball()

    if (
        hit_ball.dx > 0
        and 370 < hit_ball.xcor() < 390
        and right_pad.ycor() - 70 < hit_ball.ycor() < right_pad.ycor() + 70
    ):
        hit_ball.setx(370)
        hit_ball.dx *= -1

    if (
        hit_ball.dx < 0
        and -390 < hit_ball.xcor() < -370
        and left_pad.ycor() - 70 < hit_ball.ycor() < left_pad.ycor() + 70
    ):
        hit_ball.setx(-370)
        hit_ball.dx *= -1
