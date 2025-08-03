Example for Setting the BootLoader Password
===========================================

Example for Setting the BootLoader Password

#### Networking Requirements

By default, the BootLoader has no password, and you are required to set one upon the first login. To prevent unauthorized users from accessing the BootLoader menu, you need to change the password periodically.

As shown in [Figure 1](#EN-US_TASK_0000001564124581__fig10223312194113), the serial port on a PC is connected to the console port on a device, and the network port on the PC is connected to the device's management Ethernet port. You can log in to the device through the terminal emulation software to change the BootLoader password.

**Figure 1** Connecting a PC to a device through a console port  
![](figure/en-us_image_0000001646840754.png)
![](public_sys-resources/notice_3.0-en-us.png) 

After changing the password, ensure that it is retained securely.

For device security purposes, change the password periodically.

The actual command output varies depending on the device. The command output provided in this section is only an example.



#### Procedure

1. Log in to the device through the console port. When the message **Press Ctrl+B to enter BOOT menu** is displayed during device startup, press **Ctrl+B** within 3 seconds to access the BootLoader main menu.
   
   
   * Set a password when accessing the BootLoader main menu for the first time.
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
     ```
   * Change the password for accessing the BootLoader main menu.
     
     Access the password manager submenu, enter the old password, and then enter the new password.
     
     ```
     Press Ctrl+B to enter BOOT menu: 3                                              
     Password:
                                
             Main Menu                                                               
     
         1. Default startup                                                          
         2. Serial submenu    
         3. Ethernet submenu                                                         
         4. Startup parameters submenu                                               
         5. List file                                                                
         6. Password manager submenu                                                 
         7. DFX submenu                                                             
         8. Reboot      
     
        
     Enter your choice(1-8):  6           //Access the password manager submenu.
      
             Password manager submenu                                                
     
         1. Modify bootloader password                                               
         2. Clear the console login password
         3. Reset bootloader password                                               
         0. Return                                                                   
     
     Enter your choice(0-3): 1                 
     
     Old password:                          //Enter the old password.
     
     New password:                         //Enter a new password. The new password cannot be the same as the old password.
     Confirm password:                      
     Warning: The bootloader password will be written to the device.                                                                    
     Continue now? Yes(y) or No(n): y
     
     The password is changed successfully.  
     ```

#### Verifying the Configuration

You can use the new password to log in to the Bootloader menu.