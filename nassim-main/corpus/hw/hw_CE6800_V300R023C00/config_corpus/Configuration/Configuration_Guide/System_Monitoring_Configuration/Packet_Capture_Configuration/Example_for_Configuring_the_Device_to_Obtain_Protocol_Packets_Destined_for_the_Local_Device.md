Example for Configuring the Device to Obtain Protocol Packets Destined for the Local Device
===========================================================================================

Example for Configuring the Device to Obtain Protocol Packets Destined for the Local Device

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563872221__fig168713817385), DeviceA connects to the Internet through interface 1.

When DeviceA is abnormal, the network administrator needs to obtain all the protocol packets sent from interface 1 to the local device and save the obtained packets to the **capture.cap** file. In this way, the network administrator can process invalid packets promptly to ensure stable running of the local device.

**Figure 1** Network diagram for obtaining protocol packets destined for the local device![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001563872233.png)

#### Procedure

1. Configure DeviceA to obtain packets sent from 100GE 1/0/1 to the local device and save the obtained packets to the **capture.cap** file.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] quit
   <DeviceA> capture-packet local-host interface 100ge 1/0/1 destination file capture.cap
   Warning: The capture packet may disclosure the personal information.
   Warning: Capture-packet data will be saved to flash:/logfile/capture.cap.           
   ```

#### Verifying the Configuration

# Run the [**display capture-packet file flash:/logfile/capture.cap**](cmdqueryname=display+capture-packet+file+flash%3A%2Flogfile%2Fcapture.cap) command on DeviceA to view the content of the **capture.cap** file.

```
<DeviceA> display capture-packet file flash:/logfile/capture.cap
a1 b2 c3 d4 00 02 00 04 00 00 00 00 00 00 00 00
00 00 ff ff 00 00 00 09 4d 10 36 db 00 0a d5 81
00 00 00 0c 00 00 00 0c ff 03 c0 21 09 9d 00 08
8a 8c bc c3 4d 10 36 db 00 0a d6 ae
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
return
```