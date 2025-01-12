"""
2.	Write python user input code that will ask for 
items bought in the market and add the prices
items are bread, yam,rice and stationeries
"""
print("What item did you purchase from the store")
bread=input()
print("How much did you spend on bread?")
bread=int(input())
print("What else did you buy?")
yam=input()
print("How much did you spend on yam?")
yam=int(input())
print("What else did you buy?")
rice=input()
print("How much did you spend on rice?")
rice=int(input())
print("Anything else?")
stationeries=input()
print("How much did you spend on stationeries?")
stationeries=int(input())
mspent=(bread + yam + rice + stationeries)
print("The total amount I spent at the store is: ", mspent)