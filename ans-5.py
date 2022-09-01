"""Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number."""

n=int(input("enter a number : "))
if n%2==0:
    print("saurabh shukla")
elif n%2!=0 and n<0:
    print("prateek jain")    
elif n%2!=0 and n>0:
    print("aditya chaudhary")    
