'''
Auteur = Abyselom Tibebe
Date = 23-10 2022

name = e rounding
helps to round e number to the decimal place we want
'''


# by importing mathe we can get the actual value of e
import math

e = math.e
#we take the lengthe of decimal that the e would have
theNumberOfDecimal=int(input("How many decimal place of e: "))
#the round take two argument 
#the frst the number we will round
#the secod the decimal it will be rouned to
ans =round(e,theNumberOfDecimal)

print(ans)
