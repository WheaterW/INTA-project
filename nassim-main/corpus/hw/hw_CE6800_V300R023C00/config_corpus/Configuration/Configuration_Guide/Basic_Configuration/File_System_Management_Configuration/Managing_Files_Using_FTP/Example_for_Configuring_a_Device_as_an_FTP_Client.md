Example for Configuring a Device as an FTP Client
=================================================

Example for Configuring a Device as an FTP Client

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513150630__fig_dc_cfg_file_002401), the remote device with IP address 10.1.1.1/24 functions as the FTP server. The device with IP address 10.2.1.1/24 functions as the FTP client and has reachable routes to the FTP server.

The FTP client needs to be upgraded. To be specific, you need to download the system software from the FTP server to the FTP client and back up the current configuration file of the FTP client to the FTP server.

**Figure 1** Network diagram for accessing files on another device using FTP![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001563990913.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Run the FTP software on the FTP server and configure an FTP user.
2. Establish a connection between the FTP client and FTP server.
3. Download files from and upload files to the FTP server using FTP commands.

#### Configuration Precautions

In insecure network environments, you are advised to use a secure password authentication mode, encryption authentication algorithm, or protocol. For details about secure configuration examples, see [Example for Configuring a Device as an SFTP Client (Password Authentication and RSA Authentication)](vrp_file_cfg_0017.html).


#### Procedure

1. Run the **install feature-software WEAKEA** command in the user view to install the weak security algorithm/protocol feature package (WEAKEA).
2. Run the FTP software on the FTP server and configure an FTP user. For details, see the help document of the third-party software.
3. Establish a connection between the FTP client and FTP server.
   
   
   ```
   <HUAWEI> ftp 10.1.1.1
   Trying 10.1.1.1 ...
   Press CTRL + K to abort
   Connected to 10.1.1.1.
   220 FTP service ready.
   User(10.1.1.1:(none)):admin
   331 Password required for admin.
   Enter password:
   230 User logged in.                  
   [ftp] 
   ```
4. Download files from and upload files to the FTP server using FTP commands.
   
   
   ```
   [ftp] binary
   200 Type is Image (Binary)
   [ftp] get devicesoft.cc
   500 Unidentified command SIZE test123.cfg   
   200 PORT command okay
   150 "D:\FTP\test123.cfg" file ready to send (3544 bytes) in IMAGE / Binary mode
   .. 
   226 Transfer finished successfully.  
   FTP: 107973953 byte(s) received in 151.05 second(s) 560.79Kbyte(s)/sec.   
   [ftp] put vrpcfg.zip
   200 PORT command okay 
   150 "D:\FTP\vrpcfg.zip" file ready to receive in IMAGE / Binary mode
   /     100% [***********]
   226 Transfer finished successfully.
   FTP: 1257 byte(s) send in 0.03 second(s) 40.55Kbyte(s)/sec.    
   [ftp] quit
   ```

#### Verifying the Configuration

# Run the **dir** command on the FTP client to check whether the system software is successfully downloaded.

```
<HUAWEI> dir
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

# Access the working directory on the FTP server and check for the **vrpcfg.zip** file.


#### Configuration Scripts

None