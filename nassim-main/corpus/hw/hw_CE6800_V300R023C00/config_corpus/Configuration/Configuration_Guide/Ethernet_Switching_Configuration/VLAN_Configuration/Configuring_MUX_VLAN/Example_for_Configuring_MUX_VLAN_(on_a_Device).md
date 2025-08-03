Example for Configuring MUX VLAN (on a Device)
==============================================

Example for Configuring MUX VLAN (on a Device)

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176742303__fig229313713402), hosts communicate with the server through DeviceA. Hosts and the server are on the same network segment. It is required that hosts in VLAN 3 can communicate with each other, but hosts in VLAN 4 cannot communicate with each other.

**Figure 1** Network diagram of configuring MUX VLAN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, interface 3, interface 4, and interface 5 represent 100GE 1/0/1, 100GE 1/0/2, 100GE 1/0/3, 100GE 1/0/4, and 100GE 1/0/5, respectively.


  
![](figure/en-us_image_0000001130622886.png)

#### Procedure

1. Create VLANs.
   
   
   ```
   <HUAWEI> system-view 
   [~HUAWEI] sysname DeviceA 
   [*HUAWEI] commit
   [~DeviceA] vlan batch 2 3 4
   [*DeviceA] commit
   ```
2. Configure MUX VLAN. Configure VLAN 2 as a principal VLAN, VLAN 3 as a group VLAN, and VLAN 4 as a separate VLAN.
   
   
   ```
   [~DeviceA] vlan 2
   [*DeviceA-vlan2] mux-vlan
   [*DeviceA-vlan2] subordinate group 3
   [*DeviceA-vlan2] subordinate separate 4
   [*DeviceA-vlan2] quit 
   [*DeviceA] commit
   ```
3. Add interfaces to VLANs and enable the MUX VLAN function on the interfaces.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] portswitch
   [~DeviceA-100GE1/0/1] port link-type access
   [~DeviceA-100GE1/0/1] port default vlan 2
   [*DeviceA-100GE1/0/1] port mux-vlan enable vlan 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 3
   [*DeviceA-100GE1/0/2] port mux-vlan enable vlan 3
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type access
   [*DeviceA-100GE1/0/3] port default vlan 3
   [*DeviceA-100GE1/0/3] port mux-vlan enable vlan 3
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100ge 1/0/4
   [*DeviceA-100GE1/0/4] portswitch
   [*DeviceA-100GE1/0/4] port link-type access
   [*DeviceA-100GE1/0/4] port default vlan 4
   [*DeviceA-100GE1/0/4] port mux-vlan enable vlan 4
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] interface 100ge 1/0/5
   [*DeviceA-100GE1/0/5] portswitch
   [*DeviceA-100GE1/0/5] port link-type access
   [*DeviceA-100GE1/0/5] port default vlan 4
   [*DeviceA-100GE1/0/5] port mux-vlan enable vlan 4
   [*DeviceA-100GE1/0/5] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

* Host1, Host2, Host3, and Host4 can communicate with the server.
* Host1 and Host2 can ping each other.
* Host3 and Host4 cannot ping each other.
* Host1 and Host2 in VLAN 3 and Host3 and Host4 in VLAN 4 cannot ping each other.

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 2 to 4
#
vlan 2
 mux-vlan
 subordinate separate 4
 subordinate group 3
#
interface 100GE1/0/1
 port default vlan 2
 port mux-vlan enable vlan 2
#
interface 100GE1/0/2
 port default vlan 3
 port mux-vlan enable vlan 3
#
interface 100GE1/0/3
 port default vlan 3
 port mux-vlan enable vlan 3
#
interface 100GE1/0/4
 port default vlan 4
 port mux-vlan enable vlan 4
#
interface 100GE1/0/5
 port default vlan 4
 port mux-vlan enable vlan 4
#
return
```