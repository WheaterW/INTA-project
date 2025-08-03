Example for Configuring Port Security
=====================================

Example for Configuring Port Security

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0000001217042343__fig168879525502), PC1, PC2, and PC3 can communicate with each other in VLAN 10, and connect to the company network through DeviceA. For security purposes, only PC1, PC2, and PC3 can access the company network, and external users cannot access the company network.

**Figure 1** Network diagram of port security![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001219868965.png)

#### Configuration Roadmap

1. Configure a VLAN to enable employee PCs to communicate with each other.
2. Enable port security and limit the number of MAC addresses learned on an interface, so that external users cannot access the company network.

#### Procedure

1. Configure a VLAN.
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] [commit](cmdqueryname=commit)
   [~DeviceA] vlan batch 10
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] portswitch
   [*DeviceA-100GE1/0/1] port link-type access
   [*DeviceA-100GE1/0/1] port default vlan 10
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] portswitch
   [*DeviceA-100GE1/0/2] port link-type access
   [*DeviceA-100GE1/0/2] port default vlan 10
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] portswitch
   [*DeviceA-100GE1/0/3] port link-type access
   [*DeviceA-100GE1/0/3] port default vlan 10
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```
2. Configure port security.
   
   
   ```
   [~DeviceA] interface 100ge 1/0/1
   [*DeviceA-100GE1/0/1] port-security enable maximum 1
   [*DeviceA-100GE1/0/1] port-security mac-address sticky
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] interface 100ge 1/0/2
   [*DeviceA-100GE1/0/2] port-security enable maximum 1
   [*DeviceA-100GE1/0/2] port-security mac-address sticky
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   [~DeviceA] interface 100ge 1/0/3
   [*DeviceA-100GE1/0/3] port-security enable maximum 1
   [*DeviceA-100GE1/0/3] port-security mac-address sticky
   [*DeviceA-100GE1/0/3] quit
   [*DeviceA] [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Only PC1, PC2, and PC3 connected to the three interfaces on DeviceA can access the company network.


#### Configuration Scripts

```
#
 sysname DeviceA
#
vlan batch 10
#
interface 100GE1/0/1
 port default vlan 10
 port-security enable maximum 1
 port-security mac-address sticky
#
interface 100GE1/0/2
 port default vlan 10
 port-security enable maximum 1
 port-security mac-address sticky
#
interface 100GE1/0/3
 port default vlan 10
 port-security enable maximum 1
 port-security mac-address sticky
#
return
```