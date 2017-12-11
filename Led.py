#import RPi.GPIO as GPIO
import MapObject
#
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(4, GPIO.OUT)  #R
# GPIO.setup(11, GPIO.OUT) #Or
# GPIO.setup(12, GPIO.OUT) #Y
# GPIO.setup(13, GPIO.OUT) # P
# GPIO.setup(15, GPIO.OUT) #B
#
# #Color
# GPIO.setup(16, GPIO.OUT) #G
# GPIO.setup(18, GPIO.OUT) #L Or


#class LED:
def send(location,color):
    if (int)(location) / 12 >= 1:
        turnOn(4)
    else:
        turnOff(4)

    formatedVal = getBinary(location,4)
    print(formatedVal)
    for x in range(0,len(formatedVal)):
        print("Location")
        turnOn(int(formatedVal[x:x+1]))
    formatedVal=getBinary(color,2)
    for x in range(0,len(formatedVal)):
        print("Color")
        turnOn(int(formatedVal[x:x+1]))
    sendDefault()



def sendDefault():
    turnOff(4)
    turnOn(11)
    turnOn(12)
    turnOn(13)
    turnOn(15)
def getBinary(val,type):
    bformat='{0:0'
    bformat+=str(type)
    bformat+='b}'
    return bformat.format((int)(val))

def turnOn(pin):
    print("Turn On Pin ",pin)
    #GPIO.output(pin,GPIO.HIGH)
def turnOff(pin):
    print("Turn Off Pin ",pin)
    #GPIO.output(pin,GPIO.LOW)
def main():
    userInput=input('Hey put in a thing form 0-23')
    userColor=input('Put the number from 0-3')
    send(userInput,userColor)





if __name__ == "__main__":
    main()
