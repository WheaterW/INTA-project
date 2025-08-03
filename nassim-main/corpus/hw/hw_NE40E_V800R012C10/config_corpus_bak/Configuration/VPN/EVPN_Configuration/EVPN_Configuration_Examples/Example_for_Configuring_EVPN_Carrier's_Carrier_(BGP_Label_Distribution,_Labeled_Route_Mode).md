Example for Configuring EVPN Carrier's Carrier (BGP Label Distribution, Labeled Route Mode)
===========================================================================================

This section provides an example for configuring carrier's carrier in a scenario where the Level 1 and Level 2 carriers belong to different ASs. After this configuration, the Level 2 carriers can provide BGP/MPLS IP VPN services.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001213911665__fig_dc_vrp_mpls-l3vpn-v4_cfg_204301), the Level 1 and Level 2 carriers are in different ASs, and the Level 2 carriers provide BGP/MPLS IP VPN services for their customers.

The difference between this section and [Example for Configuring EVPN Carrier's Carrier (LDP Multi-Instance)](dc_vrp_evpn_cfg_csc_0020.html) lies in that the Level 1 and Level 2 carriers belong to different ASs.

**Figure 1** Configuring carrier's carrier (solution 2)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](figure/en-us_image_0000001214071621.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. The exchange of two types of routes is essential to the implementation of carrier's carrier:
   
   * Exchange of the Level 2 carrier's internal routes on the Level 1 carrier's backbone network: The Level 1 carrier network regards the Level 2 carrier network as its access CE.
   * Exchange of the Level 2 carrier's external routes between Level 2 carrier PEs: An MP-EBGP peer relationship needs to be established between the Level 2 carrier PEs (PE3 and PE4).
2. During the configuration of inter-AS carrier's carrier, labeled MP-EBGP need to be configured between Level 1 carrier PEs and CEs for the exchange of labeled routes (because these devices belong to different ASs).

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of Level 1 carrier PEs and Level 2 carrier PEs and CEs
* Data required for configuring an IGP
* Names, RDs, and VPN targets of VPN instances created on PEs
* Two route-policies on Level 1 carrier CEs

#### Procedure

1. Configure EVPN on the Level 1 carrier's backbone network and use IS-IS as the IGP on the network. Enable LDP between PE1 and PE2, and establish an EVPN IBGP peer relationship.
   
   
   
   For detailed configurations, see [Example for Configuring EVPN Carrier's Carrier (LDP Multi-Instance)](dc_vrp_evpn_cfg_csc_0020.html).
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   During the IGP configuration, the 32-bit loopback interface address of each PE needs to be advertised.
2. Configure the Level 2 carrier network. Specifically, use OSPF as the IGP and enable LDP between PE3 and CE1 and between PE4 and CE2.
   
   
   
   The detailed configuration procedure is similar to that of [Example for Configuring EVPN Carrier's Carrier (LDP Multi-Instance)](dc_vrp_evpn_cfg_csc_0020.html).
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   During the IGP configuration, the 32-bit loopback interface address of each PE and CE needs to be advertised.
3. Configure Level 1 carrier CEs to access Level 1 carrier PEs and configure the exchange of labeled IPv4 routes between them.
   
   
   
   # Configure CE1 to exchange labeled IPv4 routes with PE1 and PE3.
   
   ```
   <~CE1> system-view
   ```
   ```
   [~CE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*CE1-Gigabitethernet0/2/0] ip address 11.1.1.1 24
   ```
   ```
   [*CE1-Gigabitethernet0/2/0] mpls
   ```
   ```
   [*CE1-Gigabitethernet0/2/0] quit
   ```
   ```
   [*CE1] route-policy policy1 permit node 1
   ```
   ```
   [*CE1-route-policy] apply mpls-label
   ```
   ```
   [*CE1-route-policy] quit
   ```
   ```
   [*CE1] route-policy policy2 permit node 2
   ```
   ```
   [*CE1-route-policy] if-match mpls-label
   ```
   ```
   [*CE1-route-policy] apply mpls-label
   ```
   ```
   [*CE1-route-policy] quit
   ```
   ```
   [*CE1] bgp 200
   ```
   ```
   [*CE1-bgp] peer 1.1.1.9 as-number 200
   ```
   ```
   [*CE1-bgp] peer 1.1.1.9 connect-interface loopback 1
   ```
   ```
   [*CE1-bgp] peer 1.1.1.9 route-policy policy2 export
   ```
   ```
   [*CE1-bgp] peer 1.1.1.9 label-route-capability
   ```
   ```
   [*CE1-bgp] peer 11.1.1.2 as-number 100
   ```
   ```
   [*CE1-bgp] peer 11.1.1.2 route-policy policy1 export
   ```
   ```
   [*CE1-bgp] peer 11.1.1.2 label-route-capability
   ```
   ```
   [*CE1-bgp] import-route ospf 1
   ```
   ```
   [*CE1-bgp] commit
   ```
   ```
   [~CE1-bgp] quit
   ```
   
   # Configure PE1 to exchange labeled IPv4 routes with CE1.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To ensure normal forwarding, configure only the one-label-per-route mode for the VPN instance.
   
   ```
   <~PE1> system-view
   ```
   ```
   [~PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 200:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] apply-label per-route evpn
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both evpn
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-Gigabitethernet0/1/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE1-Gigabitethernet0/1/0] ip address 11.1.1.2 24
   ```
   ```
   [*PE1-Gigabitethernet0/1/0] mpls
   ```
   ```
   [*PE1-Gigabitethernet0/1/0] quit
   ```
   ```
   [*PE1] route-policy policy1 permit node 1
   ```
   ```
   [*PE1-route-policy] apply mpls-label
   ```
   ```
   [*PE1-route-policy] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-vpn1] peer 11.1.1.1 as-number 200
   ```
   ```
   [*PE1-bgp-vpn1] peer 11.1.1.1 route-policy policy1 export
   ```
   ```
   [*PE1-bgp-vpn1] peer 11.1.1.1 label-route-capability
   ```
   ```
   [*PE1-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*PE1-bgp-vpn1] commit
   ```
   ```
   [~PE1-bgp-vpn1] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure PE3 to exchange labeled IPv4 routes with CE1.
   
   ```
   <~PE3> system-view
   ```
   ```
   [~PE3] bgp 200
   ```
   ```
   [*PE3-bgp] peer 2.2.2.9 as-number 200
   ```
   ```
   [*PE3-bgp] peer 2.2.2.9 connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] peer 2.2.2.9 label-route-capability
   ```
   ```
   [*PE3-bgp] commit
   ```
   ```
   [~PE3-bgp] quit
   ```
   
   After the configuration is complete, a BGP peer relationship is established between CE1 and PE3 and between CE1 and PE1.
   
   ```
   [~CE1] display bgp peer
   ```
   ```
    BGP local router ID : 2.2.2.9
   ```
   ```
    Local AS number : 200
   ```
   ```
    Total number of peers : 2               Peers in established state : 2
   ```
   ```
     Peer       V   AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
   ```
   ```
     1.1.1.9    4  200        7        8     0 00:04:07 Established       0
   ```
   ```
     11.1.1.2   4  100        3        4     0 00:00:08 Established       0
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configurations of PE4, CE2, and PE2 are similar to those of PE3, CE1, and PE1, respectively.
4. Configure Level 2 carrier CEs to access Level 2 carrier PEs.
   
   
   
   The detailed configuration procedure is similar to that of [Example for Configuring EVPN Carrier's Carrier (LDP Multi-Instance)](dc_vrp_evpn_cfg_csc_0020.html).
5. Establish an MP-EBGP peer relationship between the Level 2 carrier PEs to exchange the VPN routes of Level 2 carrier CEs.
   
   
   
   # Configure PE3.
   
   ```
   <~PE3> system-view
   ```
   ```
   [~PE3] bgp 200
   ```
   ```
   [*PE3-bgp] peer 6.6.6.9 as-number 300
   ```
   ```
   [*PE3-bgp] peer 6.6.6.9 connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] peer 6.6.6.9 ebgp-max-hop 10
   ```
   ```
   [*PE3-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE3-bgp-af-vpnv4] peer 6.6.6.9 enable
   ```
   ```
   [*PE3-bgp-af-vpnv4] commit
   ```
   ```
   [~PE3-bgp-af-vpnv4] quit
   ```
   ```
   [~PE3-bgp] quit
   ```
   
   # Configure PE4.
   
   ```
   <~PE4> system-view
   ```
   ```
   [~PE4] bgp 300
   ```
   ```
   [*PE4-bgp] peer 1.1.1.9 as-number 200
   ```
   ```
   [*PE4-bgp] peer 1.1.1.9 connect-interface loopback 1
   ```
   ```
   [*PE4-bgp] peer 1.1.1.9 ebgp-max-hop 10
   ```
   ```
   [*PE4-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE4-bgp-af-vpnv4] peer 1.1.1.9 enable
   ```
   ```
   [*PE4-bgp-af-vpnv4] commit
   ```
   ```
   [~PE4-bgp-af-vpnv4] quit
   ```
   ```
   [~PE4-bgp] quit
   ```
6. Verify the configuration.
   
   
   
   After completing the configuration, run the **display ip routing-table** command on PE1 and PE2. The command output shows that only routes from the Level 1 carrier's network exist in the public routing tables on PE1 and PE2. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   ```
   ```
   Routing Table: Public
   ```
   ```
            Destinations : 7        Routes : 7
   ```
   ```
     Destination/Mask  Proto  Pre  Cost      Flags   NextHop        Interface
   ```
   ```
           3.3.3.9/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
           4.4.4.9/32  ISIS   15   10            D  30.1.1.2        Gigabitethernet0/2/0
   ```
   ```
          30.1.1.0/24  Direct 0    0             D  30.1.1.1        Gigabitethernet0/2/0
   ```
   ```
          30.1.1.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
          30.1.1.2/32  Direct 0    0             D  30.1.1.2        Gigabitethernet0/2/0
   ```
   ```
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   
   Run the **display ip routing-table vpn-instance** command on PE1 and PE2. The command output shows that only the Level 2 carriers' internal routes exist in the VPN routing tables of PE1 and PE2. The Level 2 carriers' external routes do not exist in these routing tables. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table vpn-instance vpn1
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   ```
   ```
   Routing Table: vpn1
   ```
   ```
            Destinations : 11       Routes : 11
   ```
   ```
   Destination/Mask  Proto  Pre  Cost        Flags  NextHop         Interface
   ```
   ```
         1.1.1.9/32  EBGP   255  10              D  11.1.1.1        Gigabitethernet0/1/0
   ```
   ```
         2.2.2.9/32  EBGP   255  0               D  11.1.1.1        Gigabitethernet0/1/0
   ```
   ```
         5.5.5.9/32  IBGP   255  0              RD  4.4.4.9         Gigabitethernet0/2/0
   ```
   ```
         6.6.6.9/32  IBGP   255  10             RD  4.4.4.9         Gigabitethernet0/2/0
   ```
   ```
        40.1.1.0/24  EBGP   255  0               D  11.1.1.1        Gigabitethernet0/1/0
   ```
   ```
        11.1.1.0/24  Direct 0    0               D  11.1.1.2        Gigabitethernet0/1/0
   ```
   ```
        11.1.1.1/32  Direct 0    0               D  11.1.1.1        Gigabitethernet0/1/0
   ```
   ```
        11.1.1.2/32  Direct 0    0               D  127.0.0.1       InLoopBack0
   ```
   ```
        20.1.1.0/24  IBGP    255  0              RD  4.4.4.9         Gigabitethernet0/2/0
   ```
   ```
        21.1.1.0/24  IBGP    255  0              RD  4.4.4.9         Gigabitethernet0/2/0
   ```
   ```
        21.1.1.2/32  IBGP    255  0              RD  4.4.4.9         Gigabitethernet0/2/0
   ```
   
   Run the **display ip routing-table** command on CE1 and CE2. The command output shows that only the Level 2 carriers' internal routes exist in the public network routing tables of CE1 and CE2. The Level 2 carriers' external routes do not exist in these routing tables. The following example uses the command output on CE1.
   
   ```
   [~CE1] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   ```
   ```
   Routing Table: Public
   ```
   ```
            Destinations : 15       Routes : 15
   ```
   ```
     Destination/Mask  Proto  Pre  Cost       Flags  NextHop         Interface
   ```
   ```
         1.1.1.9/32  OSPF   10   1              D  40.1.1.1        Gigabitethernet0/1/0
   ```
   ```
         2.2.2.9/32  Direct 0    0              D  127.0.0.1       InLoopBack0
   ```
   ```
         5.5.5.9/32  EBGP   255  0              D  11.1.1.2        Gigabitethernet0/2/0
   ```
   ```
         6.6.6.9/32  EBGP   255  0              D  11.1.1.2        Gigabitethernet0/2/0
   ```
   ```
        40.1.1.0/24  Direct 0    0              D  40.1.1.2        Gigabitethernet0/1/0
   ```
   ```
        40.1.1.1/32  Direct 0    0              D  40.1.1.1        Gigabitethernet0/1/0
   ```
   ```
        40.1.1.2/32  Direct 0    0              D  127.0.0.1       InLoopBack0
   ```
   ```
        11.1.1.0/24  Direct 0    0              D  11.1.1.1        Gigabitethernet0/2/0
   ```
   ```
        11.1.1.1/32  Direct 0    0              D  127.0.0.1       InLoopBack0
   ```
   ```
        11.1.1.2/32  Direct 0    0              D  11.1.1.2        Gigabitethernet0/2/0
   ```
   ```
        20.1.1.0/24  EBGP   255  0              D  11.1.1.2        Gigabitethernet0/2/0
   ```
   ```
        21.1.1.0/24  EBGP   255  0              D  11.1.1.2        Gigabitethernet0/2/0
   ```
   ```
        21.1.1.2/32  EBGP   255  0              D  11.1.1.2        Gigabitethernet0/2/0
   ```
   ```
        127.0.0.0/8  Direct 0    0              D  127.0.0.1       InLoopBack0
   ```
   ```
       127.0.0.1/32  Direct 0    0              D  127.0.0.1       InLoopBack0
   ```
   
   Run the **display ip routing-table** command on PE3 and PE4. The command output shows that the Level 2 carrier' internal routes exist in the public routing tables of PE3 and PE4. The following example uses the command output on PE3.
   
   ```
   [~PE3] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   ```
   ```
   Routing Table: Public
   ```
   ```
            Destinations : 14       Routes : 14
   ```
   ```
     Destination/Mask  Proto  Pre  Cost       Flags  NextHop         Interface
   ```
   ```
         1.1.1.9/32  Direct 0    0              D  127.0.0.1       InLoopBack0
   ```
   ```
         2.2.2.9/32  OSPF   10   1              D  40.1.1.2        Gigabitethernet0/2/0
   ```
   ```
         5.5.5.9/32  IBGP   255  0             RD  2.2.2.9         Gigabitethernet0/2/0
   ```
   ```
         6.6.6.9/32  IBGP   255  0             RD  2.2.2.9         Gigabitethernet0/2/0
   ```
   ```
        40.1.1.0/24  Direct 0    0              D  40.1.1.1        Gigabitethernet0/2/0
   ```
   ```
        40.1.1.1/32  Direct 0    0              D  127.0.0.1       InLoopBack0
   ```
   ```
        40.1.1.2/32  Direct 0    0              D  40.1.1.2        Gigabitethernet0/2/0
   ```
   ```
        11.1.1.0/24  EBGP   255  0             RD  6.6.6.9         Gigabitethernet0/2/0
   ```
   ```
        11.1.1.1/32  EBGP   255  0             RD  6.6.6.9         Gigabitethernet0/2/0
   ```
   ```
        20.1.1.0/24  IBGP   255  0             RD  2.2.2.9         Gigabitethernet0/2/0
   ```
   ```
        21.1.1.0/24  IBGP   255  0             RD  2.2.2.9         Gigabitethernet0/2/0
   ```
   ```
        21.1.1.2/32  IBGP   255  0             RD  2.2.2.9         Gigabitethernet0/2/0
   ```
   ```
        127.0.0.0/8  Direct 0    0              D  127.0.0.1       InLoopBack0
   ```
   ```
       127.0.0.1/32  Direct 0    0              D  127.0.0.1       InLoopBack0
   ```
   
   Run the **display ip routing-table vpn-instance** command on PE3 and PE4. The command output shows that the Level 2 carriers' external routes exist in the VPN routing tables of PE3 and PE4. The following example uses the command output on PE3.
   
   ```
   [~PE3] display ip routing-table vpn-instance vpn1
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   ```
   ```
   Routing Table: vpn1
   ```
   ```
            Destinations : 3        Routes : 3
   ```
   ```
     Destination/Mask  Proto  Pre  Cost      Flags  NextHop        Interface
   ```
   ```
         172.16.1.0/24 Direct 0    0             D  172.16.1.2     GigabitEthernet0/1/0
   ```
   ```
         172.16.1.2/32 Direct 0    0             D  127.0.0.1      InLoopBack0
   ```
   ```
         172.16.2.0/24 EBGP   255  0            RD  6.6.6.9        Gigabitethernet0/2/0
   ```
   
   PE3 and PE4 can ping each other.
   
   ```
   [~PE3] ping 20.1.1.2
   ```
   ```
     PING 20.1.1.2: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 20.1.1.2: bytes=56 Sequence=1 ttl=251 time=116 ms
   ```
   ```
       Reply from 20.1.1.2: bytes=56 Sequence=2 ttl=251 time=92 ms
   ```
   ```
       Reply from 20.1.1.2: bytes=56 Sequence=3 ttl=251 time=118 ms
   ```
   ```
       Reply from 20.1.1.2: bytes=56 Sequence=4 ttl=251 time=103 ms
   ```
   ```
       Reply from 20.1.1.2: bytes=56 Sequence=5 ttl=251 time=121 ms
   ```
   ```
     --- 20.1.1.2 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 92/110/121 ms
   ```
   
   CE3 and CE4 can ping each other.
   
   ```
   [~CE3] ping 172.16.2.1
   ```
   ```
     PING 172.16.2.1: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 172.16.2.1: bytes=56 Sequence=1 ttl=251 time=65 ms
   ```
   ```
       Reply from 172.16.2.1: bytes=56 Sequence=2 ttl=251 time=114 ms
   ```
   ```
       Reply from 172.16.2.1: bytes=56 Sequence=3 ttl=251 time=80 ms
   ```
   ```
       Reply from 172.16.2.1: bytes=56 Sequence=4 ttl=251 time=88 ms
   ```
   ```
       Reply from 172.16.2.1: bytes=56 Sequence=5 ttl=251 time=105 ms
   ```
   ```
     --- 172.16.2.1 ping statistics ---
   ```
   ```
       5 packet(s) transmitted
   ```
   ```
       5 packet(s) received
   ```
   ```
       0.00% packet loss
   ```
   ```
       round-trip min/avg/max = 65/90/114 ms
   ```

#### Configuration Files

* CE3 configuration file
  
  ```
  #
  sysname CE3
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.1.1 255.255.255.0
  #
  bgp 65410
   peer 172.16.1.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 172.16.1.2 enable
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-route
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 172.16.1.2 255.255.255.0
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 40.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #
  bgp 200
   peer 2.2.2.9 as-number 200
   peer 2.2.2.9 connect-interface LoopBack1
   peer 6.6.6.9 as-number 300
   peer 6.6.6.9 ebgp-max-hop 10
   peer 6.6.6.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.9 enable
    peer 2.2.2.9 label-route-capability
    peer 6.6.6.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 6.6.6.9 enable
   #
   ipv4-family vpn-instance vpn1
    import-route direct
    peer 172.16.1.1 as-number 65410
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 40.1.1.0 0.0.0.255
  #
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #
  mpls ldp
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 40.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 11.1.1.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  bgp 200
   peer 11.1.1.2 as-number 100
   peer 1.1.1.9 as-number 200
   peer 1.1.1.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    import-route ospf 1
    peer 11.1.1.2 enable
    peer 11.1.1.2 route-policy policy1 export
    peer 11.1.1.2 label-route-capability
    peer 1.1.1.9 enable
    peer 1.1.1.9 route-policy policy2 export
    peer 1.1.1.9 label-route-capability
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 40.1.1.0 0.0.0.255
    network 11.1.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  route-policy policy2 permit node 2
   if-match mpls-label
   apply mpls-label
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:1
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    evpn mpls routing-enable
    apply-label per-route evpn
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0004.00
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 11.1.1.2 255.255.255.0
   mpls
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 30.1.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 4.4.4.9 as-number 100
   peer 4.4.4.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.9 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 4.4.4.9 enable
   #
   ipv4-family vpn-instance vpn1
    peer 11.1.1.1 as-number 200
    peer 11.1.1.1 route-policy policy1 export
    peer 11.1.1.1 label-route-capability
    import-route direct
    advertise l2vpn evpn
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 200:2
    vpn-target 1:1 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity evpn
    evpn mpls routing-enable
    apply-label per-route evpn
  #
  mpls lsr-id 4.4.4.9
  #
  mpls
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0005.00
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 30.1.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 21.1.1.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 3.3.3.9 as-number 100
   peer 3.3.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.9 enable
   #
   l2vpn-family evpn
    policy vpn-target
    peer 3.3.3.9 enable
   #
   ipv4-family vpn-instance vpn1
    peer 21.1.1.2 as-number 300
    peer 21.1.1.2 route-policy policy1 export
    peer 21.1.1.2 label-route-capability
    import-route direct
    advertise l2vpn evpn
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  mpls lsr-id 5.5.5.9
  #
  mpls
  #
  mpls ldp
  #
  interface Gigabitethernet0/1/0
   undo shutdown
   ip address 21.1.1.2 255.255.255.0
   mpls
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 20.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 5.5.5.9 255.255.255.255
  #
  bgp 300
   peer 21.1.1.1 as-number 100
   peer 6.6.6.9 as-number 300
   peer 6.6.6.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    import-route ospf 1
    peer 21.1.1.1 enable
    peer 21.1.1.1 route-policy policy1 export
    peer 21.1.1.1 label-route-capability
    peer 6.6.6.9 enable
    peer 6.6.6.9 route-policy policy2 export
    peer 6.6.6.9 label-route-capability
  #
  ospf 1
   area 0.0.0.0
    network 5.5.5.9 0.0.0.0
    network 21.1.1.0 0.0.0.255
    network 20.1.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  route-policy policy2 permit node 1
   if-match mpls-label
   apply mpls-label
  #
  return
  ```
* PE4 configuration file
  
  ```
  #
  sysname PE4
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:2
    apply-label per-route
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 6.6.6.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 172.16.2.2 255.255.255.0
  #
  interface Gigabitethernet0/2/0
   undo shutdown
   ip address 20.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 6.6.6.9 255.255.255.255
  #
  bgp 300
   peer 5.5.5.9 as-number 300
   peer 5.5.5.9 connect-interface LoopBack1
   peer 1.1.1.9 as-number 200
   peer 1.1.1.9 ebgp-max-hop 10
   peer 1.1.1.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 5.5.5.9 enable
    peer 5.5.5.9 label-route-capability
    peer 1.1.1.9 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.9 enable
   #
   ipv4-family vpn-instance vpn1
    peer 172.16.2.1 as-number 65420
    import-route direct
  #
  ospf 1
   area 0.0.0.0
    network 6.6.6.9 0.0.0.0
    network 20.1.1.0 0.0.0.255
  #
  return
  ```
* CE4 configuration file
  
  ```
  #
  sysname CE4
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 172.16.2.1 255.255.255.0
  #
  bgp 65420
   peer 172.16.2.2 as-number 300
   #
   ipv4-family unicast
    undo synchronization
    import-route direct
    peer 172.16.2.2 enable
  #
  return
  ```