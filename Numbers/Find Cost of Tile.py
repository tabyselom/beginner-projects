'''
Auteur = Abyselom Tibebe
Date = 23-10 2022

name : Tile lengthe calculate and cost
'''

mesurmentOfTile=input("for meter 'm' ,for centimeter 'cm'")
mesurmentOfRoom=input("for meter 'm' ,for centimeter 'cm'")
gapBetweenTile=int(input("the gup b/n tiles: "))

if mesurmentOfTile == 'm' and mesurmentOfRoom == 'cm':
    length=int(input("the length of tile: ")) * 100
    width=int(input("the width of tile: ")) * 100

    areaTile=( length +gapBetweenTile) * (width+gapBetweenTile)
    
    lengthOfRoom=int(input("the length of the room: "))
    widtheOfTheRoom=int(input("the width of the room: "))

    areaOfRoom=lengthOfRoom * widtheOfTheRoom

    pice =areaOfRoom /areaTile
    pice=round(pice)
    cost = int(input("how much is the tiles: "))
    price = pice *cost
    print("you need ",pice," tiles \nit will cost ",price)
elif mesurmentOfTile == 'cm' and mesurmentOfRoom == 'm':
    length=int(input("the length of tile: "))
    width=int(input("the width of tile: ")) 

    areaTile=( length +gapBetweenTile) * (width+gapBetweenTile)
    
    lengthOfRoom=int(input("the length of the room: "))*100
    widtheOfTheRoom=int(input("the width of the room: "))*100

    areaOfRoom=lengthOfRoom * widtheOfTheRoom

    pice =areaOfRoom /areaTile
    pice=round(pice)
    cost = int(input("how much is the tiles: "))
    price = pice *cost
    print("you need ",pice," tiles \nit will cost ",price)
elif mesurmentOfTile == 'm' and mesurmentOfRoom == 'm':
    length=int(input("the length of tile: "))
    width=int(input("the width of tile: ")) 

    areaTile=( length +gapBetweenTile) * (width+gapBetweenTile)

    
    lengthOfRoom=int(input("the length of the room: "))
    widtheOfTheRoom=int(input("the width of the room: "))

    areaOfRoom=lengthOfRoom * widtheOfTheRoom

    pice =areaOfRoom /areaTile
    pice=round(pice)
    
    cost = int(input("how much is the tiles: "))
    price = pice * cost
    print("you need ",pice," tiles \nit will cost ",price)

elif mesurmentOfTile == 'cm' and mesurmentOfRoom == 'cm':
    length=int(input("the length of tile: "))
    width=int(input("the width of tile: ")) 

    areaTile=( length +gapBetweenTile) * (width+gapBetweenTile)

    
    lengthOfRoom=int(input("the length of the room: "))
    widtheOfTheRoom=int(input("the width of the room: "))

    areaOfRoom=lengthOfRoom * widtheOfTheRoom

    pice =areaOfRoom /areaTile
    pice=round(pice)
    cost = int(input("how much is the tiles: "))
    price = pice *cost
    print("you need ",pice," tiles \nit will cost ",price)

else:
    print("your input is not correct Try agin!!!")