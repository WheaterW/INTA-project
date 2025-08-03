First Login Through the Console Port
====================================

First Login Through the Console Port

#### Prerequisites

Before logging in to a device locally for the first time through the console port, you have completed the following tasks:

* Power on the device properly.
* Prepare a console cable.
* Prepare the terminal emulation software.
  
  For details about how to use specific terminal emulation software, see the related software user guide or online help. This section uses the third-party software PuTTY as an example.

#### Default Settings

**Table 1** Default settings for the console port
| Parameter | Default Setting |
| --- | --- |
| Transmission rate | 9600 bit/s |
| Flow control mode | No flow control |
| Parity bit | No parity bit configured, indicating no parity check |
| Stop bit | 1 |
| Data bit | 8 |




#### Procedure

1. Connect the DB9 connector of the prepared console cable to the PC's serial port (COM), and the RJ45 connector to the device's console port. If there is no DB9 serial port on your terminal (PC), use a DB9-to-USB cable to connect the USB port to the terminal.
2. Start PuTTY on the PC (PuTTY is an example terminal emulator). Create a connection, select the connection port, and set communication parameters.
   1. Click **Session** to create a connection, as shown in [Figure 1](#EN-US_TASK_0000001563881529__fig158458444263).
      
      **Figure 1** Creating a connection  
      ![](figure/en-us_image_0000001564121665.png)
   2. Click **Serial** and set the port to be connected and the communication parameters, as shown in [Figure 2](#EN-US_TASK_0000001563881529__fig195331415132713).
      
      
      1. Select the port according to your requirements. For example, in a Windows operating system, you can open Device Manager to view port information and select the port to be connected.
      2. Ensure that the communication parameters you set in the terminal emulation software are consistent with the default parameter settings of the device's console port.
      3. Click **Open**.![](public_sys-resources/note_3.0-en-us.png) 
      
      A PC may have multiple ports that can be connected to the device. In this step, the port to be connected to a console cable must be selected. In most cases, COM1 is used.
      
      If the device's communication parameters are modified, those on the PC must be modified accordingly and the connection must be re-established.
      
      
      **Figure 2** Setting the connection port and communication parameters  
      ![](figure/en-us_image_0000001564001837.png)
3. Press **Enter** until information similar to the following is displayed. Enter a password and confirm the password as prompted. (The following information is for reference only.)
   
   
   ```
   User interface con0 is available
   
   Please Press ENTER.
   
   Please configure the login password (8-16)
   Enter Password: 
   Confirm Password: //Enter the password for logging in to the device through the console port.
   Info: Save the password now. Please wait for a moment.
   Info: The max number of VTY users is 21, the number of current VTY users online is 0, and total number of terminal users online is 1.
         The current login time is 2020-06-30 18:15:10+08:00
   <HUAWEI>
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * You must set a login password upon first login to the device through the console port. After the login is successful, the console port has the default administrator rights.
   * The password is a string of 8 to 16 case-sensitive characters. It must contain at least two of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters do not include question marks (?) or spaces.
   * In interactive mode, the entered password is not displayed on the terminal screen.
   * For security purposes, change the password periodically.
   
   
   
   After completing the preceding steps, you can run commands to configure the device. Enter a question mark (?) whenever you need help.