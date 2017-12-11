<<<<<<< HEAD
from MapObject import Map
from Event import Event
import sys

def Menu():
    print("Enter 1 to create a Database (is required on intial load)")
    print("Enter 2 to generate a new Map")
    print("Enter 3 to Demo map")
    print("Enter 0 to exit program")

def gateKeeper(InitMap,user):
    if(user==str(0)):
        sys.exit()
    if (user==str(1)):
        InitMap.CreateDB()
        return
    if(user==str(2)):
        InitMap.RandMap()
        DMap=Event(InitMap.map)
        Coordinates=DMap.SelectCoordinates()
        DMap.PopulateMap(Coordinates)
        return
    if(user==str(3)):
        InitMap.test()
        return
    else:
        print("Invalid input please try again.")
        return

def main():
    print("Welcome to Map Generator v 1.0")
    InitMap=Map()
    user=-1
    while(user!=0):
        Menu()
        user=input()
        gateKeeper(InitMap,user)

if __name__ == "__main__":
=======
from MapObject import Map
from Event import Event
import sys

def Menu():
    print("Enter 1 to create a Database (is required on intial load)")
    print("Enter 2 to generate a new Map")
    print("Enter 3 to Demo map")
    print("Enter 0 to exit program")

def gateKeeper(InitMap,user):
    if(user==str(0)):
        sys.exit()
    if (user==str(1)):
        InitMap.CreateDB()
        return
    if(user==str(2)):
        InitMap.RandMap()
        DMap=Event(InitMap.map)
<<<<<<< HEAD
        val = [[0 for i in range(6)] for j in range(4)]
        for i in range(0, InitMap.ysize):
         val = DMap.CommonPath( val, 0, i)
        Coordinates = DMap.CoordinateOfLargestIntersections(val, DMap.LargestIntersection(val))
        Coordinates=DMap.SelectCoordinates(Coordinates)
        DMap.PopulateMap(Coordinates)

=======
        Coordinates=DMap.SelectCoordinates()
        DMap.PopulateMap(Coordinates)
>>>>>>> eef7671f2294886f504c85595229ddf183de448a
        return
    if(user==str(3)):
        InitMap.test()
        return
    else:
        print("Invalid input please try again.")
        return

def main():
    print("Welcome to Map Generator v 1.0")
    InitMap=Map()
    user=-1
    while(user!=0):
        Menu()
        user=input()
        gateKeeper(InitMap,user)

if __name__ == "__main__":
>>>>>>> eded338cecd39cfc9a4e4ad33cfb748f236ab37c
    main()