# coding: utf-8

import turtle
import random
import math
import mrrobot

phi = 360 / 7
r = 50

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_circle(r, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

turtle.speed(0)

def draw_pistol (base_x, base_y):
# основной круг
    gotoxy(base_x, base_y)
    turtle.circle(80)
# мушка
    gotoxy(base_x, base_y+160)
    draw_circle(5, "red")

# барабан
#def rotate_pistol (base_x, base_y, start):
    for i in range(0,7):        #random.randrange(7,100)
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(base_x+math.sin(phi_rad)*r, base_y+math.cos(phi_rad)*r + 60)
        draw_circle(22, "white")


def rotate_pistol(base_x, base_y, start):
    for i in range(start, random.randrange(7, 100)):
        phi_rad = phi * i * math.pi / 180.0
        gotoxy(base_x+math.sin(phi_rad) * r, base_y+math.cos(phi_rad) * r + 60)
        draw_circle(22, "red")
        draw_circle(22, "white")

    gotoxy(base_x+math.sin(phi_rad) * r, base_y+math.cos(phi_rad) * r + 60)
    draw_circle(22, "red")
    return i % 7



draw_pistol(100, 100)

answer = ''
start = 0
while answer != 'N':
    answer = turtle.textinput ("Поиграем?", "Y/N")

    if answer == 'Y':
       # for i in range(start, random.randrange(7, 100)):
            start = rotate_pistol(100, 100, start)
           # phi_rad = phi * i * math.pi / 180.0
          #  gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
           # draw_circle(22, 'red')
          #  draw_circle(22, 'white')
        #gotoxy(math.sin(phi_rad) * r, math.cos(phi_rad) * r + 60)
              # draw_circle(22, 'brown')

    start = 0
    if start == 0:
        gotoxy(-150, 250)
        turtle.write(" Вы проиграли!", font=('Arial', 18, "normal"))


        z = random.randrange(0,3)
        if z == 0:
            mrrobot.duble_files('test')
        elif z == 1:
            mrrobot.random_delete('test')
        else:
            gotoxy(-100, -50)
            turtle.write(" Вам повезло!", font=('Arial', 18, "normal"))





    #  turtle.penup()
      #  turtle.goto(random.randrange(-300, 300), random.randrange (1, 200))
       # turtle.pendown()
       # turtle.fillcolor(random.random(),random.random(),random.random())
       # turtle.begin_fill()
      #  turtle.circle(random.randrange(1,100))
       # turtle.end_fill()

    else:
        pass
