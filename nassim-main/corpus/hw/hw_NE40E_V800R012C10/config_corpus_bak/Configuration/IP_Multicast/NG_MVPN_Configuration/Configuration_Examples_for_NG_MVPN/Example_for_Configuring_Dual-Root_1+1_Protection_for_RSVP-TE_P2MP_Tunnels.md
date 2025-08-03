Example for Configuring Dual-Root 1+1 Protection for RSVP-TE P2MP Tunnels
=========================================================================

This section provides an example for configuring dual-root 1+1 protection for P2MP TE tunnels.

#### Networking Requirements

In an NG MVPN scenario, if a sender PE on a P2MP tunnel fails, the C-multicast service will be interrupted. The network can rely only on unicast route convergence for recovery. However, unicast route convergence takes a long time and may fail to meet the high reliability requirements of some multicast services. To resolve this problem, you can configure dual-root 1+1 protection for RSVP-TE P2MP tunnels. On the network shown in [Figure 1](#EN-US_TASK_0000001225833364__fig_dc_vrp_cfg_ngmvpn_001601), a primary RSVP-TE P2MP tunnel is established with PE1 as the root node, and a backup RSVP-TE P2MP tunnel is established with PE2 as the root node. When links are working properly, multicast traffic is forwarded through both the primary and backup tunnels bidirectionally. The leaf node PE3 selects the multicast traffic received from the primary tunnel and discards the multicast traffic received from the backup tunnel. If PE1 fails, the leaf node can use BFD for P2MP TE to quickly detect the RSVP-TE P2MP tunnel fault and choose to accept the multicast traffic received from the backup tunnel. This accelerates multicast service convergence and improves reliability.

**Figure 1** Configuring dual-root 1+1 protection for RSVP-TE P2MP tunnels![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001270153841.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BGP/MPLS IP VPN to ensure that the unicast VPN is running properly.
2. Enable P2MP TE globally and configure a P2MP TE template on PEs so that the PEs can use RSVP-TE to establish P2MP tunnels.
3. Establish BGP MVPN peer relationships between the PEs so that the PEs can use BGP to exchange BGP A-D and BGP C-multicast routes.
4. Configure PE1 and PE2 as sender PEs. Configure RSVP-TE P2MP on PE1 and PE2 so that two RSVP-TE P2MP tunnels are established. One of the tunnels is rooted at PE1, the other tunnel is rooted at PE2, and PE3 is a leaf node on both tunnels.
5. Configure BFD for P2MP TE on the PEs to allow them to detect public network node or link failures.
6. Configure VPN FRR on PE3 so that PE3 can have two routes to the multicast source. PE3 uses the route advertised by PE1 as the primary route and the route advertised by PE2 as the backup route.
7. Enable C-multicast FRR on PE3.
8. Configure PIM on the PE interfaces bound to VPN instances and on the CE interfaces connecting to PEs to allow a VPN multicast routing table to be established to guide multicast traffic forwarding.
9. Configure IGMP on the interfaces connecting a multicast device to a user network segment to allow the device to manage multicast group members on the network segment.

#### Data Preparation

To complete the configuration, you need the following data:

* IS-IS process on the public network (process 1) in a Level-2 area; System IDs of PE1, PE2, and PE3 (10.0000.0000.0001.00, 10.0000.0000.0002.00, and 10.0000.0000.0003.00)
* VPN instance name on PE1, PE2, and PE3: VPNA; other data shown in [Table 1](#EN-US_TASK_0000001225833364__table_dc_vrp_cfg_ngmvpn_001601)
  
  **Table 1** Data preparation
  | Device Name | IP Address of Loopback 1 | MPLS LSR ID | MVPN ID | RD | VPN-Target | AS Number |
  | --- | --- | --- | --- | --- | --- | --- |
  | CE1 | 1.1.1.1 | - | - | - | - | AS65001 |
  | PE1 | 2.2.2.2 | 2.2.2.2 | 2.2.2.2 | 200:1 | 3:3 | AS100 |
  | PE2 | 3.3.3.3 | 3.3.3.3 | 3.3.3.3 | 300:1 | 3:3 | AS100 |
  | PE3 | 4.4.4.4 | 4.4.4.4 | 4.4.4.4 | 400:1 | 3:3 | AS100 |
  | CE2 | 5.5.5.5 | - | - | - | - | AS65002 |

#### Procedure

1. Configure BGP/MPLS IP VPN.
   1. Assign an IP address to each interface of devices on the VPN backbone network and VPN sites.
      
      
      
      Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0000001225833364__fig_dc_vrp_cfg_ngmvpn_001601). For configuration details, see [Configuration Files](#EN-US_TASK_0000001225833364__example_dc_vrp_cfg_ngmvpn_001601) in this section.
   2. Configure an IGP for interworking on the BGP/MPLS IP VPN backbone network.
      
      
      
      IS-IS is used in this example. For configuration details, see [Configuration Files](#EN-US_TASK_0000001225833364__example_dc_vrp_cfg_ngmvpn_001601) in this section.
   3. Configure basic MPLS functions and MPLS TE on the MPLS backbone network to establish MPLS TE tunnels.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] isis 1
        ```
        ```
        [*PE1-isis-1] cost-style wide
        ```
        ```
        [*PE1-isis-1] traffic-eng level-2
        ```
        ```
        [*PE1-isis-1] quit
        ```
        ```
        [*PE1] mpls lsr-id 2.2.2.2
        ```
        ```
        [*PE1] mpls
        ```
        ```
        [*PE1-mpls] mpls te
        ```
        ```
        [*PE1-mpls] mpls rsvp-te
        ```
        ```
        [*PE1-mpls] mpls te cspf
        ```
        ```
        [*PE1-mpls] quit
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
        [*PE1] interface Tunnel10
        ```
        ```
        [*PE1-Tunnel10] ip address unnumbered interface LoopBack1
        ```
        ```
        [*PE1-Tunnel10] tunnel-protocol mpls te
        ```
        ```
        [*PE1-Tunnel10] destination 4.4.4.4
        ```
        ```
        [*PE1-Tunnel10] mpls te tunnel-id 100
        ```
        ```
        [*PE1-Tunnel10] mpls te reserved-for-binding
        ```
        ```
        [*PE1-Tunnel10] quit
        ```
        ```
        [*PE1] commit
        ```
      * # Configure PE2.
        
        ```
        [~PE2] isis 1
        ```
        ```
        [*PE2-isis-1] cost-style wide
        ```
        ```
        [*PE2-isis-1] traffic-eng level-2
        ```
        ```
        [*PE2-isis-1] quit
        ```
        ```
        [*PE2] mpls lsr-id 3.3.3.3
        ```
        ```
        [*PE2] mpls
        ```
        ```
        [*PE2-mpls] mpls te
        ```
        ```
        [*PE2-mpls] mpls rsvp-te
        ```
        ```
        [*PE2-mpls] mpls te cspf
        ```
        ```
        [*PE2-mpls] quit
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
        [*PE2] interface Tunnel10
        ```
        ```
        [*PE2-Tunnel10] ip address unnumbered interface LoopBack1
        ```
        ```
        [*PE2-Tunnel10] tunnel-protocol mpls te
        ```
        ```
        [*PE2-Tunnel10] destination 4.4.4.4
        ```
        ```
        [*PE2-Tunnel10] mpls te tunnel-id 200
        ```
        ```
        [*PE2-Tunnel10] mpls te reserved-for-binding
        ```
        ```
        [*PE2-Tunnel10] quit
        ```
        ```
        [*PE2] commit
        ```
      * # Configure PE3.
        
        ```
        [~PE3] isis 1
        ```
        ```
        [*PE3-isis-1] cost-style wide
        ```
        ```
        [*PE3-isis-1] traffic-eng level-2
        ```
        ```
        [*PE3-isis-1] quit
        ```
        ```
        [*PE3] mpls lsr-id 4.4.4.4
        ```
        ```
        [*PE3] mpls
        ```
        ```
        [*PE3-mpls] mpls te
        ```
        ```
        [*PE3-mpls] mpls rsvp-te
        ```
        ```
        [*PE3-mpls] mpls te cspf
        ```
        ```
        [*PE3-mpls] quit
        ```
        ```
        [*PE3] interface gigabitethernet0/1/1
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] mpls
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] mpls te
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] mpls rsvp-te
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
        [*PE3-GigabitEthernet0/1/2] mpls te
        ```
        ```
        [*PE3-GigabitEthernet0/1/2] mpls rsvp-te
        ```
        ```
        [*PE3-GigabitEthernet0/1/2] quit
        ```
        ```
        [*PE3] interface Tunnel10
        ```
        ```
        [*PE3-Tunnel10] ip address unnumbered interface LoopBack1
        ```
        ```
        [*PE3-Tunnel10] tunnel-protocol mpls te
        ```
        ```
        [*PE3-Tunnel10] destination 2.2.2.2
        ```
        ```
        [*PE3-Tunnel10] mpls te tunnel-id 100
        ```
        ```
        [*PE3-Tunnel10] mpls te reserved-for-binding
        ```
        ```
        [*PE3-Tunnel10] quit
        ```
        ```
        [*PE3] interface Tunnel11
        ```
        ```
        [*PE3-Tunnel11] ip address unnumbered interface LoopBack1
        ```
        ```
        [*PE3-Tunnel11] tunnel-protocol mpls te
        ```
        ```
        [*PE3-Tunnel11] destination 3.3.3.3
        ```
        ```
        [*PE3-Tunnel11] mpls te tunnel-id 200
        ```
        ```
        [*PE3-Tunnel11] mpls te reserved-for-binding
        ```
        ```
        [*PE3-Tunnel11] quit
        ```
        ```
        [*PE3] commit
        ```
   4. Establish an MP-IBGP peer relationship between the PEs.
      
      
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
        [*PE1-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE1-bgp-af-vpnv4] peer 4.4.4.4 enable
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
        [*PE2-bgp] peer 4.4.4.4 connect-interface LoopBack1
        ```
        ```
        [*PE2-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE2-bgp-af-vpnv4] peer 4.4.4.4 enable
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
        [*PE3-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE3-bgp-af-vpnv4] peer 2.2.2.2 enable
        ```
        ```
        [*PE3-bgp-af-vpnv4] peer 3.3.3.3 enable
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
   5. Configure a VPN instance on each PE for the access of the corresponding CE.
      
      
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
        [*PE2] interface gigabitethernet0/1/2
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] ip binding vpn-instance VPNA
        ```
        ```
        [*PE2-GigabitEthernet0/1/2] ip address 192.168.2.2 24
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
        [*PE3-GigabitEthernet0/1/0] ip address 192.168.3.1 24
        ```
        ```
        [*PE3-GigabitEthernet0/1/0] quit
        ```
        ```
        [*PE3] commit
        ```
   6. Configure a tunnel policy and apply it to the VPN instance.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] tunnel-policy p1
        ```
        ```
        [*PE1-tunnel-policy-p1] tunnel binding destination 4.4.4.4 te Tunnel10 down-switch
        ```
        ```
        [*PE1-tunnel-policy-p1] quit
        ```
        ```
        [*PE1] ip vpn-instance VPNA
        ```
        ```
        [*PE1-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*PE1-vpn-instance-VPNA-af-ipv4] tnl-policy p1
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
        [~PE2] tunnel-policy p1
        ```
        ```
        [*PE2-tunnel-policy-p1] tunnel binding destination 4.4.4.4 te Tunnel10 down-switch
        ```
        ```
        [*PE2-tunnel-policy-p1] quit
        ```
        ```
        [*PE2] ip vpn-instance VPNA
        ```
        ```
        [*PE2-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*PE2-vpn-instance-VPNA-af-ipv4] tnl-policy p1
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
      * # Configure PE3.
        
        ```
        [~PE3] tunnel-policy p1
        ```
        ```
        [*PE3-tunnel-policy-p1] tunnel binding destination 2.2.2.2 te Tunnel10 down-switch
        ```
        ```
        [*PE3-tunnel-policy-p1] tunnel binding destination 3.3.3.3 te Tunnel11 down-switch
        ```
        ```
        [*PE3-tunnel-policy-p1] quit
        ```
        ```
        [*PE3] ip vpn-instance VPNA
        ```
        ```
        [*PE3-vpn-instance-VPNA] ipv4-family
        ```
        ```
        [*PE3-vpn-instance-VPNA-af-ipv4] tnl-policy p1
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
   7. Establish BGP peer relationships between the PEs and CEs to import VPN routes.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] bgp 100
        ```
        ```
        [*PE1-bgp] ipv4-family vpn-instance VPNA
        ```
        ```
        [*PE1-bgp-VPNA] peer 192.168.1.1 as-number 65001
        ```
        ```
        [*PE1-bgp-VPNA] import-route direct
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
      * # Configure CE1.
        
        ```
        [~CE1] bgp 65001
        ```
        ```
        [*CE1-bgp] peer 192.168.1.2 as-number 100
        ```
        ```
        [*CE1-bgp] import-route direct
        ```
        ```
        [*CE1-bgp] quit
        ```
        ```
        [*CE1] commit
        ```
      
      The configurations between PE2 and CE1, and between PE3 and CE2 are similar to the configurations between PE1 and CE1. For configuration details, see [Configuration Files](#EN-US_TASK_0000001225833364__example_dc_vrp_cfg_ngmvpn_001601) in this section.
      
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
            NextHop: 2.2.2.2          Neighbour: 0.0.0.0
              State: Active Adv Relied      Age: 00h14m34s
                Tag: 0                 Priority: low
              Label: 32829              QoSInfo: 0x0
         IndirectID: 0xF60000B5        Instance: 
       RelayNextHop: 0.0.0.0          Interface: Tunnel10
           TunnelID: 0x000000000300000001 Flags: RD
          BkNextHop: 3.3.3.3        BkInterface: Tunnel11
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
2. Enable P2MP TE globally and configure a P2MP TE template.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls
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
   [*PE1-te-p2mp-template-t1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
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
   [*PE2-te-p2mp-template-t1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] mpls
   ```
   ```
   [*PE3-mpls] mpls te p2mp-te
   ```
   ```
   [*PE3-mpls] quit
   ```
   ```
   [*PE3] commit
   ```
3. Establish a BGP MVPN peer relationship between PEs.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] bgp 100
     ```
     ```
     [*PE1-bgp] ipv4-family mvpn
     ```
     ```
     [*PE1-bgp-af-mvpn] peer 4.4.4.4 enable
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
     [*PE2-bgp-af-mvpn] peer 4.4.4.4 enable
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
   * # Configure PE3.
     
     ```
     [~PE3] bgp 100
     ```
     ```
     [*PE3-bgp] ipv4-family mvpn
     ```
     ```
     [*PE3-bgp-af-mvpn] peer 2.2.2.2 enable
     ```
     ```
     [*PE3-bgp-af-mvpn] peer 3.3.3.3 enable
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
   
   After completing the configurations, run the [**display bgp mvpn all peer**](cmdqueryname=display+bgp+mvpn+all+peer) command on the PEs. The command output shows that PE3 has established a BGP MVPN peer relationship with PE1 and PE2. The command output on PE3 is used as an example.
   
   ```
   [~PE3] display bgp mvpn all peer
   ```
   ```
    BGP local router ID : 10.1.1.2
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2.2.2.2         4         100      275      290     0 03:10:56 Established    1
     3.3.3.3         4         100      286      294     0 03:44:39 Established    1
   ```
4. Configure each PE to use RSVP-TE to establish an I-PMSI tunnel.
   
   
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
   * # Configure PE3.
     
     ```
     [~PE3] multicast mvpn 4.4.4.4
     ```
     ```
     [*PE3] ip vpn-instance VPNA
     ```
     ```
     [*PE3-vpn-instance-VPNA] ipv4-family
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv4] multicast routing-enable
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv4] mvpn
     ```
     ```
     [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
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
   
   After completing the configuration, run the [**display mvpn vpn-instance ipmsi**](cmdqueryname=display+mvpn+vpn-instance+ipmsi) command on the PEs to check I-PMSI tunnel information. The following example uses the command outputs on PE1 and PE2.
   
   ```
   [~PE1] display mvpn vpn-instance VPNA ipmsi
   ```
   ```
   MVPN local I-PMSI information for VPN-Instance: VPNA
   Tunnel type: RSVP-TE P2MP LSP
   Tunnel state: Up 
   P2MP ID: 0x2020202
   Tunnel ID: 32769
   Extended tunnel ID: 2.2.2.2
   Root: 2.2.2.2 (local)
   Leaf:
     1: 4.4.4.4       
   ```
   ```
   [~PE2] display mvpn vpn-instance VPNA ipmsi
   ```
   ```
   MVPN local I-PMSI information for VPN-Instance: VPNA
   Tunnel type: RSVP-TE P2MP LSP
   Tunnel state: Up 
   P2MP ID: 0x3030303
   Tunnel ID: 32769
   Extended tunnel ID: 3.3.3.3
   Root: 3.3.3.3 (local)
   Leaf:
     1: 4.4.4.4    
   ```
   
   According to the preceding command outputs, two RSVP-TE P2MP tunnels have been established, with PE1 and PE2 as their root nodes and PE3 as a leaf node.
5. Configure BFD for P2MP TE on the PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls te bandwidth max-reservable-bandwidth 100000
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls te bandwidth bc0 100000
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] bfd
   ```
   ```
   [*PE1-bfd] quit
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
   [*PE1-te-p2mp-template-t1] bfd enable
   ```
   ```
   [*PE1-te-p2mp-template-t1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   
   
   # Configure PE2.
   
   ```
   [*PE2] interface gigabitethernet0/1/1
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] mpls te bandwidth max-reservable-bandwidth 100000
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] mpls te bandwidth bc0 100000
   ```
   ```
   [*PE2-GigabitEthernet0/1/1] quit
   ```
   ```
   [~PE2] bfd
   ```
   ```
   [*PE2-bfd] quit
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
   [*PE2-te-p2mp-template-t1] bfd enable
   ```
   ```
   [*PE2-te-p2mp-template-t1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   
   
   # Configure PE3.
   
   ```
   [~PE3] bfd
   ```
   ```
   [*PE3-bfd] mpls-passive
   ```
   ```
   [*PE3-bfd] quit
   ```
   ```
   [*PE3] commit
   ```
6. Configure VPN FRR on PE3.
   
   
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
7. Enable C-multicast FRR on PE3.
   
   
   ```
   [~PE3] ip vpn-instance VPNA
   ```
   ```
   [*PE3-vpn-instance-VPNA] ipv4-family
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv4] mvpn
   ```
   ```
   [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast frr
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
8. Configure PIM.
   
   
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
     [*PE2] interface gigabitethernet0/1/2
     ```
     ```
     [*PE2-GigabitEthernet0/1/2] pim sm
     ```
     ```
     [*PE2-GigabitEthernet0/1/2] quit
     ```
     ```
     [*PE2] commit
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
9. Configure IGMP.
   
   
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
10. Verify the configuration.
    
    
    
    After the configurations are complete, RSVP-TE P2MP tunnels have dual-root 1+1 protection. After users of CE2 send IGMPv3 Report messages and the multicast source at 10.1.3.2 sends multicast traffic, you can check multicast routing entries.
    
    * When the links are working properly:
      
      # Check the PIM routing table on PE3. As dual-root 1+1 protection is configured for RSVP-TE P2MP tunnels, the command output shows that a backup PIM entry has been generated.
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
               Upstream neighbor: 2.2.2.2
               RPF prime neighbor: 2.2.2.2
               Backup Upstream neighbor: 3.3.3.3
               Backup RPF prime neighbor: 3.3.3.3
           Downstream interface(s) information:
           Total number of downstreams: 1
              1: GigabitEthernet0/1/0
                   Protocol: pim-sm, UpTime: 03:12:27, Expires: 00:03:05 
      ```
      
      # Check the PIM routing table on CE1. The command output shows that a backup PIM entry has been generated.
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
              1: GigabitEthernet0/1/1
                   Protocol: pim-sm, UpTime: 03:28:03, Expires: 00:03:28   
              1: GigabitEthernet0/1/2
                   Protocol: pim-sm, UpTime: 03:28:03, Expires: 00:03:28   
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
               Upstream neighbor: 3.3.3.3
               RPF prime neighbor: 3.3.3.3
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
           Upstream interface: GigabitEthernet0/1/2, Refresh time: 03:25:51
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
      
      The command outputs show that traffic exists in the backup tunnel because a backup upstream device is available. Multicast traffic in the backup tunnel is forwarded to receivers immediately after BFD detects that the primary tunnel is faulty.

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
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 65001
   peer 192.168.1.2 as-number 100
   peer 192.168.2.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 192.168.1.2 enable
    peer 192.168.2.2 enable
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
    tnl-policy p1
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     ipmsi-tunnel
      mpls te
       p2mp-template t1
  #
  bfd
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
   bfd enable
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0001.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 100000
   mpls te bandwidth bc0 100000
   mpls rsvp-te
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 4.4.4.4
   mpls te reserved-for-binding
   mpls te tunnel-id 100
  #
  bgp 100
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.4 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 4.4.4.4 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
    peer 192.168.1.1 as-number 65001
  #
  tunnel-policy p1
   tunnel binding destination 4.4.4.4 te Tunnel10 down-switch 
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
    tnl-policy p1
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     ipmsi-tunnel
      mpls te
       p2mp-template t1
  #
  bfd
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
   bfd enable    
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0002.00
   traffic-eng level-2
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls te bandwidth max-reservable-bandwidth 100000
   mpls te bandwidth bc0 100000
   mpls rsvp-te     
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.2.2 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 4.4.4.4
   mpls te reserved-for-binding
   mpls te tunnel-id 200
  #
  bgp 100
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.4 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 4.4.4.4 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
    peer 192.168.2.1 as-number 65001
  #
  tunnel-policy p1
   tunnel binding destination 4.4.4.4 te Tunnel10 down-switch
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  multicast mvpn 4.4.4.4
  #
  ip vpn-instance VPNA
   ipv4-family
    route-distinguisher 400:1
    apply-label per-instance
    tnl-policy p1
    vpn-target 3:3 export-extcommunity
    vpn-target 3:3 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     c-multicast frr
  #
  bfd
   mpls-passive
  #
  mpls lsr-id 4.4.4.4    
  #
  mpls
   mpls te
   mpls te p2mp-te
   mpls rsvp-te
   mpls te cspf
  #
  isis 1
   is-level level-2
   cost-style wide
   network-entity 10.0000.0000.0003.00
   traffic-eng level-2
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
   mpls te
   mpls rsvp-te      
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
   mpls
   mpls te
   mpls rsvp-te   
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
   isis enable 1
  #
  interface Tunnel10
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 2.2.2.2
   mpls te reserved-for-binding
   mpls te tunnel-id 100
  #
  interface Tunnel11
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te reserved-for-binding
   mpls te tunnel-id 200
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
   ipv4-family mvpn
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-instance VPNA
    import-route direct
    auto-frr
    peer 192.168.3.2 as-number 65002
  #
  tunnel-policy p1
   tunnel binding destination 2.2.2.2 te Tunnel10 down-switch
   tunnel binding destination 3.3.3.3 te Tunnel11 down-switch  
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
  #
  interface LoopBack1
   ip address 5.5.5.5 255.255.255.255
  #
  bgp 65002
   peer 192.168.3.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 192.168.3.1 enable
  #
  return
  ```