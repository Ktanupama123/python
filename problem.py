a=int(input("enter anumber:"))
b=int(input("enter a number:"))
operation=int(input("enter the number:"))
if (operation==1):
    sum=a+b
    print("sum=",sum)
elif(operation==2):
    diff=a-b
    print("diff=",diff)
elif(operation==3):
        product=a*b
        print("product=",product)

elif(operation==4):
    if(b!=0):
        div=a/b
        print("div=",div)
    else:
        print("division is not possible")
else:
    print("invalied choice")
