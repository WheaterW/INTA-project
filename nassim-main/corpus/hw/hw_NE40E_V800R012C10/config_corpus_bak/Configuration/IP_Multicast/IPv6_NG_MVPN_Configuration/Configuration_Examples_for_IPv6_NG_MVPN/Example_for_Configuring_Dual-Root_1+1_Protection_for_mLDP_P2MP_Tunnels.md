Example for Configuring Dual-Root 1+1 Protection for mLDP P2MP Tunnels
======================================================================

This section provides an example for configuring dual-root 1+1 protection for mLDP P2MP tunnels.

#### Networking Requirements

In an NG MVPN scenario, if a sender PE on a P2MP tunnel fails, the C-multicast service will be interrupted. Multicast services can rely only on unicast route convergence for recovery. However, unicast route convergence takes a long time, which is unacceptable to the multicast services that have high reliability requirements. To resolve this problem, you can configure dual-root 1+1 protection for mLDP P2MP tunnels. On the network shown in [Figure 1](#EN-US_TASK_0317769405__fig_dc_vrp_cfg_ngmvpn_002201), a primary mLDP P2MP tunnel is established with PE1 as the root node, and a backup mLDP P2MP tunnel is established with PE2 as the root node. When links are working properly, the same multicast traffic is forwarded through both the primary and backup tunnels. The leaf node PE3 selects the multicast traffic received from the primary tunnel and discards the multicast traffic received from the backup tunnel. If PE1 fails, the leaf node can use BFD for mLDP P2MP to quickly detect the mLDP P2MP tunnel fault and choose to accept the multicast traffic received from the backup tunnel. This accelerates multicast service convergence and improves reliability.

**Figure 1** Configuring dual-root 1+1 protection for mLDP P2MP tunnels![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0318082092.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BGP/MPLS IPv6 VPN and ensure that the unicast VPN is working properly.
2. Enable mLDP globally on PEs so that the PEs can use mLDP to establish P2MP tunnels.
3. Enable all PEs to establish BGP MVPN peer relationships and configure BGP to transmit A-D and C-multicast routes.
4. Configure PE1 and PE2 as sender PEs. Configure mLDP P2MP on PE1 and PE2 so that two mLDP P2MP tunnels rooted at PE1 and PE2 respectively can be established, with PE3 as a leaf node.
5. Configure BFD for mLDP P2MP on the PEs to detect public network node or link failures.
6. Configure VPN FRR on PE3 so that PE3 can have two routes to the same multicast source. PE3 uses the route advertised by PE1 as the primary route and the route advertised by PE2 as the backup route.
7. Enable C-multicast FRR on PE3.
8. Configure PIM on the PEs' interfaces bound to a VPN instance and on the CEs' interfaces connected to PEs so that VPN multicast routing entries are generated for multicast traffic forwarding.
9. Configure MLD on the interface connecting a multicast device (CE2) to the user network segment to allow the device to manage multicast group members on the local network.

#### Data Preparation

To complete the configuration, you need the following data:

* Public network OSPF process ID: 1; area ID: 0 OSPF multi-instance process ID: 2; area ID: 0
* VPN instance name on PE1, PE2, and PE3: VPNA; other data is shown in [Table 1](#EN-US_TASK_0317769405__table_dc_vrp_cfg_ngmvpn_002201).
  
  **Table 1** Data needed for each device
  | Device | IP Address of Loopback 1 | MPLS LSR-ID | MVPN ID | RD | VPN-Target | AS Number |
  | --- | --- | --- | --- | --- | --- | --- |
  | CE1 | 1.1.1.1 | - | - | - | - | AS65001 |
  | PE1 | 2.2.2.2 | 2.2.2.2 | 2.2.2.2 | 200:1 | 3:3 | AS100 |
  | PE2 | 3.3.3.3 | 3.3.3.3 | 3.3.3.3 | 300:1 | 3:3 | AS100 |
  | PE3 | 4.4.4.4 | 4.4.4.4 | 4.4.4.4 | 400:1 | 3:3 | AS100 |
  | CE2 | 5.5.5.5 | - | - | - | - | AS65002 |

#### Procedure

1. Configure BGP/MPLS IPv6 VPN.
   1. Assign an IP address to each interface of devices on the backbone network and VPN sites.
      
      
      
      Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0317769405__fig_dc_vrp_cfg_ngmvpn_002201). For configuration details, see [Configuration Files](#EN-US_TASK_0317769405__example_dc_vrp_cfg_ngmvpn_002201) in this section.
   2. Configure an IGP for interworking on the BGP/MPLS IPv6 VPN backbone network.
      
      
      
      OSPF is used in this example. For configuration details, see [Configuration Files](#EN-US_TASK_0317769405__example_dc_vrp_cfg_ngmvpn_002201) in this section.
   3. Configure basic MPLS functions and MPLS LDP on the MPLS backbone network to establish LDP LSPs.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] mpls lsr-id 2.2.2.2
        ```
        ```
        [*PE1] mpls
        ```
        ```
        [*PE1-mpls] quit
        ```
        ```
        [*PE1] mpls ldp
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
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] mpls lsr-id 3.3.3.3
        ```
        ```
        [*PE2] mpls
        ```
        ```
        [*PE2-mpls] quit
        ```
        ```
        [*PE2] mpls ldp
        ```
        ```
        [*PE2-mpls-ldp] quit
        ```
        ```
        [*PE2] interface gigabitethernet0/1/1
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] mpls
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] mpls ldp
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE2] commit
        ```
      * # Configure PE3.
        
        ```
        [~PE3] mpls lsr-id 4.4.4.4
        ```
        ```
        [*PE3] mpls
        ```
        ```
        [*PE3-mpls] quit
        ```
        ```
        [*PE3] mpls ldp
        ```
        ```
        [*PE3-mpls-ldp] quit
        ```
        ```
        [*PE3] interface gigabitethernet0/1/1
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] mpls
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] mpls ldp
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] quit
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
   4. Establish an MP-IBGP peer relationship between PEs.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] bgp 100
        ```
        ```
        [*PE1-bgp] peer 4.4.4.4 as-number 100
        ```
        ```
        [*PE1-bgp] peer 4.4.4.4 connect-interface LoopBack1
        ```
        ```
        [*PE1-bgp] ipv6-family vpnv6
        ```
        ```
        [*PE1-bgp-af-vpnv6] peer 4.4.4.4 enable
        ```
        ```
        [*PE1-bgp-af-vpnv6] quit
        ```
        ```
        [*PE1-bgp] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] bgp 100
        ```
        ```
        [*PE2-bgp] peer 4.4.4.4 as-number 100
        ```
        ```
        [*PE2-bgp] peer 4.4.4.4 connect-interface LoopBack1
        ```
        ```
        [*PE2-bgp] ipv6-family vpnv6
        ```
        ```
        [*PE2-bgp-af-vpnv6] peer 4.4.4.4 enable
        ```
        ```
        [*PE2-bgp-af-vpnv6] quit
        ```
        ```
        [*PE2-bgp] quit
        ```
        ```
        [*PE2] commit
        ```
      * # Configure PE3.
        
        ```
        [~PE3] bgp 100
        ```
        ```
        [*PE3-bgp] peer 2.2.2.2 as-number 100
        ```
        ```
        [*PE3-bgp] peer 2.2.2.2 connect-interface LoopBack1
        ```
        ```
        [*PE3-bgp] peer 3.3.3.3 as-number 100
        ```
        ```
        [*PE3-bgp] peer 3.3.3.3 connect-interface LoopBack1
        ```
        ```
        [*PE3-bgp] ipv6-family vpnv6
        ```
        ```
        [*PE3-bgp-af-vpnv6] peer 2.2.2.2 enable
        ```
        ```
        [*PE3-bgp-af-vpnv6] peer 3.3.3.3 enable
        ```
        ```
        [*PE3-bgp-af-vpnv6] quit
        ```
        ```
        [*PE3-bgp] quit
        ```
        ```
        [*PE3] commit
        ```
   5. Configure a VPN instance on each PE so that each CE can access the corresponding PE.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] ip vpn-instance VPNA
        ```
        ```
        [*PE1-vpn-instance-VPNA] ipv6-family
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv6] route-distinguisher 200:1
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv6] vpn-target 3:3
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv6] quit
        ```
        ```
        [*PE1-vpn-instance-VPNA] quit
        ```
        ```
        [*PE1] interface gigabitethernet0/1/1
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] ipv6 enable
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] ipv6 address 2001:DB8:2::2 64
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] ip vpn-instance VPNA
        ```
        ```
        [*PE2-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*PE2-vpn-instance-VPNA-af-ipv4] route-distinguisher 300:1
        ```
        ```
        [*PE2-vpn-instance-VPNA-af-ipv4] vpn-target 3:3
        ```
        ```
        [*PE2-vpn-instance-VPNA-af-ipv4] quit
        ```
        ```
        [*PE2-vpn-instance-VPNA] quit
        ```
        ```
        [*PE2] interface gigabitethernet0/1/2
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] ip binding vpn-instance VPNA
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] ipv6 enable
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] ipv6 address 2001:DB8:3::2 64
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] quit
        ```
        ```
        [*PE2] commit
        ```
      * # Configure PE3.
        
        ```
        [~PE3] ip vpn-instance VPNA
        ```
        ```
        [*PE3-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*PE3-vpn-instance-VPNA-af-ipv4] route-distinguisher 400:1
        ```
        ```
        [*PE3-vpn-instance-VPNA-af-ipv4] vpn-target 3:3
        ```
        ```
        [*PE3-vpn-instance-VPNA-af-ipv4] quit
        ```
        ```
        [*PE3-vpn-instance-VPNA] quit
        ```
        ```
        [*PE3] interface gigabitethernet0/1/0
        ```
        ```
        [*PE3-GigabitEthernet0/1/0] ip binding vpn-instance VPNA
        ```
        ```
        [*PE3-GigabitEthernet0/1/0] ipv6 enable
        ```
        ```
        [*PE3-GigabitEthernet0/1/0] ipv6 address 2001:DB8:4::2 64
        ```
        ```
        [*PE3-GigabitEthernet0/1/0] quit
        ```
        ```
        [*PE3] commit
        ```
   6. Configure OSPF multi-instance on each PE to import VPN routes.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] ospfv3 2 vpn-instance VPNA
        ```
        ```
        [*PE1-ospfv3-2] router-id 2.2.2.2
        ```
        ```
        [*PE1-ospfv3-2] import-route bgp
        ```
        ```
        [*PE1-ospfv3-2] area 0
        ```
        ```
        [*PE1-ospfv3-2-area-0.0.0.0] quit
        ```
        ```
        [*PE1-ospfv3-2] quit
        ```
        ```
        [*PE1] interface gigabitethernet0/1/1
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] ospfv3 2 area 0
        ```
        ```
        [*PE1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*PE1] bgp 100
        ```
        ```
        [*PE1-bgp] ipv6-family vpn-instance VPNA
        ```
        ```
        [*PE1-bgp-6-VPNA] import-route ospfv3 2
        ```
        ```
        [*PE1-bgp-6-VPNA] quit
        ```
        ```
        [*PE1-bgp] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] ospfv3 2 vpn-instance VPNA
        ```
        ```
        [*PE2-ospfv3-2] router-id 3.3.3.3
        ```
        ```
        [*PE2-ospfv3-2] import-route bgp
        ```
        ```
        [*PE2-ospfv3-2] area 0
        ```
        ```
        [*PE2-ospfv3-2-area-0.0.0.0] quit
        ```
        ```
        [*PE2-ospfv3-2] quit
        ```
        ```
        [*PE2] interface gigabitethernet0/1/2
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] ospfv3 2 area 0
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] quit
        ```
        ```
        [*PE2] bgp 100
        ```
        ```
        [*PE2-bgp] ipv6-family vpn-instance VPNA
        ```
        ```
        [*PE2-bgp-6-VPNA] import-route ospfv3 2
        ```
        ```
        [*PE2-bgp-6-VPNA] quit
        ```
        ```
        [*PE2-bgp] quit
        ```
        ```
        [*PE2] commit
        ```
      * # Configure PE3.
        
        ```
        [~PE3] ospfv3 2 vpn-instance VPNA
        ```
        ```
        [*PE3-ospfv3-2] router-id 4.4.4.4
        ```
        ```
        [*PE3-ospfv3-2] import-route bgp
        ```
        ```
        [*PE3-ospfv3-2] area 0
        ```
        ```
        [*PE3-ospfv3-2-area-0.0.0.0] quit
        ```
        ```
        [*PE3-ospfv3-2] quit
        ```
        ```
        [*PE3] interface GigabitEthernet0/1/0
        ```
        ```
        [*PE3-GigabitEthernet0/1/0] ospfv3 2 area 0
        ```
        ```
        [*PE3-GigabitEthernet0/1/0] quit
        ```
        ```
        [*PE3] bgp 100
        ```
        ```
        [*PE3-bgp] ipv6-family vpn-instance VPNA
        ```
        ```
        [*PE3-bgp-6-VPNA] import-route ospfv3 2
        ```
        ```
        [*PE3-bgp-6-VPNA] quit
        ```
        ```
        [*PE3-bgp] quit
        ```
        ```
        [*PE3] commit
        ```
   7. Configure OSPFv3 on CEs.
      
      
      * # Configure CE1.
        
        ```
        [~CE1] ospfv3 2
        ```
        ```
        [*CE1-ospfv3-2] router-id 1.1.1.1
        ```
        ```
        [*CE1-ospfv3-2] area 0
        ```
        ```
        [*CE1-ospfv3-2-area-0.0.0.0] network 1.1.1.1 0.0.0.0
        ```
        ```
        [*CE1-ospfv3-2-area-0.0.0.0] quit
        ```
        ```
        [*CE1-ospf-2] quit
        ```
        ```
        [*CE1] interface GigabitEthernet0/1/1
        ```
        ```
        [*CE1-GigabitEthernet0/1/1] ospfv3 2 area 0
        ```
        ```
        [*CE1-GigabitEthernet0/1/1] quit
        ```
        ```
        [*CE1] interface GigabitEthernet0/1/2
        ```
        ```
        [*CE1-GigabitEthernet0/1/2] ospfv3 2 area 0
        ```
        ```
        [*CE1-GigabitEthernet0/1/2] quit
        ```
        ```
        [*CE1] commit
        ```
      * # Configure CE2.
        
        ```
        [~CE2] ospfv3 2
        ```
        ```
        [*CE2-ospfv3-2] router-id 5.5.5.5
        ```
        ```
        [*CE2-ospfv3-2] area 0
        ```
        ```
        [*CE2-ospfv3-2-area-0.0.0.0] network 5.5.5.5 0.0.0.0
        ```
        ```
        [*CE2-ospfv3-2-area-0.0.0.0] quit
        ```
        ```
        [*CE2-ospfv3-2] quit
        ```
        ```
        [*CE2] interface GigabitEthernet0/1/0
        ```
        ```
        [*CE2-GigabitEthernet0/1/0] ospfv3 2 area 0
        ```
        ```
        [*CE2-GigabitEthernet0/1/0] quit
        ```
        ```
        [*CE2] commit
        ```
      
      After the configurations are complete, run the [**display ipv6 routing-table vpn-instance verbose**](cmdqueryname=display+ipv6+routing-table+vpn-instance+verbose) command on PE3. The command output shows a backup unicast route to the multicast source.
      
      ```
      [~PE3] display ipv6 routing-table vpn-instance VPNA 2001:DB8:1::6 verbose
      ```
      ```
      Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
      ------------------------------------------------------------------------------
      Routing Table : VPNA
      Summary Count : 1
      Destination  : 2001:DB8:1::                            PrefixLength : 64
      NextHop      : ::FFFF:2.2.2.2                          Preference   : 255
      Neighbour    : ::2.2.2.2                               ProcessID    : 0
      Label        : 48062                                   Protocol     : IBGP
      State        : Active Adv Relied                       Cost         : 20
      Entry ID     : 0                                       EntryFlags   : 0x00000000
      Reference Cnt: 0                                       Tag          : 0
      Priority     : low                                     Age          : 74sec
      IndirectID   : 0x1000120                               Instance     : 
      RelayNextHop :                                         TunnelID     : 0x0000000001004c4b47
      Interface    : GigabitEthernet1/0/1                    Flags        : RD
      BkNextHop    : ::FFFF:3.3.3.3                          BkInterface  : GigabitEthernet1/0/2
      BkLabel      : 48061                                   BkTunnelID   : 0x0  
      BkPETunnelID : 0x0000000001004c4b43                    BkIndirectID : 0x100011A 
      ```
2. Enable mLDP globally.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] mpls ldp
     ```
     ```
     [*PE1-mpls-ldp] mldp p2mp
     ```
     ```
     [*PE1-mpls-ldp] commit
     ```
     ```
     [~PE1-mpls-ldp] quit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] mpls ldp
     ```
     ```
     [*PE2-mpls-ldp] mldp p2mp
     ```
     ```
     [*PE2-mpls-ldp] commit
     ```
     ```
     [~PE2-mpls-ldp] quit
     ```
   * # Configure PE3.
     
     ```
     [~PE3] mpls ldp
     ```
     ```
     [*PE3-mpls-ldp] mldp p2mp
     ```
     ```
     [*PE3-mpls-ldp] commit
     ```
     ```
     [~PE3-mpls-ldp] quit
     ```
3. Establish a BGP MVPN peer relationship between PEs.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] bgp 100
     ```
     ```
     [*PE1-bgp] ipv6-family mvpn
     ```
     ```
     [*PE1-bgp-af-mvpn6] peer 4.4.4.4 enable
     ```
     ```
     [*PE1-bgp-af-mvpn6] quit
     ```
     ```
     [*PE1-bgp] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] bgp 100
     ```
     ```
     [*PE2-bgp] ipv6-family mvpn
     ```
     ```
     [*PE2-bgp-af-mvpn6] peer 4.4.4.4 enable
     ```
     ```
     [*PE2-bgp-af-mvpn6] quit
     ```
     ```
     [*PE2-bgp] quit
     ```
     ```
     [*PE2] commit
     ```
   * # Configure PE3.
     
     ```
     [~PE3] bgp 100
     ```
     ```
     [*PE3-bgp] ipv6-family mvpn
     ```
     ```
     [*PE3-bgp-af-mvpn6] peer 2.2.2.2 enable
     ```
     ```
     [*PE3-bgp-af-mvpn6] peer 3.3.3.3 enable
     ```
     ```
     [*PE3-bgp-af-mvpn6] quit
     ```
     ```
     [*PE3-bgp] quit
     ```
     ```
     [*PE3] commit
     ```
   
   After completing the configurations, run the [**display bgp mvpn vpnv6 all peer**](cmdqueryname=display+bgp+mvpn+vpnv6+all+peer) command on the PEs. The command output shows that PE3 has established a BGP MVPN peer relationship with PE1 and PE2. The following example uses the command output on PE3.
   
   ```
   [~PE3] display bgp mvpn vpnv6 all peer
   ```
   ```
    BGP local router ID : 10.1.1.2
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2.2.2.2         4         100      275      290     0 03:10:56 Established    1
     3.3.3.3         4         100      286      294     0 03:44:39 Established    1
   
   ```
4. Configure each PE to use mLDP to establish an I-PMSI tunnel.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] multicast ipv6 mvpn 2.2.2.2
     ```
     ```
     [*PE1] ip vpn-instance VPNA
     ```
     ```
     [*PE1-vpn-instance-VPNA] ipv6-family
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6] multicast ipv6 routing-enable
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6] mvpn
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] sender-enable
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast signaling bgp
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] ipmsi-tunnel
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-ipmsi] mldp
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn-ipmsi] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6-mvpn] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv6] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] multicast ipv6 mvpn 3.3.3.3
     ```
     ```
     [*PE2] ip vpn-instance VPNA
     ```
     ```
     [*PE2-vpn-instance-VPNA] ipv6-family
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6] multicast ipv6 routing-enable
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6] mvpn
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] sender-enable
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast signaling bgp
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] ipmsi-tunnel
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6-mvpn-ipmsi] mldp
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6-mvpn-ipmsi] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6-mvpn] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv6] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA] quit
     ```
     ```
     [*PE2] commit
     ```
   * # Configure PE3.
     
     ```
     [~PE3] multicast ipv6 mvpn 4.4.4.4
     ```
     ```
     [*PE3] ip vpn-instance VPNA
     ```
     ```
     [*PE3-vpn-instance-VPNA] ipv6-family
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv6] multicast ipv6 routing-enable
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv6] mvpn
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast signaling bgp
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] quit
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv6] quit
     ```
     ```
     [*PE3-vpn-instance-VPNA] quit
     ```
     ```
     [*PE3] commit
     ```
   
   After the configuration is complete, run the [**display mvpn ipv6 vpn-instance ipmsi**](cmdqueryname=display+mvpn+ipv6+vpn-instance+ipmsi) command on the PEs to check I-PMSI tunnel information. The following example uses the command outputs on PE1 and PE2.
   
   ```
   [~PE1] display mvpn ipv6 vpn-instance VPNA ipmsi
   ```
   ```
   MVPN local I-PMSI information for VPN-Instance: VPNA
   Tunnel type: mLDP P2MP LSP
   Tunnel state: Up
   Root-ip: 2.2.2.2
   Opaque value: 0x01000400008043
   Root: 2.2.2.2 (local)
   Leaf:
     1: 4.4.4.4
   ```
   ```
   [~PE2] display mvpn ipv6 vpn-instance VPNA ipmsi
   ```
   ```
   MVPN local I-PMSI information for VPN-Instance: VPNA
   Tunnel type: mLDP P2MP LSP
   Tunnel state: Up
   Root-ip: 3.3.3.3
   Opaque value: 0x01000400008023
   Root: 3.3.3.3 (local)
   Leaf:
     1: 4.4.4.4
   ```
   
   According to the preceding command outputs, two mLDP P2MP tunnels have been established, with PE1 and PE2 as their root nodes and PE3 as a leaf node.
5. Configure BFD for mLDP P2MP on the PEs.
   
   
   
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
6. Configure VPN FRR on PE3.
   
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] ipv6-family vpn-instance VPNA
   ```
   ```
   [*PE3-bgp-6-VPNA] auto-frr
   ```
   ```
   [*PE3-bgp-6-VPNA] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
7. Enable C-multicast FRR on PE3.
   
   
   ```
   [~PE3] ip vpn-instance VPNA
   ```
   ```
   [*PE3-vpn-instance-VPNA] ipv6-family
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6] mvpn
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] c-multicast frr
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6-mvpn] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv6] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA] quit
   ```
   ```
   [*PE3] commit
   ```
8. Configure PIM.
   
   
   * # Configure PE1.
     
     ```
     [*PE1] interface gigabitethernet0/1/1
     ```
     ```
     [*PE1-GigabitEthernet0/1/1] pim ipv6 sm
     ```
     ```
     [*PE1-GigabitEthernet0/1/1] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure CE1.
     
     ```
     [~CE1] multicast ipv6 routing-enable
     ```
     ```
     [*CE1] interface gigabitethernet0/1/0
     ```
     ```
     [*CE1-GigabitEthernet0/1/0] pim ipv6 sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/0] quit
     ```
     ```
     [*CE1] interface gigabitethernet0/1/1
     ```
     ```
     [*CE1-GigabitEthernet0/1/1] pim ipv6 sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/1] quit
     ```
     ```
     [*CE1] interface gigabitethernet0/1/2
     ```
     ```
     [*CE1-GigabitEthernet0/1/2] pim ipv6 sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/2] quit
     ```
     ```
     [*CE1] commit
     ```
   * # Configure PE2.
     
     ```
     [*PE2] interface gigabitethernet0/1/2
     ```
     ```
     [*PE2-GigabitEthernet0/1/2] pim ipv6 sm
     ```
     ```
     [*PE2-GigabitEthernet0/1/2] quit
     ```
     ```
     [*PE2] commit
     ```
   * # Configure CE2.
     
     ```
     [~CE2] multicast ipv6 routing-enable
     ```
     ```
     [*CE2] interface gigabitethernet0/1/0
     ```
     ```
     [*CE2-GigabitEthernet0/1/0] pim ipv6 sm
     ```
     ```
     [*CE2-GigabitEthernet0/1/0] quit
     ```
     ```
     [*CE2] interface gigabitethernet0/1/1
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] pim ipv6 sm
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] quit
     ```
     ```
     [*CE2] commit
     ```
   * # Configure PE3.
     
     ```
     [*PE3] interface gigabitethernet0/1/0
     ```
     ```
     [*PE3-GigabitEthernet0/1/0] pim ipv6 sm
     ```
     ```
     [*PE3-GigabitEthernet0/1/0] quit
     ```
     ```
     [*PE3] commit
     ```
9. Configure MLD.
   
   
   ```
   [~CE2] interface gigabitethernet0/1/1
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] pim ipv6 sm
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] mld enable
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] mld version 2
   ```
   ```
   [*CE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [*CE2] commit
   ```
10. Verify the configuration.
    
    
    
    After the configurations are complete, mLDP P2MP tunnels have dual-root 1+1 protection. After users of CE2 send MLD Report messages and the multicast source at 2001:DB8:1::264 sends multicast traffic, you can check multicast routing entries.
    
    * When the links are working properly:
      
      # Display the PIM routing table on PE3. As dual-root 1+1 protection is configured for mLDP P2MP tunnels, the command output shows that a backup PIM entry has been generated.
      ```
      [~PE3] display pim ipv6 vpn-instance VPNA routing-table
      ```
      ```
       VPN-Instance: VPNA
       Total 0 (*, G) entry; 1 (S, G) entry
      
       (2001:DB8:1::264, FF1E::3)
           RP: NULL
           Protocol: pim-sm, Flag: SPT ACT
           UpTime: 03:12:27
           Upstream interface: through-BGP, Refresh time: 03:12:27
               Upstream neighbor: ::FFFF:2.2.2.2
               RPF prime neighbor: ::FFFF:2.2.2.2
           Backup upstream interface: through-BGP
               Backup Upstream neighbor: ::FFFF:3.3.3.3
               Backup RPF prime neighbor: ::FFFF:3.3.3.3
           Downstream interface(s) information:
           Total number of downstreams: 1
              1: GigabitEthernet0/1/0
                   Protocol: pim-sm, UpTime: 03:12:27, Expires: 00:03:05 
      ```
    * If a link fails:
      
      # Run the **shutdown** command on GE 0/1/0 of PE1 to simulate a link failure.
      ```
      [~PE1] interface gigabitethernet0/1/0
      ```
      ```
      [~PE1-GigabitEthernet0/1/0] shutdown
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE1] commit
      ```
      
      # Run the [**display pim ipv6 routing-table**](cmdqueryname=display+pim+ipv6+routing-table) command on receiver CE2 and sender CE1 to check their PIM routing tables. Run the [**display pim ipv6 vpn-instance**](cmdqueryname=display+pim+ipv6+vpn-instance) **routing-table** command on receiver PE3 and sender PE2 to check the PIM routing table of the VPN instance.
      
      ```
      [~CE2] display pim ipv6 routing-table
      ```
      ```
       VPN-Instance: public net
       Total 0 (*, G) entry; 1 (S, G) entry
      
       (2001:DB8:1::264, FF1E::3)
           RP: NULL
           Protocol: pim-sm, Flag: SPT SG_RCVR ACT
           UpTime: 05:39:14
           Upstream interface: GigabitEthernet0/1/0, Refresh time: 05:39:14
               Upstream neighbor: FE80::3AA3:8FFF:FE51:305
               RPF prime neighbor: FE80::3AA3:8FFF:FE51:305
           Downstream interface(s) information:
           Total number of downstreams: 1
              1: GigabitEthernet0/1/1
                   Protocol: mld, UpTime: 05:39:14, Expires: -  
      ```
      ```
      [~PE3] display pim ipv6 vpn-instance VPNA routing-table
      ```
      ```
       VPN-Instance: VPNA
       Total 0 (*, G) entry; 1 (S, G) entry
      
       (2001:DB8:1::264, FF1E::3)
           RP: NULL
           Protocol: pim-sm, Flag: SPT ACT
           UpTime: 03:32:13
           Upstream interface: through-BGP, Refresh time: 03:32:13
               Upstream neighbor: FE80::3AA3:8FFF:FE51:304
               RPF prime neighbor: FE80::3AA3:8FFF:FE51:304
           Downstream interface(s) information:
           Total number of downstreams: 1
              1: GigabitEthernet0/1/0
                   Protocol: pim-sm, UpTime: 03:32:13, Expires: 00:03:19   
      ```
      ```
      [~PE2] display pim ipv6 vpn-instance VPNA routing-table
      ```
      ```
       VPN-Instance: VPNA
       Total 0 (*, G) entry; 1 (S, G) entry
      
       (2001:DB8:1::264, FF1E::3)
           RP: NULL
           Protocol: pim-sm, Flag: SPT SG_RCVR ACT
           UpTime: 03:25:51
           Upstream interface: GigabitEthernet0/1/2, Refresh time: 03:25:51
               Upstream neighbor: FE80::3AA3:8FFF:FE51:304
               RPF prime neighbor: FE80::3AA3:8FFF:FE51:304
           Downstream interface(s) information:
           Total number of downstreams: 1
              1: pseudo
                   Protocol: BGP, UpTime: 03:25:51, Expires: -        
      ```
      ```
      [~CE1] display pim ipv6 routing-table
      ```
      ```
       VPN-Instance: public net
       Total 0 (*, G) entry; 1 (S, G) entry
      
       (2001:DB8:1::264, FF1E::3)
           RP: NULL
           Protocol: pim-sm, Flag: SPT LOC ACT
           UpTime: 03:35:37
           Upstream interface: GigabitEthernet0/1/0, Refresh time: 03:35:37
               Upstream neighbor: NULL
               RPF prime neighbor: NULL
           Downstream interface(s) information:
           Total number of downstreams: 1
              1: GigabitEthernet0/1/2
                   Protocol: pim-sm, UpTime: 03:28:03, Expires: 00:03:28   
      ```
      
      The command outputs show that traffic exists in the backup tunnel because a backup upstream device is available. Multicast traffic in the backup tunnel is forwarded to receivers immediately after BFD detects that the primary tunnel is faulty.

#### Configuration Files

* CE1
  
  ```
  #
  sysname CE1
  #
  multicast ipv6 routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   pim ipv6 sm
   ospfv3 2 area 0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   pim ipv6 sm
   ospfv3 2 area 0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
   pim ipv6 sm
   ospfv3 2 area 0
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  ospfv3 2
   router-id 1.1.1.1
   area 0.0.0.0
   network 1.1.1.1 0.0.0.0
  #
  return
  ```
* PE1
  
  ```
  #
  sysname PE1
  #
  multicast ipv6 mvpn 2.2.2.2
  #
  ip vpn-instance VPNA
   ipv6-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast ipv6 routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     ipmsi-tunnel
      mldp
  #
  bfd
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls mldp bfd enable
   mpls mldp p2mp bfd-trigger-tunnel all
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0 
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   pim ipv6 sm
   ospfv3 2 area 0
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.4 enable
   #
   ipv6-family mvpn
    policy vpn-target
    peer 4.4.4.4 enable
   #
   ipv6-family vpnv6 
    policy vpn-target 
    peer 4.4.4.4 enable
   #
   ipv6-family vpn-instance VPNA
    import-route ospfv3 2
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  ospfv3 2 vpn-instance VPNA
   router-id 2.2.2.2
   import-route bgp
   area 0.0.0.0
  #
  return
  ```
* PE2
  
  ```
  #
  sysname PE2
  #
  multicast ipv6 mvpn 3.3.3.3
  #
  ip vpn-instance VPNA
   ipv6-family
    route-distinguisher 300:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast ipv6 routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     ipmsi-tunnel
      mldp
  #
  bfd
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls mldp bfd enable
   mpls mldp p2mp bfd-trigger-tunnel all
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance VPNA
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
   pim ipv6 sm
   ospfv3 2 area 0
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.4 enable
   #
   ipv6-family mvpn
    policy vpn-target
    peer 4.4.4.4 enable
   #
   ipv6-family vpnv6 
    policy vpn-target 
    peer 4.4.4.4 enable
   #
   ipv6-family vpn-instance VPNA
    import-route ospfv3 2
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.2.0 0.0.0.255
  #
  ospfv3 2 vpn-instance VPNA
   router-id 3.3.3.3
   import-route bgp
   area 0.0.0.0
  #
  return
  ```
* PE3
  
  ```
  #
  sysname PE3
  #
  multicast ipv6 mvpn 4.4.4.4
  #
  ip vpn-instance VPNA
   ipv6-family
    route-distinguisher 400:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast ipv6 routing-enable
    mvpn
     c-multicast signaling bgp
     c-multicast frr
  #
  bfd
  #
  mpls lsr-id 4.4.4.4    
  #
  mpls
   mpls mldp bfd enable
   mpls mldp p2mp bfd-trigger-tunnel all
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance VPNA
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64
   pim ipv6 sm
   ospfv3 2 area 0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv6-family mvpn
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv6-family vpn-instance VPNA
    import-route ospfv3 2
    auto-frr
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
  #
  ospfv3 2 vpn-instance VPNA
   router-id 4.4.4.4
   import-route bgp
   area 0.0.0.0
  #
  return
  ```
* CE2
  
  ```
  #
  sysname CE2
  #
  multicast ipv6 routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:4::2/64
   pim ipv6 sm
   ospfv3 2 area 0
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:5::1/64
   pim ipv6 sm
   mld enable
   mld static-group FF1E::3 source 2001:DB8:1::2 64
   ospfv3 2 area 0
  #
  interface LoopBack1
   ip address 5.5.5.5 255.255.255.255
  #
  ospfv3 2
   router-id 5.5.5.5
   area 0.0.0.0
   network 5.5.5.5 0.0.0.0
  #
  return
  ```