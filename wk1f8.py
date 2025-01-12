"""
You are given the following 2.56.78.34.23,21
in a list. Write a python code that add all the numbers together as total.
Check if the total is greater than 50, if yes divide this result by 20
and add 19 and print final outcome 
Else just add 500 to the initials total and print out outcomes

"""


a=2
b=56
c=78
d=34
e=23
f=21
g=(a+b+c+d+e+f)
if g==50:
    h=(g/20)+19
    print("The result is:", h)
else:
    g=(g+500) 
    print("The result is:", g )