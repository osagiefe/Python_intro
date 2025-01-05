#You have been asked to multiply five numbers: 2,10,15,1,30 the result subtract 200
#check if the new result is equal to 300, then print result, and multiply result by 4
#else add 1000 to the result
a=2
b=10
c=15
d=1
e=30
f=(a+b+c+d+e)-200
print(f)

if f==300:
    g=f/4
    print(g)
else:
     g=f+1000
     print("The result is ", g)   