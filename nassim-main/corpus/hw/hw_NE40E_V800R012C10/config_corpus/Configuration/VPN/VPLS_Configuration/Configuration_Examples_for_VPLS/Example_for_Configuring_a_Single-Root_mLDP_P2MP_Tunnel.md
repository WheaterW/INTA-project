Example for Configuring a Single-Root mLDP P2MP Tunnel
======================================================

This section provides an example for configuring mLDP P2MP tunnels.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370278__fig_dc_vrp_vpls_cfg_507201), PE1, PE2, PE3, and PE4 use BGP AD to establish a full-mesh multicast VPLS network. PE1 functions as the root node, PE2 a bud node, and PE3 and PE4 the leaf nodes. (The configurations on bud and leaf nodes are the same.) To carry multicast services, configure mLDP P2MP tunnels. The configuration simplifies network deployment.

**Figure 1** Configuring mLDP P2MP tunnels![](../../../../public_sys-resources/note_3.0-en-us.png) 

* In this example, interface1, interface2, interface3, and subinterface4.1 represent GE0/1/0, GE0/1/1, GE0/1/2, and GE0/1/3.1, respectively.

  
![](images/fig_dc_vrp_vpls_cfg_507201.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a routing protocol for each involved interface to ensure IP connectivity at the network layer. This example uses OSPF as the routing protocol.
2. Configure an MPLS LSR ID and globally enable MPLS, MPLS LDP, and mLDP P2MP.
3. Configure a local LDP session on each PE.
4. Configure BGP AD VPLS among PE1, PE2, PE3, and PE4.
5. Configure PE1 as the root node.
6. Configure PE2, PE3, and PE4 as leaf nodes.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of involved interfaces
* OSPF process ID (100) and area ID (0.0.0.0) for each node
* BGP AS numbers of PE1, PE2, PE3, and PE4
* VSI names, VPLS IDs, and VPN targets
* Number of the interface bound to each VSI
* IP address of the mLDP P2MP tunnel's root node (1.1.1.1)

#### Procedure

1. Configure an IP address and a routing protocol for each involved interface to ensure IP connectivity at the network layer.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370278__section_dc_vrp_vpls_cfg_507201).
2. Configure an MPLS LSR ID and globally enable MPLS, MPLS LDP, and mLDP P2MP.
   
   
   
   # Configure PE1.
   
   ```
   <PE1> system-view
   ```
   ```
   [~PE1] mpls lsr-id 1.1.1.1
   ```
   ```
   [*PE1] mpls
   ```
   ```
   [*PE1-mpls] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] mldp p2mp 
   ```
   ```
   [*PE1-mpls-ldp] quit 
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configurations of PE2, PE3, and PE4 are similar to the configuration of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370278__section_dc_vrp_vpls_cfg_507201).
3. Configure a local LDP session on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet0/1/0
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/2
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/1/2] commit
   ```
   
   The configurations of PE2, PE3, and PE4 are similar to the configuration of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370278__section_dc_vrp_vpls_cfg_507201).
4. Configure BGP AD VPLS on PE1, PE2, PE3, and PE4.
   
   # Configure BGP AD VPLS on PE1.
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 connect-interface loopback1
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback1
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 as-number 100
   ```
   ```
   [*PE1-bgp] peer 4.4.4.4 connect-interface loopback1
   ```
   ```
   [*PE1-bgp] l2vpn-ad-family
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] peer 2.2.2.2 enable
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] peer 4.4.4.4 enable
   ```
   ```
   [*PE1-bgp-af-l2vpn-ad] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] mpls l2vpn
   ```
   ```
   [*PE1-l2vpn] quit
   ```
   ```
   [*PE1] vsi vsi1
   ```
   ```
   [*PE1-vsi-vsi1] bgp-ad
   ```
   ```
   [*PE1-vsi-vsi1-bgpad] vpls-id 2:2  
   ```
   ```
   [*PE1-vsi-vsi1-bgpad] vpn-target 2:2 import-extcommunity 
   ```
   ```
   [*PE1-vsi-vsi1-bgpad] vpn-target 2:2 export-extcommunity  
   ```
   ```
   [*PE1-vsi-vsi1-bgpad] quit
   ```
   ```
   [*PE1-vsi-vsi1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] l2 binding vsi vsi1
   ```
   ```
   [*PE1-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure BGP AD VPLS on PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 connect-interface loopback1
   ```
   ```
   [*PE2-bgp] l2vpn-ad-family
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] mpls l2vpn
   ```
   ```
   [*PE2-l2vpn] quit
   ```
   ```
   [*PE2] vsi vsi1
   ```
   ```
   [*PE2-vsi-vsi1] bgp-ad
   ```
   ```
   [*PE2-vsi-vsi1-bgpad] vpls-id 2:2  
   ```
   ```
   [*PE2-vsi-vsi1-bgpad] vpn-target 2:2 import-extcommunity 
   ```
   ```
   [*PE2-vsi-vsi1-bgpad] vpn-target 2:2 export-extcommunity  
   ```
   ```
   [*PE2-vsi-vsi1-bgpad] quit
   ```
   ```
   [*PE2-vsi-vsi1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/3.1
   ```
   ```
   [*PE2-GigabitEthernet0/1/3.1] vlan-type dot1q 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/3.1] l2 binding vsi vsi1
   ```
   ```
   [*PE2-GigabitEthernet0/1/3.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure BGP AD VPLS on PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE3-bgp] peer 1.1.1.1 connect-interface loopback1
   ```
   ```
   [*PE3-bgp] l2vpn-ad-family
   ```
   ```
   [*PE3-bgp-af-l2vpn-ad] peer 1.1.1.1 enable
   ```
   ```
   [*PE3-bgp-af-l2vpn-ad] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] mpls l2vpn
   ```
   ```
   [*PE3] vsi vsi1
   ```
   ```
   [*PE3-vsi-vsi1] bgp-ad
   ```
   ```
   [*PE3-vsi-vsi1-bgpad] vpls-id 2:2  
   ```
   ```
   [*PE3-vsi-vsi1-bgpad] vpn-target 2:2 import-extcommunity 
   ```
   ```
   [*PE3-vsi-vsi1-bgpad] vpn-target 2:2 export-extcommunity  
   ```
   ```
   [*PE3-vsi-vsi1-bgpad] quit
   ```
   ```
   [*PE3-vsi-vsi1] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/1/3.1
   ```
   ```
   [*PE3-GigabitEthernet0/1/3.1] vlan-type dot1q 10
   ```
   ```
   [*PE3-GigabitEthernet0/1/3.1] l2 binding vsi vsi1
   ```
   ```
   [*PE3-GigabitEthernet0/1/3.1] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure BGP AD VPLS on PE4.
   
   ```
   [~PE4] bgp 100
   ```
   ```
   [*PE4-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE4-bgp] peer 1.1.1.1 connect-interface loopback1
   ```
   ```
   [*PE4-bgp] l2vpn-ad-family
   ```
   ```
   [*PE4-bgp-af-l2vpn-ad] peer 1.1.1.1 enable
   ```
   ```
   [*PE4-bgp-af-l2vpn-ad] quit
   ```
   ```
   [*PE4-bgp] quit
   ```
   ```
   [*PE4] mpls l2vpn
   ```
   ```
   [*PE4] vsi vsi1
   ```
   ```
   [*PE4-vsi-vsi1] bgp-ad
   ```
   ```
   [*PE4-vsi-vsi1-bgpad] vpls-id 2:2  
   ```
   ```
   [*PE4-vsi-vsi1-bgpad] vpn-target 2:2 import-extcommunity 
   ```
   ```
   [*PE4-vsi-vsi1-bgpad] vpn-target 2:2 export-extcommunity  
   ```
   ```
   [*PE4-vsi-vsi1-bgpad] quit
   ```
   ```
   [*PE4-vsi-vsi1] quit
   ```
   ```
   [*PE4] interface gigabitethernet0/1/3.1
   ```
   ```
   [*PE4-GigabitEthernet0/1/3.1] vlan-type dot1q 10
   ```
   ```
   [*PE4-GigabitEthernet0/1/3.1] l2 binding vsi vsi1
   ```
   ```
   [*PE4-GigabitEthernet0/1/3.1] quit
   ```
   ```
   [*PE4] commit
   ```
5. Configure PE1 as the root node.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] vsi vsi1
   ```
   ```
   [*PE1-vsi-vsi1] inclusive-provider-tunnel
   ```
   ```
   [*PE1-vsi-vsi1-inclusive] root
   ```
   ```
   [*PE1-vsi-vsi1-inclusive-root] mldp p2mp
   ```
   ```
   [*PE1-vsi-vsi1-inclusive-root-mldpp2mp] root-ip 1.1.1.1
   ```
   ```
   [*PE1-vsi-vsi1-inclusive-root-mldpp2mp] quit
   ```
   ```
   [*PE1-vsi-vsi1-inclusive-root] quit
   ```
   ```
   [*PE1-vsi-vsi1-inclusive] quit
   ```
   ```
   [*PE1-vsi-vsi1] quit
   ```
   ```
   [*PE1] commit
   ```
6. Configure PE2, PE3, and PE4 as leaf nodes.
   
   
   
   # Configure PE2 as a leaf node.
   
   ```
   [~PE2] vsi vsi1
   ```
   ```
   [*PE2-vsi-vsi1] inclusive-provider-tunnel
   ```
   ```
   [*PE2-vsi-vsi1-inclusive] leaf
   ```
   ```
   [*PE2-vsi-vsi1-inclusive-leaf] quit
   ```
   ```
   [*PE2-vsi-vsi1-inclusive] quit
   ```
   ```
   [*PE2-vsi-vsi1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   The configurations of PE3 and PE4 are similar to the configuration of PE2. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370278__section_dc_vrp_vpls_cfg_507201).
7. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display vsi name inclusive-provider-tunnel** command on PE1 to check multicast VPLS tunnel information.
   
   ```
   [~PE1] display vsi name vsi1 inclusive-provider-tunnel
   ```
   ```
   VSI name: vsi1
    Ingress provider tunnel
       PMSI type      : P2MP mLDP
       Root ip        : 1.1.1.1
       Opaque value   : 01000400002001
       State         : up
       Leaf list count: 3
       Leaf list      : 2.2.2.2
                        3.3.3.3
                        4.4.4.4
     Egress provider tunnel
     Egress PMSI count: 0
   
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi1
   bgp-ad
    vpls-id 2:2
    vpn-target 2:2 import-extcommunity
    vpn-target 2:2 export-extcommunity
   inclusive-provider-tunnel
    root
     mldp p2mp
      root-ip 1.1.1.1
  #
  mpls ldp
   mldp p2mp
  #                                                                            
  interface GigabitEthernet0/1/0
   undo shutdown                            
   ip address 10.1.2.1 255.255.255.0        
   mpls                                     
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown                            
   l2 binding vsi vsi1
  #
  interface GigabitEthernet0/1/2
   undo shutdown                            
   ip address 10.1.3.1 255.255.255.0        
   mpls                                     
   mpls ldp 
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100 
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1 
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1 
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1 
   #
   l2vpn-ad-family
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
  ospf 100                                  
   area 0.0.0.0                             
    network 1.1.1.1 0.0.0.0                 
    network 10.1.2.0 0.0.0.255              
    network 10.1.3.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi1
   bgp-ad
    vpls-id 2:2
    vpn-target 2:2 import-extcommunity
    vpn-target 2:2 export-extcommunity
   inclusive-provider-tunnel
    leaf
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/0
   undo shutdown                            
   ip address 10.1.2.2 255.255.255.0        
   mpls                                     
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown                            
   ip address 10.1.5.1 255.255.255.0        
   mpls                                     
   mpls ldp
  #
  interface GigabitEthernet0/1/3.1
   vlan-type dot1q 10  
   l2 binding vsi vsi1
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100 
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1 
   #
   l2vpn-ad-family
    peer 1.1.1.1 enable
   #
  ospf 100                                  
   area 0.0.0.0                             
    network 2.2.2.2 0.0.0.0                 
    network 10.1.2.0 0.0.0.255
    network 10.1.5.0 0.0.0.255
  #                                         
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi1
   bgp-ad
    vpls-id 2:2
    vpn-target 2:2 import-extcommunity
    vpn-target 2:2 export-extcommunity
   inclusive-provider-tunnel
    leaf
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/2
   undo shutdown                            
   ip address 10.1.3.2 255.255.255.0        
   mpls                                     
   mpls ldp 
  #
  interface GigabitEthernet0/1/3.1
   vlan-type dot1q 10  
   l2 binding vsi vsi1
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100 
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1 
   #
   l2vpn-ad-family
    peer 1.1.1.1 enable
  #
  ospf 100                                  
   area 0.0.0.0                             
    network 3.3.3.3 0.0.0.0                 
    network 10.1.3.0 0.0.0.255
  #                                         
  return
  ```
* PE4 configuration file
  
  ```
  #
  sysname PE4
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls l2vpn
  #
  vsi vsi1
   bgp-ad
    vpls-id 2:2
    vpn-target 2:2 import-extcommunity
    vpn-target 2:2 export-extcommunity
   inclusive-provider-tunnel
    leaf
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/1
   undo shutdown                            
   ip address 10.1.5.2 255.255.255.0        
   mpls                                     
   mpls ldp
  #
  interface GigabitEthernet0/1/3.1
   vlan-type dot1q 10  
   l2 binding vsi vsi1
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100 
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1 
   #
   l2vpn-ad-family
    peer 1.1.1.1 enable
  #
  ospf 100                                  
   area 0.0.0.0                             
    network 4.4.4.4 0.0.0.0                 
    network 10.1.5.0 0.0.0.255    
  #                                         
  return
  ```