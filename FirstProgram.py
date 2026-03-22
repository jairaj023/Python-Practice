# print("Hello World")
# print("Jairaj Choudhary")
# i=8

# if i<10:
#     print("won")

# else:
#     print("loose")

# # i=8

# if 12<10:
#     print("won")

# else:
#     print("loose")

# a = int(input("Enter Any Number:"))

# if a%2==0:
#     print("Even")

# else:
#     print("Odd")

# a=int(input("enter 1st number"))
# b=int(input("enter 2nd number"))
# c=int(input("enter 3rd number"))

# if a>=b and a>=c:
#     print(a," is greatest")
# elif b>=c:
#     print(b," is greatest")
# else:
#     print(c," is greatest")

# i = int(input("Enter Any Number :"))

# while i<=10:
#     print(i)
#     i = i+1

# for i in range(1,11):
#     print(i)

#print table of 18

# n = int(input("Enter Any Number:"))

# for i in range(1, 11):
#     print(n*i)

# for i in range(1,20):
#     if i<10:
#         continue
#     else:
#         print(i,end=", ")

# def samyak(a):
#     return a + 69

# b = samyak(10)
# print("b = ", b)

# def greatest(a,b,c):
#     if a > b and a > c:
#         print(a, "is greatest among this three numbers;")

#     elif b > c:
#         print(b, "is greatest among this three numbers;")
    
#     else:
#         print(c, "is greatest among this three numbers;")

# a = int(input("Enter 1st value : "))
# b = int(input("Enter 2nd value : "))
# c = int(input("Enter 3rd value : "))

# greatest(a,b,c)

# Tupple
# a = (10,20,30,40,50)

# print(a.index(10))
# print(sum(a))
# print(a.count(30))
# print(min(a))
# print(max(a))

#Set

# a = {10,20,30,20,50,40}

# print(a)
# print(sum(a))
# print(min(a))
# print(max(a))

# Dictionary
# a={10,20,30,40,50}
# b={10,15,20,25,30}

# print(a.union(b))
# print(a.intersection(b))

#abolute -ve value canges to +ve value
# print(abs(-10))

#sqrt 
# import math

# print(math.sqrt(25))

# import random

# print(random.random())

#Lottery System

# import random

# a = int(input("Enter Your Lottery Number : "))
# b = random.randrange(1,6)

# print("My Lottery Number is : ", a)
# print("Lottery Number is : ", b)

# if a==b:
#     print("You Won The Lottery!")
# else:
#     print("Better Luck Next Time!")

#File Handling

# import os

# # # os.mkdir("D:/samyak/xyz.txt")
# # open("D:/samyak/xyz.txt")

# file=open("D:/samyak.txt","r")  #a means append mode

# # text=", we are learning file handling in python"

# file.read()

# file.close()

# a = int(input("Enter an Integer Number : "))

# try:
#     user_input = input("Enter Integer Number : ")
#     number = input(user_input)
#     print("integer entered : number")

# except:
#     print("u have wrong integer which is string")

# finally:
#     print("code Running...")

# a = int(input("Enter 1st Number : "))
# b = int(input("Enter 2nd Number : "))

# try:
#     c = a/b
# except:
#     print("You Had Taken Wrong Input Which is 0")
# else:
#     print("Division : ", c)
# finally:
#     print("Code Running...")

# Date Time
# import datetime

# date = datetime.datetime.now()

# print(date.strftime("%A %d-%b-%Y %H:%M:%S %p"))

# from turtle import *
# import turtle

# speed(1)

# forward(200)
# setheading(90)
# forward(200)
# penup()
# setheading(180)
# forward(200)
# pendown()
# setheading(270)
# forward(200)
# done()

# from turtle import *
# import turtle

# speed(0)

# for i in range(1,40):
#     circle(100)
#     left(10)


# done()

# from turtle import *
# import turtle

# speed(9)
# color('black','silver')
# begin_fill()
# circle(50)
# end_fill()
# left(180)
# color('black','silver')
# begin_fill()
# circle(100)
# end_fill()
# right(90)
# penup()
# left(90)
# forward(70)
# right(90)
# forward(60)
# right(90)
# forward(50)
# pendown()
# color('black','black')
# begin_fill()
# circle(10)
# end_fill()
# penup()
# left(360)
# forward(40)
# pendown()
# color('black','black')
# begin_fill()
# circle(10)
# end_fill()
# penup()
# left(90)
# forward(10)
# color('black','lightblue')
# begin_fill()
# circle(5)
# end_fill()
# penup()
# left(90)
# forward(40)
# pendown()
# color('black','lightblue')
# begin_fill()
# circle(5)
# end_fill()

# done()

# program for snow man

# from turtle import *
# import turtle

# color('black','red')
# begin_fill()
# left(180)
# circle(100)
# end_fill()

# right(180)
# circle(50)
# penup()
# left(90)
# forward(70)
# left(90)
# forward(20)
# pendown()
# circle(10)
# penup()
# right(180)
# forward(40)
# right(90)
# forward(10)
# pendown()
# right(10)
# circle(10)
# done()

# import numpy as np

# a=np.array([10,20,30,40,50])

# print(a)

# import numpy as np

# a=np.arange(5)

# print(a)

# import numpy as np

# a=np.r_[10:20,30,40]

# print(a)

# import numpy as np

# x = np.arange(5)
# x = x**2

# print(x)

# import numpy as np

# x = np.arange(5)
# x = x**3

# print(x)

# import numpy as np

# x=np.array([[4,8],[7,6]])

# print(x)
# print(x.sum())

# import numpy as np

# x=np.array([[4,8],[7,6]])
# y=np.array([[6,8],[2,3]])

# print(x-y)

# import numpy as np

# x=np.array([[4,8],[7,6]])
# y=np.array([[6,8],[2,3]])

# print(np.dot(x,y))

# import numpy as np

# x=np.array([[4,8],[7,6]])
# y=np.array([[6,8],[2,3]])

# print(x,y.T)

# import numpy as np

# x=np.zeros((2,2))
# y=np.zeros((2,2))

# print(x,y)

# import numpy as np

# x=np.eye((2))
# y=np.eye((2))

# print(x,y)

# Class And Object

# class abc:

#     def input(self):
#         self.i=int(input("Enter 1st Number : "))
#         self.j=int(input("Enter 2nd Number : "))

#     def display(self):
#         print("sum = ", self.i+self.j)

# a=abc()
# a.input()
# a.display()

class abc:

    def input(self):
        self.name=input("Enter name:")
        self.rollno=input("Enter Rollno.")
        self.Totalmarks=input("Enter totalmarks")

    def display(self):
        print("Name = ", self.name)
        print("Roll No. = ", self.rollno)
        print("Total Marks = ", self.Totalmarks)

a=abc()
a.input()
a.display()