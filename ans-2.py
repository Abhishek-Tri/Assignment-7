"""Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""
n1=eval(input("enter 1st number : "))
n2=eval(input("enter second number : "))
print("1.Addition")
print("2.Subtraction")
print("3.Multiply")
print("4.Division")
m=int(input("now enter you choice : "))
match m:
    case 1:
        print("Addition: ",n1+n2)
    case 2:
        print("subtraction: ",n1-n2)
    case 3:
        print("multiply: ",n1*n2)
    case 4:
        print("division: ",n1/n2)
    case _:
        print("you entered wrong choice")
                        