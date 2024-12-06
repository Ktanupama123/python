employee={'Antony':55000,'Susan':45000,'Kiran':60000}
a=dict(map(lambda x:(x[0],"high" if x[1]>50000 else"low" ),employee.items()))
print(a)