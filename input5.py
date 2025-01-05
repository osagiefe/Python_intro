#python files to ask for input

print("whats is your name")
name=input("enter your name")
print("which market did you go to")
market=input("enter the market name")
print("what did you buy")
bread=input("enter what you bought")
print("enter brreasd amount")
amountbread=float(input("enter bread amount "))
print("what else did yiu buy")
fish=input("enter what you bought ")
print("enter fish ammount")
amoutfish=float(input("fish amount"))
total=amountbread + amoutfish
print("My purchase details are : " + name + " which market :" + market + ", what i bought: " + bread + "," + str(amountbread) + "," +fish + "," + str(amoutfish)+ ",The total: " + str(total))