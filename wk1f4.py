"""
You are given the following numbers: 500,120,478,200 
write a python code that adds all these numbers together 
and print out the result. Check if the total is greater than 120
if yes , multiply this result by 5 and add 140 and print the final outcome. 
Else just subtract  450 from the initials total and print out outcomes.

"""

a=500
b=120
c=478
d=200
e=(a+b+c+d)
if e==120:
    f=(e*5)+140
    print("The result is:", f)
else:
    g=(e-450) 
    print("The result is:", g )