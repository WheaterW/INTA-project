Example for Configuring Port-based VLAN Assignment
==================================================

The networking in this example is simple. After VLANs are assigned, users in different VLANs cannot directly communicate with each other at Layer 2, but users in the same VLAN can do so.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172363164__fig_dc_vrp_vlan_cfg_003401), a department has multiple project teams. To improve service security, it is required that employees in the same project team can communicate with each other but employees in different project teams cannot communicate with each other.

**Figure 1** Networking for port-based VLAN assignment![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 4 represent GE0/1/1, GE0/1/2, GE0/1/3, and GE0/1/4, respectively.


  
![](figure/en-us_image_0000001367586377.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VLANs and determine mappings between employees and VLANs.
2. Configure port types to determine the device connected to each port.
3. Add the port connected to group 1 to VLAN 2 and the port connected to group 2 to VLAN 3 to prevent employees in group 1 from communicating with employees in group 2.

#### Data Preparation

To complete the configuration, you need the following data:

* Number of each port connecting CE to a PC
* ID of each VLAN

#### Procedure

1. Create VLANs.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE] vlan batch 2 3
   ```
2. Configure port types.
   
   
   ```
   [*CE] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/1] port link-type access
   ```
   ```
   [*CE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE] interface gigabitethernet 0/1/2
   ```
   ```
   [*CE-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/2] port link-type access
   ```
   ```
   [*CE-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE] interface GigabitEthernet 0/1/3
   ```
   ```
   [*CE-GigabitEthernet0/1/3] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/3] port link-type access
   ```
   ```
   [*CE-GigabitEthernet0/1/3] quit
   ```
   ```
   [*CE] interface GigabitEthernet 0/1/4
   ```
   ```
   [*CE-GigabitEthernet0/1/4] portswitch
   ```
   ```
   [*CE-GigabitEthernet0/1/4] undo shutdown
   ```
   ```
   [*CE-GigabitEthernet0/1/4] port link-type access
   ```
   ```
   [*CE-GigabitEthernet0/1/4] quit
   ```
3. Add ports to VLANs.
   
   
   
   # Add GE 0/1/1 and GE 0/1/2 to VLAN 2.
   
   ```
   [*CE] vlan 2
   ```
   ```
   [*CE-vlan2] port gigabitethernet 0/1/1 to 0/1/2
   ```
   ```
   [*CE-vlan2] quit
   ```
   
   # Add GE 0/1/3 and GE 0/1/4 to VLAN 3.
   
   ```
   [*CE] vlan 3
   ```
   ```
   [*CE-vlan3] port gigabitethernet 0/1/3 to 0/1/4
   ```
   ```
   [*CE-vlan3]quit
   ```
   ```
   [*CE] commit
   ```
4. Verify the configuration.
   
   
   
   After the configurations are complete, run the [**display vlan**](cmdqueryname=display+vlan) command to view the VLAN status.
   
   ```
   [~CE] display vlan
   ```
   ```
   The total number of vlans is : 2                                               
   VID  Type     Status  Property  MAC-LRN STAT    BC  MC  UC  Description         
   --------------------------------------------------------------------------------
      2 common   enable  default   enable  disable FWD FWD FWD VLAN 0002
      3 common   enable  default   enable  disable FWD FWD FWD VLAN 0003
   ```
   
   Ping a PC in group 2 from a PC in group 1. The ping fails. PCs in the same group can ping each other successfully.

#### Configuration Files

```
#
```
```
sysname CE
```
```
#
```
```
vlan batch 2 3
```
```
#
```
```
interface GigabitEthernet0/1/1
```
```
 portswitch
```
```
 undo shutdown
```
```
 port link-type access
```
```
 port default vlan 2
```
```
#
```
```
interface GigabitEthernet0/1/2
```
```
 portswitch
```
```
 undo shutdown
```
```
 port link-type access
```
```
 port default vlan 2
```
```
#
```
```
interface GigabitEthernet0/1/3
```
```
 portswitch
```
```
 undo shutdown
```
```
 port link-type access
```
```
 port default vlan 3
```
```
#
```
```
interface GigabitEthernet0/1/4
```
```
 portswitch
```
```
 undo shutdown
```
```
 port link-type access
```
```
 port default vlan 3
```
```
#
```
```
return
```