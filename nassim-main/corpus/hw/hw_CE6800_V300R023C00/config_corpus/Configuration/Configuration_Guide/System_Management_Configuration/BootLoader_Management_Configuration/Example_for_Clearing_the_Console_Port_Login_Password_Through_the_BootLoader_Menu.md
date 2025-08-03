Example for Clearing the Console Port Login Password Through the BootLoader Menu
================================================================================

Example for Clearing the Console Port Login Password Through the BootLoader Menu

#### Networking Requirements

If you attempt to log in to a device through the console port but enter an incorrect console port login password, the login fails. If you cannot remember the correct console port login password, you can access the BootLoader menu to clear it. As shown in [Figure 1](#EN-US_TASK_0000001564004745__fig_dc_s_cfg_10332801), a PC is connected to a device through the console port, and the device is powered on.

![](public_sys-resources/note_3.0-en-us.png) 

The actual command output varies depending on the device. The command outputs provided in this section are only examples.


**Figure 1** Connecting a PC to a device through the console port  
![](figure/en-us_image_0000001563764841.png)

#### Procedure

1. Restart the device. When the message **Press Ctrl+B to enter BOOT menu** is displayed during device startup, press **Ctrl+B** within 3 seconds to access the BootLoader main menu.
   
   
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
2. In the BootLoader main menu, enter **6** to access the password manager submenu.
   
   
   ```
           Main Menu                                                                
   
       1. Default startup                                                           
       2. Serial submenu     
       3. Ethernet submenu                                                          
       4. Startup parameters submenu                                                
       5. List file                                                                 
       6. Password manager submenu                                                  
       7. DFX submenu                                                              
       8. Reboot      
   
   Enter your choice(1-8): 6            //Access the password manager submenu.
   
           Password manager submenu                                                 
   
       1. Modify bootloader password                                                
       2. Clear the console login password 
       3. Reset bootloader password                                                
       0. Return                                                                    
   
   Enter your choice(0-3): 
   ```
3. In the password manager submenu, enter **2** to access the **Clear the console login password** menu.
   
   
   ```
           Password manager submenu 
     
        1. Modify bootloader password 
        2. Clear the console login password 
        3. Reset bootloader password 
        0. Return 
     
    Enter your choice(0-3): 2 
     
    Caution: A new console password must be set after the restart. 
    Continue now? Yes(y) or No(n):
   ```
4. In the **Clear the console login password** menu, enter **y** to continue with the device startup.
   
   
   ```
    Caution: A new console password must be set after the restart. 
    Continue now? Yes(y) or No(n): y 
    Password:     //Enter the BootLoader password and press Enter to continue with the device startup.
   ```
5. After the device starts, log in to the device and reset the console port login password.
   
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] user-interface console 0 
   [~HUAWEI-ui-console0] authentication-mode password 
   [*HUAWEI-ui-console0] set authentication password 
   Please configure the login password (8-16)              
   Enter Password:  
   Confirm Password:   
   [~HUAWEI-ui-console0] commit 
   [~HUAWEI-ui-console0] return
   ```
6. Save the configuration to prevent configuration loss after restart.
   
   
   ```
   <HUAWEI> save 
    Warning: The current configuration will be written to the device. Continue? [Y/N]:y  
    Now saving the current configuration to the slot 1 
    Info: Save the configuration successfully.
   ```

#### Verifying the Configuration

After the configuration is complete, you can use the new password to log in to the device through the console port.