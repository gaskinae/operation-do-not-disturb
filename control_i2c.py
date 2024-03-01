# Import necessary modules
from machine import Pin, I2C
import LCD1602
import time

# Create an I2C object for the default I2C bus (0)
# Set the SDA (data) pin to GP4 (Pin 4) and SCL (clock) pin to GP5 (Pin 5)
# Set the frequency to 400000 Hz (400 kHz)
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

# Scan for I2C devices connected to the bus
devices = i2c.scan()

# Check if any I2C devices are found
if devices:
    print("I2C devices found:", devices)
else:
    print("No I2C devices found.")

# Set up the pins for the LCD1602 module
# Note: GP4 corresponds to physical pin 4, and GP5 corresponds to physical pin 5 on Raspberry Pi Pico
LCD1602_SDA = Pin(4)
LCD1602_SCL = Pin(5)

# Create an I2C object specifically for the LCD1602 module
# Set the SDA pin to GP4 and SCL pin to GP5 with a frequency of 400000 Hz
LCD1602_I2C = I2C(0, sda=LCD1602_SDA, scl=LCD1602_SCL, freq=400000)

# Specify the I2C address for the LCD1602 module 
# Obtain this value by converting the I2C device address decimal to hexadecimal
# E.g. If # Check if any I2C devices are found printed 62, the hexadecimal equivalent would be 0x3E
LCD_ADDRESS = 0x3E

# Create an instance of the LCD1602 class with 16 columns and 2 rows
lcd = LCD1602.LCD1602(16, 2)

try:
    # Enter an infinite loop to continuously display messages on the LCD
    while True:
        # Set the cursor to the beginning of the first line
        lcd.setCursor(0, 0)
        # Print the first line message
        lcd.printout("Do not disturb")

        # Set the cursor to the beginning of the second line
        lcd.setCursor(0, 1)
        # Print the second line message
        lcd.printout("Thank you :)")
        
        # Pause for a short duration (0.1 seconds)
        time.sleep(0.1)

# Handle KeyboardInterrupt (Ctrl+C) to exit the program gracefully
except KeyboardInterrupt:
    # Clear the LCD display
    lcd.clear()
    # Delete the LCD instance
    del lcd
