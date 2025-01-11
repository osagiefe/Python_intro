""""
mrs yinka monthly upkeep budget given by her husband  is #250,000
she  was meticulous enough to buy the following items 
4 tubers of yam@ #500 each, 
bought three stationeries@ #2000 each
pays debt of 45,000, 
pays shop deal of 25k monthly for three months due
Write python  code that determines how much she has left from the budget

"""

inibudget=250000
yam=(4*500)
stationeries=(3*2000)
debtpaid=45000
shopfees=(3*25000)
expenses=(yam + stationeries + shopfees + debtpaid)
balance=(inibudget - expenses)
print("Mrs. Yinka's balance is: ", balance)
