#Write a python script to display the number of days in a given month number.
n=int(input("enter month in numeric format : "))
match n:
    case n if n in (1,3,5,7,8,10,12):
        print("31 days")
    case n if n in (4,6,9,11):
        print("30 days")
    case n if n==2:
        print("28 or 29 days")  
    case _:
        print("you entered wrong month number")               