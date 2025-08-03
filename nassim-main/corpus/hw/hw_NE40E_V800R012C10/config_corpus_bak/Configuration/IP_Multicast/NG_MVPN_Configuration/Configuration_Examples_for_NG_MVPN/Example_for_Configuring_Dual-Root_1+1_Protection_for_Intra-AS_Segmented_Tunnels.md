Example for Configuring Dual-Root 1+1 Protection for Intra-AS Segmented Tunnels
===============================================================================

This section provides an example for configuring dual-root 1+1 protection for NG MVPN in intra-AS segmented tunnel scenarios.

#### Networking Requirements

In an NG MVPN scenario, if a sender PE on a P2MP tunnel fails, the C-multicast service will be interrupted. The network can rely only on unicast route convergence for recovery. However, unicast route convergence takes a long time and may fail to meet the high reliability requirements of some multicast services. To resolve this issue, configure dual-root 1+1 protection based on traffic detection. On the network shown in [Figure 1](#EN-US_TASK_0000001270153593__fig_dc_vrp_cfg_ngmvpn_010101), when links are working properly, the same multicast traffic is forwarded along both the primary and backup tunnels. Leaf node PE3 selects the multicast traffic from the primary tunnel (rooted at PE1) and discards the multicast traffic from the backup tunnel (rooted at PE2). If PE1 fails, the leaf nodes can use traffic detection technology to quickly detect the tunnel fault and choose to accept the multicast traffic received from the backup tunnel. This accelerates multicast service convergence and improves reliability.

**Figure 1** Configuring dual-root 1+1 protection for intra-AS segmented tunnels![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001225513856.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BGP/MPLS IP VPN to ensure that the unicast VPN is running properly.
2. Enable P2MP TE globally on PE1, PE2, ABR1, and ABR2, and configure a P2MP TE template so that PE1, PE2, ABR1, and ABR2 can use RSVP-TE to establish P2MP tunnels.
3. Enable mLDP globally on ABR1, ABR2, and PE3 so that ABR1, ABR2, and PE3 can use mLDP to establish P2MP tunnels.
4. Enable all PEs and ABRs to establish BGP MVPN peer relationships and configure BGP to transmit A-D and C-multicast routes.
5. Configure PE1 and PE2 as sender PEs. Configure P2MP TE on PE1 and PE2 so that two P2MP TE tunnels rooted at PE1 and PE2 can be established. Configure ABR1 and ABR2 as leaf nodes of the two tunnels.
6. Configure ABR1 and ABR2 to support segmented tunnels and configure tunnel stitching so that two mLDP P2MP tunnels are established, with one rooted at ABR1 and the other rooted at ABR2. Configure PE3 as a leaf node of both tunnels.
7. Configure VPN FRR on PE3 so that PE3 can have two routes to the multicast source. PE3 uses the route advertised by PE1 as the primary route and the route advertised by PE2 as the backup route.
8. Configure MVPN FRR on PE3, and set the detection mode to traffic-based detection.
9. Configure PIM on the PE interfaces bound to VPN instances and on the CEs' interfaces connected to PEs to allow a VPN multicast routing table to be established to guide multicast traffic forwarding.
10. Configure IGMP on the interfaces connecting a multicast device to a user network segment to allow the device to manage multicast group members on the network segment.

#### Data Preparation

To complete the configuration, you need the following data:

* IS-IS process ID of the public network: 1; OSPF process ID: 10; area ID: 0.0.0.1; OSPF multi-process ID: 2; area ID: 0.0.0.0
* VPN instance name on PE1, PE2, and PE3: VPNA; other data shown in [Table 1](#EN-US_TASK_0000001270153593__table_dc_vrp_cfg_ngmvpn_010101)
  
  **Table 1** Data needed for each device
  | Device | Loopback 0 Interface Address | MPLS LSR-ID | MVPN ID | RD | VPN-Target | AS Number |
  | --- | --- | --- | --- | --- | --- | --- |
  | CE1 | 1.1.1.1 | - | - | - | - | AS100 |
  | PE1 | 2.2.2.2 | 2.2.2.2 | 2.2.2.2 | 200:1 | 3:3 | AS100 |
  | PE2 | 3.3.3.3 | 3.3.3.3 | 3.3.3.3 | 300:1 | 3:3 | AS100 |
  | ABR1 | 4.4.4.4 | 4.4.4.4 | 4.4.4.4 | 400:1 | 3:3 | AS100 |
  | ABR2 | 5.5.5.5 | 5.5.5.5 | 5.5.5.5 | 500:1 | 3:3 | AS100 |
  | PE3 | 6.6.6.6 | 6.6.6.6 | 6.6.6.6 | 600:1 | 3:3 | AS100 |
  | CE2 | 7.7.7.7 | - | - | - | - | AS100 |

#### Procedure

1. Configure BGP/MPLS IP VPN.
   1. Assign an IP address to each interface of devices on the VPN backbone network and VPN sites.
      
      
      
      Configure an IP address for each interface according to [Figure 1](#EN-US_TASK_0000001270153593__fig_dc_vrp_cfg_ngmvpn_010101). For configuration details, see [Figure 1](#EN-US_TASK_0000001270153593__fig_dc_vrp_cfg_ngmvpn_010101) in this section.
   2. Configure an IGP for interworking on the BGP/MPLS IP VPN backbone network.
      
      
      
      OSPF and IS-IS are used in this example. For configuration details, see [Configuration Files](#EN-US_TASK_0000001270153593__example_dc_vrp_cfg_ngmvpn_010101) in this section.
   3. Configure basic MPLS functions and enable MPLS TE or MPLS LDP on the MPLS backbone network to establish MPLS TE tunnels or LDP LSPs.
      
      
      
      # Configure PE1.
      
      ```
      [~PE1] mpls lsr-id 2.2.2.2
      ```
      ```
      [*PE1] mpls
      ```
      ```
      [*PE1-mpls] mpls te p2mp-te
      ```
      ```
      [*PE1-mpls] quit
      ```
      ```
      [*PE1] mpls te p2mp-template t1
      ```
      ```
      [*PE1-te-p2mp-template-t1] record-route label
      ```
      ```
      [*PE1-te-p2mp-template-t1] bandwidth ct0 100
      ```
      ```
      [*PE1-te-p2mp-template-t1] fast-reroute bandwidth
      ```
      ```
      [*PE1-te-p2mp-template-t1] bypass-attributes bandwidth 10 priority 7 7
      ```
      ```
      [*PE1-te-p2mp-template-t1] quit
      ```
      ```
      [*PE1] interface gigabitethernet0/1/0
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] mpls te
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] mpls rsvp-te
      ```
      ```
      [*PE1-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE1] interface gigabitethernet0/1/1
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] mpls te
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] mpls rsvp-te
      ```
      ```
      [*PE1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE1] commit
      ```
      
      
      
      # Configure PE2.
      
      ```
      [~PE2] mpls lsr-id 3.3.3.3
      ```
      ```
      [~PE2] mpls
      ```
      ```
      [*PE2-mpls] mpls te p2mp-te
      ```
      ```
      [*PE2-mpls] quit
      ```
      ```
      [*PE2] mpls te p2mp-template t1
      ```
      ```
      [*PE2-te-p2mp-template-t1] record-route label
      ```
      ```
      [*PE2-te-p2mp-template-t1] bandwidth ct0 100
      ```
      ```
      [*PE2-te-p2mp-template-t1] fast-reroute bandwidth
      ```
      ```
      [*PE2-te-p2mp-template-t1] bypass-attributes bandwidth 10 priority 7 7
      ```
      ```
      [*PE2-te-p2mp-template-t1] quit
      ```
      ```
      [*PE2] interface gigabitethernet0/1/0
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] mpls
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] mpls te
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] mpls rsvp-te
      ```
      ```
      [*PE2-GigabitEthernet0/1/0] quit
      ```
      ```
      [*PE2] interface gigabitethernet0/1/1
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] mpls te
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] mpls rsvp-te
      ```
      ```
      [*PE2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*PE2] commit
      ```
      
      
      
      # Configure ABR1.
      
      ```
      [~ABR1] mpls lsr-id 4.4.4.4
      ```
      ```
      [~ABR1] mpls
      ```
      ```
      [*ABR1-mpls] mpls te p2mp-te
      ```
      ```
      [*ABR1-mpls] quit
      ```
      ```
      [*ABR1] mpls ldp
      ```
      ```
      [*ABR1-mpls-ldp] quit
      ```
      ```
      [*ABR1] interface gigabitethernet0/1/0
      ```
      ```
      [*ABR1-GigabitEthernet0/1/0] mpls
      ```
      ```
      [*ABR1-GigabitEthernet0/1/0] mpls te
      ```
      ```
      [*ABR1-GigabitEthernet0/1/0] mpls rsvp-te
      ```
      ```
      [*ABR1-GigabitEthernet0/1/0] quit
      ```
      ```
      [*ABR1] interface gigabitethernet0/1/1
      ```
      ```
      [*ABR1-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*ABR1-GigabitEthernet0/1/1] mpls ldp
      ```
      ```
      [*ABR1-GigabitEthernet0/1/1] quit
      ```
      ```
      [*ABR1] commit
      ```
      
      
      
      # Configure ABR2.
      
      ```
      [~ABR2] mpls lsr-id 5.5.5.5
      ```
      ```
      [~ABR2] mpls
      ```
      ```
      [*ABR2-mpls] mpls te p2mp-te
      ```
      ```
      [*ABR2-mpls] quit
      ```
      ```
      [*ABR2] mpls ldp
      ```
      ```
      [*ABR2-mpls-ldp] quit
      ```
      ```
      [*ABR2] interface gigabitethernet0/1/0
      ```
      ```
      [*ABR2-GigabitEthernet0/1/0] mpls
      ```
      ```
      [*ABR2-GigabitEthernet0/1/0] mpls te
      ```
      ```
      [*ABR2-GigabitEthernet0/1/0] mpls rsvp-te
      ```
      ```
      [*ABR2-GigabitEthernet0/1/0] quit
      ```
      ```
      [*ABR2] interface gigabitethernet0/1/1
      ```
      ```
      [*ABR2-GigabitEthernet0/1/1] mpls
      ```
      ```
      [*ABR2-GigabitEthernet0/1/1] mpls ldp
      ```
      ```
      [*ABR2-GigabitEthernet0/1/1] quit
      ```
      ```
      [*ABR2] commit
      ```
      
      
      
      # Configure PE3.
      
      ```
      [~PE3] mpls lsr-id 6.6.6.6
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
   4. Establish a Multiprotocol Internal Border Gateway Protocol (MP-IBGP) peer relationship between PEs and ABRs.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] bgp 100
        ```
        ```
        [*PE1-bgp] peer 4.4.4.4 as-number 100
        ```
        ```
        [*PE1-bgp] peer 4.4.4.4 connect-interface LoopBack0
        ```
        ```
        [*PE1-bgp] peer 5.5.5.5 as-number 100
        ```
        ```
        [*PE1-bgp] peer 5.5.5.5 connect-interface LoopBack0
        ```
        ```
        [*PE1-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE1-bgp-af-vpnv4] peer 4.4.4.4 enable
        ```
        ```
        [*PE1-bgp-af-vpnv4] peer 5.5.5.5 enable
        ```
        ```
        [*PE1-bgp-af-vpnv4] quit
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
        [*PE2-bgp] peer 4.4.4.4 connect-interface LoopBack0
        ```
        ```
        [*PE2-bgp] peer 5.5.5.5 as-number 100
        ```
        ```
        [*PE2-bgp] peer 5.5.5.5 connect-interface LoopBack0
        ```
        ```
        [*PE2-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE2-bgp-af-vpnv4] peer 4.4.4.4 enable
        ```
        ```
        [*PE2-bgp-af-vpnv4] peer 5.5.5.5 enable
        ```
        ```
        [*PE2-bgp-af-vpnv4] quit
        ```
        ```
        [*PE2-bgp] quit
        ```
        ```
        [*PE2] commit
        ```
      * # Configure ABR1.
        
        ```
        [~ABR1] bgp 100
        ```
        ```
        [*ABR1-bgp] peer 2.2.2.2 as-number 100
        ```
        ```
        [*ABR1-bgp] peer 2.2.2.2 connect-interface LoopBack0
        ```
        ```
        [*ABR1-bgp] peer 3.3.3.3 as-number 100
        ```
        ```
        [*ABR1-bgp] peer 3.3.3.3 connect-interface LoopBack0
        ```
        ```
        [*ABR1-bgp] peer 6.6.6.6 as-number 100
        ```
        ```
        [*ABR1-bgp] peer 6.6.6.6 connect-interface LoopBack0
        ```
        ```
        [*ABR1-bgp] ipv4-family vpnv4
        ```
        ```
        [*ABR1-bgp-af-vpnv4] peer 2.2.2.2 enable
        ```
        ```
        [*ABR1-bgp-af-vpnv4] peer 3.3.3.3 enable
        ```
        ```
        [*ABR1-bgp-af-vpnv4] peer 6.6.6.6 enable
        ```
        ```
        [*ABR1-bgp-af-vpnv4] quit
        ```
        ```
        [*ABR1-bgp] quit
        ```
        ```
        [*ABR1] commit
        ```
      * # Configure ABR2.
        
        ```
        [~ABR2] bgp 100
        ```
        ```
        [*ABR2-bgp] peer 2.2.2.2 as-number 100
        ```
        ```
        [*ABR2-bgp] peer 2.2.2.2 connect-interface LoopBack0
        ```
        ```
        [*ABR2-bgp] peer 3.3.3.3 as-number 100
        ```
        ```
        [*ABR2-bgp] peer 3.3.3.3 connect-interface LoopBack0
        ```
        ```
        [*ABR2-bgp] peer 6.6.6.6 as-number 100
        ```
        ```
        [*ABR2-bgp] peer 6.6.6.6 connect-interface LoopBack0
        ```
        ```
        [*ABR2-bgp] ipv4-family vpnv4
        ```
        ```
        [*ABR2-bgp-af-vpnv4] peer 2.2.2.2 enable
        ```
        ```
        [*ABR2-bgp-af-vpnv4] peer 3.3.3.3 enable
        ```
        ```
        [*ABR2-bgp-af-vpnv4] peer 6.6.6.6 enable
        ```
        ```
        [*ABR2-bgp-af-vpnv4] quit
        ```
        ```
        [*ABR2-bgp] quit
        ```
        ```
        [*ABR2] commit
        ```
      * # Configure PE3.
        
        ```
        [~PE3] bgp 100
        ```
        ```
        [*PE3-bgp] peer 4.4.4.4 as-number 100
        ```
        ```
        [*PE3-bgp] peer 4.4.4.4 connect-interface LoopBack0
        ```
        ```
        [*PE3-bgp] peer 5.5.5.5 as-number 100
        ```
        ```
        [*PE3-bgp] peer 5.5.5.5 connect-interface LoopBack0
        ```
        ```
        [*PE3-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE3-bgp-af-vpnv4] peer 4.4.4.4 enable
        ```
        ```
        [*PE3-bgp-af-vpnv4] peer 5.5.5.5 enable
        ```
        ```
        [*PE3-bgp-af-vpnv4] quit
        ```
        ```
        [*PE3-bgp] quit
        ```
        ```
        [*PE3] commit
        ```
   5. Configure a VPN instance on the PEs and bind the VPN instance to interfaces.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] ip vpn-instance VPNA
        ```
        ```
        [*PE1-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv4] route-distinguisher 200:1
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv4] vpn-target 3:3
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv4] quit
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
        [*PE1-GigabitEthernet0/1/1] ip address 192.168.1.2 24
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
        [*PE2] interface gigabitethernet0/1/1
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] ip address 192.168.2.2 24
        ```
        ```
        [*PE2-GigabitEthernet0/1/1] quit
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
        [*PE3-vpn-instance-VPNA-af-ipv4] route-distinguisher 600:1
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
        [*PE3-GigabitEthernet0/1/0] ip address 192.168.3.1 24
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
        [~PE1] ospf 2 vpn-instance VPNA
        ```
        ```
        [*PE1-ospf-2] import-route bgp
        ```
        ```
        [*PE1-ospf-2] area 0.0.0.0
        ```
        ```
        [*PE1-ospf-2-area-0.0.0.0] network 192.168.1.0 0.0.0.255
        ```
        ```
        [*PE1-ospf-2-area-0.0.0.0] quit
        ```
        ```
        [*PE1-ospf-2] quit
        ```
        ```
        [*PE1] bgp 100
        ```
        ```
        [*PE1-bgp] ipv4-family vpn-instance VPNA
        ```
        ```
        [*PE1-bgp-VPNA] import-route ospf 2
        ```
        ```
        [*PE1-bgp-VPNA] quit
        ```
        ```
        [*PE1-bgp] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] ospf 2 vpn-instance VPNA
        ```
        ```
        [*PE2-ospf-2] import-route bgp
        ```
        ```
        [*PE2-ospf-2] area 0.0.0.0
        ```
        ```
        [*PE2-ospf-2-area-0.0.0.0] network 192.168.2.0 0.0.0.255
        ```
        ```
        [*PE2-ospf-2-area-0.0.0.0] quit
        ```
        ```
        [*PE2-ospf-2] quit
        ```
        ```
        [*PE2] bgp 100
        ```
        ```
        [*PE2-bgp] ipv4-family vpn-instance VPNA
        ```
        ```
        [*PE2-bgp-VPNA] import-route ospf 2
        ```
        ```
        [*PE2-bgp-VPNA] quit
        ```
        ```
        [*PE2-bgp] quit
        ```
        ```
        [*PE2] commit
        ```
      * # Configure PE3.
        
        ```
        [~PE3] ospf 2 vpn-instance VPNA
        ```
        ```
        [*PE3-ospf-2] import-route bgp
        ```
        ```
        [*PE3-ospf-2] area 0
        ```
        ```
        [*PE3-ospf-2-area-0.0.0.0] network 192.168.3.0 0.0.0.255
        ```
        ```
        [*PE3-ospf-2-area-0.0.0.0] quit
        ```
        ```
        [*PE3-ospf-2] quit
        ```
        ```
        [*PE3] bgp 100
        ```
        ```
        [*PE3-bgp] ipv4-family vpn-instance VPNA
        ```
        ```
        [*PE3-bgp-VPNA] import-route ospf 2
        ```
        ```
        [*PE3-bgp-VPNA] quit
        ```
        ```
        [*PE3-bgp] quit
        ```
        ```
        [*PE3] commit
        ```
   7. Configure OSPF on each CE.
      
      
      * # Configure CE1.
        
        ```
        [~CE1] ospf 2
        ```
        ```
        [*CE1-ospf-2] area 0
        ```
        ```
        [*CE1-ospf-2-area-0.0.0.0] network 192.168.1.0 0.0.0.255
        ```
        ```
        [*CE1-ospf-2-area-0.0.0.0] network 10.1.3.0 0.0.0.255
        ```
        ```
        [*CE1-ospf-2-area-0.0.0.0] network 1.1.1.1 0.0.0.0
        ```
        ```
        [*CE1-ospf-2-area-0.0.0.0] quit
        ```
        ```
        [*CE1-ospf-2] quit
        ```
        ```
        [*CE1] commit
        ```
      * # Configure CE2.
        
        ```
        [~CE2] ospf 2
        ```
        ```
        [*CE2-ospf-2] area 0
        ```
        ```
        [*CE2-ospf-2-area-0.0.0.0] network 192.168.3.0 0.0.0.255
        ```
        ```
        [*CE2-ospf-2-area-0.0.0.0] network 10.1.4.0 0.0.0.255
        ```
        ```
        [*CE2-ospf-2-area-0.0.0.0] network 7.7.7.7 0.0.0.0
        ```
        ```
        [*CE2-ospf-2-area-0.0.0.0] quit
        ```
        ```
        [*CE2-ospf-2] quit
        ```
        ```
        [*CE2] commit
        ```
      
      After the preceding configurations are completed, run the [**display ip routing-table vpn-instance verbose**](cmdqueryname=display+ip+routing-table+vpn-instance+verbose) command on PE3. The command output shows a backup unicast route to the multicast source. Run the [**ping**](cmdqueryname=ping) command on CE2 to ping CE1. The command output shows that the ping operation is successful.
      
      ```
      [~PE3] display ip routing-table vpn-instance VPNA 10.1.3.0 verbose
      ```
      ```
      Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
      ------------------------------------------------------------------------------
      Routing Table : VPNA
      Summary Count : 1
      
      Destination: 10.1.3.0/24
           Protocol: IBGP            Process ID: 0
         Preference: 255                   Cost: 0
            NextHop: 4.4.4.4          Neighbour: 0.0.0.0
              State: Active Adv Relied      Age: 00h14m34s
                Tag: 0                 Priority: low
              Label: 32829              QoSInfo: 0x0
         IndirectID: 0xF60000B5       Instance:              
       RelayNextHop: 0.0.0.0          Interface: GigabitEthernet0/1/1
           TunnelID: 0x000000000300000001 Flags: RD
          BkNextHop: 5.5.5.5        BkInterface: GigabitEthernet0/1/2
            BkLabel: 32829          SecTunnelID: 0x0
       BkPETunnelID: 0x000000000300000002 BkPESecTunnelID: 0x0
       BkIndirectID: 0xF60000B6                            
      ```
      ```
      [~CE2] ping 1.1.1.1
      ```
      ```
        PING 1.1.1.1: 56  data bytes, press CTRL_C to break
          Reply from 1.1.1.1: bytes=56 Sequence=1 ttl=253 time=5 ms
          Reply from 1.1.1.1: bytes=56 Sequence=2 ttl=253 time=3 ms
          Reply from 1.1.1.1: bytes=56 Sequence=3 ttl=253 time=3 ms
          Reply from 1.1.1.1: bytes=56 Sequence=4 ttl=253 time=3 ms
          Reply from 1.1.1.1: bytes=56 Sequence=5 ttl=253 time=2 ms
      
        --- 1.1.1.1 ping statistics ---
          5 packet(s) transmitted
          5 packet(s) received
          0.00% packet loss
          round-trip min/avg/max = 2/3/5 ms
      ```
2. Establish BGP MVPN peer relationships on the PEs and ABRs.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] bgp 100
     ```
     ```
     [*PE1-bgp] ipv4-family mvpn
     ```
     ```
     [*PE1-bgp-af-mvpn] policy vpn-target
     ```
     ```
     [*PE1-bgp-af-mvpn] peer 4.4.4.4 enable
     ```
     ```
     [*PE1-bgp-af-mvpn] peer 5.5.5.5 enable
     ```
     ```
     [*PE1-bgp-af-mvpn] quit
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
     [*PE2-bgp] ipv4-family mvpn
     ```
     ```
     [*PE2-bgp-af-mvpn] policy vpn-target
     ```
     ```
     [*PE2-bgp-af-mvpn] peer 4.4.4.4 enable
     ```
     ```
     [*PE2-bgp-af-mvpn] peer 5.5.5.5 enable
     ```
     ```
     [*PE2-bgp-af-mvpn] quit
     ```
     ```
     [*PE2-bgp] quit
     ```
     ```
     [*PE2] commit
     ```
   * # Configure ABR1.
     
     ```
     [~ABR1] route-policy policy_name1 permit node 1
     ```
     ```
     [*ABR1-route-policy-rp1]apply stitch-pmsi mldp
     ```
     ```
     [*ABR1-route-policy-rp1]quit
     ```
     ```
     [*ABR1] bgp 100
     ```
     ```
     [*ABR1-bgp] ipv4-family mvpn
     ```
     ```
     [*ABR1-bgp-af-mvpn] reflect change-path-attribute
     ```
     ```
     [*ABR1-bgp-af-mvpn] undo policy vpn-target
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 2.2.2.2 enable
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 2.2.2.2 reflect-client
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 3.3.3.3 enable
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 3.3.3.3 reflect-client
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 6.6.6.6 enable
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 6.6.6.6 route-policy policy_name1 export
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 6.6.6.6 reflect-client
     ```
     ```
     [*ABR1-bgp-af-mvpn] quit
     ```
     ```
     [*ABR1-bgp] quit
     ```
     ```
     [*ABR1] commit
     ```
   * # Configure ABR2.
     
     ```
     [~ABR2] route-policy policy_name1 permit node 1
     ```
     ```
     [*ABR2-route-policy-rp1] apply stitch-pmsi mldp
     ```
     ```
     [*ABR2-route-policy-rp1] quit
     ```
     ```
     [*ABR2] bgp 100
     ```
     ```
     [*ABR2-bgp] ipv4-family mvpn
     ```
     ```
     [*ABR2-bgp-af-mvpn] reflect change-path-attribute
     ```
     ```
     [*ABR2-bgp-af-mvpn] undo policy vpn-target
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 2.2.2.2 enable
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 2.2.2.2 reflect-client
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 3.3.3.3 enable
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 3.3.3.3 reflect-client
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 6.6.6.6 enable
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 6.6.6.6 route-policy policy_name1 export
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 6.6.6.6 reflect-client
     ```
     ```
     [*ABR2-bgp-af-mvpn] quit
     ```
     ```
     [*ABR2-bgp] quit
     ```
     ```
     [*ABR2] commit
     ```
   * # Configure PE3.
     
     ```
     [~PE3] ip ip-prefix PE1 index 10 permit 2.2.2.2 32
     ```
     ```
     [~PE3] ip ip-prefix PE2 index 10 permit 3.3.3.3 32
     ```
     ```
     [~PE3] ip extcommunity-list segmented-nh basic ABR1 index 10 permit 4.4.4.4:0
     ```
     ```
     [~PE3] ip extcommunity-list segmented-nh basic ABR2 index 10 permit 5.5.5.5:0
     ```
     ```
     [~PE3] route-policy rp1 permit node 10
     ```
     ```
     [*PE3-route-policy-ABR1] if-match route-type mvpn 3
     ```
     ```
     [*PE3-route-policy-ABR1] if-match ip route-originator ip-prefix PE1
     ```
     ```
     [*PE3-route-policy-ABR1] if-match extcommunity-list segmented-nh ABR1
     ```
     ```
     [*PE3-route-policy-ABR1] apply local-preference 200
     ```
     ```
     [*PE3-route-policy-ABR1] quit
     ```
     ```
     [~PE3] route-policy rp1 permit node 11
     ```
     ```
     [*PE3-route-policy-ABR1] if-match route-type mvpn 1
     ```
     ```
     [*PE3-route-policy-ABR1] if-match ip route-originator ip-prefix PE1
     ```
     ```
     [*PE3-route-policy-ABR1] if-match extcommunity-list segmented-nh ABR1
     ```
     ```
     [*PE3-route-policy-ABR1] apply local-preference 200
     ```
     ```
     [*PE3-route-policy-ABR1] quit
     ```
     ```
     [~PE3] route-policy rp2 permit node 10
     ```
     ```
     [*PE3-route-policy-ABR2] if-match route-type mvpn 3
     ```
     ```
     [*PE3-route-policy-ABR2] if-match ip route-originator ip-prefix PE2
     ```
     ```
     [*PE3-route-policy-ABR2] if-match extcommunity-list segmented-nh ABR2
     ```
     ```
     [*PE3-route-policy-ABR2] apply local-preference 200
     ```
     ```
     [*PE3-route-policy-ABR2] quit
     ```
     ```
     [~PE3] route-policy rp2 permit node 11
     ```
     ```
     [*PE3-route-policy-ABR2] if-match route-type mvpn 1
     ```
     ```
     [*PE3-route-policy-ABR2] if-match ip route-originator ip-prefix PE2
     ```
     ```
     [*PE3-route-policy-ABR2] if-match extcommunity-list segmented-nh ABR2
     ```
     ```
     [*PE3-route-policy-ABR2] apply local-preference 200
     ```
     ```
     [*PE3-route-policy-ABR2] quit
     ```
     ```
     [*PE3] bgp 100
     ```
     ```
     [*PE3-bgp] ipv4-family mvpn
     ```
     ```
     [*PE3-bgp-af-mvpn] policy vpn-target
     ```
     ```
     [*PE3-bgp-af-mvpn] peer 4.4.4.4 enable
     ```
     ```
     [*PE3-bgp-af-mvpn] peer 5.5.5.5 enable
     ```
     ```
     [*PE3-bgp-af-mvpn] peer 4.4.4.4 route-policy rp1 import
     ```
     ```
     [*PE3-bgp-af-mvpn] peer 5.5.5.5 route-policy rp2 import
     ```
     ```
     [*PE3-bgp-af-mvpn] quit
     ```
     ```
     [*PE3-bgp] quit
     ```
     ```
     [*PE3] commit
     ```
3. Establish a BGP VPNv4 peer relationship between the ABRs.
   
   
   * # Configure ABR1.
     
     ```
     [~ABR1] route-policy policy_name1 permit node 1
     ```
     ```
     [*ABR1-route-policy-rp1] apply stitch-pmsi mldp
     ```
     ```
     [*ABR1-route-policy-rp1]quit
     ```
     ```
     [*ABR1] bgp 100
     ```
     ```
     [*ABR1-bgp] ipv4-family mvpn
     ```
     ```
     [*ABR1-bgp-af-mvpn] reflect change-path-attribute
     ```
     ```
     [*ABR1-bgp-af-mvpn] undo policy vpn-target
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 2.2.2.2 enable
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 2.2.2.2 reflect-client
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 3.3.3.3 enable
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 3.3.3.3 reflect-client
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 6.6.6.6 enable
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 6.6.6.6 route-policy policy_name1 export
     ```
     ```
     [*ABR1-bgp-af-mvpn] peer 6.6.6.6 reflect-client
     ```
     ```
     [*ABR1-bgp-af-mvpn] quit
     ```
     ```
     [*ABR1-bgp] quit
     ```
     ```
     [*ABR1] commit
     ```
   * # Configure ABR2.
     
     ```
     [~ABR2] route-policy policy_name1 permit node 1
     ```
     ```
     [*ABR2-route-policy-rp1]apply stitch-pmsi mldp
     ```
     ```
     [*ABR2-route-policy-rp1]quit
     ```
     ```
     [*ABR2] bgp 100
     ```
     ```
     [*ABR2-bgp] ipv4-family mvpn
     ```
     ```
     [*ABR2-bgp-af-mvpn] reflect change-path-attribute
     ```
     ```
     [*ABR2-bgp-af-mvpn] undo policy vpn-target
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 2.2.2.2 enable
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 2.2.2.2 reflect-client
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 3.3.3.3 enable
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 3.3.3.3 reflect-client
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 6.6.6.6 enable
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 6.6.6.6 route-policy policy_name1 export
     ```
     ```
     [*ABR2-bgp-af-mvpn] peer 6.6.6.6 reflect-client
     ```
     ```
     [*ABR2-bgp-af-mvpn] quit
     ```
     ```
     [*ABR2-bgp] quit
     ```
     ```
     [*ABR2] commit
     ```
4. Configure NG MVPN to support intra-AS inter-area segmented tunnels.
   
   
   * # Configure PE1.
     
     ```
     [*PE1] ip vpn-instance VPNA
     ```
     ```
     [*PE1-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] inter-area-segmented enable
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure PE2.
     
     ```
     [*PE2] ip vpn-instance VPNA
     ```
     ```
     [*PE2-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] inter-area-segmented enable
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA] quit
     ```
     ```
     [*PE2] commit
     ```
   * # Configure ABR1.
     
     ```
     [~ABR1] multicast mvpn inter-area-segmented enable
     ```
     ```
     [*ABR1] commit
     ```
   * # Configure ABR2.
     
     ```
     [~ABR2] multicast mvpn inter-area-segmented enable
     ```
     ```
     [*ABR2] commit
     ```
5. Configure PE1, PE2, ARB1, and ABR2 to use RSVP-TE to establish I-PMSI tunnels.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] multicast mvpn 2.2.2.2
     ```
     ```
     [*PE1] ip vpn-instance VPNA
     ```
     ```
     [*PE1-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4] multicast routing-enable
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] sender-enable
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] ipmsi-tunnel
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] mpls te
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi-mpls-te] p2mp-template t1
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi-mpls-te] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] multicast mvpn 3.3.3.3
     ```
     ```
     [*PE2] ip vpn-instance VPNA
     ```
     ```
     [*PE2-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4] multicast routing-enable
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] sender-enable
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] ipmsi-tunnel
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] mpls te
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi-mpls-te] p2mp-template t1
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi-mpls-te] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA] quit
     ```
     ```
     [*PE2] commit
     ```
   * # Configure ABR1.
     
     ```
     [~ABR1] multicast mvpn 4.4.4.4
     ```
     ```
     [*ABR1] commit
     ```
   * # Configure ABR2.
     
     ```
     [~ABR2] multicast mvpn 5.5.5.5
     ```
     ```
     [*ABR2] commit
     ```
6. Configure S-PMSI tunnels on PE1 and PE2.
   
   
   * # Configure PE1.
     
     ```
     [*PE1] ip vpn-instance VPNA
     ```
     ```
     [*PE1-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] spmsi-tunnel
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi-mpls-te] group 225.1.1.1 255.255.255.255 source 10.1.3.2 255.255.255.255 rsvp-te p2mp-template t1
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi-mpls-te] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure PE2.
     
     ```
     [*PE2] ip vpn-instance VPNA
     ```
     ```
     [*PE2-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] spmsi-tunnel
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi-mpls-te] group 225.1.1.1 255.255.255.255 source 10.1.3.2 255.255.255.255 rsvp-te p2mp-template t1
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-spmsi-mpls-te] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4] quit
     ```
     ```
     [*PE2-vpn-instance-VPNA] quit
     ```
     ```
     [*PE2] commit
     ```
7. Configure VPN FRR on PE3.
   
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] ipv4-family vpn-instance VPNA
   ```
   ```
   [*PE3-bgp-VPNA] auto-frr
   ```
   ```
   [*PE3-bgp-VPNA] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
8. Enable C-multicast FRR on PE3.
   
   
   ```
   [~PE3] acl 2222
   ```
   ```
   [*PE3-acl4-basic-2222] rule permit source 225.1.1.0 0.0.0.255
   ```
   ```
   [*PE3-acl4-basic-2222] quit
   ```
   ```
   [*PE3] ip vpn-instance VPNA
   ```
   ```
   [*PE3-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv4] mvpn
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast frr 2222
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast frr flow-detection-based 2222
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv4] quit
   ```
   ```
   [*PE3-vpn-instance-VPNA] quit
   ```
   ```
   [*PE3] commit
   ```
9. Configure PIM.
   
   
   * # Configure PE1.
     
     ```
     [*PE1] interface gigabitethernet0/1/1
     ```
     ```
     [*PE1-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*PE1-GigabitEthernet0/1/1] quit
     ```
     ```
     [*PE1] commit
     ```
   * # Configure CE1.
     
     ```
     [~CE1] multicast routing-enable
     ```
     ```
     [*CE1] interface gigabitethernet0/1/0
     ```
     ```
     [*CE1-GigabitEthernet0/1/0] pim sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/0] quit
     ```
     ```
     [*CE1] interface gigabitethernet0/1/1
     ```
     ```
     [*CE1-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/1] quit
     ```
     ```
     [*CE1] interface gigabitethernet0/1/2
     ```
     ```
     [*CE1-GigabitEthernet0/1/2] pim sm
     ```
     ```
     [*CE1-GigabitEthernet0/1/2] quit
     ```
     ```
     [*CE1] commit
     ```
   * # Configure PE2.
     
     ```
     [*PE2] interface gigabitethernet0/1/1
     ```
     ```
     [*PE2-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*PE2-GigabitEthernet0/1/1] quit
     ```
     ```
     [*PE2] commit
     ```
   * # Configure PE3.
     
     ```
     [*PE3] interface gigabitethernet0/1/0
     ```
     ```
     [*PE3-GigabitEthernet0/1/0] pim sm
     ```
     ```
     [*PE3-GigabitEthernet0/1/0] quit
     ```
     ```
     [*PE3] commit
     ```
   * # Configure CE2.
     
     ```
     [~CE2] multicast routing-enable
     ```
     ```
     [*CE2] interface gigabitethernet0/1/0
     ```
     ```
     [*CE2-GigabitEthernet0/1/0] pim sm
     ```
     ```
     [*CE2-GigabitEthernet0/1/0] quit
     ```
     ```
     [*CE2] interface gigabitethernet0/1/1
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*CE2-GigabitEthernet0/1/1] quit
     ```
     ```
     [*CE2] commit
     ```
10. Configure IGMP.
    
    
    ```
    [~CE2] interface gigabitethernet0/1/1
    ```
    ```
    [*CE2-GigabitEthernet0/1/1] pim sm
    ```
    ```
    [*CE2-GigabitEthernet0/1/1] igmp enable
    ```
    ```
    [*CE2-GigabitEthernet0/1/1] igmp version 3
    ```
    ```
    [*CE2-GigabitEthernet0/1/1] quit
    ```
    ```
    [*CE2] commit
    ```
11. Verify the configuration.
    
    
    
    After the configurations are complete, mLDP P2MP tunnels have dual-root 1+1 protection. After users of CE2 send IGMPv3 Report messages and the multicast source at 10.1.3.2 sends multicast traffic, you can check multicast routing entries.
    
    * When the links are working properly:
      
      # Display the PIM routing table on PE3. As dual-root 1+1 protection is configured for mLDP P2MP tunnels, the command output shows that a backup PIM entry has been generated.
      ```
      [~PE3] display pim vpn-instance VPNA routing-table
      ```
      ```
       VPN-Instance: VPNA
       Total 0 (*, G) entry; 1 (S, G) entry
      
       (10.1.3.2, 225.1.1.1)
           RP: NULL
           Protocol: pim-sm, Flag: SPT ACT
           UpTime: 03:12:27
           Upstream interface: through-BGP, Refresh time: 03:12:27
               Upstream neighbor: 4.4.4.4
               RPF prime neighbor: 4.4.4.4
               Backup Upstream neighbor: 5.5.5.5
               Backup RPF prime neighbor: 5.5.5.5
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
      
      # Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command on receiver CE2 and sender CE1 to check their PIM routing tables. Run the [**display pim vpn-instance**](cmdqueryname=display+pim+vpn-instance) **routing-table** command on receiver PE3 and sender PE2 to check their PIM routing tables of the VPN instance.
      
      ```
      [~CE2] display pim routing-table
      ```
      ```
       VPN-Instance: public net
       Total 0 (*, G) entry; 1 (S, G) entry
      
       (10.1.3.2, 225.1.1.1)
           RP: NULL
           Protocol: pim-sm, Flag: SPT SG_RCVR ACT
           UpTime: 05:39:14
           Upstream interface: GigabitEthernet0/1/0, Refresh time: 05:39:14
               Upstream neighbor: 192.168.3.1
               RPF prime neighbor: 192.168.3.1
           Downstream interface(s) information:
           Total number of downstreams: 1
              1: GigabitEthernet0/1/1
                   Protocol: igmp, UpTime: 05:39:14, Expires: -  
      ```
      ```
      [~PE3] display pim vpn-instance VPNA routing-table
      ```
      ```
       VPN-Instance: VPNA
       Total 0 (*, G) entry; 1 (S, G) entry
      
       (10.1.3.2, 225.1.1.1)
           RP: NULL
           Protocol: pim-sm, Flag: SPT ACT
           UpTime: 03:32:13
           Upstream interface: through-BGP, Refresh time: 03:32:13
               Upstream neighbor: 5.5.5.5
               RPF prime neighbor: 5.5.5.5
           Downstream interface(s) information:
           Total number of downstreams: 1
              1: GigabitEthernet0/1/0
                   Protocol: pim-sm, UpTime: 03:32:13, Expires: 00:03:19   
      ```
      ```
      [~PE2] display pim vpn-instance VPNA routing-table
      ```
      ```
       VPN-Instance: VPNA
       Total 0 (*, G) entry; 1 (S, G) entry
      
       (10.1.3.2, 225.1.1.1)
           RP: NULL
           Protocol: pim-sm, Flag: SPT SG_RCVR ACT
           UpTime: 03:25:51
           Upstream interface: GigabitEthernet0/1/1, Refresh time: 03:25:51
               Upstream neighbor: 192.168.2.1
               RPF prime neighbor: 192.168.2.1
           Downstream interface(s) information:
           Total number of downstreams: 1
              1: pseudo
                   Protocol: BGP, UpTime: 03:25:51, Expires: -        
      ```
      ```
      [~CE1] display pim routing-table
      ```
      ```
       VPN-Instance: public net
       Total 0 (*, G) entry; 1 (S, G) entry
      
       (10.1.3.2, 225.1.1.1)
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
      
      The command outputs show that traffic exists in the backup tunnel because a backup upstream device is available. Therefore, multicast traffic in the backup tunnel can be forwarded to receivers immediately after the primary tunnel fault is detected through multicast traffic-based detection.

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.3.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 2
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  multicast mvpn 2.2.2.2
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     inter-area-segmented enable
     ipmsi-tunnel
      mpls-te
       p2mp-template t1
     spmsi-tunnel
      group 225.1.1.1 255.255.255.255 source 10.1.3.2 255.255.255.255 rsvp-te p2mp-template t1
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
   mpls te cspf
  #
  mpls te p2mp-template t1
   record-route label
   bandwidth ct0 100
   fast-reroute bandwidth
   bypass-attributes bandwidth 10 priority 7 7
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.15.2 255.255.255.0
   ospf enable 10 area 0.0.0.1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.7.1 255.255.255.0
   ospf enable 10 area 0.0.0.1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 2.2.2.2 255.255.255.255
   ospf enable 10 area 0.0.0.1
  #
  bgp 100
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack0
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.4 enable
    peer 5.5.5.5 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 4.4.4.4 enable
    peer 5.5.5.5 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.4 enable
    peer 5.5.5.5 enable
   #
   ipv4-family vpn-instance VPNA
    import-route ospf 2
  #
  ospf 2 vpn-instance VPNA
   import-route bgp
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  ospf 10
   opaque-capability enable
   area 0.0.0.1
    mpls-te enable
  #
  return
  ```
* ABR1 configuration file
  
  ```
  #
  sysname ABR1
  #
  multicast mvpn 4.4.4.4
  #
  multicast mvpn inter-area-segmented enable
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
   mpls te cspf
   lsp-trigger all
  #
  mpls ldp
   mldp p2mp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   network-entity 46.0006.0006.0004.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.15.1 255.255.255.0
   ospf enable 10 area 0.0.0.1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.7.3 255.255.255.0
   ospf enable 10 area 0.0.0.1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack0
   ip address 4.4.4.4 255.255.255.255
   ospf enable 10 area 0.0.0.1
   isis enable 1
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   peer 6.6.6.6 as-number 100
   peer 6.6.6.6 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
    peer 6.6.6.6 enable
    peer 6.6.6.6 reflect-client
   #
   ipv4-family mvpn
    reflect change-path-attribute
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
    peer 6.6.6.6 enable
    peer 6.6.6.6 route-policy policy_name1 export
    peer 6.6.6.6 reflect-client
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 2.2.2.2 next-hop-local
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
    peer 3.3.3.3 next-hop-local
    peer 6.6.6.6 enable
    peer 6.6.6.6 reflect-client
    peer 6.6.6.6 next-hop-local
  #
  ospf 10
   opaque-capability enable
   area 0.0.0.1
    mpls-te enable
  #
  route-policy policy_name1 permit node 1
   apply stitch-pmsi mldp
  #
  ip ip-prefix 1 index 10 permit 2.2.2.2 32
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  multicast mvpn 3.3.3.3
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 300:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     inter-area-segmented enable
     ipmsi-tunnel
      mpls-te
       p2mp-template t1
     spmsi-tunnel
      group 225.1.1.1 255.255.255.255 source 10.1.3.2 255.255.255.255 rsvp-te p2mp-template t1
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
   mpls te cspf
  #
  mpls te p2mp-template t1
   record-route label
   bandwidth ct0 100
   fast-reroute bandwidth
   bypass-attributes bandwidth 10 priority 7 7
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.16.2 255.255.255.0
   ospf enable 10 area 0.0.0.1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.7.1 255.255.255.0
   ospf enable 10 area 0.0.0.1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface LoopBack0
   ip address 3.3.3.3 255.255.255.255
   ospf enable 10 area 0.0.0.1
  #
  bgp 100
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack0
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.4 enable
    peer 5.5.5.5 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 5.5.5.5 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.4 enable
    peer 5.5.5.5 enable
   #
   ipv4-family vpn-instance VPNA
    import-route ospf 2
  #
  ospf 2 vpn-instance VPNA
   import-route bgp
   area 0.0.0.0
    network 192.168.2.0 0.0.0.255
  #
  ospf 10
   opaque-capability enable
   area 0.0.0.1
    mpls-te enable
  #
  return
  ```
* ABR2 configuration file
  
  ```
  #
  sysname ABR2
  #
  multicast mvpn 5.5.5.5
  #
  multicast mvpn inter-area-segmented enable
  mpls lsr-id 5.5.5.5
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
   mpls te cspf
   lsp-trigger all
  #
  mpls ldp
   mldp p2mp
   #
   ipv4-family
  #
  isis 1
   is-level level-2
   network-entity 46.0006.0006.0005.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.16.1 255.255.255.0
   ospf enable 10 area 0.0.0.1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.0.7.3 255.255.255.0
   ospf enable 10 area 0.0.0.1
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack0
   ip address 5.5.5.5 255.255.255.255
   ospf enable 10 area 0.0.0.1
   isis enable 1
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack0
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack0
   peer 6.6.6.6 as-number 100
   peer 6.6.6.6 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
    peer 6.6.6.6 enable
    peer 6.6.6.6 reflect-client
   #
   ipv4-family mvpn
    reflect change-path-attribute
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
    peer 6.6.6.6 enable
    peer 6.6.6.6 route-policy policy_name1 export
    peer 6.6.6.6 reflect-client
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 2.2.2.2 next-hop-local
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
    peer 3.3.3.3 next-hop-local
    peer 6.6.6.6 enable
    peer 6.6.6.6 reflect-client
    peer 6.6.6.6 next-hop-local
  #
  ospf 10
   opaque-capability enable
   area 0.0.0.1
    mpls-te enable
  #
  route-policy policy_name1 permit node 1
   apply stitch-pmsi mldp
  #
  ip ip-prefix 1 index 10 permit 3.3.3.3 32
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  multicast mvpn 6.6.6.6
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 600:1
    apply-label per-instance
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     c-multicast frr 2222
     c-multicast frr flow-detection-based 2222
  #
  acl 2222
   rule permit source 225.1.1.0 0.0.0.255
  #
  mpls lsr-id 6.6.6.6
  #
  mpls
  #
  mpls ldp
   mldp p2mp
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 46.0006.0006.0006.00
   traffic-eng level-1-2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.3.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack0
   ip address 6.6.6.6 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack0
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack0
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.4 enable
    peer 5.5.5.5 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 4.4.4.4 enable
    peer 4.4.4.4 route-policy rp1 import
    peer 5.5.5.5 enable
    peer 5.5.5.5 route-policy rp2 import
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.4 enable
    peer 5.5.5.5 enable
   #
   ipv4-family vpn-instance VPNA
    import-route isis 1
    import-route ospf 2
    auto-frr
  #
  ospf 2 vpn-instance VPNA
   import-route bgp
   area 0.0.0.0
    network 192.168.3.0 0.0.0.255
  #
  route-policy rp1 permit node 10
   if-match route-type mvpn 3
   if-match ip route-originator ip-prefix PE1
   if-match extcommunity-list segmented-nh ABR1
   apply local-preference 200
  #
  route-policy rp1 permit node 11
   if-match route-type mvpn 1
   if-match ip route-originator ip-prefix PE1
   if-match extcommunity-list segmented-nh ABR1
   apply local-preference 200
  #
  route-policy rp2 permit node 10
   if-match route-type mvpn 3
   if-match ip route-originator ip-prefix PE2
   if-match extcommunity-list segmented-nh ABR2
   apply local-preference 200
  #
  route-policy rp2 permit node 11
   if-match route-type mvpn 1
   if-match ip route-originator ip-prefix PE2
   if-match extcommunity-list segmented-nh ABR2
   apply local-preference 200
  #
  ip ip-prefix PE1 index 10 permit 2.2.2.2 32
  ip ip-prefix PE2 index 10 permit 3.3.3.3 32
  ip extcommunity-list segmented-nh basic ABR1 index 10 permit 4.4.4.4:0
  ip extcommunity-list segmented-nh basic ABR2 index 10 permit 5.5.5.5:0
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  multicast routing-enable
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.3.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.4.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
   igmp static-group 225.1.1.1 source 10.1.3.2
  #
  interface LoopBack0
   ip address 7.7.7.7 255.255.255.255
  #
  ospf 2
   area 0.0.0.0
    network 7.7.7.7 0.0.0.0
    network 10.1.4.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
  #
  return
  ```