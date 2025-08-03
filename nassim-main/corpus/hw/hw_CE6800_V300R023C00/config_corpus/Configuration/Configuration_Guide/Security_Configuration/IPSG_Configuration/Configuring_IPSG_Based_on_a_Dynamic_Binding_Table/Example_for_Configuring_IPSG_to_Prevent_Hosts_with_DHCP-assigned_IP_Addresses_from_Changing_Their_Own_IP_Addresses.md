Example for Configuring IPSG to Prevent Hosts with DHCP-assigned IP Addresses from Changing Their Own IP Addresses
==================================================================================================================

Example for Configuring IPSG to Prevent Hosts with DHCP-assigned IP Addresses from Changing Their Own IP Addresses

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001522209554__fig12346621111), PC1, PC2, and PC3 connect to the network through DeviceA, DeviceB functions as a DHCP server to dynamically assign IP addresses to PC1 and PC2, PC3 uses a static IP address, and Gateway is the enterprise egress gateway. The administrator hopes that the PC1 and PC2 cannot access the network using static IP addresses configured without permission.

![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


**Figure 1** Network diagram of configuring IPSG to prevent hosts with DHCP-assigned IP addresses from changing their own IP addresses  
![](../images/en-us_image_0000001573744797.png)

#### Procedure

1. Configure the DHCP server function on DeviceB.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*DeviceB] commit
   [~DeviceB] vlan batch 10
   [*DeviceB] interface 100GE 1/0/1
   [*DeviceB-100GE1/0/1] port link-type trunk
   [*DeviceB-100GE1/0/1] port trunk allow-pass vlan 10
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] dhcp enable
   [*DeviceB] ip pool 10
   [*DeviceB-ip-pool-10] network 10.1.1.0 mask 24
   [*DeviceB-ip-pool-10] gateway-list 10.1.1.1
   [*DeviceB-ip-pool-10] quit
   [*DeviceB] interface vlanif 10
   [*DeviceB-Vlanif10] dhcp enable
   [*DeviceB] interface vlanif 10
   [*DeviceB-Vlanif10] ip address 10.1.1.1 255.255.255.0
   [*DeviceB-Vlanif10] dhcp select global
   [*DeviceB-Vlanif10] quit
   [*DeviceB] commit
   ```
2. Configure DHCP snooping on DeviceA.
   
   
   
   # Create a VLAN and add interfaces to the VLAN.
   
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*DeviceA] commit
   [~DeviceA] vlan batch 10
   [*DeviceA] interface 100GE 1/0/1
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE 1/0/2
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 10
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100GE 1/0/3
   [*DeviceA-100GE1/0/3] port link-type access
   [*DeviceA-100GE1/0/3] port default vlan 10
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] interface 100GE 1/0/4
   [*DeviceA-100GE1/0/4] port link-type trunk
   [*DeviceA-100GE1/0/4] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/4] quit
   [*DeviceA] commit
   ```
   
   # Enable DHCP snooping and configure 100GE1/0/4 for connecting to the DHCP server as a trusted interface.
   
   
   
   ```
   [~DeviceA] dhcp enable
   [*DeviceA] dhcp snooping enable
   [*DeviceA] vlan 10
   [*DeviceA-vlan10] dhcp snooping enable
   [*DeviceA-vlan10] dhcp snooping trusted interface 100GE 1/0/4
   [*DeviceA] commit
   ```
3. Create a static binding entry for PC3.
   
   
   ```
   [~DeviceA] user-bind static ip-address 10.0.0.3 mac-address 00e0-fc12-3489 interface 100GE 1/0/3 vlan 10
   [*DeviceA] commit
   ```
4. Enable IPSG in VLAN 10.
   
   
   ```
   [~DeviceA] vlan 10
   [*DeviceA-vlan10] ipv4 source check user-bind enable
   [*DeviceA-vlan10] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display dynamic binding entries corresponding to PC1 and PC2.

```
[~DeviceA] display dhcp snooping user-bind all
DHCP Dynamic Bind-table: 
Flags:O - outer vlan ,I - inner vlan ,P - Vlan-mapping 
IP Address       MAC Address     VSI/VLAN(O/I/P) Interface      Lease            
-------------------------------------------------------------------------------- 
10.1.1.254       00e0-fc12-3456  10  /--  /--    GE100GE1/0/1       2014.08.17-07:31 
10.1.1.253       00e0-fc12-3478  10  /--  /--    GE100GE1/0/2        2014.08.17-07:34 
-------------------------------------------------------------------------------- 
Print count:      2     Total count:      2                 
```

# Display the static binding entry corresponding to PC3.

```
[~DeviceA] display user-bind static all                 
DHCP static Bind-table:                                   
Flags:O - outer vlan ,I - inner vlan 
IP Address           MAC Address   VLAN(O/I)         Interface 
-------------------------------------------------------------------------------- 
10.0.0.3            00e0-fc12-3489   10/--           100GE1/0/3
-------------------------------------------------------------------------------- 
Print count:      1     Total count:      1
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 10
#
dhcp enable
#
dhcp snooping enable
user-bind static ip-address 10.0.0.3 mac-address 00e0-fc12-3489 interface 100GE 1/0/3 vlan 10 
#
vlan 10
 dhcp snooping enable 
 dhcp snooping trusted interface 100GE 1/0/4
 ipv4 source check user-bind enable 
#
interface 100GE 1/0/1
 port default vlan 10 
#
interface 100GE 1/0/2
 port default vlan 10 
#
interface 100GE 1/0/3
 port default vlan 10
#
interface 100GE 1/0/4
 port link-type trunk
 port trunk allow-pass vlan 10
#
return
```

DeviceB

```
#
sysname DeviceB
#
vlan batch 10
#
dhcp enable
#
ip pool 10
 gateway-list 10.1.1.1
 network 10.1.1.0 mask 255.255.255.0
#
interface Vlanif10
 ip address 10.1.1.1 255.255.255.0
 dhcp select global
# 
interface 100GE 1/0/1
 port link-type trunk 
 port trunk allow-pass vlan 10
#
return
```