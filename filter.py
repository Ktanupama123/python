from functools import reduce
num=[3,2,6,8,4,6,2,9]
oddnum=list(filter(lambda n :n%2!=0,num))
doubles=list(map(lambda n :n*2,oddnum))
sum=reduce(lambda a,b:a+b,oddnum)
print(oddnum)
print(doubles)
print(sum)