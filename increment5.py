#Mr Gide's account in GTB has an initial balance of 1000, 
#Management have decided to add 2 naira to Mr. Gide's account
#Until Gide's account is less than 1000,000 
#print out result

naira_string=chr(8358)
i=1000
while i < 100000:
        i += 2
        print(i)
        if i == 100000:
           print("Mr Jide's account is now" ,naira_string, i)