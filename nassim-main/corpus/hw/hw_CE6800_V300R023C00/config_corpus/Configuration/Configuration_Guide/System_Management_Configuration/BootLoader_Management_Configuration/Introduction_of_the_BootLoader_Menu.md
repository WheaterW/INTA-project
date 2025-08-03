Introduction of the BootLoader Menu
===================================

You have logged in to the device through the console port.![](public_sys-resources/note_3.0-en-us.png) 

For details about the console port connection mode, see "Logging In to the CLI" in Configuration Guide - Basic Configurations. If third-party terminal emulation software is used, set communication parameters correctly. If the parameter settings are incorrect, the third-party terminal emulation software may enter excess characters when you are using the BootLoader menu. As a result, BootLoader menu operations will be abnormal.

The actual command output varies depending on the device. The command output provided in this section is only an example.



#### Shortcut Keys

You can use the following shortcut keys in any BootLoader menu:

* **Ctrl+M** or **Ctrl+J**: provides functions similar to **Enter**.
* **Ctrl+C**: cancels the current setting.

#### BootLoader Main Menu

Restart the device. When the message **Press Ctrl+B to enter BOOT menu** is displayed, press **Ctrl+B** within 3 seconds to access the BootLoader main menu.
```
Press Ctrl+B to enter BOOT menu: 3                                              
Info: The password is empty. For security purposes, change the password.        

New password:                           
Confirm password:                                                               
Warning: The bootloader password will be written to the device.                                                                     
Continue now? Yes(y) or No(n): y

The password is changed successfully.                                           

        Main Menu                                                               

    1. Default startup                                                          
    2. Serial submenu      
    3. Ethernet submenu                                                         
    4. Startup parameters submenu                                               
    5. List file                                                               
    6. Password manager submenu                                                 
    7. DFX submenu                                                              
    8. Reboot      

Enter your choice(1-8):
```

**Table 1** BootLoader main menu
| Item | Description |
| --- | --- |
| Press Ctrl+B to enter BOOT menu | Press **Ctrl+B** within 3 seconds to access the BootLoader main menu.  You can access the BootLoader main menu to perform operations such as a device upgrade when failing to access the CLI on the device. |
| New password  Confirm password | Set the BootLoader password. By default, there is no password. To improve security, set a password as prompted upon the first login. The password must contain 8 to 255 characters, including at least two types of the following: uppercase letters (A to Z), lowercase letters (a to z), digits (0 to 9), and special characters, such as exclamation marks (!), at signs (@), number signs (#), dollar signs ($), and percent signs (%).  If you enter incorrect passwords for three consecutive times, the system restarts.  To change or clear the password, access the **Password manager submenu**.  NOTE:   * The password cannot contain question marks (?) or spaces. * To prevent unauthorized users from accessing the BootLoader menu, you are advised to set the password and update the password periodically after logging in to the device. |
| Default startup | Perform this operation to directly start the device using the current configuration.  This operation does not restart the BootLoader, but continues to start the system. |
| Serial submenu | Access this submenu to change the serial port transmission rate.  No configuration is required before performing operations through the serial port. The serial port is ready once a PC is connected to the device through the serial port, but the file transmission rate is low.  After the transmission rate on the serial port is modified, synchronize the transmission rate on the PC to that on the serial port and re-establish the connection.  You can perform the following operations:   * Modify baudrate: Modify the transmission rate on the serial port. The default transmission rate is 9600 bit/s. * Return: Return to the main menu. |
| Ethernet submenu | Access this submenu to change the system software or patch file.  This operation features fast file transmission rate, but you must configure network parameters and an SFTP, FTP, or TFTP server to ensure that the device and server are reachable to each other.  For details about the operations that can be performed after you access this submenu, see [Table 2](#EN-US_CONCEPT_0000001512844942__table1668601474175322). |
| Startup parameters submenu | Access this submenu to view or modify startup configuration.  You can perform the following operations:   * Display current startup configuration: Display the system software, configuration file, and patch file for device startup. * Modify the startup file: Modify the system software. * Modify the configuration file: Modify the configuration file. * Modify the patch file: Modify the patch file. * Return: Return to the main menu.   NOTE:  The system software, configuration file, and patch file to be set must exist on the storage device. Otherwise, the setting fails.  To clear the current value, enter a period (.). To cancel the operation under this menu, press **Ctrl+C**. To make the current configuration take effect, press **Enter**. |
| List file | Access this submenu to view the list of all files in the flash memory. |
| Password manager submenu | Access this submenu to change the password for accessing the BootLoader menu, preventing unauthorized users from accessing the BootLoader menu.  You can perform the following operations:   * Modify bootloader password: Change the password for accessing the BootLoader menu. * Clear the console login password: Clear the password for logging in to the device through the console port when the login fails due to password loss. * Reset bootloader password: Clear the password for accessing the BootLoader menu. * Return: Return to the main menu.   NOTICE:   * To prevent the console port login password from being maliciously tampered with, keep the BootLoader password in a safe place. * You can run the **set boot password** command on the CLI to set the password for accessing the BootLoader menu. (When you log in to a new device for the first time through the console port, you need to immediately set the BootLoader password to prevent the console port password from being cleared without authorization. If the BootLoader password is not set, unauthorized users may attempt to log in to a device through the BootLoader and clear the console port password, which will cause security risks.) |
| DFX submenu | Access this submenu to query electronic labels.  You can perform the following operations:   * Display board E-Label: Display the electronic label of the device. * Return: Return to the main menu. |
| Reboot | After you select **Reboot**, the BootLoader restarts and the system continues to start. In most cases, you are advised not to perform this operation. |


**Table 2** Ethernet submenu
| Item | Description |
| --- | --- |
| Update software | When no system software or patch file exists in the storage medium, access this menu to download the required file from the server and specify the downloaded file for next startup. The device will start using this file.  If you do not need to specify the new system software or patch file, press **Enter** and continue operations. The device starts using the running system software or patch file.  You can perform the following operations:   * Update system software: Upgrade the system software. * Update system software with disk format: Format the flash memory and upgrade the system software. * Return: Return to the previous menu.   NOTICE:  After the storage medium is formatted through the Ethernet interface, all data in the storage medium, including history system software and configuration files, is deleted. Exercise caution when formatting the storage medium. |
| Display parameters | View Ethernet interface parameters.  You can use this menu to view the FTP service type, IP address of the SFTP, FTP, or TFTP server, IP address of the Ethernet port on the device, FTP user name, and FTP password. |
| Modify parameters | Modify Ethernet interface parameters. To enhance security, you are advised to select SFTP as the FTP service type.   * FTP type: indicates the FTP service type. The value 0 indicates SFTP, value 1 indicates FTP, and value 2 indicates TFTP. The default value is 0 (SFTP). * Server IP address: indicates the server IP address. * Local IP address: indicates the IP address of the local device. * Local IP mask: indicates the IP address mask of the local device. * FTP username: indicates the username used to log in to the FTP server. * FTP password: indicates the password used to log in to the FTP server.   NOTE:  SFTP is recommended because it is more secure than FTP.  When setting Ethernet port parameters, do not enter spaces in parameter values.  To clear the current value, enter a period (.). To cancel the operation under this menu, press **Ctrl+C**. To make the current configuration take effect, press **Enter**. |
| Return | Return to the main menu. |



#### Restoring Factory Settings

If you cannot log in to the device because you forget the password (including the BootLoader password and upper-layer password) or the username and password in the configuration file are abnormal, and the device does not have a button for restoring factory settings, you can press **Ctrl+R** to clear the configuration and menu password and restore factory settings.

After you press **Ctrl+R**, the device retains the current system software and patch file as the startup file of the device.

![](public_sys-resources/note_3.0-en-us.png) 

* The configuration file and data cannot be restored once being cleared. Therefore, exercise caution when deciding to perform this operation. You are advised to perform this operation under the guidance of technical support personnel.
* After you press **Ctrl+R**, the system displays a message. After you select "I confirm to restore factory configurations", the factory settings of the device are restored.
* **Ctrl+R**: restores factory settings. (This function is supported only in V300R022C10 and later versions.)

When the **Press Ctrl+R to enter the Recovery mode and restore factory configurations** message is displayed, press **Ctrl+R** within 3 seconds to restore factory settings.

```
Press Ctrl+R to enter the Recovery mode and restore factory configurations. 
Press Ctrl+B to enter BOOT menu: 3
If you confirm to restore factory configurations,please enter the following case-sensitive string:"I confirm to restore factory configurations"(excluding quotation marks)
The init_script service is done.
I confirm to restore factory configurations   //User input
```