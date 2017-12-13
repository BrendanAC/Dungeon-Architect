import RPi.GPIO as GPIO
import MapObject
#
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


GPIO.setup(7, GPIO.OUT)  #R
GPIO.setup(11, GPIO.OUT) #Or
GPIO.setup(12, GPIO.OUT) #Y
GPIO.setup(15, GPIO.OUT) #B

# #Color
GPIO.setup(16, GPIO.OUT) #G
GPIO.setup(18, GPIO.OUT) #L Or


#class LED:
def send(location,color):
    if (int)(location) / 12 >= 1:
        turnOn(7)
    else:
        turnOff(7)

    formatedVal = getBinary(location,4)
    #print(formatedVal)

    x=0
    if formatedVal[x:x + 1] == '1':
        turnOn(11)
    if formatedVal[x:x+1]=='0':
        turnOff(11)
    if formatedVal[x:x + 1] == '0':
        turnOff(12)
    if formatedVal[x:x + 1] == '1':
        turnOn(12)
    if formatedVal[x:x+1]=='0':
        turnOff(15)
    if formatedVal[x:x + 1] == '1':
        turnOn(15)
    formatedVal = getBinary(color, 2)
    #Color
    x=0
    if formatedVal[x:x + 1] == '0':
        turnOff(16)
    if formatedVal[x:x + 1] == '1':
        turnOn(16)
    x=x+1
    if formatedVal[x:x + 1] == '0':
        turnOff(18)
    if formatedVal[x:x + 1] == '1':
        turnOn(18)
    sendDefault()



def sendDefault():
    turnOff(7)
    turnOn(11)
    turnOn(12)
    turnOn(15)
    turnOn(16)
    turnOn(18)
def getBinary(val,type):
    bformat='{0:0'
    bformat+=str(type)
    bformat+='b}'
    return bformat.format((int)(val))

def turnOn(pin):
    #print("Turn On Pin ",pin)
    GPIO.output(pin,GPIO.HIGH)
    pass
def turnOff(pin):
    #print("Turn Off Pin ",pin)
    GPIO.output(pin,GPIO.LOW)
    pass
def main():
    userInput=input('Hey put in a thing form 0-23')
    userColor=input('Put the number from 0-3')
    send(userInput,userColor)





if __name__ == "__main__":
    main()
