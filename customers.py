# customers=['Rahul','Antony','Salman','Arun','Kiran']
# new=list(filter(lambda n:n[0]=='A',customers))
# print(new)


customers=['Rahul','Antony','Salman','Arun','Kiran']
a=list(filter(lambda n:n.startswith('A'),customers))
print(a)