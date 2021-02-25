#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
# Script to demonstrate turtle graphics
import math
import turtle
bob = turtle.Turtle()
print(bob)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(135)
k = math.sqrt(100**2+100**2)
bob.fd(k)

bob.pu()
bob.rt(135-90)
bob.fd(200)

bob.pd()
for i in range(4):
    bob.fd(100)
    bob.rt(90)
turtle.mainloop()

