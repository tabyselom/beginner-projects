'''
Auteur = Abyselom Tibebe
Date = 31-10 2022

name = change calculater
it calculte our return and giv as how much we would return in all centes
'''
accualValue = float(input("How much it cost: "))
acsepteds = float(input("How much do you take: "))

total = -(accualValue-acsepteds)

birr = round(total)
cent = int((total % birr)*100)


fifth = round(total/0.05)
tenth = round(total/0.10)
fift = round(total/0.15)
twenyfive = round(total/0.25)
fifty = round(total/0.50)
birrs = total/1
print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print("The change is ",birr,".",cent,"\nIt will be ",birrs," birr \nIt will be",fifty ," :50 cents \nIt will be ",twenyfive," :25 cents \nIt will be ",fift," :15 cents \nIt will be ",tenth," :10 cents \nIt will be ",fifth," :5 cents")
print("\n''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")