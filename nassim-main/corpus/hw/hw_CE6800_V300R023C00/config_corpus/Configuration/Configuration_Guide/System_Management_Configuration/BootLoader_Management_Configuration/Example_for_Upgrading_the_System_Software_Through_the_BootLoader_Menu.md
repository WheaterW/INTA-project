Example for Upgrading the System Software Through the BootLoader Menu
=====================================================================

Example for Upgrading the System Software Through the BootLoader Menu

#### Networking Requirements

The BootLoader menu enables you to upgrade the system software. This is useful if you cannot access the command line interface (CLI) through the console port or the system restarts repeatedly.

As shown in [Figure 1](#EN-US_TASK_0000001563884453__fig176971549194019), the serial port on a PC is connected to the console port on a device, and the network port on the PC is connected to the device's management Ethernet port. You can log in to the device through the terminal emulation software. The PC is configured as the FTP server, and the system software required for the upgrade is copied to the FTP working directory.

![](public_sys-resources/note_3.0-en-us.png) 

To enhance security, you are advised to select SFTP as the FTP service type.

The actual command output varies depending on the device. The command outputs provided in this section are only examples.


**Figure 1** Connecting a PC to a device through a console port  
![](figure/en-us_image_0000001646681278.png)

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
2. Set FTP parameters on the device for setting up an SFTP connection to the PC.
   
   
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
   
   Enter your choice(1-8): 3            //Access the password manager submenu.
             
           Ethernet submenu                                                        
   
       1. Update software                                                          
       2. Display parameters                                                       
       3. Modify parameters  
       0. Return                                                                   
   
   Enter your choice(0-3): 3             //Access the submenu for modifying parameters.
   NOTE:
   Net type define:
   0(SFTP) 1(FTP) 2(TFTP)  
   Please check network parameters:
   ENTER = no change; '.' = clear; Ctrl+C = quit
   FTP type(0:SFTP 1:FTP 2:TFTP) : 0                -   //Specify SFTP as the FTP service type.
   Server IP address             : 192.168.1.12     -   //Set the server IP address.
   Local IP address              : 192.168.1.110    -   //Set the IP address of the local device.
   Local IP mask                 : 255.255.255.0    -   //Configure the IP address mask of the local device.
   FTP username                  : root             -   //Set the username of the FTP server.
   ```
3. Download the system software required for the upgrade from the server. The device then starts with the system software.
   
   
   ```
           Ethernet submenu                                                        
   
       1. Update software                                                          
       2. Display parameters                                                       
       3. Modify parameters 
                                                          
       0. Return                                                                   
   
   Enter your choice(0-3): 1             //Access the update software submenu.
   
           Update software                                                         
   
       1. Update system software                                                   
       2. Update system software with disk format                                  
       0. Return                                                                   
   
   Enter your choice(0-2): 1             //Access the update system software submenu.
   
   Current startup file is "software.cc".
   Please input file name: softwarenew.cc             //Enter the name of the system software required for the upgrade.
   
   Current patch file is "patchfile.PAT".
   '.' = clear field; //Enter a period (.) and then press Enter to clear the patch.
   
   Please input patch name:                            //Press Enter if patch update is not required.
   ```

#### Verifying the Configuration

After the device starts, run the **display version** command in the CLI to check whether the device version is the target version.