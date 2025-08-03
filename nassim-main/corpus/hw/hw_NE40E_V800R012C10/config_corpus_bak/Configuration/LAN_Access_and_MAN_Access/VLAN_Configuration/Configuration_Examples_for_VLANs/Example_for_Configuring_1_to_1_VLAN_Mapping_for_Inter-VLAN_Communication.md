Example for Configuring 1 to 1 VLAN Mapping for Inter-VLAN Communication
========================================================================

1 to 1 VLAN mapping allows user VLAN IDs and the ISP VLAN ID to be replaced with each other to help users in different VLANs to communicate with each other.

#### Networking Requirements

Users in different residential compounds use Internet access, IPTV, and VoIP services. To simplify management, the network administrator of each residential compound configures a separate VLAN for each type of services. After the configuration, users using the same type of services in different residential compounds belong to different VLANs, but they need to communicate with each other.

On the network shown in [Figure 1](#EN-US_TASK_0172363180__fig_dc_vrp_vlan_cfg_006001), the same type of services in residential compounds 1 and 2 belong to different VLANs. It is required that these users communicate with each other at a low operating cost.

**Figure 1** Network diagram of configuring 1 to 1 VLAN mapping for inter-VLAN communication![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interfaces 1 through 3 represent GE0/1/1, GE0/1/2, and GE0/1/3, respectively.


  
![](figure/en-us_image_0000001371705773.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Add ports connecting CE1 to residential compound 1 to VLAN 6. Add ports connecting CE2 to residential compound 2 to VLAN 5.
2. Configure 1 to 1 VLAN mapping on devices at the edge of the ISP network to map user VLAN IDs to the ISP VLAN ID to allow users in different VLANs to communicate with each other.

#### Data Preparation

To complete the configuration, you need the following data:

* Number of each port connecting a CE to a user device
* Number of the ports interconnecting CEs
* VLAN IDs configured on CEs
* VLAN ID provided by the ISP

#### Procedure

1. Add ports connecting CEs to user devices to specified VLANs.
   
   
   
   # Configure CE1.
   
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
   [~CE1] vlan 6
   ```
   ```
   [*CE1-vlan6] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port link-type access
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] port default vlan 6
   ```
   ```
   [*CE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/2
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] port link-type access
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] port default vlan 6
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE1] interface gigabitethernet 0/1/3
   ```
   ```
   [*CE1-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*CE1-GigabitEthernet0/1/3] portswitch
   ```
   ```
   [*CE1-GigabitEthernet0/1/3] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/1/3] port trunk allow-pass vlan 6
   ```
   ```
   [*CE1-GigabitEthernet0/1/3] commit
   ```
   ```
   [~CE1-GigabitEthernet0/1/3] quit
   ```
   
   # Configure CE2.
   
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
   [~CE2] vlan 5
   ```
   ```
   [*CE2-vlan5] quit
   ```
   ```
   [*CE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] portswitch
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
   [*CE2-GigabitEthernet0/1/2] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] portswitch
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
   [*CE2-GigabitEthernet0/1/3] undo shutdown
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] portswitch
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] port trunk allow-pass vlan 5
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] commit
   ```
   ```
   [~CE2-GigabitEthernet0/1/3] quit
   ```
2. Configure 1 to 1 VLAN mapping.
   
   
   
   # Configure PE1.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE1
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE1] vlan 10
   ```
   ```
   [*PE1-vlan10] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] port trunk allow-pass vlan 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] port vlan-mapping vlan 6 map-vlan 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/1] quit
   ```
   
   # Configure PE2.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname PE2
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~PE2] vlan 10
   ```
   ```
   [*PE2-vlan10] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] undo shutdown
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] portswitch
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] port link-type trunk
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] port trunk allow-pass vlan 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] port vlan-mapping vlan 5 map-vlan 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/1] quit
   ```
3. Verify the configuration.
   
   
   
   After completing the configurations, run the **display vlan** command to check VLAN mapping information. Use the display on PE1 as an example.
   
   ```
   [*PE1] display vlan 10
   ```
   ```
   * : management-vlan
   ---------------------
   VLAN ID Type         Status   MAC Learning Broadcast/Multicast/Unicast Property
   --------------------------------------------------------------------------------
   10      common       enable   enable       forward   forward   forward default
   ----------------
   QinQ-map  Port: GigabitEthernet0/1/1
   ----------------
   Interface                   Physical
   GigabitEthernet0/1/1        UP
   
   ```
   
   Users in residential compounds 1 and 2 can communicate with each other.

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
  vlan batch 6
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port link-type access
  ```
  ```
   port default vlan 6
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/2
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port link-type access
  ```
  ```
   port default vlan 6
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/3
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port link-type trunk
  ```
  ```
   port trunk allow-pass vlan 6
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
  vlan batch 5
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
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
   undo shutdown
  ```
  ```
   portswitch
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
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port link-type trunk
  ```
  ```
   port trunk allow-pass vlan 5
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE1 configuration file
  
  ```
  #
  ```
  ```
  sysname PE1
  ```
  ```
  #
  ```
  ```
  vlan batch 10
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port link-type trunk
  ```
  ```
   port trunk allow-pass vlan 10
  ```
  ```
   port vlan-mapping vlan 6 map-vlan 10
  ```
  ```
  #
  ```
  ```
  return
  ```
* PE2 configuration file
  
  ```
  #
  ```
  ```
  sysname PE2
  ```
  ```
  #
  ```
  ```
  vlan batch 10
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/1
  ```
  ```
   undo shutdown
  ```
  ```
   portswitch
  ```
  ```
   port link-type trunk
  ```
  ```
   port trunk allow-pass vlan 10
  ```
  ```
   port vlan-mapping vlan 5 map-vlan 10
  ```
  ```
  #
  ```
  ```
  return
  ```