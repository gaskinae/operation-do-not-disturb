# 🚫 Operation Do Not Disturb 🚫

  

## Project Overview

  

**"Operation Do Not Disturb"** is a Raspberry Pi Pico (H) project featuring a Waveshare 1602 LCD I2C module. 

**Why have you made this?** I've always wanted a button on my desk I can press for those periods of time I Really Need To Focus and need to communicate this to everyone else in my immediate vicinity. But also, for fun. 

  

**Disclaimer:** I am aware this project is dangerously close to being an episode of Gadget Geeks (a great show!). Let me have fun being creative.


## Equipment
First, let's go shopping. Here's the kit I** bought.
***my colleague - who correctly predicted I'd become obsessed with Raspberry Pi - kindly gifted me:*
| Component | URL |
|--|--|
| **Raspberry Pi Pico (H) (with soldered headers) | https://thepihut.com/products/raspberry-pi-pico?variant=41925332566211 |
| **Breadboard | https://thepihut.com/products/full-sized-breadboard |
| Micro USB cable | https://thepihut.com/products/raspberry-pi-micro-usb-cable| 
| Waveshare LCD 1602 I2C Module| https://thepihut.com/products/lcd1602-i2c-module |
| Gravity: I2C/UART 4-pin PH2.0 to Male Jumper Cables (10-pack) | https://thepihut.com/products/gravity-i2c-uart-4-pin-ph2-0-to-male-jumper-cables-30cm-10-pack |


  

## Hardware Setup

  

### Pin Connections

For further information on the Raspberry Pi Pico pinout, see the diagram below. Pins relevant to the I2C are: GND, 3V3(OUT), GP4, GP5. These correspond with the I2C wires (VCC, GND, SDA, SCL), which are responsible for communicating signal between the Raspberry Pi Pico microcontroller and I2C device. ![pico pinout](https://www.raspberrypi.com/documentation/microcontrollers/images/pico-pinout.svg)

✨ **VCC (Voltage Common Collector):**

- Connect to the 3.3V pin on the Raspberry Pi Pico.

- Provides power to the LCD module.

  

 ✨ **GND (Ground):**

- Connect to the GND pin on the Raspberry Pi Pico.

- Serves as the common ground reference for the circuit.

  

 ✨ **SDA (Serial Data):**

- Connect to GPIO4 (GP4) on the Raspberry Pi Pico.

- Carries the data between the Raspberry Pi Pico and the LCD module.

  

 ✨ **SCL (Serial Clock):**

- Connect to GPIO5 (GP5) on the Raspberry Pi Pico.

- Manages the timing and synchronisation of data transmission.

  

## Software Setup

  

### Installing Micropython

  

Ensure Micropython is running on the Raspberry Pi Pico. Follow the official Micropython installation guide for the Raspberry Pi Pico: [Micropython Installation Guide](https://docs.micropython.org/en/latest/rp2/quickref.html)

  

### Following Waveshare Instructions

  

Follow the Waveshare wiki instructions for the LCD1602 I2C Module: [Waveshare LCD1602 I2C Module Instructions](https://www.waveshare.com/wiki/LCD1602_I2C_Module).

  

In a terminal...
... download the master code to a suitable local directory...
`wget https://files.waveshare.com/upload/d/db/LCD1602_I2C_Module_code.zip` 
...unzip the code...
`unzip LCD1602_I2C_Module_code.zip`
...upload the Python files inside this directory to the Raspberry Pi Pico (via Thonny IDE)
`cd LCD1602_I2C_Module_code/Pico` 

I have since customised the names of the files to suit this project - these instructions are just to show where I sourced the initial code from. 
  
  

### Verifying I2C Address

  

- Run the provided code to identify the I2C address:

```
if devices:
	print("I2C devices found:", devices)
else:
	print("No I2C devices found.")
```

  

- The above code will print the I2C address in a decimal format. Convert this to hexadecimal (base 16). As a cool person - who cannot do mental arithmetic - I used [Cool Conversion Dot Com](https://coolconversion.com/math/binary-octal-hexa-decimal/Convert_decimal__62_to_hexadecimal_) 😎
- For example, running the provided code printed **62** for me. In hexadecimal, this is **0x3E**.
- Important! If your I2C address is different to mine, **update the I2C address** . I cannot stress this enough. The correct address is crucial for successful communication between the microcontroller and the I2C device. If you ignore this, you *will* feel silly. Trust me.

  
## Controlling the message
The message is customisable in `control_i2c.py` by altering `lcd.printout("Do not disturb")` etc.

I will make the text scroll at some point, but this is for another iteration. Another feature for a future version release will include an analogue button which controls the code. 