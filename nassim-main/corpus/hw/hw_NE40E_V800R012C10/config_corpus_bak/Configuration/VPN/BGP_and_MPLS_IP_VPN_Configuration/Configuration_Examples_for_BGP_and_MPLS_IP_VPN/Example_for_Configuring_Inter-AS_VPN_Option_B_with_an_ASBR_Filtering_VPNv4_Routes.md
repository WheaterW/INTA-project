Example for Configuring Inter-AS VPN Option B with an ASBR Filtering VPNv4 Routes
=================================================================================

A route-policy is configured on an ASBR to filter VPNv4 routes based on VPN targets and only some VPNv4 routes are saved.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369503__fig_dc_vrp_mpls-l3vpn-v4_cfg_011401), CE1, CE2, and CE3 belong to the same VPN; PE2 is not in the same AS as PE1 and PE3; CE2 and CE3 do not need to communicate. It is required that ASBR1 be configured to filter VPNv4 routes based on RDs so that the routes of CE3 cannot be transmitted to PE2 by ASBR2.

**Figure 1** Inter-AS VPN Option B with an ASBR filtering VPN routes  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_011401.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| CE1 | Loopback1 | 10.11.11.11/32 |
| GE0/1/0 | 10.1.1.1/24 |
| PE1 | Loopback1 | 1.1.1.1/32 |
| GE0/2/0 | 10.1.1.2/24 |
| GE0/1/0 | 172.16.1.2/24 |
| CE3 | Loopback1 | 10.33.33.33/32 |
| GE0/1/0 | 10.3.1.1/24 |
| PE3 | Loopback1 | 3.3.3.3/32 |
| GE0/2/0 | 10.3.1.2/24 |
| GE0/1/0 | 172.16.3.2/24 |
| ASBR1 | Loopback1 | 5.5.5.5/32 |
| GE0/1/0 | 172.16.1.1/24 |
| GE0/2/0 | 192.168.1.1/24 |
| GE0/3/0 | 172.16.3.1/24 |
| ASBR2 | Loopback1 | 6.6.6.6/32 |
| GE0/1/0 | 10.162.1.1/24 |
| GE0/2/0 | 192.168.1.2/24 |
| CE2 | Loopback1 | 10.22.22.22/32 |
| GE0/1/0 | 10.2.1.1/24 |
| PE2 | Loopback1 | 2.2.2.2/32 |
| GE0/2/0 | 10.2.1.2/24 |
| GE0/1/0 | 10.162.1.2/24 |



#### Configuration Notes

When configuring inter-AS VPN Option B with an ASBR filtering VPNv4 routes, note the following:

* An MP-IBGP peer relationship needs to be established between PE1 and PE3.
* There is no need to create VPN instances on the ASBRs. An ASBR needs to filter the VPNv4 routes advertised to the other ASBR based on RDs.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP on the MPLS backbone network for communication between the ASBR and PE in the same AS, and set up an MPLS LDP LSP between them.
2. Set up EBGP peer relationships between PEs and CEs and set up MP-IBGP peer relationships between the PEs and ASBRs.
3. Configure VPN instances on PEs, but not ASBRs.
4. Enable MPLS on the interface that connects one ASBR to the other ASBR and set up an MP-EBGP peer relationship between the ASBRs. An ASBR needs to filter the VPNv4 routes advertised to the other ASBR based on RDs.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of PE1 (1.1.1.1), PE2 (2.2.2.2), PE3 (3.3.3.3), ASBR1 (5.5.5.5), and ASBR2 (6.6.6.6)
* Name (vpna), RD (100:1, 200:2 and 100:3), and export and import VPN targets (111:1) of the VPN instance on each PE
* Route-policy used by an ASBR to filter VPNv4 routes based on RDs

#### Procedure

1. On the MPLS backbone networks in AS 100 and AS 200, configure IGP for devices in the same AS to communicate.
   
   
   
   This example uses OSPF as IGP. For configuration details, see the configuration files.
   
   After the configurations are complete, the OSPF neighbor relationship can be established between the devices in the same AS. Run the **display ospf peer** command. The command output shows that the neighbor relationship is in the **Full** state. Run the **display ip routing-table** command. The command output shows that PEs or ASBRs have learned the routes to each other's loopback interface.
2. Configure MPLS and MPLS LDP both globally and per interface on each node of the MPLS backbone network in each AS and set up LDP LSPs.
   
   
   
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
   
   The configurations of PE2 and PE3 are similar to that of PE1. For configuration details, see the configuration files.
   
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
   [*ASBR1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/1/0] quit
   ```
   
   The configuration of ASBR2 is similar to that of ASBR1. For detailed configurations, see Configuration Files.
   
   After the configurations are complete, the LDP peer relationship is established between PEs. Run the **display mpls ldp session** command on each device. The command output shows that the session status is **Operational**. The following example uses the command output on PE1.
   
   ```
   <PE1> display mpls ldp session
   
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted. 
    -------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge      KASent/Rcv
    -------------------------------------------------------------------------
    4.4.4.4:0          Operational DU   Passive  0000:00:01  5/5
    -------------------------------------------------------------------------
    TOTAL: 1 session(s) Found.
   ```
3. Set up MP-IBGP peer relationships between the PEs and ASBR in each AS and set up an MP-IBGP peer relationship between PE1 and PE3 in AS 100.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback 1
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
   [*PE1-bgp-af-vpnv4] peer 3.3.3.3 enable
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
   
   The configurations of PE2 and PE3 are similar to the configuration of PE1. For configuration details, see the configuration files.
   
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
   
   The configuration of ASBR2 is similar to that of ASBR1. For configuration details, see the configuration file.
   
   After completing the configurations, run the **display bgp vpnv4 all peer** command on the PEs or ASBRs. The command output shows that MP-IBGP peer relationships have been established between the PEs and ASBRs. The following example uses the command output on PE1.
   
   ```
   <PE1> display bgp vpnv4 all peer
   BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
     3.3.3.3         4   100   12      18         0     00:09:38   Established   0
     5.5.5.5         4   100   12      18         0     00:09:38   Established   0
   ```
4. Configure a VPN instance on each PE and bind the interface that connects a PE to a CE to the VPN instance on that PE.
   
   
   
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
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpna
   ```
   ```
   [*PE2-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] route-distinguisher 200:2
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE2-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE2-vpn-instance-vpna] quit
   ```
   ```
   [*PE2] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip address 10.2.1.2 24
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ip vpn-instance vpna
   ```
   ```
   [*PE3-vpn-instance-vpna] ipv4-family
   ```
   ```
   [*PE3-vpn-instance-vpna-af-ipv4] route-distinguisher 100:3
   ```
   ```
   [*PE3-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
   ```
   ```
   [*PE3-vpn-instance-vpna-af-ipv4] quit
   ```
   ```
   [*PE3-vpn-instance-vpna] quit
   ```
   ```
   [*PE3] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ip binding vpn-instance vpna
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ip address 10.3.1.2 24
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] commit
   ```
   ```
   [~PE3-GigabitEthernet0/2/0] quit
   ```
   
   # After completing the configurations, run the **display ip vpn-instance verbose** command on PEs. The command output shows VPN instance configurations.
   
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
5. Set up EBGP peer relationships between PEs and CEs, and import VPN routes to the loopback interfaces of the CEs.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface loopback 1
   ```
   ```
   [*CE1-Loopback1] ip address 10.11.11.11 32
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
   [*CE1-bgp] network 10.11.11.11 32
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] commit
   ```
   
   The configurations of CE2 and CE3 are similar to the configuration of CE1. For configuration details, see the configuration files.
   
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
   
   The configurations of PE2 and PE3 are similar to the configuration of PE1. For configuration details, see the configuration files.
   
   After completing the configurations, run the **display bgp vpnv4 vpn-instance peer** command on PEs. The command output shows that BGP peer relationships have been established between PEs and CEs.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   <PE1> display bgp vpnv4 vpn-instance vpna peer
   
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1            Peers in established state : 1
     Peer            V    AS  MsgRcvd  MsgSent    OutQ  Up/Down    State        PrefRcv
     10.1.1.1        4   65001  11     9          0     00:06:37   Established  1
   ```
6. Enable MPLS on the interface that connects one ASBR to the other ASBR, set up an MP-EBGP peer relationship between the ASBRs, and configure the ASBRs to filter received VPNv4 routes.
   
   # On ASBR1, enable MPLS on GE0/2/0 connected to ASBR2.
   ```
   [~ASBR1] interface GigabitEthernet 0/2/0
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] ip address 192.168.1.1 24
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
   
   # On ASBR1, set up an MP-EBGP peer relationship between ASBR1 and ASBR2, and configure ASBR1 to filter received VPNv4 routes.
   
   ```
   [~ASBR1] ip rd-filter 10 permit 100:3
   ```
   ```
   [*ASBR1] route-policy test deny node 10
   ```
   ```
   [*ASBR1-route-policy] if-match rd-filter 10
   ```
   ```
   [*ASBR1-route-policy] quit
   ```
   ```
   [*ASBR1] route-policy test permit node 20
   ```
   ```
   [*ASBR1-route-policy] commit
   ```
   ```
   [~ASBR1-route-policy] quit
   ```
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 192.168.1.2 as-number 200
   ```
   ```
   [*ASBR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 192.168.1.2 enable
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 192.168.1.2 route-policy test export
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
   # On ASBR2, enable MPLS on GE0/2/0 connected to ASBR1.
   ```
   [~ASBR2] interface GigabitEthernet 0/2/0
   ```
   ```
   [~ASBR2-GigabitEthernet0/2/0] ip address 192.168.1.2 24
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*ASBR2] commit
   ```
   
   # On ASBR2, set up an MP-EBGP peer relationship between ASBR2 and ASBR1, and configure ASBR2 not to filter received VPNv4 routes.
   
   ```
   [~ASBR2] bgp 200
   ```
   ```
   [*ASBR2-bgp] peer 192.168.1.1 as-number 100
   ```
   ```
   [*ASBR2-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR2-bgp-af-vpnv4] peer 192.168.1.1 enable
   ```
   ```
   [*ASBR2-bgp-af-vpnv4] undo policy vpn-target
   ```
   ```
   [*ASBR2-bgp-af-vpnv4] commit
   ```
   ```
   [~ASBR2-bgp-af-vpnv4] quit
   ```
   ```
   [~ASBR2-bgp] quit
   ```
7. Verify the configuration.
   
   
   
   After completing the configurations, run the **display bgp vpnv4 all routing-table** command on ASBR1. The command output shows routes sent by PE3.
   
   ```
   <ASBR1> display bgp vpnv4 all routing-table
    BGP Local router ID is 5.5.5.5
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total number of routes from all PE: 3
    Route Distinguisher: 100:1
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  10.11.11.11/32     1.1.1.1         0          100        0      65001i
    Route Distinguisher: 200:2
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  10.22.22.22/32     6.6.6.6         0          100        0      200 65002i
    Route Distinguisher: 100:3
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  10.33.33.33/32     3.3.3.3         0          100        0      65003i
   ```
   
   Run the **display bgp vpnv4 all routing-table** command on ASBR2. The command output shows that there are no routes sent from PE3.
   
   ```
   <ASBR2> display bgp vpnv4 all routing-table
    BGP Local router ID is 6.6.6.6
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total number of routes from all PE: 2
    Route Distinguisher: 100:1
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  10.11.11.11/32     5.5.5.5         0          100        0      100 65001i
    Route Distinguisher: 200:2
   
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
    *>i  10.22.22.22/24     2.2.2.2         0          100        0      65002i
   ```
   
   CE1 and CE3, and CE1 and CE2 can successfully ping each other whereas CE2 and CE3 cannot successfully ping each other.
   
   ```
   <CE1> ping -a 10.11.11.11 10.33.33.33
     PING 10.33.33.33: 56  data bytes, press CTRL_C to break
       Reply from 10.33.33.33: bytes=56 Sequence=1 ttl=252 time=120 ms
       Reply from 10.33.33.33: bytes=56 Sequence=2 ttl=252 time=73 ms
       Reply from 10.33.33.33: bytes=56 Sequence=3 ttl=252 time=111 ms
       Reply from 10.33.33.33: bytes=56 Sequence=4 ttl=252 time=86 ms
       Reply from 10.33.33.33: bytes=56 Sequence=5 ttl=252 time=110 ms
     --- 10.33.33.33 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 73/100/120 ms 
   ```
   ```
   <CE2> ping -a 10.22.22.22 10.33.33.33
     PING 10.33.33.33: 56  data bytes, press CTRL_C to break
       Request time out
       Request time out
       Request time out
       Request time out
       Request time out
   
     --- 10.33.33.33 ping statistics ---
       5 packet(s) transmitted
       0 packet(s) received
       100.00% packet loss 
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
   ip address 10.11.11.11 255.255.255.255
  #
  bgp 65001
   peer 10.1.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 10.11.11.11 255.255.255.255
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
   ip address 172.16.1.2 255.255.255.0
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
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
    peer 5.5.5.5 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.3 enable
    peer 5.5.5.5 enable
  #
   ipv4-family vpn-instance vpna
    peer 10.1.1.1 as-number 65001
  #
  ospf 1
   area 0.0.0.0
    network 172.16.1.0 0.0.0.255
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
   ip address 172.16.3.2 255.255.255.0
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
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 5.5.5.5 as-number 100
   peer 5.5.5.5 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 5.5.5.5 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
    peer 5.5.5.5 enable
  #
   ipv4-family vpn-instance vpna
    peer 10.3.1.1 as-number 65003
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 172.16.3.0 0.0.0.255
  #
  return
  ```
* CE3 configuration file
  
  ```
  #
  sysname CE3
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
  #
  interface Loopback1
   ip address 10.33.33.33 255.255.255.255
  #
  bgp 65003
   peer 10.3.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 10.33.33.33 255.255.255.255
    peer 10.3.1.2 enable
  #
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
   ip address 172.16.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 172.16.3.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 5.5.5.5 255.255.255.255
  #
  route-policy test deny node 10
   if-match rd-filter 10
  #
  route-policy test permit node 20
  #
  ip rd-filter 10 permit 100:3
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   peer 192.168.1.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 192.168.1.2 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
    peer 192.168.1.2 enable
    peer 192.168.1.2 route-policy test export
  #
  ospf 1
   area 0.0.0.0
    network 5.5.5.5 0.0.0.0
    network 172.16.1.0 0.0.0.255
    network 172.16.3.0 0.0.0.255
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
   ip address 10.162.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 6.6.6.6 255.255.255.255
  #
  bgp 200
   peer 2.2.2.2 as-number 200
   peer 2.2.2.2 connect-interface LoopBack1
   peer 192.168.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.2 enable
    peer 5.5.5.5 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 192.168.1.1 enable
  #
  ospf 1
   area 0.0.0.0
    network 6.6.6.6 0.0.0.0
    network 10.162.1.0 0.0.0.255
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
   ip address 10.162.1.2 255.255.255.0
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
    network 10.162.1.0 0.0.0.255
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
   ip address 10.22.22.22 255.255.255.255
  #
  bgp 65002
   peer 10.2.1.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    network 10.22.22.22 255.255.255.255
    peer 10.2.1.2 enable
  #
  return
  ```