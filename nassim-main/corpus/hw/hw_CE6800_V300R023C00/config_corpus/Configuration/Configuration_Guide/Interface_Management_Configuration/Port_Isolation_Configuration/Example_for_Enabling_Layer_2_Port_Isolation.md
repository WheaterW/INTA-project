Example for Enabling Layer 2 Port Isolation
===========================================

Example for Enabling Layer 2 Port Isolation

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0000001130784690__fig_dc_cfg_int_004401), PC1, PC2, and PC3 all belong to VLAN 10. PC1 and PC2 are allowed to communicate with PC3, but are not allowed to communicate with each other.

**Figure 1** Network diagram for enabling Layer 2 port isolation![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001176664451.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Add the interfaces to the specified VLAN.
2. Enable port isolation.

#### Precautions

Switching an interface from Layer 3 to Layer 2 is required only when the interface works at Layer 3.



#### Procedure

1. Create VLAN 10 and add interfaces to VLAN 10.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] vlan 10
   [*DeviceA-vlan10] quit
   [*DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 10
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type access
   [*DeviceA-100GE1/0/3] port default vlan 10
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] commit
   ```
2. Enable Layer 2 port isolation.
   
   
   
   # Enable Layer 2 port isolation for 100GE 1/0/1.
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [~DeviceA-100GE1/0/1] port-isolate enable group 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Enable Layer 2 port isolation for 100GE 1/0/2.
   
   ```
   [~DeviceA] interface 100ge 1/0/2
   [~DeviceA-100GE1/0/2] port-isolate enable group 1
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```

#### Verifying the Configuration

* PC1 cannot communicate with PC2.
* PC1 and PC3 can communicate with each other.
* PC2 and PC3 can communicate with each other.

#### Configuration Scripts

DeviceA

```
#
sysname DeviceA
#
vlan batch 10
#
interface 100GE1/0/1
 port default vlan 10 
 port-isolate enable group 1
#
interface 100GE1/0/2
 port default vlan 10 
 port-isolate enable group 1
#
interface 100GE1/0/3
 port default vlan 10 
#
return
```