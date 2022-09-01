"""Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit."""

x=eval(input("enter 1st number : "))
y=eval(input("enter 2nd number : "))
z=eval(input("enter 3rd number : "))
print("a. Check whether a given set of three numbers are lengths of an isosceles triangle or not")
print("b. Check whether a given set of three numbers are lengths of sides of a rightangled triangle or not")
print("c. Check whether a given set of three numbers are equilateral triangle or not")
print("d. exit")
m=(input("now enter your choice : "))
match m:
    case 'a':
        if x==y or y==z or x==z:
            print("it is isosceles tringle")
        else:
            print("its not isosceles tringle")    
    case 'b':
        if(x*x)+(y*y)==(z*z) or (x*x)+(z*z)==(y*y) or (y*y)+(z*z)==(x*x):
            print("it is right angle tringle")
        else:
            print("its not right angle tringle")    
    case 'c':
        if x==y==z: 
            print("it is equilateral tringle")  
        else:
            print("it is not equilateral tringle")         
    case 'd':
        exit
    case _:
        print("wrong choice")            