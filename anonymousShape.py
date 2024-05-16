from turtle import *
import random
from math import *


class shape:
    def __init__(self, color , area):
        self.color = color
        self.area = area
    def calculate(self , number):
        while True:
            firstNumber = random.randint(1,number)
            secondNumber = random.randint(1,number)
            if firstNumber * secondNumber == number:
                return firstNumber , secondNumber
    def square(self):
        fillcolor(self.color)
        begin_fill()
        for i in range(0,4):
            forward(sqrt(self.area))
            left(90)
        end_fill()
        input()
    def rectangle(self):
        dimensions = self.calculate(self.area)
        fillcolor(self.color)
        begin_fill()
        for i in range(0,2):
            for j in range(0,1):
                forward(dimensions[0])
                left(90)
            forward(dimensions[1])
            left(90)
        end_fill()
        input()  
    def pentagon(self):
        fillcolor(self.color)
        begin_fill()
        for i in range(0,5):
            forward(sqrt((4*self.area)/sqrt(5*(5+(2*sqrt(5))))))
            left(72)
        end_fill()
        input()
    def hexagon(self):
        fillcolor(self.color)
        begin_fill()
        for i in range(0,6):
            forward(sqrt((2*self.area)/(3*sqrt(3))))
            left(60)
        end_fill()
        input()       
    def heptagon(self):
        fillcolor(self.color)
        begin_fill()
        for i in range(0,7):
            forward(sqrt((4*self.area)/7*(cos(180/7)/sin(180/7))))
            left(360/7)
        end_fill()
        input()
    def octagon(self):
        fillcolor(self.color)
        begin_fill()
        for i in range(0,8):
            forward(sqrt(self.area / (2*(1+sqrt(2)))))
            left(360/8)
        end_fill()
        input()

    
shape("red" , 16000).square()