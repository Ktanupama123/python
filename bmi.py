h=float(input("enter the height in meter:"))
w=int(input("enter the weight:"))
def bmi(h,w):
    bmi=w/(h*h)
    return bmi
data=(bmi(h,w))
print(data)

