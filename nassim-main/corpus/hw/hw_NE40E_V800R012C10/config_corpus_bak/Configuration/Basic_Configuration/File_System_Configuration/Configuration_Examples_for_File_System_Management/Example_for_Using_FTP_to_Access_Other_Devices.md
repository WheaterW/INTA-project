Example for Using FTP to Access Other Devices
=============================================

You can log in to an FTP server from an FTP client to download system software and configuration files from the server to the client.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

As FTP poses security risks, using SFTP is recommended.



#### Networking Requirements

To transfer files with a remote FTP server or manage directories of the server, configure a device as an FTP client and use FTP to access the FTP server.

On the network shown in [Figure 1](#EN-US_TASK_0000002055415252__en-us_task_0172360139_fig_dc_vrp_basic_cfg_011201), the FTP client and server are routable to each other. To download system software and configuration files from the server to the client, log in to the server from the client.

**Figure 1** Using FTP to access another device![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents GE 0/1/1.


  
![](images/fig_dc_vrp_basic_cfg_011201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the username and password for an FTP user to log in to the FTP server and the directory that the user will access.
2. Enable the FTP server function.
3. Run login commands to log in to the FTP server.
4. Configure the file transfer mode and working directory to allow the client to download files from the server.

#### Data Preparation

To complete the configuration, you need the following data:

* Username and password used by the FTP client for login
* IP address of the FTP server: 1.1.1.1
* Target file and its location on the FTP client

#### Precautions

In insecure network environments, you are advised to use a secure protocol. [Example for Using SFTP to Log In to Another Device for File Access (ECC Authentication Mode)](dc_vrp_basic_cfg_0121_2.html#EN-US_TASK_0000002091495641) provides examples for secure protocols.


#### Procedure

1. Configure an FTP user on the FTP server.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] aaa
   ```
   ```
   [*HUAWEI-aaa] local-user huawei password
   ```
   ```
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The password must meet the following requirements:
   
   * The password is entered in man-machine interaction mode. The system does not display the entered password.
   * A password is a string of 8 to 16 case-sensitive characters and must contain at least two types of the following characters: uppercase letters, lowercase letters, digits, and special characters.
   * Special characters exclude question marks (?) and spaces. However, spaces are allowed in the password if the password is enclosed in quotation marks.
     + Double quotation marks cannot contain double quotation marks if spaces are used in a password.
     + Double quotation marks can contain double quotation marks if no space is used in a password.
     
     For example, the password "Aa123"45"" is valid, but the password "Aa 123"45"" is invalid.
   
   The configured password is displayed in ciphertext in the configuration file.
   
   ```
   [*HUAWEI-aaa] local-user huawei service-type ftp
   ```
   ```
   [*HUAWEI-aaa] local-user huawei ftp-directory cfcard:/
   ```
   ```
   [*HUAWEI-aaa] local-user huawei level 3
   ```
   ```
   [*HUAWEI-aaa] commit
   ```
   ```
   [*HUAWEI-aaa] quit
   ```
2. Enable the FTP server function.
   
   
   ```
   [~HUAWEI] interface LoopBack 0
   ```
   ```
   [~HUAWEI-LoopBack0] ip address 10.1.1.1 255.255.255.255
   ```
   ```
   [*HUAWEI-LoopBack0] quit
   ```
   ```
   [*HUAWEI] ftp server enable
   ```
   ```
   [*HUAWEI] ftp server-source -i loopback 0
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~HUAWEI] quit
   ```
3. Log in to the FTP server from the FTP client.
   
   
   ```
   <HUAWEI> ftp 10.1.1.1
   ```
   ```
   Trying 10.1.1.1 ...
   ```
   ```
   Press CTRL+K to abort
   ```
   ```
   Connected to 1.1.1.1.
   ```
   ```
   220 FTP service ready.
   ```
   ```
   User(10.1.1.1:(none)):huawei
   ```
   ```
   331 Password required for huawei.
   ```
   ```
   Enter password:
   ```
   ```
   230 User logged in.  
   ```
   ```
   [ftp]
   ```
4. Set the file transfer mode to **binary** and specify the Flash working directory on the FTP client.
   
   
   ```
   [ ftp] binary
   ```
   ```
   200 Type set to I.
   ```
   ```
   [ftp] lcd new_dir:/
   ```
   ```
   The current local directory is new_dir:.
   ```
   ```
   [ftp] commit
   ```
5. Download the latest system software from the FTP server to the FTP client.
   
   
   ```
   [ftp] get V800R023C00SPC500B020D0123.cc
   ```
   ```
   200 Port command okay.
   150 Opening BINARY mode data connection for V800R023C00SPC500B020D0123.cc.
   226 Transfer complete.
   FTP: 1127 byte(s) received in 0.156 second(s) 7.22Kbyte(s)/sec.
   ```
   ```
   [ftp] quit
   ```
   
   Run the **dir** command to check whether the required file has been downloaded to the client.

#### Configuration Files

* FTP server configuration file
  
  ```
  #
  aaa
   local-user huawei password cipher @%@%UyQs4,KTtSwJo(4QmW#K,LC:@%@%
   local-user huawei ftp-directory cfcard:/
   local-user huawei level 3
   local-user huawei service-type ftp
   #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 1.1.1.1 255.255.255.0
  #
  interface loopback 0
   ip address 10.1.1.1 255.255.255.255
  ftp server enable
  ftp server-source -i loopback 0
  #
  return
  ```
* FTP client configuration file
  
  ```
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 2.1.1.1 255.255.255.0
  #
  return
  ```