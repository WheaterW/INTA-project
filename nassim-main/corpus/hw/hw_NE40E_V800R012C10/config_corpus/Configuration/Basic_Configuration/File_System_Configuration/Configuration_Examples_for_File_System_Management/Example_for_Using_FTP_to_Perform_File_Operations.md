Example for Using FTP to Perform File Operations
================================================

Files can be uploaded or downloaded using FTP.

#### Networking Requirements

As devices operate stably and are deployed on a large scale, more and more devices need to be maintained and upgraded remotely. Online software upgrade, a new upgrade method by loading software packages remotely, facilitates remote online upgrades, reduces upgrade expenditures, shortens the time that customers wait for upgrades, and improves customers' satisfaction. The delay, packet loss, and jitter affect data transmission on networks. To ensure the quality of online upgrade and data transmission, use FTP to perform online upgrades and transfer files based on TCP connections.

As shown in [Figure 1](#EN-US_TASK_0172359941__fig_dc_vrp_vfm_cfg_002501), you can log in to the FTP server from the terminal emulation program to upload or download files.

**Figure 1** File operations using FTP![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents GigabitEthernet0/0/0.


  
![](images/fig_dc_vrp_vfm_cfg_002501.png)

#### Precautions

After you log in to the FTP server through the console port, configure an IP address of a logical interface as the source address for FTP login.

In insecure network environments, you are advised to use a secure protocol. [Example for Using SFTP to Operate Files](dc_vrp_vfm_cfg_0026.html) provides examples for secure protocols.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for the FTP server.
2. Enable the FTP server function.
3. Configure an authentication mode, authorization mode, and authorized directory.
4. Log in to the FTP server by using the correct user name and password.
5. Upload a file to or download a file from the FTP server.

#### Data Preparation

To complete the configuration, you need the following data:

* IP address for the FTP server: 10.137.217.221
* FTP username (huawei) set on the server
* Path on which the file to be uploaded is saved and the path on which the file to be downloaded is saved

#### Procedure

1. Configure an IP address for the FTP server.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname server
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~server] interface GigabitEthernet0/0/0
   ```
   ```
   [~server-GigabitEthernet0/0/0] undo shutdown
   ```
   ```
   [*server-GigabitEthernet0/0/0] ip address 10.137.217.221 255.255.0.0
   ```
   ```
   [*server-GigabitEthernet0/0/0] quit
   ```
   ```
   [*server] commit
   ```
2. Enable the FTP server function.
   
   
   ```
   [~server] interface LoopBack 0
   ```
   ```
   [~server-LoopBack0] ip address 10.1.1.1 255.255.255.255
   ```
   ```
   [*server-LoopBack0] quit
   ```
   ```
   [*server] ftp server enable
   ```
   ```
   [*server] ftp server-source -i loopback 0
   ```
   ```
   [*server] commit
   ```
3. Configure an authentication mode, authorization mode, and authorized directory.
   
   
   ```
   [~server] aaa
   ```
   ```
   [*server-aaa] local-user huawei password
   ```
   ```
   Please configure the password (8-128)
   Enter Password:
   Confirm Password:
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The password is entered in interactive mode, and the system does not display the password.
   
   Special characters do not include question marks (?) or spaces. However, if the password is enclosed in double quotation marks (" "), spaces are allowed.
   * If double quotation marks are used to set a password with spaces, double quotation marks cannot be used between double quotation marks.
   * Double quotation marks can contain double quotation marks if no space is used in a password.
   
   For example, the password "Aa 123"45"" is invalid, but the password "Aa123"45"" is valid.
   
   ```
   [*server-aaa] local-user huawei service-type ftp
   ```
   ```
   [*server-aaa] local-user huawei ftp-directory cfcard:/
   ```
   ```
   [*server-aaa] local-user huawei level 3
   ```
   ```
   [*server-aaa] quit
   ```
   ```
   [*server] commit
   ```
4. Run the **ftp** command at the Windows command prompt, and enter the correct user name and password to set up an FTP connection.
5. Uploads and downloads files on the user terminal.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You can run the [**dir**](cmdqueryname=dir) command before downloading a file or after uploading a file to view the detailed information about the file.

#### FTP Server Configuration File

```
#
sysname server
#
FTP server enable
FTP server-source -i loopback 0
#
aaa
 local-user huawei password cipher @%@%:BC"Qzkbh*9PhJU|U>mX,cZQ@%@%
 local-user huawei service-type ftp
 local-user huawei level 3
 local-user huawei ftp-directory cfcard:/
#
interface GigabitEthernet0/0/0
 undo shutdown
 ip address 10.137.217.221 255.255.0.0
#
interface LoopBack 0
 ip address 10.1.1.1 255.255.255.255
#
return
```