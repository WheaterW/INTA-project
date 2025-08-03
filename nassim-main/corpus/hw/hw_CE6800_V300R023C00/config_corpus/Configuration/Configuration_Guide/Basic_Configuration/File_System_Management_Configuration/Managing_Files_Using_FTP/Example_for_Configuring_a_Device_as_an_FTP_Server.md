Example for Configuring a Device as an FTP Server
=================================================

Example for Configuring a Device as an FTP Server

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564110697__fig_dc_cfg_file_002001), PC1 connects to the device at 10.136.23.5. The device needs to be upgraded. To be specific, the device needs to function as the FTP server so that the system software can be uploaded from PC1 to the device and the configuration file of the device can be saved to PC1 for backup. In addition, an ACL policy needs to be configured so that only PC1 can access the FTP server.

**Figure 1** Network diagram for configuring a device as an FTP server![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001512831086.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure the FTP server function for the device and configure information about an FTP user, including the source address, user name, password, user privilege level, service type, and authorized directory.
2. Configure access permissions on the FTP server.
3. Save the current configuration file on the device.
4. Log in to the FTP server from PC1.
5. Upload the system software to the device and back up the configuration file of the device to PC1.

#### Configuration Precautions

In insecure network environments, you are advised to use a secure password authentication mode, encryption authentication algorithm, or protocol. For details about secure configuration examples, see [Example for Configuring a Device as an SFTP Server (IPv4)](vrp_file_cfg_0016.html).


#### Procedure

1. Run the **install feature-software WEAKEA** command in the user view to install the weak security algorithm/protocol feature package (WEAKEA).
2. Configure an IP address for the FTP server.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname FTP_Server
   [*HUAWEI] commit
   [~FTP_Server] interface 100ge 1/0/1
   [*SSH Server-100GE1/0/1] undo portswitch
   [*FTP_Server-100GE1/0/1] ip address 10.136.23.5 255.255.255.0
   [*FTP_Server-100GE1/0/1] quit
   [*FTP_Server] commit
   ```
3. Configure the FTP server function for the device and configure information about an FTP user.
   
   
   ```
   [~FTP_Server] ftp server enable
   [*FTP_Server] ftp server source all-interface
   [*FTP_Server] aaa
   [*FTP_Server-aaa] local-user admin1234 password
   Please configure the login password (8-128)
   It is recommended that the password consist of four types of characters, including lowercase letters, uppercase letters, numerals and special characters. 
   Please enter password:                                      
   Please confirm password:                               
   Info: Add a new user.
   [*FTP_Server-aaa] local-user admin1234 privilege level 3
   [*FTP_Server-aaa] local-user admin1234 service-type ftp
   [*FTP_Server-aaa] local-user admin1234 ftp-directory flash:/
   [*FTP_Server-aaa] quit
   [*FTP_Server] commit
   ```
4. Configure access permissions on the FTP server.
   
   
   ```
   [~FTP_Server] acl number 2001
   [*FTP_Server-acl4-basic-2001] rule permit source 10.136.23.10 0 
   [*FTP_Server-acl4-basic-2001] rule deny source 10.136.23.20 0
   [*FTP_Server-acl4-basic-2001] quit
   [*FTP_Server] ftp server acl 2001
   [*FTP_Server] commit
   [~FTP_Server] quit
   ```
5. Save the current configuration file on the device.
   
   
   ```
   <FTP_Server> save
   ```
6. Log in to the FTP server from PC1 using the user name **admin1234** and password **YsHsjx\_202206**. Set the file transfer mode to binary.
   
   
   
   Assume that PC1 runs the Windows operating system.
   
   ```
   C:\Documents and Settings\Administrator> ftp 10.136.23.5
   Connected to 10.136.23.5.
   220 FTP service ready.
   User (10.136.23.5:(none)): admin1234
   331 Password required for admin1234.
   Password:
   230 User logged in.
   ftp> binary
   200 Type set to I.
   ftp>
   ```
7. Upload the system software to the device and back up the configuration file of the device to PC1.
   
   
   
   # Upload the system software to the device.
   
   ```
   ftp> put devicesoft.cc
   200 Port command okay.
   150 Opening BINARY mode data connection for /devicesoft.cc
   226 Transfer complete.
   ftp: 107973953 bytes sent in 151.05Seconds 560.79Kbytes/sec.
   ```
   
   # Back up the configuration file.
   
   ```
   ftp> get vrpcfg.zip
   200 Port command okay.
   150 Opening BINARY mode data connection for /vrpcfg.zip.
   226 Transfer complete.
   ftp: 1257 bytes received in 0.03Seconds 40.55Kbytes/sec.
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   When uploading or downloading files, you need to specify the FTP working directory of the client. For example, the default FTP working directory of the Windows operating system is **C:\Windows\System32**. Save the system software to be uploaded to this directory in advance, and the backup configuration file is also saved to this directory.

#### Verifying the Configuration

# Run the **dir** command on the FTP server to check whether the system software is uploaded to the FTP server.

```
<FTP_Server> dir
Directory of flash:/

  Idx  Attr     Size(Byte)  Date        Time       FileName
    0  -rw-             14  Mar 13 2019 14:13:38   back_time_a
    1  drw-              -  Mar 11 2019 00:58:54   logfile
    2  -rw-              4  Nov 17 2019 09:33:58   snmpnotilog.txt
    3  -rw-         11,238  Mar 12 2019 21:15:56   private-data.txt
    4  -rw-          1,257  Mar 12 2019 21:15:54   vrpcfg.zip
    5  -rw-             14  Mar 13 2019 14:13:38   back_time_b
    6  -rw-    107,973,953  Mar 13 2019 14:24:24   devicesoft.cc
    7  drw-              -  Oct 31 2019 10:20:28   sysdrv
    8  drw-              -  Feb 21 2019 17:16:36   compatible
    9  drw-              -  Feb 09 2019 14:20:10   selftest
   10  -rw-         19,174  Feb 20 2019 18:55:32   backup.cfg
   11  -rw-         23,496  Oct 15 2019 20:59:36   20191015.zip
   12  -rw-            588  Nov 04 2019 13:54:04   servercert.der
   13  -rw-            320  Nov 04 2019 13:54:26   serverkey.der
   14  drw-              -  Nov 04 2019 13:58:36   security
...
670,092 KB total (569,904 KB free)
```

# Access the FTP user's working directory on PC1 and check for the **vrpcfg.zip** file.


#### Configuration Scripts

```
#
sysname FTP_Server
# 
acl number 2001
 rule 5 permit source 10.136.23.10 0
 rule 10 deny source 10.136.23.20 0
#
ftp server enable
ftp server source all-interface
ftp server acl 2001
#
aaa
 local-user admin1234 password irreversible-cipher $1d$g8wLJ`LjL!$CyE(V{3qg5DdU:PM[6=6O$UF-.fQ,Q}>^)OBzgoU$
 local-user admin1234 privilege level 3
 local-user admin1234 ftp-directory flash:
 local-user admin1234 service-type ftp
#
interface 100GE1/0/1
 undo portswitch
 ip address 10.136.23.5 255.255.255.0
#
return
```