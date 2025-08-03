Example for Disabling MAC Address Learning in a VLAN
====================================================

Example for Disabling MAC Address Learning in a VLAN

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130784714__fig_dc_cfg_mac_003401), user network 1 is connected to DeviceA through DeviceB, and DeviceA uses 100GE 1/0/1. Likewise, user network 2 is connected to DeviceA through DeviceC, and DeviceA uses 100GE 1/0/2. 100GE 1/0/1 and 100GE 1/0/2 belong to VLAN 2. To prevent hackers from launching attacks with a large number of packets containing forged source MAC addresses, disable MAC address learning in VLAN 2.

**Figure 1** Networking for disabling MAC address learning in a VLAN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001130784736.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create a VLAN and add 100GE 1/0/1 and 100GE 1/0/2 to it to implement Layer 2 forwarding.
2. Disable MAC address learning in VLAN 2 to prevent MAC address attacks.

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
2. Disable MAC address learning in VLAN 2.
   
   
   
   # Disable MAC address learning in VLAN 2.
   
   ```
   [~DeviceA] vlan 2
   [~DeviceA-vlan2] mac-address learning disable
   [*DeviceA-vlan2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Run the **display vlan 2 verbose** command in any view to check whether MAC address learning has been disabled in VLAN 2.

```
[~DeviceA] display vlan 2 verbose
* : Management-VLAN
---------------------
  VLAN ID                     : 2
  VLAN Name                   :
  VLAN Type                   : Common
  Description                 : VLAN 0002
  Status                      : Enable
  Broadcast                   : Enable
  MAC Learning              : Disable
  Smart MAC Learning          : Disable
  Current MAC Learning Result : Enable
  Statistics                  : Disable
  Property                    : Default
  VLAN State                  : Up
  ----------------                                                              
  Tagged        Port: 100GE1/0/1                  100GE1/0/2                    
  ----------------                                                              
  Active  Tag   Port: 100GE1/0/1                  100GE1/0/2                    
---------------------                                                           
Interface                   Physical                                            
100GE1/0/1                   UP                                                
100GE1/0/2                   UP 
```

#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 2
#
vlan 2
 mac-address learning disable
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