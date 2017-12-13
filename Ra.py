
import RPi.GPIO as GPIO
import time
class ServoControl:
    GPIO.setmode(GPIO.BOARD)


    def lift(self,power, ground,floor):

        GPIO.setup(40, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(36, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(29, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)

        lp = []
        p = GPIO.PWM(40, 50)
        lp.append(p)
        lp[0].start(7.5)

        p = GPIO.PWM(38, 50)
        lp.append(p)
        lp[1].start(7.5)

        p = GPIO.PWM(37, 50)
        lp.append(p)
        lp[2].start(7.5)

        p = GPIO.PWM(36, 50)
        lp.append(p)
        lp[3].start(7.5)


        if (ground == 0):
            GPIO.output(35, GPIO.HIGH)

            # Green
        if (ground == 1):
            GPIO.output(33, GPIO.HIGH)

            # Yellow
        if (ground == 2):
            GPIO.output(32, GPIO.HIGH)

            # Fushia
        if (ground == 3):
            GPIO.output(31, GPIO.HIGH)

        if (ground == 4):
            GPIO.output(29, GPIO.HIGH)

        if (ground == 5):
            GPIO.output(22, GPIO.HIGH)
        self.turn(lp[power], floor)

        self.disable()

    def disable(self):
        GPIO.output(37, 0)
        GPIO.output(38, 0)
        GPIO.output(36, 0)
        GPIO.output(35, 0)
        GPIO.output(33, 0)
        GPIO.output(32, 0)
        GPIO.output(31, 0)
        GPIO.output(29, 0)
        GPIO.output(22, 0)

    def turn(self,lp, floor):
        if (floor == 0):
            lp.ChangeDutyCycle(7.5)

        if (floor == 1):
            lp.ChangeDutyCycle(12.5)

        time.sleep(1)

def main():
    SC=ServoControl()
    SC.lift(0,0,1)
if __name__ == "__main__":
    main()

# import RPi.GPIO as GPIO
# import time
# class ServoControl:
#     GPIO.setmode(GPIO.BOARD)
#
#     def lift(self,power, ground,floor):
# <<<<<<< HEAD
#         print("raising  ",ground ," ",power)
# =======
# >>>>>>> eef7671f2294886f504c85595229ddf183de448a
#         lp = self.ListOfPower()
#         if (ground == 0):
#             GPIO.output(35, GPIO.HIGH)
#
#             # Green
#         if (ground == 1):
#             GPIO.output(33, GPIO.HIGH)
#
#             # Yellow
#         if (ground == 2):
#             GPIO.output(32, GPIO.HIGH)
#
#             # Fushia
#         if (ground == 3):
#             GPIO.output(31, GPIO.HIGH)
#
#         if (ground == 4):
#             GPIO.output(29, GPIO.HIGH)
#
#         if (ground == 5):
#             GPIO.output(22, GPIO.HIGH)
#         self.turn(lp[power], floor)
#
#         self.disable()
#
#     def disable(self):
#         GPIO.output(37, 0)
#         GPIO.output(38, 0)
#         GPIO.output(36, 0)
#         GPIO.output(35, 0)
#         GPIO.output(33, 0)
#         GPIO.output(32, 0)
#         GPIO.output(31, 0)
#         GPIO.output(29, 0)
#         GPIO.output(22, 0)
#
#     def turn(self,lp, floor):
#         if (floor == 0):
#             lp.ChangeDutyCycle(7.5)
#
#         if (floor == 1):
#             lp.ChangeDutyCycle(12.5)
#
#         time.sleep(1)
#     def ListOfPower(self):
#         lp = []
#         p = GPIO.PWM(40, 50)
#         lp.append(p)
#         lp[0].start(7.5)
#
#         p = GPIO.PWM(38, 50)
#         lp.append(p)
#         lp[1].start(7.5)
#
#         p = GPIO.PWM(37, 50)
#         lp.append(p)
#         lp[2].start(7.5)
# <<<<<<< HEAD
#
#         p = GPIO.PWM(36, 50)
#         lp.append(p)
#         lp[3].start(7.5)
#         return lp
#
#
#         p = GPIO.PWM(36, 50)
#         lp.append(p)
#         lp[3].start(7.5)
#         return lp
#
# # def main():
# #     SC=ServoControl()
# #     SC.lift(0,0,1)
# # if __name__ == "__main__":
# #     main()
