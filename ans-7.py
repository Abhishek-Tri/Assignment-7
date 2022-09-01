"""Write a python program to check whether a given number is positive, negative or
zero using match case statement"""

n=int(input("enter a number : "))
match n:
    case n if n>0:
        print("positive")
    case n if n<0:
        print("negative")
    case _:
        print("zero")       

