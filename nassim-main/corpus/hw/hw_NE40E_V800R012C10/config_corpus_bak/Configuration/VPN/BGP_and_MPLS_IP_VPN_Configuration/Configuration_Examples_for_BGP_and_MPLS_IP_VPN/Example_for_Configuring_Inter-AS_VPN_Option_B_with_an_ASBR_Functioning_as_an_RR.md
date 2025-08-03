Example for Configuring Inter-AS VPN Option B with an ASBR Functioning as an RR
===============================================================================

In a scenario in which the backbone network spans two ASs, ASBRs need to advertise VPN-IPv4 routes through MP-EBGP. When multiple PEs exist in the ASs, you can configure an ASBR as an RR to simplify configurations.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172369512__fig_dc_vrp_mpls-l3vpn-v4_cfg_011801), CE1, CE2, and CE3 belong to the same VPN, and PE2 belongs to an AS different from that to which PE1 and PE3 belong. Inter-AS VPN Option B is deployed so that CE1, CE2, and CE3 can communicate. To simplify the configuration, you do not need to establish an MP-IBGP peer relationship between PE1 and PE3. Instead, you can configure ASBR1 as an RR. After receiving a route from PE1 (PE3), ASBR1 reflects the route to PE3 (PE1) and advertises the optimal route to ASBR2.

**Figure 1** Inter-AS VPN Option B (ASBR also functioning as an RR)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0199481792.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| CE1 | Loopback1 | 11.11.11.11/32 |
| GE0/1/0 | 10.1.1.1/24 |
| PE1 | Loopback1 | 1.1.1.1/32 |
| GE0/2/0 | 10.1.1.2/24 |
| GE0/1/0 | 10.10.1.2/24 |
| CE3 | Loopback1 | 33.33.33.33/32 |
| GE0/1/0 | 10.3.1.1/24 |
| PE3 | Loopback1 | 3.3.3.3/32 |
| GE0/2/0 | 10.3.1.2/24 |
| GE0/1/0 | 10.30.1.2/24 |
| ASBR1 | Loopback1 | 5.5.5.5/32 |
| GE0/1/0 | 10.10.1.1/24 |
| GE0/2/0 | 10.21.1.1/24 |
| GE0/3/0 | 10.30.1.1/24 |
| ASBR2 | Loopback1 | 6.6.6.6/32 |
| GE0/1/0 | 10.40.1.1/24 |
| GE0/2/0 | 10.21.1.2/24 |
| CE2 | Loopback1 | 22.22.22.22/32 |
| GE0/1/0 | 10.2.1.1/24 |
| PE2 | Loopback1 | 2.2.2.2/32 |
| GE0/1/0 | 10.40.1.2/24 |
| GE0/2/0 | 10.2.1.2/24 |



#### Precautions

During the configuration, note the following:

* ASBR1 is configured as an RR, and its clients are PE1 and PE3.
* ASBR1 does not filter received VPNv4 routes based on VPN targets.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP on the MPLS backbone network for communication between the ASBR and PE in the same AS, and set up an MPLS LDP LSP between them.
2. Set up EBGP peer relationships between PEs and CEs and MP-IBGP peer relationships between PEs and ASBRs.
3. Configure VPN instances on the PEs rather than ASBRs.
4. Enable MPLS on the interconnection interfaces between ASBRs and establish an MP-EBGP peer relationship between the ASBRs.
5. Configure ASBR1 as an RR.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of PEs and ASBRs: 1.1.1.1, 2.2.2.2, 3.3.3.3, 5.5.5.5, and 6.6.6.6
* Name (vpna), RDs (100:1, 200:2, and 100:3), and import and export VPN targets (111:1) of the VPN instance on each PE

#### Procedure

1. Configure an IGP on the MPLS backbone networks in AS 100 and AS 200 so that the PE on each MPLS backbone network can communicate with the ASBR on that network.
   
   
   
   OSPF is used in this example. For detailed configurations, see Configuration Files.
   
   After OSPF is configured, an OSPF neighbor relationship is established between the PE and ASBR. Run the **display ospf peer** command. The command output shows that the neighbor status is **Full**. Run the **display ip routing-table** command. The command output shows that PEs or ASBRs have learned the routes to each other's loopback interface.
2. Configure basic MPLS capabilities and MPLS LDP on the MPLS backbone network in each AS to establish LDP LSPs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.1
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
   [*PE1] interface gigabitethernet 0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   
   The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see Configuration Files.
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls lsr-id 5.5.5.5
   ```
   ```
   [*ASBR1] mpls
   ```
   ```
   [*ASBR1-mpls] quit
   ```
   ```
   [*ASBR1] mpls ldp
   ```
   ```
   [*ASBR1-mpls-ldp] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet 0/1/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*ASBR1] interface gigabitethernet 0/3/0
   ```
   ```
   [*ASBR1-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*ASBR1-GigabitEthernet0/3/0] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/3/0] quit
   ```
   
   The configuration of ASBR2 is similar to the configuration of ASBR1. For detailed configurations, see Configuration Files.
   
   After the configuration is complete, an LDP peer relationship is set up between the PE and ASBR. Run the **display mpls ldp session** command on each Router. The command output shows that **Status** is **Operational**. The following example uses the command output on PE1.
   
   ```
   <PE1> display mpls ldp session
   
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted. 
    -------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
    -------------------------------------------------------------------------
    5.5.5.5:0          Operational DU  Passive  0000:00:01  5/5
    -------------------------------------------------------------------------
    TOTAL: 1 session(s) Found.
   ```
3. Establish an MP-IBGP peer relationship between the PE and ASBR in each AS.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 5.5.5.5 as-number 100
   ```
   ```
   [*PE1-bgp] peer 5.5.5.5 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 5.5.5.5 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] commit
   ```
   ```
   [~PE1-bgp-af-vpnv4] quit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see Configuration Files.
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*ASBR1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*ASBR1-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*ASBR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 3.3.3.3 enable
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] commit
   ```
   ```
   [~ASBR1-bgp-af-vpnv4] quit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
   
   The configuration of ASBR2 is similar to that of ASBR1. For detailed configurations, see Configuration Files.
   
   After the configuration is complete, run the **display bgp vpnv4 all peer** command on the PE, ASBR1, or ASBR2. The command output shows that an MP-IBGP peer relationship has been established between the PE and each ASBR and is in the **Established** state. The following example uses the command output on PE1.
   
   ```
   <PE1> display bgp vpnv4 all peer
   BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 3
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
     5.5.5.5         4   100   12      18         0     00:09:38   Established   0
   ```
4. Configure VPN instances on PEs and configure CEs to access PEs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpna
   ```
   ```
   [*PE1-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE1-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpna] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see Configuration Files.
   
   After the configuration is complete, run the **display ip vpn-instance verbose** command on each PE to check VPN instance configurations.
   
   ```
   <PE1> display ip vpn-instance verbose
    Total VPN-Instances configured : 1
    Total IPv4 VPN-Instances configured : 1 
    Total IPv6 VPN-Instances configured : 0
   
    VPN-Instance Name and ID : vpna, 1
     Interfaces : GigabitEthernet0/2/0
    Address family ipv4 
     Create date : 2009/09/18 11:30:35
     Up time : 0 days, 00 hours, 05 minutes and 19 seconds
     Vrf Status : UP
     Route Distinguisher : 100:1
     Export VPN Targets :  111:1
     Import VPN Targets :  111:1
     Label policy: label per route
     The diffserv-mode Information is : uniform
     The ttl-mode Information is : pipe
   ```
5. Establish EBGP peer relationships between PEs and CEs, and import loopback routes from CEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-Loopback1] ip address 11.11.11.11 32
   ```
   ```
   [*CE1-Loopback1] quit
   ```
   ```
   [*CE1] bgp 65001
   ```
   ```
   [*CE1-bgp] peer 10.1.1.2 as-number 100
   ```
   ```
   [*CE1-bgp] network 11.11.11.11 32
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [~CE1] commit
   ```
   
   The configurations of CE2 and CE3 are similar to that of CE1. For detailed configurations, see Configuration Files.
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv4-family vpn-instance vpna
   ```
   ```
   [*PE1-bgp-vpna] peer 10.1.1.1 as-number 65001
   ```
   ```
   [*PE1-bgp-vpna] commit
   ```
   ```
   [~PE1-bgp-vpna] quit
   ```
   
   The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see Configuration Files.
   
   After the configuration is complete, run the **display bgp vpnv4 vpn-instance peer** command on PEs to check whether BGP peer relationships have been established between the PEs and CEs. The command output shows that the BGP peer relationships have been established between the PEs and CEs and are in the **Established** state.
   
   The following example uses the command output on PE1 to show that a BGP peer relationship has been established between PE1 and CE1.
   
   ```
   <PE1> display bgp vpnv4 vpn-instance vpna peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1            Peers in established state : 1
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
     10.1.1.1        4   65001  11     9          0     00:06:37   Established  1
   ```
6. Enable MPLS on the interconnection interfaces between ASBRs and establish an MP-EBGP peer relationship between the ASBRs. Configure the ASBRs not to filter received VPNv4 routes.
   
   # Configure ASBR1. Enable MPLS on GE0/2/0 connected to ASBR2.
   ```
   [~ASBR1] interface GigabitEthernet 0/2/0
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] ip address 10.21.1.1 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR1] commit
   ```
   
   # Configure ASBR1 to establish an MP-EBGP peer with ASBR2, and disable ASBR1 from filtering received VPNv4 routes.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [~ASBR1-bgp] peer 10.21.1.2 as-number 200
   ```
   ```
   [*ASBR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 10.21.1.2 enable
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] undo policy vpn-target
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] commit
   ```
   ```
   [~ASBR1-bgp-af-vpnv4] quit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
   
   The configuration of ASBR2 is similar to that of ASBR1. For detailed configurations, see Configuration Files.
7. Configure an ASBR as an RR to reflect VPNv4 routes from PE1 to PE3 and those from PE3 to PE1.
   
   
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [~ASBR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 1.1.1.1 reflect-client
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 3.3.3.3 reflect-client
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] commit
   ```
   ```
   [~ASBR1-bgp-af-vpnv4] quit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
8. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display bgp vpnv4 all routing-table** command on ASBRs to check routes learned from PEs. The following example uses the command output on ASBR2.
   
   ```
   <ASBR2> display bgp vpnv4 all routing-table
    BGP Local router ID is 6.6.6.6
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
   
    Total number of routes from all PE: 3
    Route Distinguisher: 100:1
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  11.11.11.11/32     5.5.5.5         0          100        0      100 65001i
    Route Distinguisher: 200: 2
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  22.22.22.22/32     2.2.2.2         0          100        0      65002i
    Route Distinguisher: 100:3
   
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  33.33.33.33/32     5.5.5.5         0          100        0     100 65003i
   ```
   
   CE1, CE2, and CE3 can ping each other successfully.
   
   ```
   <CE1> ping -a 11.11.11.11 33.33.33.33
     PING 33.33.33.33: 56  data bytes, press CTRL_C to break
       Reply from 33.33.33.33: bytes=56 Sequence=1 ttl=252 time=120 ms
       Reply from 33.33.33.33: bytes=56 Sequence=2 ttl=252 time=73 ms
       Reply from 33.33.33.33: bytes=56 Sequence=3 ttl=252 time=111 ms
       Reply from 33.33.33.33: bytes=56 Sequence=4 ttl=252 time=86 ms
       Reply from 33.33.33.33: bytes=56 Sequence=5 ttl=252 time=110 ms
     --- 33.33.33.33 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 73/100/120 ms 
   ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
  #
  interface Loopback1
   ip address 11.11.11.11 255.255.255.255
  #
  bgp 65001
   peer 10.1.1.2 as-number 100
   network 11.11.11.11 255.255.255.255
   #
   ipv4-family unicast
    undo synchronization
    peer 10.1.1.2 enable
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.1.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 5.5.5.5 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 5.5.5.5 enable
   #
   ipv4-family vpn-instance vpna
    peer 10.1.1.1 as-number 65001
  #
  ospf 1
   area 0.0.0.0
    network 10.10.1.0 0.0.0.255
    network 1.1.1.1 0.0.0.0
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 100:3
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.30.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.3.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 5.5.5.5 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 5.5.5.5 enable
   #
   ipv4-family vpn-instance vpna
    peer 10.3.1.1 as-number 65003
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.30.1.0 0.0.0.255
  #
  return
  ```
* CE3 configuration file
  
  ```
  #
  ```
  ```
  sysname CE3
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.3.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface Loopback1
  ```
  ```
   ip address 33.33.33.33 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 65003
  ```
  ```
   peer 10.3.1.2 as-number 100
  ```
  ```
   network 33.33.33.33 255.255.255.255
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization
    peer 10.3.1.2 enable
  ```
  ```
  #
  ```
  ```
  return
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
  #
  mpls lsr-id 5.5.5.5
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.21.1.1 255.255.255.0
   mpls
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.30.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 5.5.5.5 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 10.21.1.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 10.21.1.2 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
    peer 10.21.1.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 5.5.5.5 0.0.0.0
    network 10.10.1.0 0.0.0.255
    network 10.30.1.0 0.0.0.255
  #
  return
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  mpls lsr-id 6.6.6.6
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.40.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.21.1.2 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 6.6.6.6 255.255.255.255
  #
  bgp 200
   peer 2.2.2.2 as-number 200
   peer 2.2.2.2 connect-interface LoopBack1
   peer 10.21.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 10.21.1.1 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 10.21.1.1 enable
  #
  ospf 1
   area 0.0.0.0
    network 6.6.6.6 0.0.0.0
    network 10.40.1.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpna
   ipv4-family
    route-distinguisher 200:2
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.40.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpna
   ip address 10.2.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 200
   peer 6.6.6.6 as-number 200
   peer 6.6.6.6 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 6.6.6.6 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 6.6.6.6 enable
   #
   ipv4-family vpn-instance vpna
    peer 10.2.1.1 as-number 65002
  #
  ospf 1
   area 0.0.0.0
    network 10.40.1.0 0.0.0.255
    network 2.2.2.2 0.0.0.0
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
  #
  interface Loopback1
   ip address 22.22.22.22 255.255.255.255
  #
  bgp 65002
   peer 10.2.1.2 as-number 200
   network 22.22.22.22 255.255.255.255
   #
   ipv4-family unicast
    undo synchronization
    peer 10.2.1.2 enable
  #
  return
  ```