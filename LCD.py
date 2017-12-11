
# Import necessary libraries for commuunication and display use
import lcddriver
import time
class lcd:
    def __init__(self):

    # Load the driver and set it to "display"
    # If you use something from the driver library use the "display." prefix first
        self.display = lcddriver.lcd()

    def writeMessage(self,message,position):
        if len(message)>16:
            print("Message is too Long")
            return 
        try:
                # Remember that your sentences can only be 16 characters long!
                print("Writing to display")
                self.display.lcd_display_string(message, position) # Write line of text to first line of display
                #  Give time for the message to be read

        except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
            print("Cleaning up!")
            self.display.lcd_clear()
