Example for Establishing an EVC Model
=====================================

This section provides an example for establishing an EVC model to implement inter-VLAN communication.

#### Networking Requirements

If various communities share the same services, such as Internet, Internet Protocol Television (IPTV), and Voice Over IP (VoIP), to facilitate management, each service can be assigned a VLAN in each community. The same service may be assigned different VLANs in different communities.

On the network shown in [Figure 1](#EN-US_TASK_0172363404__fig_dc_vrp_evc_cfg_001901), community 1 and community 2 have the same services. A service of the two communities is transmitted using the same VLAN, but a service is transmitted using different VLANs in the two communities. Devices using the same service but in different VLANs in the two communities need to communicate. To meet this requirement, an EVC model can be deployed, which has a low cost.

**Figure 1** Networking diagram for an EVC model![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, subinterface2.1, subinterface1.1, and subinterface1.2 represent GE0/1/2.1, GE0/1/1.1, and GE0/1/1.2, respectively.


  
![](images/fig_dc_vrp_evc_cfg_001901.png)

#### Precautions

Services in all VLANs are on the same network segment.


#### Configuration Roadmap

The EVC configuration roadmap is as follows:

1. Assign device interfaces in community 1 to VLAN10, and assign device interfaces in community 2 to VLAN30.
2. Configure an EVC model on a PE:
   1. Configure a bridge domain to forward services.
   2. Create an EVC Layer 2 sub-interface, add it to the bridge domain, and specify traffic encapsulation types and behaviors on the EVC Layer 2 sub-interface.

#### Data Preparation

To complete the configuration, you need the following data:

* Number of each interface connecting each device to users
* Number of each interface connecting each device to another device
* ID of each VLAN to which each interface belongs
* Bridge domain ID


#### Procedure

1. Assign interfaces connecting each CE to users to a specified VLAN.
   
   
   
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
   [~CE1] vlan 10
   ```
   ```
   [*CE1-vlan10] quit
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
   [*CE1-GigabitEthernet0/1/1] port default vlan 10
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
   [*CE1-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] port trunk allow-pass vlan 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE1] commit
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
   [~CE2] vlan batch 10 30
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
   [*CE2-GigabitEthernet0/1/1] port default vlan 30
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
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
   [*CE2-GigabitEthernet0/1/3] port link-type access
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] port default vlan 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/3] quit
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
   [*CE2-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] port trunk allow-pass vlan 10 30
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE2] commit
   ```
2. Establish an EVC model.
   
   
   1. Configure a bridge domain on each PE.
      
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
      [~PE1] bridge-domain 10
      ```
      ```
      [~PE1-bd10] quit
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
      [~PE2] bridge-domain 10
      ```
      ```
      [~PE2-bd10] quit
      ```
   2. Create an EVC Layer 2 sub-interface on each PE, add the EVC Layer 2 sub-interface to a bridge domain, and specify traffic encapsulation and behaviors on the EVC Layer 2 sub-interface.
      
      # Configure PE1.
      
      ```
      [*PE1] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/1.1 mode l2
      ```
      ```
      [*PE1-GigabitEthernet0/1/1.1] encapsulation dot1q vid 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/1.1] bridge-domain 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/1.1] quit
      ```
      ```
      [~PE1] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE1] interface gigabitethernet 0/1/2.1 mode l2
      ```
      ```
      [*PE1-GigabitEthernet0/1/2.1] encapsulation dot1q vid 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/2.1] bridge-domain 10
      ```
      ```
      [*PE1-GigabitEthernet0/1/2.1] commit
      ```
      ```
      [~PE1-GigabitEthernet0/1/2] quit
      ```
      
      # Configure PE2.
      
      ```
      [*PE2] interface gigabitethernet 0/1/1
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/1.1 mode l2
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.1] encapsulation dot1q vid 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.1] bridge-domain 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.1] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/1.2 mode l2
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.2] encapsulation dot1q vid 30
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.2] rewrite map 1-to-1 vid 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.2] bridge-domain 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/1.2] quit
      ```
      ```
      [~PE2] interface gigabitethernet 0/1/2
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] undo shutdown
      ```
      ```
      [*PE2-GigabitEthernet0/1/2] quit
      ```
      ```
      [*PE2] interface gigabitethernet 0/1/2.1 mode l2
      ```
      ```
      [*PE2-GigabitEthernet0/1/2.1] encapsulation dot1q vid 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/2.1] bridge-domain 10
      ```
      ```
      [*PE2-GigabitEthernet0/1/2.1] commit
      ```
      ```
      [~PE2-GigabitEthernet0/1/2] quit
      ```
3. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) command. The command output shows the BD to which an EVC Layer 2 sub-interface belongs and the BD status. The following example uses the command output on PE1.
   
   ```
   [~PE1] display bridge-domain
   ```
   ```
   The total number of bridge-domains is : 1
   --------------------------------------------------------------------------------
   MAC_LRN: MAC learning;         STAT: Statistics;         SPLIT: Split-horizon;
   BC: Broadcast;                 MC: Unknown multicast;    UC: Unknown unicast;
   *down: Administratively down;  FWD: Forward;             DSD: Discard;
   --------------------------------------------------------------------------------
   
   BDID  State MAC-LRN STAT    BC  MC  UC  SPLIT   Description
   --------------------------------------------------------------------------------
   10    up    enable  disable FWD FWD FWD disable
   ```
   
   Run the [**display ethernet uni information**](cmdqueryname=display+ethernet+uni+information) command. The command output shows the traffic encapsulation type and behavior configured on an EVC Layer 2 sub-interface. The following example uses the command output on PE2.
   
   ```
   [~PE2] display ethernet uni information
   ```
   ```
     GigabitEthernet0/1/1.1
       Total encapsulation number: 1
         encapsulation dot1q vid 10
       No action
     GigabitEthernet0/1/1.2
       Total encapsulation number: 1
         encapsulation dot1q vid 30
       Rewrite map 1-to-1 vid 10
     GigabitEthernet0/1/2.1
       Total encapsulation number: 1
         encapsulation dot1q vid 10
       No action
   ```
   
   With the EVC model, users in two communities can communicate across VLANs.

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  bridge-domain 10
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  bridge-domain 10
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface GigabitEthernet0/1/1.2 mode l2
   encapsulation dot1q vid 30
   rewrite map 1-to-1 vid 10
   bridge-domain 10
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  vlan batch 10
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  vlan batch 10 30
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type access
   port default vlan 30
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10 30
  #
  interface GigabitEthernet0/1/3
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
  #
  return
  ```