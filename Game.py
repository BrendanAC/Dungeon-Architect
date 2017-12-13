import RPi.GPIO as GPIO
import Led
import time
import LCD
GPIO.setmode(GPIO.BOARD)

GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)#up
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)#left
GPIO.setup(21,GPIO.IN, pull_up_down=GPIO.PUD_UP)#down
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)#right
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)#Accept
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)#Back
class Gam:

    def __init__(self,DMap):
        self.Player=DMap.FindPlayer()
        self.DMap=DMap
        self.l=LCD.lcd()
        self.acceptval=0


    def start(self):

        self.l.writeMessage("Confirm Map Y/N",1)
        for i in range(10,0):
            self.Player.lcdObject.writeMessage(i,2)
            time.sleep(1)

        #if self.acceptval == 1:
        self.MainGameLoop()

    # def accept(self):
    #     if GPIO.input(24):
    #        self.acceptval=10

    def updateMap(self):
        self.Player.TurnOn(2)

    def UserTest(self):
        useri = input('enter input')
        if useri == 'w':
            if (self.Player.Cy - 1 < 0):
                return
            else:
                if(self.DMap.CMap[self.Player.Cy-1][self.Player.Cx] =='1'):
                    return
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx] = '0'
                self.Player.Cy = self.Player.Cy - 1
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx]= '2'
        if useri == 'a':
            if self.Player.Cy - 1 < 0:
                return
            else:
                if (self.DMap.CMap[self.Player.Cy] [self.Player.Cx-1] == '1'):
                    return
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx] = '0'
                self.Player.Cx = self.Player.Cx - 1
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx]= '2'
        if useri == 's':
            if self.Player.Cy + 1 > 3:
                return
            else:
                if (self.DMap.CMap [self.Player.Cy+1][self.Player.Cx]== '1'):
                    return
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx] = '0'
                self.Player.Cy = self.Player.Cy + 1
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx] = '2'
        if useri == 'd':
            if self.Player.Cx + 1 > 5:
                return
            else:
                if (self.DMap.CMap[self.Player.Cy ][self.Player.Cx+1] == '1'):
                    return
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx]= '0'
                self.Player.Cx = self.Player.Cx + 1
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx]= '2'
    def EventNear(self):
        if (self.DMap.CMap[self.Player.Cx][self.Player.Cy-1] == 3):
            self.EventAlert('N')
        if (self.DMap.CMap[self.Player.Cx][self.Player.Cy+1] == 3):
            self.EventAlert('S')
        if (self.DMap.CMap[self.Player.Cx-1][self.Player.Cy]==3):
            self.EventAlert('W')
        if (self.DMap.CMap[self.Player.Cx+1][self.Player.Cy]==3):
            self.EventAlert('E')
        time.sleep(3)
        if(self.acceptval==1):
            #self.lightEvent()
            self.acceptval=0



    def EventAlert(self,coor):
        self.l.writeMessage("There is an",1)
        self.l.writeMessage("Event "+str(coor)+"Y/N",2)


    def MainGameLoop(self):
        while(self.Player.Cx!=5):
            self.updateMap()
            self.UserTest()
            self.EventNear()
            print(self.Player.Cx, " ",self.Player.Cy)
            for i in range(0,4):
                print(self.DMap.CMap[i])
        self.acceptval=0
    def up(self):
        if GPIO.input(7):
            if (self.Player.Cy - 1 < 0):
                return
            else:
                if (self.DMap.CMap[self.Player.Cy - 1][self.Player.Cx] == '1'):
                    return
                self.DMap.CMap[self.Player.Cy][self.Player.Cx] = '0'
                self.Player.Cy = self.Player.Cy - 1
                self.DMap.CMap[self.Player.Cy][self.Player.Cx] = '2'
    def down(self):
        if GPIO.input(19):
            if self.Player.Cy + 1 > 3:
                return
            else:
                if (self.DMap.CMap [self.Player.Cy+1][self.Player.Cx]== '1'):
                    return
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx] = '0'
                self.Player.Cy = self.Player.Cy + 1
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx] = '2'
    def left(self):
        if GPIO.input(21):
            if self.Player.Cy - 1 < 0:
                return
            else:
                if (self.DMap.CMap[self.Player.Cy] [self.Player.Cx-1] == '1'):
                    return
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx] = '0'
                self.Player.Cx = self.Player.Cx - 1
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx]= '2'
    def right(self):
        if GPIO.input(23):
            if self.Player.Cx + 1 > 5:
                return
            else:
                if (self.DMap.CMap[self.Player.Cy ][self.Player.Cx+1] == '1'):
                    return
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx]= '0'
                self.Player.Cx = self.Player.Cx + 1
                self.DMap.CMap[self.Player.Cy] [self.Player.Cx]= '2'
    def accept(self):
        self.acceptval=self.acceptval+1
    GPIO.add_event_detect(13, GPIO.RISING, callback=up, bouncetime=300)
    GPIO.add_event_detect(19, GPIO.RISING, callback=left, bouncetime=300)
    GPIO.add_event_detect(21, GPIO.RISING, callback=down, bouncetime=300)
    GPIO.add_event_detect(23, GPIO.RISING, callback=right, bouncetime=300)
    GPIO.add_event_detect(24, GPIO.RISING, callback=accept, bouncetime=300)

