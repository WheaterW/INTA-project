Example for Configuring Packet Trace
====================================

Example for Configuring Packet Trace

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001564116393__fig_01), Host1 and Host2 are connected to DeviceB through DeviceA, and DeviceB is connected to an external network. Traffic sent from Host1 and Host2 is forwarded to the external network through DeviceB. However, as some packets sent from Host1 and Host2 are lost, the network administrator has determined that packet loss occurs on DeviceB. In this scenario, the network administrator can configure packet trace on DeviceB to locate the packet loss cause.

![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 represents 100GE 1/0/1.


**Figure 1** Network diagram of packet trace  
![](figure/en-us_image_0000001563996565.png)

#### Procedure

1. Use a packet obtaining tool to obtain the content (hexadecimal character string) of the packet discarded by DeviceB.
2. Configure a packet trace profile on DeviceB.
   
   
   
   # Configure a packet trace profile on DeviceB by specifying the detection packet content, which is the packet content obtained in step 1.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] detector packet-trace profile test packet 286ed489a46300005e00010b0800450000343ba44000fd0677fd0a87002c0a87b4e81a6805d67407d364ebadef9a50189f96d84300000a8001aec0cf84cf6b7f6d84
   [*DeviceB] commit
   ```
3. Specify an interface for receiving the detection packet to simulate packet forwarding inside DeviceB.
   
   
   
   # On DeviceB, specify 100GE 1/0/1 as the interface for receiving detection packets and display the cause of any discarded service packets. If the cause is displayed as **VLAN not valid**, check the VLAN configuration.
   
   ```
   [~DeviceB] display detector packet-trace profile test interface 100ge 1/0/1 result
   Packet trace result:
   --------------------------------------------------------------------------------
   Packet Profile                  : test
   Packet Inbound Interface        : 100GE 1/0/1
   Packet Outbound VLAN            : -
   Packet drop cause               : VLAN not valid
   --------------------------------------------------------------------------------
   ```

#### Verifying the Configuration

Display information about the packet trace profile configured on DeviceB.

```
<DeviceB> display detector packet-trace profile
Packet trace profile Maximum: 16
Total: 1
Packet trace profile: test
-------------------------------------------------------------------------------
Packet             : 286ed489a46300005e00010b0800450000343ba44000fd0677fd0a8700
                     2c0a87b4e81a6805d67407d364ebadef9a50189f96d84300000a8001ae
                     c0cf84cf6b7f6d84
-------------------------------------------------------------------------------
```

#### Configuration Scripts

DeviceB

```
#
sysname DeviceB
#
detector packet-trace profile test packet 286ed489a46300005e00010b0800450000343ba44000fd0677fd0a87002c0a87b4e81a6805d67407d364ebadef9a50189f96d84300000a8001aec0cf84cf6b7f6d84
#
return
```