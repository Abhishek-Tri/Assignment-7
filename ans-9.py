"""" Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year"""
year=int(input("enter a year : "))
match year:
    case year if year%4==0 and year%100!=0:
        print("non century leap year")
    case year if year%400==0:    
        print("century leap year") 
    case year if year%400!=0 and year%100!=0:     
        print("non century non leap year")
    case year if year%400!=0:   
        print("century non leap year")    
