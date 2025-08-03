Example for Configuring Users in a VLAN to Communicate by Using a Trunk Link
============================================================================

If employees of a department work in different buildings, devices in the buildings can be connected by using a trunk link to allow the employees to communicate.

#### Networking Requirements

A company has several departments. Employees of each department reside in different buildings.

On the network shown in [Figure 1](#EN-US_TASK_0172363172__fig_dc_vrp_vlan_cfg_003501), employees of the financial or marketing department work in different buildings. It is required that employees of the same department can communicate with each other but employees of different departments cannot communicate with each other.

**Figure 1** Configuring users in a VLAN to communicate by using a trunk link![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 5 are GE0/1/1, GE0/1/2, GE0/1/3, GE0/1/4, and GE0/1/5, respectively.


  
![](figure/en-us_image_0000001316416682.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Add the device port connected to the financial department to VLAN 5 and the device port connected to the marketing department to VLAN 9 to isolate these two departments.
2. Configure links between CEs and PE as trunk links to allow frames from VLAN 5 and VLAN 9 to pass through, allowing employees of the same department but different buildings to communicate with each other.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only Layer 2 ports are able to identify frames with tags. Therefore, you need to switch the interfaces connecting PEs and CEs to Layer 2 ports.

#### Data Preparation

To complete the configuration, you need the following data:

* Number of each port connecting a CE to a PC
* Number of each port connecting a CE to the PE
* Number of each port connecting the PE to a CE
* ID of each VLAN

#### Procedure

1. Add the downlink interfaces of the CEs to the specified VLANs.
   
   
   
   # Configure CE 1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE1] vlan batch 5 9
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port link-type access
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port default vlan 5
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/2
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] port link-type access
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] port default vlan 5
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/3
   ```
   ```
   [*CE1-GigabitEthernet0/1/3] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/3] port link-type access
   ```
   ```
   [*CE1-GigabitEthernet0/1/3] port default vlan 9
   ```
   ```
   [*CE1-GigabitEthernet0/1/3] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/4
   ```
   ```
   [*CE1-GigabitEthernet0/1/4] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/4] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/4] port link-type access
   ```
   ```
   [*CE1-GigabitEthernet0/1/4] port default vlan 9
   ```
   ```
   [*CE1-GigabitEthernet0/1/4] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/4] quit
   ```
   
   # Configure CE 2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname CE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~CE2] vlan batch 5 9
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port link-type access
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] port default vlan 5
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/2
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] port link-type access
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] port default vlan 5
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/3
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] port link-type access
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] port default vlan 9
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/4
   ```
   ```
   [*CE2-GigabitEthernet0/1/4] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/4] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/4] port link-type access
   ```
   ```
   [*CE2-GigabitEthernet0/1/4] port default vlan 9
   ```
   ```
   [*CE2-GigabitEthernet0/1/4] commit
   ```
   ```
   [~CE2-GigabitEthernet0/1/4] quit
   ```
2. Configure links between CEs and the PE as trunk links.
   
   
   
   # Configure CE 1.
   
   ```
   [*CE1] interface gigabitethernet 0/1/5
   ```
   ```
   [*CE1-GigabitEthernet0/1/5] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/5] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/5] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/1/5] port trunk allow-pass vlan 5 9
   ```
   ```
   [*CE1-GigabitEthernet0/1/5] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE 2.
   
   ```
   [*CE2] interface gigabitethernet 0/1/5
   ```
   ```
   [*CE2-GigabitEthernet0/1/5] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/5] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/5] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/5] port trunk allow-pass vlan 5 9
   ```
   ```
   [*CE2-GigabitEthernet0/1/5] quit
   ```
   ```
   [*CE2] commit
   ```
3. Configure PE.
   
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*PE-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*PE-GigabitEthernet0/1/1] port trunk allow-pass vlan 5 9
   ```
   ```
   [*PE-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE] interface gigabitethernet 0/1/2
   ```
   ```
   [*PE-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*PE-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*PE-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*PE-GigabitEthernet0/1/2] port trunk allow-pass vlan 5 9
   ```
   ```
   [*PE-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE] commit
   ```
4. Verify the configuration.
   
   
   
   After the configurations are complete, run the [**display vlan**](cmdqueryname=display+vlan) command to view VLAN status. In the following example, the display on CE1 is used:
   
   ```
   [~CE1] display vlan 5
   ```
   ```
   --------------------------------------------------------------------------------
   U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
   MP: Vlan-mapping;               ST: Vlan-stacking;
   #: ProtocolTransparent-vlan;    *: Management-vlan;
   --------------------------------------------------------------------------------
   
   VID  Type    Ports
   --------------------------------------------------------------------------------
   5    common  UT:0/1/1(U)     0/1/2(U)
                TG:0/1/5(U)
   
   VID  Status  Property      MAC-LRN Statistics Description
   --------------------------------------------------------------------------------
   5    enable  default       enable  disable    VLAN 0005  
   ```
   
   Run the [**display port vlan**](cmdqueryname=display+port+vlan) command to view the list of VLANs configured on the trunk port. The following uses CE1 as an example:
   
   ```
   [*CE1] display port vlan gigabitethernet0/1/5
   ```
   ```
   Port                     Link Type    PVID    Trunk VLAN List
   --------------------------------------------------------------
   GigabitEthernet0/1/5     trunk        0       5 9
   ```
   
   In either VLAN 5 or VLAN 9, a PC connected to CE 1 can ping a PC connected to CE 2 successfully.

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  ```
  ```
   sysname CE1
  ```
  ```
  #
  ```
  ```
   vlan batch 5 9
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
   port default vlan 5
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
   port default vlan 5
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
   port default vlan 9
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
   port default vlan 9
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/5
  ```
  ```
   portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   port link-type trunk
  ```
  ```
   port trunk allow-pass vlan 5 9
  ```
  ```
  #
  ```
  ```
  return
  ```
* CE2 configuration file
  
  ```
  #
  ```
  ```
   sysname CE2
  ```
  ```
  #
  ```
  ```
   vlan batch 5 9
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
   port default vlan 5
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
   port default vlan 5
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
   port default vlan 9
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
   port default vlan 9
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/5
  ```
  ```
   portswitch
  ```
  ```
   undo shutdown
  ```
  ```
   port link-type trunk
  ```
  ```
   port trunk allow-pass vlan 5 9
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE configuration file
  
  ```
  #
  ```
  ```
   sysname PE
  ```
  ```
  #
  ```
  ```
   vlan batch 5 9
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
   port link-type trunk
  ```
  ```
   port trunk allow-pass vlan 5 9
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
   port link-type trunk
  ```
  ```
   port trunk allow-pass vlan 5 9
  ```
  ```
  #
  ```
  ```
  return
  ```