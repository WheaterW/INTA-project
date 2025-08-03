Example for Configuring the Device to Obtain Hardware-Forwarded Packets
=======================================================================

Example for Configuring the Device to Obtain Hardware-Forwarded Packets

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001512832702__fig168713817385), DeviceA connects to the Internet through interface 1.

When traffic forwarding on DeviceA is abnormal, the network administrator needs to obtain packets forwarded by interface 1 on DeviceA and save the obtained packets to the **capture.cap** file. In this way, the network administrator can process invalid packets promptly to ensure correct data transmission.

**Figure 1** Network diagram for obtaining hardware-forwarded packets![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001563752609.png)

#### Procedure

1. Configure DeviceA to obtain packets forwarded by 100GE 1/0/1 and save the obtained packets to the **capture.cap** file.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] quit
   <DeviceA> capture-packet interface 100ge 1/0/1 destination file capture.cap
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