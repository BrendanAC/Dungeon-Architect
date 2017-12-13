
from MapObject import Map
from Event import Event
from Game import Gam
import LCD
import sys


l=LCD.lcd()
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


        l.writeMessage("Creating the map", 1)
        l.writeMessage("Please Wait.", 2)

        InitMap.RandMap()
        DMap=Event(InitMap.map)

        DMap.PopulateMap()
        l.writeMessage("Map Complete", 1)
        l.writeMessage("                ", 2)
        Game=Gam(DMap)
        Game.start()


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
    main()