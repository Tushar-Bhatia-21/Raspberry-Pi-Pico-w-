Hello, and welcome to Raspberry Pi 🍓 Pico/Pico w Devlopment.

This guide assumes that you are new to Micro controller Devlopment, Hence will take extreme care towards your understanding.

For further information, reference links are provided at the end.

<b>Hardware Information</b>


These are the common terms that you should be familiar with for the Raspberry Pi Pico/ Pico W.

1. RX- It means Reciever. SPI RX indicates that data will be recieved by your sensor or module. For eg. Display will be connnected at Rx.
2. Tx- It means Transmitter. SPI Transmitter indicates that data will be transmitted to your Raspberry Pi Pico board.
3. CSn- It means Chip Select with 'n' indicating number of chips. This is used to indicate to which chips data will be transferred or recieved.
4. SCK- It means Serial Clock. As we discussed earlier that at different times data will be transferred. SCK will ensure that the those times are synchromized.
5. SDA- It means Serial Data- The transfer of data will take place through this pin.
6. SCL- It means Serial Clock. It is equivalent to SCK.

 
 There also exists differnet modes which are indicated as 0,1,2,3. 
    For eg.
    
    These modes are listed as SPI,I2C,UART followed by mode number such as SPI0,SPI1 etc. On your Pin out Diagram.
    These modes indicate different time at which data is being transferred. These are trivial for now.

Following terms can be seen on your Pin Out Diagram.

These are Transfer Rules or Interfaces, these are used for communication between your Board and Sensors.
1. GPIO- General Purpose Input/ Output- As the name suggests these are your Input-Output Pins where, sensors and other peripherals can be connected.
   They are followed by Pin number such as GPIO23 etc. 
3. SPI-Serial Peripheral Interface- It enables the exchange of data from both your host device and Raspberry Pi Pico.  
4. I2C- Inter-Integrated Circuit. It is a connection protocol, used for serial communication with your Sensors and Raspberry Pi Pico Board.
5. UART- Universal Asynchronous Reciever Transmitter. This is a hardware device. It allows the data transferred speed to be configured.


SPI,I2C,UART is listed with different terms such as RX,CSn,TX,SCK.

The combination of the above info will be used in Pins by your Raspberry Pi Pico/Pico W. 

For eg. SPI0 TX- This indicates that SPI interface is being used. With Mode 0 and is used as Transmitter.

There are a few other terms that can be seen on the Pin Out Diagram:
1. GND- Ground. It means 0 voltage drop.
2. ADC- Analog to Digital Converter. These pins are used to convert Analog Signals to digital and offer 12 bit output. With use of Compilers such as THonny, this range can be extended to 16 bit.
3. VBUS- This Pin can be used to power your board instead of Micro-USB port, also can be used to power modules with 3.3 V.
4. RUN-Instead of Using your BOOTSEL button, it can be shorted to reset the board. However, it is not recommended for a beginners.
5. VSYS-System input voltage (1.8 V to 5.5 V) used by the on- board SMPS(Switched Mode Power Supply) to generate +3.3 V supply for the board.
6. V_ref- Reference Voltage.
7. 3V3_EN- 3v Input.
8. 3V3_(OUT)-3V Output.

<b>Software Information</b>

Your Pico/Pico W can be programmed using ASSEMBLY, C, C++, Micropython and Circuitpython.

Below is the tutorial for using with Micropython. For C/C++/ASM Check the other repository.

Step 1.    Download and Install Thonny. https://thonny.org/

Step 2.    Plug in your Raspberry Pi Pico/Pico W micro-controller board while holding down the BOOTSEL button.

Step 3.    Open Thonny IDE and click on right hand corner Local Python 3.
  ![image](https://user-images.githubusercontent.com/113343003/209993350-6cf66df1-87d3-45bc-92d7-0274c6710a9c.png)

Step 4.    Select Install Micropython and Select the latest Variant.

![image](https://user-images.githubusercontent.com/113343003/209993541-9aa28b0d-29b4-4492-8da1-3b4d5e2754ab.png)

![image](https://user-images.githubusercontent.com/113343003/209993577-abae8ed8-c913-4200-bfaf-ff6224bd2136.png)

Step 5.    Click on Install and the board will automatically plug itself in FS mode.

Step 6.    Close the dialog box and your board is ready for Devlopment.

Check out Blink Project, to see if everything is working correctly or not.

To setup with C/C++/ASM Check out SETUP USING C/C++/ASM.

########################################

Happy Coding😀😀

Reference Links:
1. https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html
2. https://www.geeksforgeeks.org/i2c-communication-protocol/
3. https://www.circuitbasics.com/basics-of-the-spi-communication-protocol/
4. https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter
