Example for Configuring IPSG Based on a Dynamic Binding Table in a VLAN
=======================================================================

Example for Configuring IPSG Based on a Dynamic Binding Table in a VLAN

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001563889233__fig718132012204), PC1 and PC2 access the network through DeviceA. The administrator wants the PCs to use dynamically allocated IP addresses to access the Internet and deny the access to the Internet if statically configured IP addresses are used.

**Figure 1** Network diagram of configuring IPSG based on a dynamic binding table in a VLAN![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001512849718.png)

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
   [*DeviceA-100GE1/0/3] port link-type trunk
   [*DeviceA-100GE1/0/3] port trunk allow-pass vlan 10
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
2. Enable DHCP snooping and configure 100GE1/0/3 for connecting to the DHCP server as a trusted interface.
   
   
   ```
   [~DeviceA] dhcp enable
   [*DeviceA] dhcp snooping enable
   [*DeviceA] vlan 10
   [*DeviceA-vlan10] dhcp snooping enable
   [*DeviceA-vlan10] dhcp snooping trusted interface 100GE 1/0/3
   [*DeviceA] commit
   ```
3. Enable IPSG in VLAN 10 of DeviceA.
   
   
   ```
   [~DeviceA-vlan10] ipv4 source check user-bind enable
   [*DeviceA-vlan10] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

# Display dynamic binding entries.

```
[~DeviceA] display ip source check user-bind status
DHCP Bind-table on slot 1: 
-------------------------------------------------------------------------------- 
IP Address                MAC Address         Vlan(O/I)        Interface      
                                              Type             Status                                                                        
-------------------------------------------------------------------------------- 
10.1.1.254               00e0-fc12-3456       10   /-          100GE1/0/1    
                                              Dynamic            IPv4/-
10.1.1.253               00e0-fc12-3478       10   /-          100GE1/0/2     
                                              Dynamic             IPv4/-
-------------------------------------------------------------------------------- 
Total count:           2                      
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
# 
vlan 10
 dhcp snooping enable 
 dhcp snooping trusted interface 100GE1/0/3
 ipv4 source check user-bind enable
#
interface 100GE1/0/1   
 port default vlan 10
#
interface 100GE1/0/2  
 port default vlan 10
#
interface 100GE1/0/3
 port link-type trunk  
 port trunk allow-pass vlan 10  
#
return
```