Example for Configuring MAC Address Learning Limit in a VLAN
============================================================

Example for Configuring MAC Address Learning Limit in a VLAN

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130784732__fig_dc_cfg_mac_003401), user network 1 is connected to DeviceA through DeviceB, and DeviceA uses 100GE 1/0/1. Likewise, user network 2 is connected to DeviceA through DeviceC, and DeviceA uses 100GE 1/0/2. 100GE 1/0/1 and 100GE 1/0/2 both belong to VLAN 2. To control the number of access users, configure MAC address learning limit in VLAN 2.

**Figure 1** Networking of MAC address learning limit in a VLAN![](public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001176744411.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VLAN 2 and add 100GE 1/0/1 and 100GE 1/0/2 to it to implement Layer 2 forwarding.
2. Configure MAC address learning limit on 100GE 1/0/1 and 100GE 1/0/2 to control the number of access users.

#### Procedure

1. Create a VLAN and add 100GE 1/0/1 and 100GE 1/0/2 to it.
   
   
   
   # Add 100GE 1/0/1 and 100GE 1/0/2 to VLAN 2.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 2
   [*DeviceA-vlan2] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type trunk
   [*DeviceA-100GE1/0/1] port trunk allow-pass vlan 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type trunk
   [*DeviceA-100GE1/0/2] port trunk allow-pass vlan 2
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
2. Configure MAC address learning limit in VLAN 2.
   
   
   
   # Set the maximum number of MAC address entries that can be dynamically learned in VLAN 2 to 100, and set an action for the device to take to forward when the configured maximum number is reached. New MAC addresses are not added to the MAC address table.
   
   ```
   [~DeviceA] vlan 2
   [~DeviceA-vlan2] mac-address limit maximum 100 action forward
   [*DeviceA-vlan2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display mac-address limit** command in any view to check whether the maximum number of MAC address entries that can be dynamically learned and the action for the device to take when the configured maximum number is reached are configured successfully.

```
[~DeviceA] display mac-address limit
MAC Address Limit is enabled
Total MAC Address limit rule count : 1

Port                 VLAN/VSI/SI/BD      Slot Maximum Action  Alarm
-------------------------------------------------------------------
--                   2                --       100 forward enable
```

#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 2
#
vlan 2
 mac-address limit maximum 100 action forward
#
interface 100GE1/0/1
 port link-type trunk
 port trunk allow-pass vlan 2
#
interface 100GE1/0/2
 port link-type trunk
 port trunk allow-pass vlan 2
#
return
```