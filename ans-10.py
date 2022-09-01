"""Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday"""

user=input("enter what colour you like : ")
match user:
    case user if 'yellow' in user:
        print("monday")
    case user if 'blue' in user: 
        print("tuesday")   
    case user if 'orange' in user: 
        print("wednesday")   
    case user if 'white' in user:  
        print("thursday")  
    case user if 'black' in user:
        print("friday")
    case user if 'red' in user:    
        print("saturday")
    case _:
        print("sunday")    

     
     

                                        

                
        
