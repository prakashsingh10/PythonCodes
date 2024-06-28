#greater number 
n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
n3=int(input("enter the third number:"))


if n1>n2 and n1>n3:
    print(f"{n1} is greater number .")
elif n2>n1 and n2>n3:
    print(f"{n2} is greater number" ) 
elif n3>n1 and n3>n2 :
    print(f"{n3} is greater number  ") 
else:
    print(f"invalid")      
       