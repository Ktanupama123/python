def add(x,y):
     sum=a+b
     return sum
def subtraction(x,y):
     diff=a-b
     return diff
def product(x,y):
     product=a*b
     return product
def division(x,y):
     div=a/b
     return div
for i in range(5):
    print("the operation are 1.addition\n2.subtraction\n3.multiplication\n4.division\n5.exit")
    operation=int(input("enter the number:"))
    if operation==1:
        a=float(input("enter anumber:"))
        b=float(input("enter a number:"))
        c=add(a,b)
        print(c)
    elif operation==2:
        a=float(input("enter anumber:"))
        b=float(input("enter a number:"))
        c=subtraction(a,b)
        print(a)
    elif operation==3:
        a=float(input("enter anumber:"))
        b=float(input("enter a number:"))
        c=product(a,b)
        print(c)
    elif operation==4:
        a=float(input("enter anumber:"))
        b=float(input("enter a number:"))
        if b!=0:
            c=division(a,b)
            print(c)
        else:
            print("division by zero is not possible")
    elif operation==5:
            print("Exit")
            break
    else:
        print("invalied choice")
