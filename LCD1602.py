# Code taken from https://www.waveshare.com/wiki/LCD1602_I2C_Module
## https://files.waveshare.com/upload/d/db/LCD1602_I2C_Module_code.zip

# -*- coding: utf-8 -*-
import time
from machine import Pin, I2C

# Define pins for SDA and SCL
LCD1602_SDA = Pin(4)
LCD1602_SCL = Pin(5)

# Initialise I2C with specified pins and frequency
LCD1602_I2C = I2C(0, sda=LCD1602_SDA, scl=LCD1602_SCL, freq=400000)

# Device I2C Address
LCD_ADDRESS = (0x7c >> 1)

# LCD command constants
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# Flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# Flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# Flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# Flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x8DOTS = 0x00

class LCD1602:
    def __init__(self, col, row):
        """
        Initialise LCD1602 with specified columns and rows.

        :param col: Number of columns
        :param row: Number of rows
        """
        self._row = row
        self._col = col

        # Set initial display configuration
        self._showfunction = LCD_4BITMODE | LCD_1LINE | LCD_5x8DOTS
        self.begin(self._row, self._col)

    def command(self, cmd):
        """
        Send a command to the LCD.

        :param cmd: Command to be sent
        """
        LCD1602_I2C.writeto_mem(LCD_ADDRESS, 0x80, chr(cmd))

    def write(self, data):
        """
        Write data to the LCD.

        :param data: Data to be written
        """
        LCD1602_I2C.writeto_mem(LCD_ADDRESS, 0x40, chr(data))

    def setCursor(self, col, row):
        """
        Set the cursor position.

        :param col: Column
        :param row: Row
        """
        if row == 0:
            col |= 0x80
        else:
            col |= 0xc0
        LCD1602_I2C.writeto(LCD_ADDRESS, bytearray([0x80, col]))

    def clear(self):
        """Clear the display."""
        self.command(LCD_CLEARDISPLAY)
        time.sleep(0.002)

    def printout(self, arg):
        """
        Print data to the LCD.

        :param arg: Data to be printed
        """
        if isinstance(arg, int):
            arg = str(arg)

        for x in bytearray(arg, 'utf-8'):
            self.write(x)

    def display(self):
        """Turn on the display."""
        self._showcontrol |= LCD_DISPLAYON
        self.command(LCD_DISPLAYCONTROL | self._showcontrol)

    def begin(self, cols, lines):
        """
        Begin the LCD initialisation.

        :param cols: Number of columns
        :param lines: Number of lines
        """
        if lines > 1:
            self._showfunction |= LCD_2LINE

        self._numlines = lines
        self._currline = 0

        time.sleep(0.05)

        # Send function set command sequence
        self.command(LCD_FUNCTIONSET | self._showfunction)
        time.sleep(0.005)
        self.command(LCD_FUNCTIONSET | self._showfunction)
        time.sleep(0.005)
        self.command(LCD_FUNCTIONSET | self._showfunction)
        time.sleep(0.005)
        self.command(LCD_FUNCTIONSET | self._showfunction)

        # Turn on the display with no cursor or blinking default
        self._showcontrol = LCD_DISPLAYON | LCD_CURSOROFF | LCD_BLINKOFF
        self.display()

        # Clear the display
        self.clear()

        # Initialise to default text direction (for romance languages)
        self._showmode = LCD_ENTRYLEFT | LCD_ENTRYSHIFTDECREMENT
        self.command(LCD_ENTRYMODESET | self._showmode)

