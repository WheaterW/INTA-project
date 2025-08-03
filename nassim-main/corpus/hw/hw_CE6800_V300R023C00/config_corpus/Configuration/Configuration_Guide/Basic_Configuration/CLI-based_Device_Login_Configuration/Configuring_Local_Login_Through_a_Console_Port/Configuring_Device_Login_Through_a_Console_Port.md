Configuring Device Login Through a Console Port
===============================================

Configuring Device Login Through a Console Port

#### Prerequisites

Before configuring device login through a console port, you have completed the following tasks:

* Prepare a console cable.
* Install the terminal emulation software on the PC.![](public_sys-resources/note_3.0-en-us.png) 
  
  If the system does not provide terminal emulation software, obtain it from a third party. For details about how to use the software, see the software user guide or online help.

#### Default Settings

**Table 1** Default settings for the console port
| Parameter | Default Setting |
| --- | --- |
| Transmission rate | 9600 bit/s |
| Flow control mode | No flow control |
| Parity check | None |
| Stop bits | 1 |
| Data bits | 8 |



#### Procedure

1. Connect the DB9 connector of the prepared console cable to the PC's serial port (COM), and the RJ45 connector to the device's console port. If there is no DB9 serial port on your terminal (PC), use a DB9-to-USB cable to connect the USB port to the terminal.
2. Start PuTTY on the PC (PuTTY is an example terminal emulator). Create a connection, select the connection port, and set communication parameters.
   1. Click **Session** to create a connection, as shown in [Figure 1](#EN-US_TASK_0000001512853512__en-us_task_0000001563881529_fig158458444263).
      
      **Figure 1** Creating a connection  
      ![](figure/en-us_image_0000001564121665.png)
   2. Click **Serial** and set the port to be connected and the communication parameters, as shown in [Figure 2](#EN-US_TASK_0000001512853512__en-us_task_0000001563881529_fig195331415132713).
      
      
      1. Select the port according to your requirements. For example, in a Windows operating system, you can open Device Manager to view port information and select the port to be connected.
      2. Ensure that the communication parameters you set in the terminal emulation software are consistent with the default parameter settings of the device's console port.
      3. Click **Open**.![](public_sys-resources/note_3.0-en-us.png) 
      
      A PC may have multiple ports that can be connected to the device. In this step, the port to be connected to a console cable must be selected. In most cases, COM1 is used.
      
      If the device's communication parameters are modified, those on the PC must be modified accordingly and the connection must be re-established.
      
      
      **Figure 2** Setting the connection port and communication parameters  
      ![](figure/en-us_image_0000001564001837.png)
3. Press **Enter** until the system prompts you to enter the password. (During AAA authentication, the system asks you to enter the user name and password. The following information is for reference only.)
   
   
   ```
   Login authentication
   
   
   Password:
   ```
   
   You can run commands to configure the device. Enter a question mark (?) if you need help.

#### Verifying the Configuration

* Run the [**display users**](cmdqueryname=display+users) [ **all** ] command to check information about users who have logged in to a device through the user interfaces.
* Run the [**display user-interface**](cmdqueryname=display+user-interface) **console 0** command to check information about the user interface.
* Run the [**display local-user**](cmdqueryname=display+local-user) command to check attributes of local users.
* Run the [**display access-user**](cmdqueryname=display+access-user) command to check information about online users.