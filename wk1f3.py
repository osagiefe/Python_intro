"""
You are given the following numbers: 50,40,60,70 
write a python code that adds all these numbers together 
and print out the result. Check if the total is equal  120  
if yes , divide this result by 5 and add 50 and print the final outcome. 
Else just add 300 to the initials total and print out outcomes

"""


a=50
b=40
c=60
d=70
e=(a+b+c+d)
if e==120:
    f=(e/5)+50
    print("The result is:", f)
else:
    e=(e+300) 
    print("The result is:", e )