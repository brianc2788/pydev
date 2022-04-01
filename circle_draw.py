#!/usr/bin/env python3
'''
circle_draw.py
------------------------------
Trying out turtle graphics.
I've heard of educational programming
languages like Forth & Logos (for kids,
unlike Pascal; an educational programming
lang for adults), but this will be my first
personal experience with them.

I've put together a simple, little app that
creates a blank 'canvas' and draws circles
wherever the user clicks the mouse.

Can see the potential for games & guis;
but should probably just look into Tcl/
Tk, which is the gui engine that powers
the turtle module.

brianc2788@gmail.com
http://github.com/user5260/pyscripts
'''
import turtle,random

t1 = turtle.Turtle()

def drawCircle(x,y):
	cRadius = random.randint(15,100)	# Causes the circle to vary in size on each click; psuedo-randomly.
	t1.setpos(x,(y+cRadius))		# Add cRadius, so the circle's center is on mouse.
	t1.setheading(180)			# Sets the 'turtle' to turn 180 deg; faces left.
	t1.pendown()
	t1.begin_fill()
	t1.circle(cRadius)
	t1.end_fill()
	t1.penup()				# leave pen up.

def main():
	t1.color('red','black')
	t1.hideturtle()
	t1.penup()
	t1.speed(0)
	screen = t1.getscreen()
	screen.onclick(drawCircle)	# gives mouse x,y to fun[ction].
	turtle.mainloop()

if __name__ == '__main__':
	main()
