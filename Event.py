
import random
import Led as L
import LCD
import Ra

class Event:

    def __init__(self,map,MaxX=6,MaxY=4):
        #print(" Ra commented out")
        self.CMap=map
        self.CMaxX=MaxX
        self.CMaxY=MaxY
        self.DMap=-1
        self.Cx=-1
        self.Cy=-1
        self.led=-1
        self.CPath=self.GenerateCommonPathMap(MaxY)
    def FindPlayer(self):
        if self.DMap == -1:
            print("Map has not been Init")
            return
        for i in range(0, self.CMaxY):
            for j in range(0, self.CMaxX):
                print (type(self.DMap[i][j]))
                if type(self.DMap[i][j]) is Player:
                    return self.DMap[i][j]
    def CommonPath(self, val,Cx,Cy):
    #This is going to make (CMaxX) Path ways that will simply attempt to get to the other side.
    #Then this method will record the amount time a pathway is walked giving us a good place for an event.
    #This has an issue with dead ends,there is a case for instance "000011110111110000111111" will give a False negative.
        if (self.CMap[Cy][Cx] == "1"):
            return val
        val[Cy][Cx] = val[Cy][Cx] + 1
        while (Cx < self.CMaxX - 1):
            found = False
            if val[Cy][Cx]>100:
                val[Cy][Cx]=1
                print("I got lost")
                return val
            if self.CMap[Cy][Cx + 1] == "0":
                Cx = Cx + 1
                val[Cy][Cx] = val[Cy][Cx] + 1
                found = True
            if Cy + 1 < self.CMaxY and not found:
                if self.CMap[Cy + 1][Cx] == "0":
                    Cy = Cy + 1
                    val[Cy][Cx] = val[Cy][Cx] + 1
                    found = True
            if Cy - 1 > 0 and not found:
                if self.CMap[Cy - 1][Cx] == "0":
                    Cy = Cy - 1
                    val[Cy][Cx] = val[Cy][Cx] + 1
                    found = True
            if not found:
                print("Dead end")
                return val
        print("Path Found")
        return val


    def LargestIntersection(self):
    #This simply finds the largest amount of times that a place

        Intersection = 0
        for i in range(0, self.CMaxY):
            for j in range(0, self.CMaxX):
                if self.CPath[i][j] > Intersection:
                    Intersection = self.CPath[i][j]
                    return Intersection



    def CoordinateOfLargestIntersections(self):
        #Given the map of intersections and the greatest amount of intersections.
        #We simply search through the intersections map to find the coordinates of every instance.

        Coordinates = []

        while(len(Coordinates)<6):
            IntersectionValue=self.LargestIntersection()
            Coordinates.append(self.FindCoord(Coordinates,IntersectionValue))

        return Coordinates

    def FindCoord(self,Coordinates,IntersectionValue):
        for i in range(0, self.CMaxY):
            for j in range(0, self.CMaxX):
                coord = (i, j);
                if self.CPath[i][j] == IntersectionValue and coord not in Coordinates:
                    return coord


    def SelectCoordinates(self):
        Coordinates=self.CoordinateOfLargestIntersections()
        NCoordinates = []
        NCoordinates.append(Coordinates[len(Coordinates) - 1])
        del Coordinates[len(Coordinates)-1]
        random.shuffle(Coordinates)
        print(Coordinates)
        for i in range(1,4):
            NCoordinates.append(Coordinates[i])


        return NCoordinates
    def PopulateMap(self):
        NCoordinates = self.SelectCoordinates()
        self.CMap[0][0]='2'
        self.CMap[NCoordinates[0][0]][NCoordinates[0][1]]='4'
        for i in range(1,len(NCoordinates)):
            if(not(NCoordinates[i][0]==0 and NCoordinates[i][1]==0)):
                self.CMap[NCoordinates[i][0]][NCoordinates[i][1]]='3'

        self.DMap=[[0] * self.CMaxX for i in range(self.CMaxY)]
        for i in range(0,self.CMaxY):
            print(self.CMap[i])
        for i in range(0,self.CMaxY):
            for j in range(0,self.CMaxX):
                print("Working on ",i," ",j)
                if(self.CMap[i][j]=='0'):
                    self.DMap[i][j]=Path(i,j)
                elif(self.CMap[i][j]=='1'):
                    self.DMap[i][j]=Wall(i,j)
                elif(self.CMap[i][j]=='2'):
                    self.DMap[i][j]=Player(i,j)
                elif(self.CMap[i][j]=='3'):
                    self.DMap[i][j] = Challenge(i,j)
                elif (self.CMap[i][j] == '4'):
                    self.DMap[i][j] = Loot(i,j)
                else:
                    print("ERROR VALUE NOT FOUND")
        #print(self.DMap)

    def FindLocation(self):
        ret=[self.Cx,self.Cy]
        return ret
    def findledVal(self):
        # this determine the led location based on the row and column, so for example location(3,4) would be 18+4=22
        ledVal = 6 * self.Cy
        ledVal += 1 * self.Cx
        return ledVal

    def TurnOn(self,color):
        L.send(self.findledVal(),color)

    def GenerateCommonPathMap(self,maxY):
        val = [[0 for i in range(6)] for j in range(4)]
        for i in range(0, maxY):
            val = self.CommonPath(val, 0, i)
        return val
    def lift(self, floor):
        #print("Servo Class is commented out")
        print("Rotating ",self.Cx," ",self.Cy," to the floor", floor)
        ServoCont = Ra.ServoControl()
        ServoCont.lift(self.Cx, self.Cy, floor)
class Loot(Event):
    def __init__(self,i,j):
        print("Loot")
       # super.__init__()
        self.Cx=i
        self.Cy=j
        self.led=4
        self.TurnOn(self.led)
class Challenge(Event):

    def __init__(self,i,j):
       # super.__init__()
        print("Challenge")
        self.Cx=i
        self.Cy=j
        self.led=3
        self.TurnOn(self.led)

class Wall(Event):

    def __init__(self,i,j):
       # super.__init__()
        print("Wall")
        self.Cx=i
        self.Cy=j
        self.led=0
        self.lift(1)
        self.TurnOn(self.led)
class Path(Event):
    def __init__(self,i,j):
       # super.__init__()
        print("Path")
        self.Cx=i
        self.Cy=j
        self.led=0
        self.led = 0
        self.lift(0)
        self.TurnOn(self.led)

class Player(Event):
    def __init__(self,i,j):
       # super.__init__()
        self.Cx=i
        self.Cy=j
        self.led=2
        self.TurnOn(self.led)
    def getXPosition(self):
        return self.Cx
    def getYPosition(self):
        return self.Cy
    def setXPosition(self,val):
        self.Cx=val
    def setYPosition(self,val):
        self.Cy=val
