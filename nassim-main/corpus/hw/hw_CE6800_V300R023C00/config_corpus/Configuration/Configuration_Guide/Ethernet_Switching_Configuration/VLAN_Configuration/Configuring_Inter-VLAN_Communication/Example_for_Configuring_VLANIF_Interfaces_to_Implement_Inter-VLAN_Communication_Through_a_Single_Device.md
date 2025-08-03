Example for Configuring VLANIF Interfaces to Implement Inter-VLAN Communication Through a Single Device
=======================================================================================================

Example for Configuring VLANIF Interfaces to Implement Inter-VLAN Communication Through a Single Device

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130782662__fig19632192318597), the two hosts connected to DeviceA are located on different network segments. One belongs to VLAN 2, and the other belongs to VLAN 3. Both hosts need to communicate with each other.

**Figure 1** Networking diagram for configuring VLANIF interfaces to implement inter-VLAN communication through a single device![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1 and interface 2 represent 100GE 1/0/1 and 100GE 1/0/2, respectively.


  
![](figure/en-us_image_0000001130622924.png)

#### Procedure

1. Create VLANs and add interfaces to the VLANs.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan batch 2 3
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 2
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 3
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
2. Configure an IP address for each VLANIF interface.
   
   
   ```
   [~DeviceA] interface vlanif 2
   [*DeviceA-Vlanif2] ip address 10.10.10.2 24
   [*DeviceA-Vlanif2] quit
   [*DeviceA] interface vlanif 3
   [*DeviceA-Vlanif3] ip address 10.10.20.2 24
   [*DeviceA-Vlanif3] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

Set the IP address of the host in VLAN 2 to 10.10.10.1/24 and default gateway address to 10.10.10.2/24 (IP address of VLANIF 2), and set the IP address of the host in VLAN 3 to 10.10.20.1/24 and default gateway address to 10.10.20.2/24 (IP address of VLANIF 3). After the configuration is complete, hosts in VLAN 2 and VLAN 3 can ping each other.


#### Configuration Scripts

```
#
sysname DeviceA
#
vlan batch 2 to 3
# 
interface Vlanif2
 ip address 10.10.10.2 255.255.255.0 
# 
interface Vlanif3
 ip address 10.10.20.2 255.255.255.0 
# 
interface 100GE1/0/1
 port default vlan 2
#
interface 100GE1/0/2
 port default vlan 3
#
return
```