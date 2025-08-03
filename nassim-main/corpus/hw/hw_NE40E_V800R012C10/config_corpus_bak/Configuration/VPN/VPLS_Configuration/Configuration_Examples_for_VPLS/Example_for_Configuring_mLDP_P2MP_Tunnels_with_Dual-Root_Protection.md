Example for Configuring mLDP P2MP Tunnels with Dual-Root Protection
===================================================================

This section provides an example for configuring mLDP P2MP tunnels with dual-root protection.

#### Networking Requirements

On the BGP AD VPLS network under VPLS P2MP dual-root protection shown in [Figure 1](#EN-US_TASK_0172370281__fig_dc_vrp_vpls_cfg_604801), a primary mLDP P2MP tunnel rooted at PE1 and a backup mLDP P2MP tunnel rooted at PE2 are established, with PE1 as the working root node, PE2 the protection root node, and PE3 and PE4 the leaf nodes. If PE1's AC interface (GE0/1/1) or the primary mLDP P2MP tunnel fails, service traffic can be quickly switched to the backup mLDP P2MP tunnel.

**Figure 1** Configuring mLDP P2MP tunnels with dual-root protection  
![](images/fig_dc_vrp_vpls_cfg_604801.png)  

**Table 1** Interfaces and IP addresses
| **Device** | **Interface** | **IP Address** |
| --- | --- | --- |
| PE1 | GE0/1/0 | 10.1.2.1/24 |
| GE0/1/2 | 10.1.3.1/24 |
| PE2 | GE0/1/0 | 10.1.5.1/24 |
| GE0/1/2 | 10.1.6.1/24 |
| PE3 | GE0/1/0 | 10.1.2.2/24 |
| GE0/1/2 | 10.1.6.2/24 |
| PE4 | GE0/1/0 | 10.1.5.2/24 |
| GE0/1/2 | 10.1.3.2/24 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address and a routing protocol for each involved interface to ensure IP connectivity at the network layer. This example uses OSPF as the routing protocol.
2. Configure an MPLS LSR ID and globally enable MPLS, MPLS LDP, and mLDP P2MP.
3. Configure a local LDP session on each PE.
4. Establish a BGP AD VPLS connection between PE1 and PE3, PE1 and PE4, PE2 and PE3, and PE2 and PE4.
5. Establish the primary and backup mLDP P2MP tunnels.
6. Configure PE3 and PE4 as leaf nodes.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses of all interfaces listed in [Table 1](#EN-US_TASK_0172370281__tab_dc_vrp_vpls_cfg_604801)
* OSPF process ID (100) and area ID (0.0.0.0) for each node
* BGP AS numbers of PE1, PE2, PE3, and PE4
* VSI names, VPLS IDs, and VPN targets
* Number of the interface bound to each VSI

#### Procedure

1. Configure an IP address and a routing protocol for each involved interface to ensure IP connectivity at the network layer.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370281__section_dc_vrp_vpls_cfg_604801).
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
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   <PE2> system-view
   ```
   ```
   [~PE2] mpls lsr-id 2.2.2.2
   ```
   ```
   [*PE2] mpls
   ```
   ```
   [*PE2-mpls] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE2-mpls-ldp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   <PE3> system-view
   ```
   ```
   [~PE3] mpls lsr-id 3.3.3.3
   ```
   ```
   [*PE3] mpls
   ```
   ```
   [*PE3-mpls] mpls ldp
   ```
   ```
   [*PE3-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE3-mpls-ldp] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE4.
   
   ```
   <PE4> system-view
   ```
   ```
   [~PE4] mpls lsr-id 4.4.4.4
   ```
   ```
   [*PE4] mpls
   ```
   ```
   [*PE4-mpls] mpls ldp
   ```
   ```
   [*PE4-mpls-ldp] mldp p2mp
   ```
   ```
   [*PE4-mpls-ldp] quit
   ```
   ```
   [*PE4] commit
   ```
3. Configure a local LDP session on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls ldp
   ```
   ```
   [*PE1-mpls-ldp] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls
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
   [*PE1-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls ldp
   ```
   ```
   [*PE2-mpls-ldp] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/2
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] mpls ldp
   ```
   ```
   [*PE3-mpls-ldp] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/1/0
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/1/2
   ```
   ```
   [*PE3-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*PE3-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*PE3-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE4.
   
   ```
   [~PE4] mpls ldp
   ```
   ```
   [*PE4-mpls-ldp] quit
   ```
   ```
   [*PE4] interface gigabitethernet0/1/0
   ```
   ```
   [*PE4-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE4-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE4-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE4] interface gigabitethernet0/1/2
   ```
   ```
   [*PE4-GigabitEthernet0/1/2] mpls
   ```
   ```
   [*PE4-GigabitEthernet0/1/2] mpls ldp
   ```
   ```
   [*PE4-GigabitEthernet0/1/2] quit
   ```
   ```
   [*PE4] commit
   ```
4. Establish a BGP AD VPLS connection between PE1 and PE3, PE1 and PE4, PE2 and PE3, and PE2 and PE4.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
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
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 connect-interface loopback1
   ```
   ```
   [*PE2-bgp] peer 4.4.4.4 as-number 100
   ```
   ```
   [*PE2-bgp] peer 4.4.4.4 connect-interface loopback1
   ```
   ```
   [*PE2-bgp] l2vpn-ad-family
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] peer 3.3.3.3 enable
   ```
   ```
   [*PE2-bgp-af-l2vpn-ad] peer 4.4.4.4 enable
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
   [*PE2] interface gigabitethernet0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] l2 binding vsi vsi1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
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
   [*PE3-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE3-bgp] peer 2.2.2.2 connect-interface loopback1
   ```
   ```
   [*PE3-bgp] l2vpn-ad-family
   ```
   ```
   [*PE3-bgp-af-l2vpn-ad] peer 1.1.1.1 enable
   ```
   ```
   [*PE3-bgp-af-l2vpn-ad] peer 2.2.2.2 enable
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
   [*PE3-l2vpn] vpls p2mp group-select ldp enable
   ```
   ```
   [*PE3-l2vpn] quit
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
   
   # Configure PE4.
   
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
   [*PE4-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE4-bgp] peer 2.2.2.2 connect-interface loopback1
   ```
   ```
   [*PE4-bgp] l2vpn-ad-family
   ```
   ```
   [*PE4-bgp-af-l2vpn-ad] peer 1.1.1.1 enable
   ```
   ```
   [*PE4-bgp-af-l2vpn-ad] peer 2.2.2.2 enable
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
   [*PE4-l2vpn] vpls p2mp group-select ldp enable
   ```
   ```
   [*PE4-l2vpn] quit
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
5. Configure mLDP P2MP tunnels on PE1 (working root node) and PE2 (protection root node) and configure BFD to monitor the AC interface GE 0/1/1. 
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bfd
   ```
   ```
   [*PE1-bfd] quit
   ```
   ```
   [*PE1] vsi vsi1
   ```
   ```
   [*PE1-vsi-vsi1] inclusive-provider-tunnel
   ```
   ```
   [*PE1-vsi-vsi1-inclusive] root
   ```
   ```
   [*PE1-vsi-vsi1-inclusive-root] data-switch disable
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
   [*PE1-vsi-vsi1-inclusive-root] bfd track interface gigabitethernet 0/1/1
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
   
   # Configure PE2.
   
   ```
   [~PE2] bfd
   ```
   ```
   [*PE2-bfd] quit
   ```
   ```
   [*PE2] vsi vsi1
   ```
   ```
   [*PE2-vsi-vsi1] inclusive-provider-tunnel
   ```
   ```
   [*PE2-vsi-vsi1-inclusive] root
   ```
   ```
   [*PE2-vsi-vsi1-inclusive-root] data-switch disable
   ```
   ```
   [*PE2-vsi-vsi1-inclusive-root] mldp p2mp
   ```
   ```
   [*PE2-vsi-vsi1-inclusive-root-mldpp2mp] root-ip 2.2.2.2
   ```
   ```
   [*PE2-vsi-vsi1-inclusive-root-mldpp2mp] quit
   ```
   ```
   [*PE2-vsi-vsi1-inclusive-root] bfd track interface gigabitethernet 0/1/1
   ```
   ```
   [*PE2-vsi-vsi1-inclusive-root] quit
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
6. Configure PE3 and PE4 as leaf nodes and specify the primary and backup mLDP P2MP tunnels.
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] bfd
   ```
   ```
   [*PE3-bfd] quit
   ```
   ```
   [*PE3] vsi vsi1
   ```
   ```
   [*PE3-vsi-vsi1] inclusive-provider-tunnel
   ```
   ```
   [*PE3-vsi-vsi1-inclusive] leaf
   ```
   ```
   [*PE3-vsi-vsi1-inclusive-leaf] primary-root 1.1.1.1 track bfd backup-root 2.2.2.2 track bfd
   ```
   ```
   [*PE3-vsi-vsi1-inclusive-leaf] quit
   ```
   ```
   [*PE3-vsi-vsi1-inclusive] quit
   ```
   ```
   [*PE3-vsi-vsi1] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE4.
   
   ```
   [~PE4] bfd
   ```
   ```
   [*PE4-bfd] quit
   ```
   ```
   [*PE4] vsi vsi1
   ```
   ```
   [*PE4-vsi-vsi1] inclusive-provider-tunnel
   ```
   ```
   [*PE4-vsi-vsi1-inclusive] leaf
   ```
   ```
   [*PE4-vsi-vsi1-inclusive-leaf] primary-root 1.1.1.1 track bfd backup-root 2.2.2.2 track bfd
   ```
   ```
   [*PE4-vsi-vsi1-inclusive-leaf] quit
   ```
   ```
   [*PE4-vsi-vsi1-inclusive] quit
   ```
   ```
   [*PE4-vsi-vsi1] quit
   ```
   ```
   [*PE4] commit
   ```
7. Configure BFD for mLDP P2MP on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bfd
   ```
   ```
   [*PE1-bfd] quit
   ```
   ```
   [*PE1] commit
   ```
   ```
   [~PE1] mpls
   ```
   ```
   [*PE1-mpls] mpls mldp bfd enable
   ```
   ```
   [*PE1-mpls] mpls mldp p2mp bfd-trigger-tunnel all
   ```
   ```
   [*PE1-mpls] quit
   ```
   ```
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] bfd
   ```
   ```
   [*PE2-bfd] quit
   ```
   ```
   [*PE2] commit
   ```
   ```
   [~PE2] mpls
   ```
   ```
   [*PE2-mpls] mpls mldp bfd enable
   ```
   ```
   [*PE2-mpls] mpls mldp p2mp bfd-trigger-tunnel all
   ```
   ```
   [*PE2-mpls] quit
   ```
   ```
   [*PE2] commit
   ```
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] bfd
   ```
   ```
   [*PE3-bfd] quit
   ```
   ```
   [*PE3] commit
   ```
   ```
   [~PE3] mpls
   ```
   ```
   [*PE3-mpls] mpls mldp bfd enable
   ```
   ```
   [*PE3-mpls] mpls mldp p2mp bfd-trigger-tunnel all
   ```
   ```
   [*PE3-mpls] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure PE4.
   
   ```
   [~PE4] bfd
   ```
   ```
   [*PE4-bfd] quit
   ```
   ```
   [*PE4] commit
   ```
   ```
   [~PE4] mpls
   ```
   ```
   [*PE4-mpls] mpls mldp bfd enable
   ```
   ```
   [*PE4-mpls] mpls mldp p2mp bfd-trigger-tunnel all
   ```
   ```
   [*PE4-mpls] quit
   ```
   ```
   [*PE4] commit
   ```
8. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display vsi name inclusive-provider-tunnel** command on PE1 to check mLDP P2MP tunnel information.
   
   ```
   [~PE1]display vsi name vsi1 inclusive-provider-tunnel
   ```
   ```
   VSI name: vsi1
     Ingress provider tunnel
       PMSI type      : P2MP mLDP
       Root ip        : 1.1.1.1
       Opaque value   : 01000400002001
       State         : up
       Leaf list count: 2
       Leaf list      : 3.3.3.3
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
  bfd
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls mldp bfd enable
   mpls mldp p2mp bfd-trigger-tunnel all
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
     data-switch disable
     bfd track interface GigabitEthernet0/1/1
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
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1 
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1 
   #
   l2vpn-ad-family
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
  bfd
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls mldp bfd enable
   mpls mldp p2mp bfd-trigger-tunnel all
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
     data-switch disable
     bfd track interface GigabitEthernet0/1/1
     mldp p2mp
      root-ip 2.2.2.2
  #
  mpls ldp
   mldp p2mp
  #                                                                            
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.5.1 255.255.255.0        
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   l2 binding vsi vsi1
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.6.1 255.255.255.0        
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1 
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1 
   #
   l2vpn-ad-family
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
  ospf 100                                  
   area 0.0.0.0                             
    network 2.2.2.2 0.0.0.0                 
    network 10.1.5.0 0.0.0.255              
    network 10.1.6.0 0.0.0.255
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  bfd
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls mldp bfd enable
   mpls mldp p2mp bfd-trigger-tunnel all
  #
  mpls l2vpn
   vpls p2mp group-select ldp enable
  #
  vsi vsi1
   bgp-ad
    vpls-id 2:2
    vpn-target 2:2 import-extcommunity
    vpn-target 2:2 export-extcommunity
   inclusive-provider-tunnel
    leaf
     primary-root 1.1.1.1 track bfd backup-root 2.2.2.2 track bfd
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
  interface GigabitEthernet0/1/2
   undo shutdown                            
   ip address 10.1.6.2 255.255.255.0        
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
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
  #
   l2vpn-ad-family
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #
  ospf 100                                  
   area 0.0.0.0                             
    network 3.3.3.3 0.0.0.0                 
    network 10.1.2.0 0.0.0.255
    network 10.1.6.0 0.0.0.255
  #                                         
  return
  ```
* PE4 configuration file
  
  ```
  #
  sysname PE4
  #
  bfd
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
   mpls mldp bfd enable
   mpls mldp p2mp bfd-trigger-tunnel all
  #
  mpls l2vpn
   vpls p2mp group-select ldp enable
  #
  mpls ldp
   mldp p2mp
  #
  vsi vsi1
   bgp-ad
    vpls-id 2:2
    vpn-target 2:2 import-extcommunity
    vpn-target 2:2 export-extcommunity
   inclusive-provider-tunnel
    leaf
     primary-root 1.1.1.1 track bfd backup-root 2.2.2.2 track bfd
  
  #
  interface GigabitEthernet0/1/0
   undo shutdown                            
   ip address 10.1.5.2 255.255.255.0        
   mpls
   mpls ldp
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
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100 
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1 
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1 
   #
   l2vpn-ad-family
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
  #
  ospf 100                                  
   area 0.0.0.0                             
    network 4.4.4.4 0.0.0.0                 
    network 10.1.5.0 0.0.0.255    
    network 10.1.3.0 0.0.0.255    
  #                                         
  return
  ```