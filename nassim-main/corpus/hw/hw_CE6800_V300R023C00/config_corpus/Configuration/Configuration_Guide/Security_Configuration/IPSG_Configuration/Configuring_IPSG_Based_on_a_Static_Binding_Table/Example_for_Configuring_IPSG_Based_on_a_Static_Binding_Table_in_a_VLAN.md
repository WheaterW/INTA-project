Example for Configuring IPSG Based on a Static Binding Table in a VLAN
======================================================================

Example for Configuring IPSG Based on a Static Binding Table in a VLAN

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001513049270__fig773733913179), PC1 and PC2 access the network through DeviceA, and they both use static IP addresses. The Gateway functions as the enterprise egress gateway. The administrator wants the PCs to use fixed IP addresses to access the Internet through fixed interfaces. For security purposes, the administrator does not allow external hosts to access the intranet without permission.

**Figure 1** Network diagram of configuring IPSG based on a static binding table in a VLAN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent 100GE1/0/1, 100GE1/0/2, 100GE1/0/3, and 100GE1/0/4, respectively.


  
![](figure/en-us_image_0000001512849706.png)

#### Procedure

1. Create a VLAN and add interfaces to the VLAN.
   
   
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
2. Configure static binding entries on 100GE1/0/1 and 100GE1/0/2 of DeviceA.
   
   
   ```
   [~DeviceA] user-bind static ip-address 10.0.0.1 mac-address 00e0-fc12-3456 interface 100GE 1/0/1
   [*DeviceA] user-bind static ip-address 10.0.0.2 mac-address 00e0-fc12-3478 interface 100GE 1/0/2
   [*DeviceA] commit
   ```
3. Configure the upstream interface 100GE1/0/4 as a trusted interface.
   
   
   ```
   [~DeviceA] dhcp enable
   [*DeviceA] dhcp snooping enable
   [*DeviceA] interface 100GE 1/0/4
   [*DeviceA-100GE1/0/4] dhcp snooping trusted
   [*DeviceA-100GE1/0/4] quit
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

# Display static binding entries.

```
[~DeviceA] display ip source check user-bind status
DHCP Bind-table on slot 1:  
-------------------------------------------------------------------------------- 
IP Address          MAC Address           Vlan(O/I)        Interface    
                                           Type             Status                                                                        
-------------------------------------------------------------------------------- 
10.0.0.1           00e0-fc12-3456         -   /-           100GE1/0/1      
                                           Static           IPv4/-
10.0.0.2           00e0-fc12-3478         -   /-           100GE1/0/2      
                                           Static           IPv4/-
-------------------------------------------------------------------------------- 
Total count:           2                      
```

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
# 
dhcp enable  
# 
dhcp snooping enable
user-bind static ip-address 10.0.0.1 mac-address 00e0-fc12-3456 interface 100GE1/0/1
user-bind static ip-address 10.0.0.2 mac-address 00e0-fc12-3478 interface 100GE1/0/2
# 
vlan batch 10
# 
vlan 10  
 ipv4 source check user-bind enable
#
interface 100GE1/0/1   
 port link-type access
 port default vlan 10
#
interface 100GE1/0/2    
 port link-type access
 port default vlan 10
#
interface 100GE1/0/3  
 port link-type access
 port default vlan 10
#
interface 100GE1/0/4
 port link-type trunk  
 port trunk allow-pass vlan 10  
 dhcp snooping trusted
#
return
```