def add(x,y):
     sum=a+b
     print("sum=",sum)
def subtraction(x,y):
     diff=a-b
     print("diff=",diff)
def product(x,y):
     product=a*b
     print("product=",product)
def division(x,y):
     div=a/b
     print("div=",div)
for i in range(5):
    print("the operation are 1.addition\n2.subtraction\n3.multiplication\n4.division\n5.exit")
    operation=int(input("enter the number:"))
    if operation==1:
        a=float(input("enter anumber:"))
        b=float(input("enter a number:"))
        add(a,b)
    elif operation==2:
        a=float(input("enter anumber:"))
        b=float(input("enter a number:"))
        subtraction(a,b)
    elif operation==3:
        a=float(input("enter anumber:"))
        b=float(input("enter a number:"))
        product(a,b)
    elif operation==4:
        a=float(input("enter anumber:"))
        b=float(input("enter a number:"))
        if b!=0:
            division(a,b)
        else:
            print("division by zero is not possible")
    elif operation==5:
            print("Exit")
            break
    else:
        print("invalied choice")
