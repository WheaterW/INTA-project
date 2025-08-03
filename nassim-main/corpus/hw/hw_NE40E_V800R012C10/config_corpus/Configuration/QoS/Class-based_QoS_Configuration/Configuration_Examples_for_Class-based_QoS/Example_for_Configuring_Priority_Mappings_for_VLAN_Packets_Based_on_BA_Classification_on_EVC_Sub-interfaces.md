Example for Configuring Priority Mappings for VLAN Packets Based on BA Classification on EVC Sub-interfaces
===========================================================================================================

This section provides an example for configuring priority mappings for VLAN packets based on BA classification on EVC sub-interfaces.

#### Networking Requirements

Different communities require the same services, such as Internet access, IPTV, and VoIP services. To facilitate management, network administrators of different communities add services to the same VLAN. They also configure BA classification on PE1 and PE2 (Routers) to provide differentiated services.

As shown in [Figure 1](#EN-US_TASK_0172371321__fig_dc_ne_qos_cfg_007101), communities 1 and 2 have the same services, which belong to the same VLAN. Communities 1 and 2 need to communicate with each other at low costs. In addition, priority mappings need to be configured for DiffServ domains on PE1 and PE2. The outer 802.1p and DSCP values of downstream traffic on the EVC sub-interface GE 0/1/1.1 of PE1 and the outer 802.1p and EXP values of downstream traffic on the EVC sub-interface GE 0/1/1.1 of PE2 need to remain unchanged.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, and Subinterface1.1 in this example represent GE 0/1/1, GE 0/1/2, and GE 0/1/1.1, respectively.


**Figure 1** Networking diagram for configuring EVC QoS  
![](images/fig_dc_ne_qos_feature_new_05701.png)  


#### Configuration Notes

Services in all VLANs are on the same network segment.


#### Configuration Roadmap

Establish an EVC model.

1. Add interfaces of devices in communities 1 and 2 to VLAN 10.
2. Configure an EVC model on each PE:
   
   * Configure a BD to forward services.
   * Create Layer 2 sub-interfaces, add them to the BD, and configure traffic encapsulation on the downstream interface to ensure that communities 1 and 2 can communicate with each other.

Enable BA classification.

1. Configure mappings between the 802.1p priority, service class, and color on the EVC sub-interface GE 0/1/1.1 of PE1.
2. Configure mappings between the 802.1p priority, service class, and color on the EVC sub-interface GE 0/1/1.1 of PE2.

#### Data Preparation

To complete the configuration, you need the following data:

* Numbers of interfaces connecting devices to the user side
* Numbers of interfaces interconnecting devices
* IDs of VLANs to which services belong
* BD IDs
* 802.1p priorities, service classes, and colors to be mapped

#### Procedure

1. Add downstream interfaces of the CEs to a specific VLAN.
   
   
   
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
   [~CE2] vlan 10
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
   [*CE2-GigabitEthernet0/1/1] port default vlan 10
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
   [*CE2-GigabitEthernet0/1/2] port link-type trunk
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] port trunk allow-pass vlan 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*CE2] commit
   ```
2. Establish an EVC model.
   
   
   1. Create BDs on the PEs.
      
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
   2. Create Layer 2 sub-interfaces, add them to the BD, and configure traffic encapsulation and traffic behaviors.
      
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
      [*PE1-GigabitEthernet0/1/1.1] commit
      ```
      ```
      [~PE1-GigabitEthernet0/1/1.1] quit
      ```
      
      # Configure PE2.
      
      ```
      [~PE2] interface gigabitethernet 0/1/1
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
      [*PE2-GigabitEthernet0/1/1.1] commit
      ```
      ```
      [~PE2-GigabitEthernet0/1/1.1] quit
      ```
3. Enable BA classification on the EVC sub-interfaces.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] diffserv domain gina
   ```
   ```
   [*PE1-dsdomain-gina] 8021p-outbound cs6 red map 5
   ```
   ```
   [*PE1-dsdomain-gina] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/1.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet0/1/1.1] trust upstream gina
   ```
   ```
   [*PE1-GigabitEthernet0/1/1.1] qos phb outer-8021p disable
   ```
   ```
   [*PE1-GigabitEthernet0/1/1.1] qos phb dscp disable
   ```
   ```
   [*PE1-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/1.1] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] diffserv domain gina
   ```
   ```
   [*PE2-dsdomain-gina] 8021p-inbound 2 phb af1 green
   ```
   ```
   [*PE2-dsdomain-gina] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/1/1.1 mode l2
   ```
   ```
   [*PE2-GigabitEthernet0/1/1.1] trust upstream gina
   ```
   ```
   [*PE2-GigabitEthernet0/1/1.1] qos phb outer-8021p disable
   ```
   ```
   [*PE2-GigabitEthernet0/1/1.1] qos phb mpls-exp disable
   ```
   ```
   [*P-GigabitEthernet0/1/1.1] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/1] quit
   ```
4. Verify the configuration.
   
   
   
   After completing the configuration, run the [**display bridge-domain**](cmdqueryname=display+bridge-domain) command to check BD information, including the BD to which a Layer 2 sub-interface belongs and the BD status. PE1 is used as an example.
   
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
   
   After completing the configuration, run the [**display diffserv domain**](cmdqueryname=display+diffserv+domain) [ *ds-domain-name* ] [ **8021p** | **dscp** | **exp** ] [ **inbound** | **outbound** ] command to check the DiffServ domain configuration. PE1 is used as an example.
   
   ```
   [~PE1] display diffserv domain gina
   ```
   ```
   Diffserv domain name:gina                                                       
   8021p-inbound 0 phb be green                                                    
   8021p-inbound 1 phb af1 green                                                   
   8021p-inbound 2 phb af2 green                                                   
   8021p-inbound 3 phb af3 green                                                   
   8021p-inbound 4 phb af4 green                                                   
   8021p-inbound 5 phb ef green                                                    
   8021p-inbound 6 phb cs6 green                                                   
   8021p-inbound 7 phb cs7 green                                                   
   8021p-outbound be green map 0                                                   
   8021p-outbound be yellow map 0                                                  
   8021p-outbound be red map 0                                                     
   8021p-outbound af1 green map 1                                                  
   8021p-outbound af1 yellow map 1                                                 
   8021p-outbound af1 red map 1                                                    
   8021p-outbound af2 green map 2                                                  
   8021p-outbound af2 yellow map 2                                                 
   8021p-outbound af2 red map 2                                                    
   8021p-outbound af3 green map 3                                                  
   8021p-outbound af3 yellow map 3                                                 
   8021p-outbound af3 red map 3                                                    
   8021p-outbound af4 green map 4                                                  
   8021p-outbound af4 yellow map 4                                                 
   8021p-outbound af4 red map 4                                                    
   8021p-outbound ef green map 5                                                   
   8021p-outbound ef yellow map 5                                                  
   8021p-outbound ef red map 5                                                     
   8021p-outbound cs6 green map 6                                                  
   8021p-outbound cs6 yellow map 6                                                 
   8021p-outbound cs6 red map 5                                                    
   8021p-outbound cs7 green map 7                                                  
   8021p-outbound cs7 yellow map 7                                                 
   8021p-outbound cs7 red map 7                                                    
   ip-dscp-inbound 0 phb be green                                                  
   ip-dscp-inbound 1 phb be green                                                  
   ip-dscp-inbound 2 phb be green                                                  
   ip-dscp-inbound 3 phb be green                                                  
   ip-dscp-inbound 4 phb be green                                                  
   ip-dscp-inbound 5 phb be green                                                  
   ip-dscp-inbound 6 phb be green                                                  
   ip-dscp-inbound 7 phb be green                                                  
   ip-dscp-inbound 8 phb af1 green                                                 
   ip-dscp-inbound 9 phb be green                                                  
   ip-dscp-inbound 10 phb af1 green                                                
   ip-dscp-inbound 11 phb be green                                                 
   ip-dscp-inbound 12 phb af1 yellow                                               
   ip-dscp-inbound 13 phb be green                                                 
   ip-dscp-inbound 14 phb af1 red                                                  
   ip-dscp-inbound 15 phb be green                                                 
   ip-dscp-inbound 16 phb af2 green                                                
   ip-dscp-inbound 17 phb be green                                                 
   ip-dscp-inbound 18 phb af2 green                                                
   ip-dscp-inbound 19 phb be green                                                 
   ip-dscp-inbound 20 phb af2 yellow                                               
   ip-dscp-inbound 21 phb be green                                                 
   ip-dscp-inbound 22 phb af2 red                                                  
   ip-dscp-inbound 23 phb be green                                                 
   ip-dscp-inbound 24 phb af3 green                                                
   ip-dscp-inbound 25 phb be green                                                 
   ip-dscp-inbound 26 phb af3 green                                                
   ip-dscp-inbound 27 phb be green                                                 
   ip-dscp-inbound 28 phb af3 yellow                                               
   ip-dscp-inbound 29 phb be green                                                 
   ip-dscp-inbound 30 phb af3 red                                                  
   ip-dscp-inbound 31 phb be green                                                 
   ip-dscp-inbound 32 phb af4 green                                                
   ip-dscp-inbound 33 phb be green                                                 
   ip-dscp-inbound 34 phb af4 green                                                
   ip-dscp-inbound 35 phb be green                                                 
   ip-dscp-inbound 36 phb af4 yellow                                               
   ip-dscp-inbound 37 phb be green                                                 
   ip-dscp-inbound 38 phb af4 red                                                  
   ip-dscp-inbound 39 phb be green                                                 
   ip-dscp-inbound 40 phb ef green                                                 
   ip-dscp-inbound 41 phb be green                                                 
   ip-dscp-inbound 42 phb be green                                                 
   ip-dscp-inbound 43 phb be green                                                 
   ip-dscp-inbound 44 phb be green                                                 
   ip-dscp-inbound 45 phb be green                                                 
   ip-dscp-inbound 46 phb ef green                                                 
   ip-dscp-inbound 47 phb be green                                                 
   ip-dscp-inbound 48 phb cs6 green                                                
   ip-dscp-inbound 49 phb be green                                                 
   ip-dscp-inbound 50 phb be green                                                 
   ip-dscp-inbound 51 phb be green                                                 
   ip-dscp-inbound 52 phb be green                                                 
   ip-dscp-inbound 53 phb be green                                                 
   ip-dscp-inbound 54 phb be green                                                 
   ip-dscp-inbound 55 phb be green                                                 
   ip-dscp-inbound 56 phb cs7 green                                                
   ip-dscp-inbound 57 phb be green                                                 
   ip-dscp-inbound 58 phb be green                                                 
   ip-dscp-inbound 59 phb be green                                                 
   ip-dscp-inbound 60 phb be green                                                 
   ip-dscp-inbound 61 phb be green                                                 
   ip-dscp-inbound 62 phb be green                                                 
   ip-dscp-inbound 63 phb be green                                                 
   ip-dscp-outbound be green map 0                                                 
   ip-dscp-outbound be yellow map 0                                                
   ip-dscp-outbound be red map 0                                                   
   ip-dscp-outbound af1 green map 10                                               
   ip-dscp-outbound af1 yellow map 12                                              
   ip-dscp-outbound af1 red map 14                                                 
   ip-dscp-outbound af2 green map 18                                               
   ip-dscp-outbound af2 yellow map 20                                              
   ip-dscp-outbound af2 red map 22                                                 
   ip-dscp-outbound af3 green map 26                                               
   ip-dscp-outbound af3 yellow map 28                                              
   ip-dscp-outbound af3 red map 30                                                 
   ip-dscp-outbound af4 green map 34                                               
   ip-dscp-outbound af4 yellow map 36                                              
   ip-dscp-outbound af4 red map 38                                                 
   ip-dscp-outbound ef green map 46                                                
   ip-dscp-outbound ef yellow map 46                                               
   ip-dscp-outbound ef red map 46                                                  
   ip-dscp-outbound cs6 green map 48                                               
   ip-dscp-outbound cs6 yellow map 48                                              
   ip-dscp-outbound cs6 red map 48                                                 
   ip-dscp-outbound cs7 green map 56                                               
   ip-dscp-outbound cs7 yellow map 56                                              
   ip-dscp-outbound cs7 red map 56
   user-priority 0 phb be green                                                    
   user-priority 1 phb af1 green                                                   
   user-priority 2 phb af2 green                                                   
   user-priority 3 phb af3 green                                                   
   user-priority 4 phb af4 green                                                   
   user-priority 5 phb ef green                                                    
   user-priority 6 phb cs6 green                                                   
   user-priority 7 phb cs7 green 
   mpls-exp-inbound 0 phb be green                                                 
   mpls-exp-inbound 1 phb af1 green                                                
   mpls-exp-inbound 2 phb af2 green                                                
   mpls-exp-inbound 3 phb af3 green                                                
   mpls-exp-inbound 4 phb af4 green                                                
   mpls-exp-inbound 5 phb ef green                                                 
   mpls-exp-inbound 6 phb cs6 green                                                
   mpls-exp-inbound 7 phb cs7 green                                                
   mpls-exp-outbound be green map 0                                                
   mpls-exp-outbound be yellow map 0                                               
   mpls-exp-outbound be red map 0                                                  
   mpls-exp-outbound af1 green map 1                                               
   mpls-exp-outbound af1 yellow map 1                                              
   mpls-exp-outbound af1 red map 1                                                 
   mpls-exp-outbound af2 green map 2                                               
   mpls-exp-outbound af2 yellow map 2                                              
   mpls-exp-outbound af2 red map 2                                                 
   mpls-exp-outbound af3 green map 3                                               
   mpls-exp-outbound af3 yellow map 3                                              
   mpls-exp-outbound af3 red map 3                                                 
   mpls-exp-outbound af4 green map 4                                               
   mpls-exp-outbound af4 yellow map 4                                              
   mpls-exp-outbound af4 red map 4                                                 
   mpls-exp-outbound ef green map 5                                                
   mpls-exp-outbound ef yellow map 5                                               
   mpls-exp-outbound ef red map 5                                                  
   mpls-exp-outbound cs6 green map 6                                               
   mpls-exp-outbound cs6 yellow map 6                                              
   mpls-exp-outbound cs6 red map 6                                                 
   mpls-exp-outbound cs7 green map 7                                               
   mpls-exp-outbound cs7 yellow map 7                                              
   mpls-exp-outbound cs7 red map 7                                                 
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  diffserv domain gina
   8021p-outbound cs6 red map 5
  #
  bridge-domain 10
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
   trust upstream gina
   qos phb outer-8021p disable  
   qos phb dscp disable
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  diffserv domain gina
   8021p-inbound 2 phb af1 green
  #
  bridge-domain 10
  #
  interface GigabitEthernet0/1/1
   undo shutdown
  #
  interface GigabitEthernet0/1/1.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
   trust upstream gina
   qos phb outer-8021p disable
   qos phb mpls-exp disable
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
   dcn
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
  vlan 10
  #
  interface GigabitEthernet0/1/1
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
   dcn
  #
  interface GigabitEthernet0/1/2
   portswitch
   undo shutdown
   port link-type trunk
   port trunk allow-pass vlan 10
  #
  return
  ```