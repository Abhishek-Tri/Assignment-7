"""Write a python program to check whether a given string is a multiword string or single
word string using match case statement
"""

string=input("enter a string : ")
match string:
    case match if ' ' in string:
        print("multiword string")
    case match if ' ' not in string:
        print("single string")    


