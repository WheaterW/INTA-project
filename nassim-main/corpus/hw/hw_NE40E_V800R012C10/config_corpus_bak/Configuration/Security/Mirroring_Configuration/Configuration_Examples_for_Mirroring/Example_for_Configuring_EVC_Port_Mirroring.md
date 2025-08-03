Example for Configuring EVC Port Mirroring
==========================================

Example_for_Configuring_EVC_Port_Mirroring

#### Networking Requirements

This section provides an example for configuring port mirroring for the traffic of an EVC Layer 2 sub-interface through the EVC model.

On the network shown in [Figure 1](#EN-US_TASK_0172343810__fig_dc_ne_portmirror_cfg_002801), services such as Internet, IPTV, and VoIP services are deployed in communities 1 and 2. To facilitate management, network administrators allocate the same services to the same VLAN, and allocate different services to different VLANs. In addition, an EVC model is used to achieve service interworking between the two communities.

For security purposes, VLAN 10 traffic transmitted from CE1 to PE1 through sub-interface 1.1 needs to be monitored and analyzed. This can be achieved by specifying interface 2 on PE1 as an observing port and configuring port mirroring on sub-interface 1.1. In this way, all the packets received through sub-interface 1.1 are copied to interface 2 for analysis by the analyzer.

**Figure 1** Networking diagram for configuring EVC port mirroring![](../../../../public_sys-resources/note_3.0-en-us.png) 

* The configurations in this example are performed on CE1, CE2, PE1, and PE2. The HUAWEI NE40E-M2 series functions only as PE1.
* Interface 1, sub-interface 1.1, sub-interface 1.2, interface 2, interface 3, and interface 4 in this example represent GE0/1/1, GE0/1/1.1, GE0/1/1.2, GE0/2/1, GE0/1/2, and GE0/1/3, respectively.

  
![](images/fig_dc_ne_portmirror_cfg_002801.png)

#### Configuration Notes

Services in all VLANs are on the same subnet.


#### Configuration Roadmap

Deploy EVC port mirroring to configure the EVC Layer 2 sub-interface GE0/1/1.1 as a mirrored port and GE0/2/1 as an observing port. In this way, the inbound traffic of GE0/1/1.1 is copied to GE0/2/1 for analysis by the analyzer.

The configuration roadmap is as follows:

1. Deploy an EVC model to achieve service interworking between communities 1 and 2.
2. Configure GE0/2/1 on PE1 as an observing port to which the copied traffic is sent.
3. Configure GE0/1/1.1 on PE1 as a mirrored port so that the inbound traffic of GE0/1/1.1 is copied.
4. Specify the observing port for mirroring and enable the device to mirror the traffic entering GE0/1/1.1.

#### Data Preparation

To complete the configuration, you need the following data:

* Numbers of interfaces connecting devices to the user side
* Numbers of interfaces interconnecting devices
* IDs of VLANs to which services belong
* BD IDs
* Mirroring instance name
* Number of the mirrored port
* Number of the observing port


#### Procedure

1. Deploy an EVC model to achieve service interworking between communities 1 and 2.
   
   
   
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
   [*PE1-bd10] quit
   ```
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
   [*PE2-bd10] quit
   ```
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
2. Configure GE0/2/1 on PE1 as an observing port.
   
   
   ```
   [*PE1] interface gigabitethernet 0/2/1
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] port-observing observe-index 1
   ```
   ```
   [*PE1-GigabitEthernet0/2/1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/2/1] quit
   ```
3. Configure GE0/1/1.1 on PE1 as a mirrored port.
   
   
   ```
   [*PE1] mirror instance evcto201 location
   ```
   ```
   [*PE1] commit
   ```
   ```
   [~PE1] interface gigabitethernet 0/1/1.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet0/1/1.1] port-mirroring instance evcto201 inbound vid 10 identifier none
   ```
   ```
   [*PE1-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/1.1] quit
   ```
4. Map the mirrored port to the observing port.
   
   
   ```
   [*PE1] slot 1
   ```
   ```
   [*PE1-slot1] mirror to observe-index 1
   ```
   ```
   [*PE1-slot1] commit
   ```
   ```
   [~PE1-slot1] quit
   ```
5. Verify the configuration.
   
   
   
   After completing the preceding configuration, run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) command to check BD information, including the BD to which an EVC Layer 2 sub-interface belongs and the BD status. The following example uses the command output on PE1.
   
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
   
   Run the [**display ethernet uni information**](cmdqueryname=display+ethernet+uni+information) command. The command output shows the traffic encapsulation and traffic behavior information configured on each EVC Layer 2 sub-interface. The following example uses the command output on PE2.
   
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
   
   Through the EVC model, the users in community 1 and community 2 can communicate with each other.
   
   Run the [**display mirror instance**](cmdqueryname=display+mirror+instance) [ *instance-name* ] **location** command to check the configuration of the specified mirroring instance on an EVC Layer 2 sub-interface.
   
   ```
   [~PE1] display mirror instance location
   instance evcto201 
       car                   : -
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mirror instance evcto201 location
  #
  slot 1 
   mirror to observe-index 1
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
   port-mirroring instance evcto201 inbound vid 10 identifier none
  #
  interface GigabitEthernet0/1/2
   undo shutdown
  #
  interface GigabitEthernet0/1/2.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface GigabitEthernet0/2/1
   port-observing observe-index 1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
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
  vlan 10
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
  sysname CE1
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