Example for Configuring a Single-AS NG MVPN to Carry Multicast Traffic over an mLDP P2MP Tunnel
===============================================================================================

This section provides an example for configuring a single-AS NG MVPN to carry multicast traffic over an mLDP P2MP tunnel.

#### Networking Requirements

NG MVPN is deployed on the service provider's backbone network to solve multicast service issues that arise due to traffic congestion, transmission reliability, and data security. On the network shown in [Figure 1](#EN-US_TASK_0000001225513432__fig_dc_vrp_cfg_ngmvpn_001301), MPLS LDP tunnels have been deployed to carry BGP/MPLS IP VPN services. The service provider wants to provide MVPN services for users based on the existing network. To meet this requirement, configure a single-AS NG MVPN to carry multicast traffic over an mLDP P2MP tunnel.

**Figure 1** Single-AS NG MVPN networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE 0/1/0, GE 0/1/1, and GE 0/1/2, respectively.


  
![](figure/en-us_image_0000001225513780.png "Click to enlarge")

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure BGP/MPLS IP VPN to ensure that the unicast VPN is running properly. In this example, ensure mutual communication between CE1 and CE2, between CE1 and CE3, but not between CE2 and CE3.
2. Enable mLDP globally on all PEs so that they can use mLDP to establish P2MP tunnels.
3. Establish BGP MVPN peer relationships between the PEs so that the PEs can use BGP to exchange BGP A-D and BGP C-multicast routes.
4. Configure PE1 to use mLDP to establish an inclusive-provider multicast service interface (I-PMSI) tunnel.
5. Configure PE1 to use mLDP to establish an S-PMSI tunnel so that an mLDP P2MP tunnel is established.
6. Configure PIM on the PE interfaces bound to VPN instances and on the CE interfaces connecting to PEs to allow a VPN multicast routing table to be established to guide multicast traffic forwarding.
7. Configure IGMP on the interfaces connecting a multicast device to a user network segment to allow the device to manage multicast group members on the network segment.

#### Data Preparation

To complete the configuration, you need the following data:

* Public network OSPF process ID: 1; area ID: 0 OSPF multi-instance process ID: 2; area ID: 0
* VPN instance name on PE1, PE2, and PE3: VPNA; other data shown in [Table 1](#EN-US_TASK_0000001225513432__table_dc_vrp_cfg_ngmvpn_001301)
  
  **Table 1** Data preparation
  | Device Name | IP Address of Loopback 1 | MPLS LSR ID | MVPN ID | RD | VPN-Target | AS Number |
  | --- | --- | --- | --- | --- | --- | --- |
  | CE1 | 1.1.1.1 | - | - | - | - | - |
  | PE1 | 2.2.2.2 | 2.2.2.2 | 2.2.2.2 | 200:1 | 3:3 4:4 | AS100 |
  | PE2 | 3.3.3.3 | 3.3.3.3 | 3.3.3.3 | 300:1 | 3:3 | AS100 |
  | PE3 | 4.4.4.4 | 4.4.4.4 | 4.4.4.4 | 400:1 | 4:4 | AS100 |
  | CE2 | 5.5.5.5 | - | - | - | - | - |
  | CE3 | 6.6.6.6 | - | - | - | - | - |

#### Procedure

1. Configure BGP/MPLS IP VPN.
   1. Assign an IP address to each interface of devices on the VPN backbone network and VPN sites.
      
      
      
      Assign an IP address to each interface according to [Figure 1](#EN-US_TASK_0000001225513432__fig_dc_vrp_cfg_ngmvpn_001301). For configuration details, see [Configuration Files](#EN-US_TASK_0000001225513432__example_dc_vrp_cfg_ngmvpn_001301) in this section.
   2. Configure an IGP for interworking on the BGP/MPLS IP VPN backbone network.
      
      
      
      OSPF is used in this example. For configuration details, see [Configuration Files](#EN-US_TASK_0000001225513432__example_dc_vrp_cfg_ngmvpn_001301) in this section.
   3. Configure basic MPLS functions and enable MPLS LDP to establish LDP LSPs on the MPLS backbone network.
      
      
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
        [*PE3] commit
        ```
   4. Establish a Multiprotocol Internal Border Gateway Protocol (MP-IBGP) peer relationship between PEs.
      
      
      * # Configure PE1.
        
        ```
        [~PE1] bgp 100
        ```
        ```
        [*PE1-bgp] peer 3.3.3.3 as-number 100
        ```
        ```
        [*PE1-bgp] peer 3.3.3.3 connect-interface LoopBack1
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
        [*PE1-bgp-af-vpnv4] peer 3.3.3.3 enable
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
        [*PE2-bgp] peer 2.2.2.2 as-number 100
        ```
        ```
        [*PE2-bgp] peer 2.2.2.2 connect-interface LoopBack1
        ```
        ```
        [*PE2-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE2-bgp-af-vpnv4] peer 2.2.2.2 enable
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
        [*PE3-bgp] ipv4-family vpnv4
        ```
        ```
        [*PE3-bgp-af-vpnv4] peer 2.2.2.2 enable
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
   5. Configure a VPN instance on each PE so that each CE can access the corresponding PE.
      
      
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
        [*PE1-vpn-instance-VPNA-af-ipv4] vpn-target 3:3 4:4
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
        [*PE2-GigabitEthernet0/1/1] ip address 192.168.2.1 24
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
        [*PE3-vpn-instance-VPNA-af-ipv4] route-distinguisher 400:1
        ```
        ```
        [*PE3-vpn-instance-VPNA-af-ipv4] vpn-target 4:4
        ```
        ```
        [*PE3-vpn-instance-VPNA-af-ipv4] quit
        ```
        ```
        [*PE3-vpn-instance-VPNA] quit
        ```
        ```
        [*PE3] interface gigabitethernet0/1/1
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] ip binding vpn-instance VPNA
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] ip address 192.168.3.1 24
        ```
        ```
        [*PE3-GigabitEthernet0/1/1] quit
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
        [*PE1-ospf-2] area 0
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
        [*PE2-ospf-2] area 0
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
   7. # Configure OSPF on each CE.
      
      
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
        [*CE2-ospf-2-area-0.0.0.0] network 192.168.2.0 0.0.0.255
        ```
        ```
        [*CE2-ospf-2-area-0.0.0.0] network 10.1.4.0 0.0.0.255
        ```
        ```
        [*CE2-ospf-2-area-0.0.0.0] network 5.5.5.5 0.0.0.0
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
      * # Configure CE3.
        
        ```
        [~CE3] ospf 2
        ```
        ```
        [*CE3-ospf-2] area 0
        ```
        ```
        [*CE3-ospf-2-area-0.0.0.0] network 192.168.3.0 0.0.0.255
        ```
        ```
        [*CE3-ospf-2-area-0.0.0.0] network 10.1.5.0 0.0.0.255
        ```
        ```
        [*CE3-ospf-2-area-0.0.0.0] network 6.6.6.6 0.0.0.0
        ```
        ```
        [*CE3-ospf-2-area-0.0.0.0] quit
        ```
        ```
        [*CE3-ospf-2] quit
        ```
        ```
        [*CE3] commit
        ```
      
      After completing the configurations, run the [**display ip routing-table**](cmdqueryname=display+ip+routing-table) command on CE2 and CE3. The command outputs show that CE2 and CE3 have routes to CE1. Run the [**ping**](cmdqueryname=ping) command on CE2 and CE3 to ping CE1. The command outputs show the ping operations are successful. The command output on CE3 is used as an example.
      
      ```
      [~CE3] display ip routing-table
      ```
      ```
      Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
      ------------------------------------------------------------------------------
      Routing Table : _public_
               Destinations : 11       Routes : 11
      
      Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
      
              1.1.1.1/32  OSPF    10   3             D  192.168.3.1     GigabitEthernet0/1/0
              6.6.6.6/32  Direct  0    0             D  127.0.0.1       LoopBack1
             10.1.3.0/24  OSPF    10   4             D  192.168.3.1     GigabitEthernet0/1/0
            127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
            127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
      127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
          192.168.1.0/24  OSPF    10   3             D  192.168.3.1     GigabitEthernet0/1/0
          192.168.3.0/24  Direct  0    0             D  192.168.3.2     GigabitEthernet0/1/0
          192.168.3.2/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
          192.168.3.3/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
      255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0  
      ```
      ```
      [~CE3] ping 1.1.1.1
      ```
      ```
        PING 1.1.1.1: 56  data bytes, press CTRL_C to break
          Reply from 1.1.1.1: bytes=56 Sequence=1 ttl=253 time=118 ms
          Reply from 1.1.1.1: bytes=56 Sequence=2 ttl=253 time=3 ms
          Reply from 1.1.1.1: bytes=56 Sequence=3 ttl=253 time=4 ms
          Reply from 1.1.1.1: bytes=56 Sequence=4 ttl=253 time=3 ms
          Reply from 1.1.1.1: bytes=56 Sequence=5 ttl=253 time=3 ms
      
        --- 1.1.1.1 ping statistics ---
          5 packet(s) transmitted
          5 packet(s) received
          0.00% packet loss
          round-trip min/avg/max = 3/26/118 ms                     
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
3. Establish a BGP MVPN peer relationship between the PEs.
   
   
   * # Configure PE1.
     
     ```
     [~PE1] bgp 100
     ```
     ```
     [*PE1-bgp] ipv4-family mvpn
     ```
     ```
     [*PE1-bgp-af-mvpn] peer 3.3.3.3 enable
     ```
     ```
     [*PE1-bgp-af-mvpn] peer 4.4.4.4 enable
     ```
     ```
     [*PE1-bgp-af-mvpn] commit
     ```
     ```
     [~PE1-bgp-af-mvpn] quit
     ```
     ```
     [~PE1-bgp] quit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] bgp 100
     ```
     ```
     [*PE2-bgp] ipv4-family mvpn
     ```
     ```
     [*PE2-bgp-af-mvpn] peer 2.2.2.2 enable
     ```
     ```
     [*PE2-bgp-af-mvpn] commit
     ```
     ```
     [~PE2-bgp-af-mvpn] quit
     ```
     ```
     [~PE2-bgp] quit
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
     [*PE3-bgp-af-mvpn] commit
     ```
     ```
     [~PE3-bgp-af-mvpn] quit
     ```
     ```
     [~PE3-bgp] quit
     ```
   
   After completing the configurations, run the [**display bgp mvpn all peer**](cmdqueryname=display+bgp+mvpn+all+peer) command on the PEs. The command output shows that PE1 has established a BGP MVPN peer relationship with PE2 and PE3. The following example uses the command output on PE1:
   
   ```
   [~PE1] display bgp mvpn all peer
   ```
   ```
    BGP local router ID : 10.1.2.1
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     3.3.3.3         4         100       43       42     0 00:29:28 Established        2
     4.4.4.4         4         100       32       35     0 00:21:59 Established        1  
   ```
4. Configure each PE to use mLDP to establish an S-PMSI tunnel.
   
   
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
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] ipmsi-tunnel
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] mldp
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-ipmsi] quit
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn] spmsi-tunnel
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] group 225.0.0.0 255.255.255.0 mldp limit 1
     ```
     ```
     [*PE1-vpn-instance-VPNA-af-ipv4-mvpn-spmsi] quit
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
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] c-multicast signaling bgp
     ```
     ```
     [*PE2-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
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
     [*PE3-vpn-instance-VPNA-af-ipv4-mvpn] rpt-spt mode
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
   
   After completing the configuration, run the [**display mvpn vpn-instance ipmsi**](cmdqueryname=display+mvpn+vpn-instance+ipmsi) command on the PEs to check I-PMSI tunnel information. The following example uses the command output on PE1:
   
   ```
   [~PE1] display mvpn vpn-instance VPNA ipmsi
   ```
   ```
   MVPN local I-PMSI information for VPN-Instance: VPNA
   Tunnel type: mLDP P2MP LSP
   Tunnel state: Up 
   Root-ip: 2.2.2.2
   Opaque value: 0x01000400008021
   Root: 2.2.2.2 (local)
   Leaf:
     1: 3.3.3.3
     2: 4.4.4.4
   ```
   
   The command output shows that an mLDP P2MP tunnel has been established, with PE1 as the root node and PE2 and PE3 as leaf nodes.
5. Configure PIM.
   
   
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
     [*PE3] interface gigabitethernet0/1/1
     ```
     ```
     [*PE3-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*PE3-GigabitEthernet0/1/1] quit
     ```
     ```
     [*PE3] commit
     ```
   * # Configure CE3.
     
     ```
     [~CE3] multicast routing-enable
     ```
     ```
     [*CE3] interface gigabitethernet0/1/0
     ```
     ```
     [*CE3-GigabitEthernet0/1/0] pim sm
     ```
     ```
     [*CE3-GigabitEthernet0/1/0] quit
     ```
     ```
     [*CE3] interface gigabitethernet0/1/1
     ```
     ```
     [*CE3-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*CE3-GigabitEthernet0/1/1] quit
     ```
     ```
     [*CE3] commit
     ```
6. Configure IGMP and set the IGMP version to IGMPv3.
   
   
   * # Configure CE2.
     
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
     [*CE2-GigabitEthernet0/1/1] commit
     ```
     ```
     [~CE2-GigabitEthernet0/1/1] quit
     ```
   * # Configure CE3.
     
     ```
     [~CE3] interface gigabitethernet0/1/1
     ```
     ```
     [*CE3-GigabitEthernet0/1/1] pim sm
     ```
     ```
     [*CE3-GigabitEthernet0/1/1] igmp enable
     ```
     ```
     [*CE3-GigabitEthernet0/1/1] igmp version 3
     ```
     ```
     [*CE3-GigabitEthernet0/1/1] commit
     ```
     ```
     [~CE3-GigabitEthernet0/1/1] quit
     ```
7. Configure a static RP.
   
   
   * # Configure CE1.
     
     ```
     [~CE1] pim
     ```
     ```
     [*CE1-pim] static-rp 1.1.1.1
     ```
     ```
     [*CE1-pim] commit
     ```
     ```
     [~CE1-pim] quit
     ```
   * # Configure CE2.
     
     ```
     [~CE2] pim
     ```
     ```
     [*CE2-pim] static-rp 1.1.1.1
     ```
     ```
     [*CE2-pim] commit
     ```
     ```
     [~CE2-pim] quit
     ```
   * # Configure CE3.
     
     ```
     [~CE3] pim
     ```
     ```
     [*CE3-pim] static-rp 1.1.1.1
     ```
     ```
     [*CE3-pim] commit
     ```
     ```
     [~CE3-pim] quit
     ```
   * # Configure PE1.
     
     ```
     [~PE1] pim vpn-instance VPNA
     ```
     ```
     [*PE1-pim-VPNA] static-rp 1.1.1.1
     ```
     ```
     [*PE1-pim-VPNA] commit
     ```
     ```
     [~PE1-pim-VPNA] quit
     ```
   * # Configure PE2.
     
     ```
     [~PE2] pim vpn-instance VPNA
     ```
     ```
     [*PE2-pim-VPNA] static-rp 1.1.1.1
     ```
     ```
     [*PE2-pim-VPNA] commit
     ```
     ```
     [~PE2-pim-VPNA] quit
     ```
   * # Configure PE3.
     
     ```
     [~PE3] pim vpn-instance VPNA
     ```
     ```
     [*PE3-pim-VPNA] static-rp 1.1.1.1
     ```
     ```
     [*PE3-pim-VPNA] commit
     ```
     ```
     [~PE3-pim-VPNA] quit
     ```
8. Verify the configuration.
   
   
   
   After the configurations are complete, NG MVPN functions have been configured. If CE2 or CE3 has access users, CE1 can use the BGP/MPLS IP VPN to forward multicast data to the users. In this example, the user connected to CE2 or CE3 sends an IGMPv3 Report message, and the multicast source 10.1.3.1 sends multicast data. A check on multicast routing entries can determine whether NG MVPN is configured successfully.
   
   Run the [**display pim routing-table**](cmdqueryname=display+pim+routing-table) command on CE2, CE3, and CE1 to check the PIM routing table. Run the [**display pim vpn-instance**](cmdqueryname=display+pim+vpn-instance) **routing-table** command on PE2, PE3, and PE1 to check the PIM routing table of the VPN instance.
   
   ```
   [~CE2] display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.1.3.1, 225.1.1.1)
        RP:1.1.1.1
        Protocol: pim-sm, Flag: SPT SG_RCVR ACT
        UpTime: 00:54:11
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:54:11
            Upstream neighbor: 192.168.2.1
            RPF prime neighbor: 192.168.2.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: igmp, UpTime: 00:54:11, Expires: -
   ```
   ```
   [~CE3] display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.1.3.1, 226.1.1.1)
        RP:1.1.1.1
        Protocol: pim-sm, Flag: SPT SG_RCVR ACT
        UpTime: 00:01:57
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:01:57
            Upstream neighbor: 192.168.3.1
            RPF prime neighbor: 192.168.3.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: igmp, UpTime: 00:01:57, Expires: - 
   ```
   ```
   [~PE2] display pim vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.1.3.1, 225.1.1.1)
        RP:1.1.1.1
        Protocol: pim-sm, Flag: SPT ACT
        UpTime: 00:48:18
        Upstream interface: through-BGP, Refresh time: 00:48:18
            Upstream neighbor: 2.2.2.2
            RPF prime neighbor: 2.2.2.2
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:48:18, Expires: 00:03:12     
   ```
   ```
   [~PE3] display pim vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 0 (*, G) entry; 1 (S, G) entry
   
    (10.1.3.1, 226.1.1.1)
        RP:1.1.1.1
        Protocol: pim-sm, Flag: SPT ACT
        UpTime: 00:02:06
        Upstream interface: through-BGP, Refresh time: 00:02:06
            Upstream neighbor: 2.2.2.2
            RPF prime neighbor: 2.2.2.2
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:02:06, Expires: 00:03:26 
   ```
   ```
   [~PE1] display pim vpn-instance VPNA routing-table
   ```
   ```
    VPN-Instance: VPNA
    Total 0 (*, G) entry; 2 (S, G) entries
   
    (10.1.3.1, 225.1.1.1)
        RP:1.1.1.1
        Protocol: pim-sm, Flag: SPT SG_RCVR ACT
        UpTime: 00:46:58
        Upstream interface: GigabitEthernet0/1/1, Refresh time: 00:46:58
            Upstream neighbor: 192.168.1.1
            RPF prime neighbor: 192.168.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: pseudo
                Protocol: BGP, UpTime: 00:46:58, Expires: -
   
    (10.1.3.1, 226.1.1.1)
        RP:1.1.1.1
        Protocol: pim-sm, Flag: SPT SG_RCVR ACT
        UpTime: 00:00:23
        Upstream interface: GigabitEthernet0/1/1, Refresh time: 00:00:23
            Upstream neighbor: 192.168.1.1
            RPF prime neighbor: 192.168.1.1
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: pseudo
                Protocol: BGP, UpTime: 00:00:26, Expires: - 
   ```
   ```
   [~CE1] display pim routing-table
   ```
   ```
    VPN-Instance: public net
    Total 0 (*, G) entry; 2 (S, G) entries
   
    (10.1.3.1, 225.1.1.1)
        RP:1.1.1.1 (local)
        Protocol: pim-sm, Flag: SPT LOC ACT
        UpTime: 00:47:29
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:47:29
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:47:29, Expires: 00:03:03
   
    (10.1.3.1, 226.1.1.1)
        RP:1.1.1.1 (local)
        Protocol: pim-sm, Flag: SPT LOC ACT
        UpTime: 00:00:54
        Upstream interface: GigabitEthernet0/1/0, Refresh time: 00:00:54
            Upstream neighbor: NULL
            RPF prime neighbor: NULL
        Downstream interface(s) information:
        Total number of downstreams: 1
           1: GigabitEthernet0/1/1
                Protocol: pim-sm, UpTime: 00:00:54, Expires: 00:02:36  
   ```
   
   The command output shows that the CE connected to the multicast source has received PIM Join messages from the CEs connected to multicast receivers and that PIM routing entries are generated.

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
   ip address 10.1.3.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  ospf 2
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 192.168.1.0 0.0.0.255
  #
  pim
   static-rp 1.1.1.1
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
    vpn-target 4:4 export-extcommunity
    vpn-target 3:3 import-extcommunity
    vpn-target 4:4 import-extcommunity
    multicast routing-enable
    mvpn
     sender-enable
     c-multicast signaling bgp
     rpt-spt mode
     ipmsi-tunnel
      mldp
     spmsi-tunnel
      group 225.0.0.0 255.255.255.0 mldp limit 1
  #
  mpls lsr-id 2.2.2.2
  mpls
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
   ip binding vpn-instance VPNA
   ip address 192.168.1.2 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
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
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 3.3.3.3 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpn-instance VPNA
    import-route ospf 2
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
  #
  ospf 2 vpn-instance VPNA
   import-route bgp
   area 0.0.0.0
    network 192.168.1.0 0.0.0.255
  #
  pim vpn-instance VPNA
   static-rp 1.1.1.1
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
   ip address 192.168.2.2 255.255.255.0
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
  ospf 2
   area 0.0.0.0
    network 5.5.5.5 0.0.0.0
    network 10.1.4.0 0.0.0.255
    network 192.168.2.0 0.0.0.255
  #
  pim
   static-rp 1.1.1.1
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
     c-multicast signaling bgp
     rpt-spt mode
  #
  mpls lsr-id 3.3.3.3
  mpls
  #
  mpls ldp
   mldp p2mp
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip binding vpn-instance VPNA
   ip address 192.168.2.1 255.255.255.0
   pim sm
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance VPNA
    import-route ospf 2
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  ospf 2 vpn-instance VPNA
   import-route bgp
   area 0.0.0.0
    network 192.168.2.0 0.0.0.255
  #
  pim vpn-instance VPNA
   static-rp 1.1.1.1
  #
  
  return
  ```
* CE3 configuration file
  
  ```
  #
  sysname CE3
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
   ip address 10.1.5.1 255.255.255.0
   pim sm
   igmp enable
   igmp version 3
  #
  interface LoopBack1
   ip address 6.6.6.6 255.255.255.255
  #
  ospf 2
   area 0.0.0.0
    network 6.6.6.6 0.0.0.0
    network 10.1.5.0 0.0.0.255
    network 192.168.3.0 0.0.0.255
  #
  pim
   static-rp 1.1.1.1
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
    vpn-target 4:4 export-extcommunity
    vpn-target 4:4 import-extcommunity
    multicast routing-enable
    mvpn
     c-multicast signaling bgp
     rpt-spt mode
  #
  mpls lsr-id 4.4.4.4
  mpls
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
   ip binding vpn-instance VPNA
   ip address 192.168.3.1 255.255.255.0
   pim sm
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family mvpn
    policy vpn-target
    peer 2.2.2.2 enable
   #
   ipv4-family vpn-instance VPNA
    import-route ospf 2
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.1.2.0 0.0.0.255
  #
  ospf 2 vpn-instance VPNA
   import-route bgp
   area 0.0.0.0
    network 192.168.3.0 0.0.0.255
  #
  pim vpn-instance VPNA
   static-rp 1.1.1.1
  #
  return
  ```