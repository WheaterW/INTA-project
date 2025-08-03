Example for Configuring a Device as a TFTP Client
=================================================

Example for Configuring a Device as a TFTP Client

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563750985__fig_dc_cfg_file_002301), the remote device with IP address 10.1.1.1/24 functions as the TFTP server. The device with IP address 10.2.1.1/24 functions as the TFTP client and has reachable routes to the TFTP server.

The TFTP client needs to be upgraded. To be specific, you need to download the system software from the TFTP server to the TFTP client and back up the current configuration file of the TFTP client to the TFTP server.

**Figure 1** Network diagram for accessing files on another device using TFTP![](public_sys-resources/note_3.0-en-us.png) 

SFTP V2 or SCP is more secure than TFTP, and is therefore recommended.

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001512671498.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Run the TFTP software on the TFTP server and set the TFTP working directory.
2. Upload files from and download files to the TFTP client using TFTP commands.

#### Configuration Precautions

In insecure network environments, you are advised to use a secure password authentication mode, encryption authentication algorithm, or protocol. For details about secure configuration examples, see [Example for Configuring a Device as an SCP Client](vrp_file_cfg_0021.html).


#### Procedure

1. Run the **install feature-software WEAKEA** command in the user view to install the weak security algorithm/protocol feature package (WEAKEA).
2. Run the TFTP software on the TFTP server and set the TFTP working directory. For details, see the help document of the third-party software.
3. Upload files from and download files to the TFTP client using TFTP commands.
   
   
   ```
   <HUAWEI> tftp 10.1.1.1 get devicesoft.cc
   Info: Transfer file in binary mode.
   Please wait for a while...
   /    107973953 bytes transferred
   Info: Downloaded the file successfully.
   <HUAWEI> tftp 10.1.1.1 put vrpcfg.zip 
   Info: Transfer file in binary mode.
   Please wait for a while...
   /     100% [***********]
   Info: Uploaded the file successfully. 
   ```

#### Verifying the Configuration

# Run the **dir** command on the TFTP client to check whether the system software is successfully downloaded.

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

# Access the working directory on the TFTP server and check whether the **vrpcfg.zip** file has been uploaded successfully.


#### Configuration Scripts

None