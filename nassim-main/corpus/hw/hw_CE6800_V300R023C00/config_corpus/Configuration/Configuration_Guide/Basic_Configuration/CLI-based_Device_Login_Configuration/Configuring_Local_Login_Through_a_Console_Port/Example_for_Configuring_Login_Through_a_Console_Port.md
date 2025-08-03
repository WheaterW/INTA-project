Example for Configuring Login Through a Console Port
====================================================

Example for Configuring Login Through a Console Port

#### Networking Requirements

If users cannot remotely log in to a device, they can locally log in to the device through the console port on the device. Password authentication is used for login through the console port. To prevent unauthorized users from accessing a device, you can change the authentication mode of the console user interface (used for login through the console port) to AAA authentication.

**Figure 1** Network diagram of login through the console port  
![](figure/en-us_image_0000001563893033.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Use the terminal emulation software to log in to the device through the console port.
2. Configure the authentication mode for the console user interface.

![](public_sys-resources/note_3.0-en-us.png) 

If the system does not provide terminal emulation software, obtain it from a third party. For details about how to use the software, see the software user guide or online help.



#### Procedure

1. Connect the DB9 connector of the prepared console cable to the PC's serial port (COM), and the RJ45 connector to the device's console port. If there is no DB9 serial port on your terminal (PC), use a DB9-to-USB cable to connect the USB port to the terminal.
2. Start PuTTY on the PC (PuTTY is an example terminal emulator). Create a connection, select the connection port, and set communication parameters.
   1. Click **Session** to create a connection, as shown in [Figure 2](#EN-US_TASK_0000001564013285__en-us_task_0000001512853512_en-us_task_0000001563881529_fig158458444263).
      
      **Figure 2** Creating a connection  
      ![](figure/en-us_image_0000001564121665.png)
   2. Click **Serial** and set the port to be connected and the communication parameters, as shown in [Figure 3](#EN-US_TASK_0000001564013285__en-us_task_0000001512853512_en-us_task_0000001563881529_fig195331415132713).
      
      
      1. Select the port according to your requirements. For example, in a Windows operating system, you can open Device Manager to view port information and select the port to be connected.
      2. Ensure that the communication parameters you set in the terminal emulation software are consistent with the default parameter settings of the device's console port.
      3. Click **Open**.![](public_sys-resources/note_3.0-en-us.png) 
      
      A PC may have multiple ports that can be connected to the device. In this step, the port to be connected to a console cable must be selected. In most cases, COM1 is used.
      
      If the device's communication parameters are modified, those on the PC must be modified accordingly and the connection must be re-established.
      
      
      **Figure 3** Setting the connection port and communication parameters  
      ![](figure/en-us_image_0000001564001837.png)
3. Press **Enter** until the system prompts you to enter the password. (During AAA authentication, the system asks you to enter the user name and password. The following information is for reference only.)
   
   
   ```
   Login authentication
   
   
   Password:
   ```
   
   You can run commands to configure the device. Enter a question mark (?) if you need help.
4. Configure the authentication mode for the console user interface. (The user name is **admin1234** and the password is **YsHsjx\_202206**.)
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] user-interface console 0
   [~HUAWEI-ui-console0] authentication-mode aaa
   [*HUAWEI-ui-console0] user privilege level 3
   [*HUAWEI-ui-console0] quit
   [*HUAWEI] aaa
   [*HUAWEI-aaa] local-user admin1234 password
   Please configure the login password (8-128)
   It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
   Please enter password:                                      
   Please confirm password:                               
   [*HUAWEI-aaa] local-user admin1234 privilege level 3
   [*HUAWEI-aaa] local-user admin1234 service-type terminal
   [*HUAWEI-aaa] commit
   ```

#### Verifying the Configuration

After the preceding operations, you must enter the user name **admin1234** and password **YsHsjx\_202206** when logging in to the device.

```
Username:admin1234
Password:
<HUAWEI>
```

#### Configuration Scripts

```
#
aaa
 local-user admin1234 password irreversible-cipher $1d$g8wLJ`LjL!$CyE(V{3qg5DdU:PM[6=6O$UF-.fQ,Q}>^)OBzgoU$
 local-user admin1234 service-type terminal
 local-user admin1234 privilege level 3
#
user-interface con 0
 authentication-mode aaa
 user privilege level 3
#
return
```