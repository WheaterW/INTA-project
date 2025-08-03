Example for Upgrading a New Device
==================================

Example for Upgrading a New Device

#### Networking Requirements

Use a console cable (serial cable) and a network cable to set up a network between your PC and the device. Specifically, connect the console cable from your PC to the console port of the device, and connect the network cable from your PC to any Ethernet interface on the device, as shown in [Figure 1](#EN-US_TASK_0000001609058757__fig17492611181218).

**Figure 1** Network diagram for upgrading a new device  
![](figure/en-us_image_0000001619018317.png)
![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.



#### Configuration Roadmap

1. Log in to the device through the console port.
2. Run any FTP software on the PC and configure an FTP user.
3. Configure the management IP address of the device so that the device and the PC reside on the same network segment.
4. Configure the device as the FTP client to obtain the system software package from the PC and check whether the system software package is successfully loaded.
5. Specify the system software and patch for next startup.
6. Restart the device.

#### Configuration Precautions

* Prepare the upgrade tools, including the PC, network cable, and serial cable.
* Obtain the target system software.
  + Visit [Huawei enterprise technical support website](https://support.huawei.com/enterprise/en/index.html) and select the corresponding product in the software download area.
  + Select software of the required version.
  + Click **Download** next to the ***product*****\_*****version*****.cc** file of the required version.
* Obtain the target patch file.
  + Visit [Huawei enterprise technical support website](https://support.huawei.com/enterprise/en/index.html) and select the corresponding product in the software download area.
  + Select software of the required version.
  + Click **Download** next to the ***product*****\_*****version*****.PAT** file of the required version.
* SFTP is recommended because it is more secure than FTP.

#### Procedure

1. Log in to the device from the PC through the console port. For details, see [First Login Through the Console Port](vrp_first_cfg_0004.html).
2. Run the **install feature-software WEAKEA** command in the user view to install the weak security algorithm/protocol feature package (WEAKEA).
3. Run any FTP software on the PC.
4. Configure a management IP address for the device to ensure that the device and PC reside in the same network segment and can ping each other.
   
   
   
   # Configure a management IP address for the device.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] interface 100ge 1/0/1 
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ip address 10.10.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
5. Establish an FTP connection between the device and the PC.
   
   
   ```
   <DeviceA> ftp 10.10.1.2
   Trying 10.10.1.2 ...
   Press CTRL + K to abort
   Connected to 10.10.1.2.
   220 FTP service ready.
   User(10.10.1.2:(none)):admin
   331 Password required for admin.
   Enter password:
   230 User logged in.                  
   [ftp] 
   ```
6. Configure the device as the FTP client to transfer files to the PC using FTP commands.
   
   
   ```
   [ftp] binary
   200 Type is Image (Binary)
   [ftp] get product_version.cc    //Load the system software to the device. product_version.cc is the file name of the system software.
   500 Unidentified command SIZE product_version.cc   
   200 PORT command okay
   150 "D:\FTP\product_version.cc" file ready to send (3544 bytes) in IMAGE / Binary mode
   .. 
   226 Transfer finished successfully.  
   FTP: 107973953 byte(s) received in 151.05 second(s) 560.79Kbyte(s)/sec.   
   [ftp] get product_version.PAT   //Load the patch file to the device. product_version.PAT is the file name of the system patch.
   200 PORT command okay 
   150 "D:\FTP\product_version.PAT" file ready to receive in IMAGE / Binary mode
   /     100% [***********]
   226 Transfer finished successfully.
   FTP: 1257 byte(s) send in 0.03 second(s) 40.55Kbyte(s)/sec.    
   [ftp] quit
   ```
7. Check whether the system software and patch are successfully loaded.
   
   
   ```
   <DeviceA> dir
   Directory of flash:/
   
   Idx  Attr     Size(Byte)  Date        Time       FileName    0  -rw-             14  Mar 13 2019 14:13:38   back_time_a
       1  drw-              -  Mar 11 2019 00:58:54   logfile
       2  -rw-              4  Nov 17 2019 09:33:58   snmpnotilog.txt
       3  -rw-         11,238  Mar 12 2019 21:15:56   private-data.txt
       4  -rw-          1,257  Mar 12 2019 21:15:54   vrpcfg.zip
       5  -rw-             14  Mar 13 2019 14:13:38   back_time_b
       6  -rw-    107,973,953  Mar 13 2019 14:24:24   product_version.cc
       7  -rw-      3,973,953  Mar 13 2019 14:24:24   product_version.PAT
       8  drw-              -  Oct 31 2019 10:20:28   sysdrv
       9  drw-              -  Feb 21 2019 17:16:36   compatible
      10  drw-              -  Feb 09 2019 14:20:10   selftest
      11  -rw-         19,174  Feb 20 2019 18:55:32   backup.cfg
      12  -rw-         23,496  Oct 15 2019 20:59:36   20191015.zip
      13  -rw-            588  Nov 04 2019 13:54:04   servercert.der
      14  -rw-            320  Nov 04 2019 13:54:26   serverkey.der
      15  drw-              -  Nov 04 2019 13:58:36   security
   ...
   670,092 KB total (569,904 KB free)
   ```
8. Specify the system software and patch for next startup.
   
   
   ```
   <DeviceA> startup system-software product_version.cc   //Specify the system software for next startup.
   <DeviceA> startup patch product_version.PAT all   //Specify the patch for next startup. If the current version does not have a corresponding patch, you do not need to run this command.
   ```
9. Check the boot items for next startup. (The actual command output varies depending on the device. The following command output is only an example.)
   
   
   ```
   <DeviceA> display startup
   MainBoard:   
     Configured startup system software:        flash:/basicsoft.cc   
     Startup system software:                   flash:/basicsoft.cc   
     Next startup system software:              flash:/product_version.cc   
     Startup saved-configuration file:          flash:/vrpcfg.zip   
     Next startup saved-configuration file:     flash:/vrpcfg.zip   
     Startup paf file:                          default   
     Next startup paf file:                     default   
     Startup patch package:                     flash:/basicsoft.PAT   
     Next startup patch package:                flash:/product_version.PAT
   ```
10. Restart the device.
    
    
    ```
    <DeviceA> reboot fast
    MPU 6:
    Next startup system software:  flash:/product_version.cc
    Next startup saved-configuration file: flash:/vrpcfg.zip
    Next startup paf file: default
    Next startup patch package: NULL
    Warning: The system will reboot. Continue? [Y/N]:y 
    ```

#### Verifying the Configuration

# Wait several minutes until the device restart is complete. Then run the **display version** command to check the current system version. If the version is new, the upgrade has succeeded.


#### Configuration Scripts

```
#
sysname DeviceA 
#
interface 100GE1/0/1
 undo portswitch 
 ip address 10.10.1.1 255.255.255.0
#
return 
```