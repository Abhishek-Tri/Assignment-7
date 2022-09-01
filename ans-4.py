"""Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""

age=int(input("enter the age : "))
if age<10:
    print("kid")
elif age<20:
    print("teen")
elif age<40:
    print("young")
elif age<60:
    print("Experienced")
else:
    print("senior citizen")
                
