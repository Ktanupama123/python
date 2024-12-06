a=5
b=0

try:
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("you cannot divide a number by zero  ",e)
except ValueError as e:
    print("invalied input")
except Exception as e:
    print("something went wrong..")
finally:
    print("resource closed")
     