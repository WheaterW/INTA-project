Example for Configuring MAC Address Learning Limit on an Interface
==================================================================

Example for Configuring MAC Address Learning Limit on an Interface

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001176664487__fig_dc_cfg_mac_006401), user networks 1 and 2 belong to VLAN 10 and VLAN 20, respectively. The two user networks are connected to DeviceA through DeviceB, and DeviceA is connected to DeviceB through 100GE 1/0/1. To control the number of access users on DeviceA, configure MAC address learning limit on 100GE 1/0/1.

**Figure 1** Networking of MAC address learning limit on an interface![](public_sys-resources/note_3.0-en-us.png) 

Interface 1 in this example represents 100GE 1/0/1.


  
![](figure/en-us_image_0000001176744421.png)![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this function.




#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VLANs and add 100GE 1/0/1 to them to implement Layer 2 forwarding.
2. Configure MAC address learning limit on 100GE 1/0/1 to control the number of access users.

#### Procedure

1. Create VLANs and add 100GE 1/0/1 to them.
   
   
   
   # Add 100GE 1/0/1 to VLAN 10 and VLAN 20.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 10 20
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 10 20
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
2. Configure MAC address learning limit on 100GE 1/0/1.
   
   
   
   # Set the maximum number of MAC addresses that can be dynamically learned on 100GE 1/0/1 to 100, and configure DeviceA to generate an alarm when the number of learned MAC addresses exceeds the limit.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] mac-address limit maximum 100 alarm enable 
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display mac-address limit** command in any view to check whether the maximum number of MAC address entries that can be dynamically learned and the action for the device to take when the configured maximum number is reached are configured successfully.

```
[~DeviceA] display mac-address limit
MAC Address Limit is enabled
Total MAC Address limit rule count : 1

Port                 VLAN/VSI/SI/BD      Slot Maximum      Action     Alarm
----------------------------------------------------------------------------    
100GE1/0/1            --               --   100          discard    enable     
```

#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 10 20
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 10 20
 mac-address limit maximum 100 alarm enable 
#
return
```