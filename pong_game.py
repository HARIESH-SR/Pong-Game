import turtle
#import pygame
import winsound
#pygame.init()
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

score_a =0
score_b =0


win = turtle.Screen()
win.setup(900,700)
win.bgcolor("blue")
win.title("Pong Game")
win.tracer(0)

pen1= turtle.Turtle()
pen1.hideturtle()
pen1.width(3)
pen1.color("light green")
pen1.left(90)
pen1.forward(350)
pen1.left(180)
pen1.forward(800)

pen0 = turtle.Turtle()
pen0.penup()
pen0.hideturtle()
pen0.setpos(-450,350)
pen0.pendown()
pen0.color("light green")
a=900
b=800
pen0.width(4)
for i in range(4):
    
    pen0.forward(a)
    pen0.right(90)
    
    pen0.forward(b+i)
    pen0.right(90)
    
    pen0.forward(a)
    pen0.right(90)
    
    pen0.forward(b+i+1)
    pen0.right(90)

    


left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("peru")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-436,0)


right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("peru")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(435,0)


ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.dx = 0.85
ball.dy = 0.85

pen = turtle.Turtle()
pen.speed(0)
pen.color("violet")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Player A:  0\t    \tPlayer B:  0",align="center",font=("Comic Sans MS",24,"normal"))


def left_paddle_up():
    if left_paddle.ycor()>290:
        return
    left_paddle.sety(left_paddle.ycor()+20)


def left_paddle_down():
    if left_paddle.ycor()<-290:
        return
    left_paddle.sety(left_paddle.ycor()-20)

def right_paddle_up():
    if right_paddle.ycor()>290:
        return
    right_paddle.sety(right_paddle.ycor()+20)

def right_paddle_down():
    if right_paddle.ycor()<-290:
        return
    right_paddle.sety(right_paddle.ycor()-20)

win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')
win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')

while True:
    win.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor()>335:
        ball.sety(335)
        winsound.PlaySound(resource_path("hit_ground.wav"),winsound.SND_ASYNC | winsound.SND_ALIAS)
        ball.dy *= -1

    if ball.xcor()>435:
        ball.setx(435)
        winsound.PlaySound(resource_path("hit_wall.wav"),winsound.SND_ASYNC | winsound.SND_ALIAS)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A:  {}\t    \tPlayer B:  {}".format(score_a,score_b),align="center",font=("Comic Sans MS",24,"normal"))

    if ball.ycor()<-335:
        ball.sety(-335)
        winsound.PlaySound(resource_path("hit_ground.wav"),winsound.SND_ASYNC | winsound.SND_ALIAS)
        ball.dy *= -1
        

    if ball.xcor()<-435:
        ball.setx(-435)
        winsound.PlaySound(resource_path("hit_wall.wav"),winsound.SND_ASYNC | winsound.SND_ALIAS)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A:  {}\t    \tPlayer B:  {}".format(score_a,score_b),align="center",font=("Comic Sans MS",24,"normal"))


    if ball.xcor()>420 and right_paddle.ycor()-50<ball.ycor()<right_paddle.ycor()+50:
        ball.setx(410)
        winsound.PlaySound(resource_path("bounce.wav"),winsound.SND_ASYNC | winsound.SND_ALIAS)
        #sound = pygame.mixer.Sound("E:/courses/python/Python-main/Pong/bounce.wav")
        #sound.play()

        ball.dx*=-1
        

    if ball.xcor()<-420 and left_paddle.ycor()-50<ball.ycor()<left_paddle.ycor()+50:
        ball.setx(-410)
        winsound.PlaySound(resource_path("bounce.wav"),winsound.SND_ASYNC | winsound.SND_ALIAS)
        #playsound("E:/courses/python/Python-main/Pong/bounce.wav")
        #sound = pygame.mixer.Sound("E:/courses/python/Python-main/Pong/bounce.wav")
        #sound.play()

        ball.dx*=-1
       

    if score_a == 5:
        pen.clear()
        pen1.clear()
        pen.goto(0,0)
        right_paddle.clear()
        left_paddle.clear()
        ball.clear
        winsound.PlaySound(resource_path("game_win.wav"),winsound.SND_ASYNC | winsound.SND_ALIAS)
        pen.write("Player A Wins",align="center",font=("Comic Sans MS",24,"bold"))
        break

    elif score_b == 5:
        pen.clear()
        pen1.clear()
        right_paddle.clear()
        left_paddle.clear()
        pen.goto(0,0)
        ball.clear
        winsound.PlaySound(resource_path("game_win.wav"),winsound.SND_ASYNC | winsound.SND_ALIAS)
        pen.write("Player B Wins",align="center",font=("Comic Sans MS",24,"bold"))
        break

win.exitonclick()
 

    
        
