print("Simple Arithmetic calculator")
print("Operation To Perform")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
x=int(input("enter number 1:"))
y=int(input("enter number 2:"))
choice=input("Enter the operation(1/2/3/4):")
if (choice=='1'):
     print("The sum of x and y is:",x+y)
elif(choice=='2'):
    
    print("The difference of x and y is:",x-y) 
elif(choice=='3'):
    
    print("The multiple of x and y is :",x*y) 
elif(choice=='4'):
    
    print("The division of x and y is:",x/y)  
else:
    print("Invalid Operation")
