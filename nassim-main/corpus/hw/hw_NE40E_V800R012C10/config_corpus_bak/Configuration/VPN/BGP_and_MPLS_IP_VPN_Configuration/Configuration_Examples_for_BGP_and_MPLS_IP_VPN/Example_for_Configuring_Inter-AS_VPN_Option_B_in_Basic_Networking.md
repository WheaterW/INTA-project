Example for Configuring Inter-AS VPN Option B in Basic Networking
=================================================================

This section provides an example for configuring inter-AS VPN Option B in basic networking. A single-hop MP-EBGP peer relationship is established between ASBRs to exchange VPNv4 routes.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369497__fig_dc_vrp_mpls-l3vpn-v4_cfg_011201), CE1 and CE2 belong to the same VPN. CE1 is connected to PE1 in AS 100, and CE2 is connected to PE2 in AS 200. It is required that an MP-EBGP peer relationship be established between the ASBRs to transmit VPNv4 routes, implementing inter-AS VPN Option B.

**Figure 1** Inter-AS VPN Option B in basic networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v4_cfg_011201.png)

#### Precautions

When configuring inter-AS VPN Option B in basic networking, note the following:

* Configure an MP-EBGP peer relationship between ASBR1 and ASBR2, and disable the ASBRs from filtering received VPNv4 routes based on VPN targets.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IGP on the MPLS backbone network for communication between the ASBR and PE in the same AS, and set up an MPLS LDP LSP between them.
2. Establish EBGP peer relationships between the PEs and CEs and MP-IBGP peer relationships between the PEs and ASBRs.
3. Configure VPN instances on the PEs rather than ASBRs.
4. Enable MPLS on the interfaces connecting the ASBRs and establish an MP-EBGP peer relationship between the ASBRs. Configure the ASBRs not to filter received VPNv4 routes based on VPN targets.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the PEs and ASBRs
* Names, RDs, and VPN targets of the VPN instances on PE1 and PE2

#### Procedure

1. Configure IGP for communication between the PE and ASBR on each MPLS backbone network (one is in AS 100 and the other in AS 200).
   
   
   
   In this example, OSPF is used as IGP. For configuration details, see the configuration files.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The PEs and ASBRs need to advertise their LSR IDs (32-bit IP addresses of loopback interfaces) using OSPF.
   
   After completing the configurations, run the **display ospf peer** command on a PE or ASBR. The command output shows that the OSPF neighbor relationship is in the **Full** state, which indicates that the OSPF neighbor relationship has been established between the ASBR and PE in the AS.
   
   The ASBR and PE in the same AS can learn the route to each other's loopback address and ping each other.
2. Configure basic MPLS capabilities and MPLS LDP on each MPLS backbone network in AS 100 and AS 200 to establish LDP LSPs.
   
   
   
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
   [*PE1-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure ASBR1.
   
   ```
   <ASBR1> system-view
   ```
   ```
   [~ASBR1] mpls lsr-id 2.2.2.2
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
   [*ASBR1] interface gigabitethernet0/1/0
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
   
   # Configure ASBR2.
   
   ```
   <ASBR2> system-view
   ```
   ```
   [~ASBR2] mpls lsr-id 3.3.3.3
   ```
   ```
   [*ASBR2] mpls
   ```
   ```
   [*ASBR2-mpls] quit
   ```
   ```
   [*ASBR2] mpls ldp
   ```
   ```
   [*ASBR2-mpls-ldp] quit
   ```
   ```
   [*ASBR2] interface gigabitethernet0/1/0
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*ASBR2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~ASBR2-GigabitEthernet0/1/0] quit
   ```
   
   # Configure PE2.
   
   ```
   <PE2> system-view
   ```
   ```
   [~PE2] mpls lsr-id 4.4.4.4
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
   [*PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] commit
   ```
   ```
   [~PE2-GigabitEthernet0/1/0] quit
   ```
   
   After completing the configurations, run the **display mpls ldp session** command on a PE or an ASBR. The command output shows that the session status is **Operational**, indicating that an LDP peer relationship has been established between the PE and ASBR in the same AS. The following example uses the command output on PE1.
   
   ```
   <PE1> display mpls ldp session
   ```
   ```
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
    -------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
   --------------------------------------------------------------------------
    2.2.2.2:0          Operational DU   Passive  0000:02:30   604/604
   --------------------------------------------------------------------------
   TOTAL: 1 Session(s) Found.
   ```
3. Configure basic BGP/MPLS IP VPN functions on PE1 and PE2.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   PE1's import and export VPN targets must match PE2's export and import VPN targets, respectively.
   
   # On CE1, establish an EBGP peer relationship with PE1.
   
   ```
   [~CE1] bgp 65001
   ```
   ```
   [*CE1-bgp] peer 10.1.1.2 as-number 100
   ```
   ```
   [*CE1-bgp] network 5.5.5.5 255.255.255.255
   ```
   ```
   [*CE1-bgp] ipv4-family unicast
   ```
   ```
   [*CE1-bgp-af-ipv4] peer 10.1.1.2 enable
   ```
   ```
   [*CE1-bgp-af-ipv4] quit
   ```
   ```
   [*CE1-bgp] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # On PE1, establish an EBGP peer relationship with CE1.
   
   ```
   [~PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] interface gigabitethernet 0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] ip address 10.1.1.2 24
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] bgp 100
   ```
   ```
   [*PE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp-vpn1] peer 10.1.1.1 as-number 65001
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
   
   # Configure PE1 to establish an IBGP peer relationship with ASBR1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.2 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*PE1-bgp-af-vpnv4] peer 2.2.2.2 enable
   ```
   ```
   [*PE1-bgp-af-vpnv4] commit
   ```
   ```
   [~PE1-bgp-af-vpnv4] quit
   ```
   
   # Configure ASBR1 to establish an IBGP peer relationship with PE1.
   
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
   [*ASBR1-bgp] ipv4-family vpnv4
   ```
   ```
   [*ASBR1-bgp-af-vpnv4] peer 1.1.1.1 enable
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
   
   The configurations of CE2, PE2, and ASBR2 are similar to the configurations of CE1, PE1, and ASBR1, respectively. For configuration details, see the configuration files.
   
   After completing the configurations, run the **display bgp vpnv4 vpn-instance** *vpn-instance-name* **peer** command on either PE. The command output shows the **Established** state, which indicates that the BGP peer relationship has been established between the PE and CE. Run the **display bgp vpnv4 all peer** command on either PE. The command output shows the **Established** state, which indicates that BGP peer relationships have been established between the PE and CE and between the PE and ASBR.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display bgp vpnv4 vpn-instance vpn1 peer
   ```
   ```
    BGP local router ID : 10.16.1.2
    Local AS number : 100
   
    VPN-Instance vpn1, Router ID 10.16.1.2:
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down        State  PrefRcv
     10.1.1.1        4       65001       79       80     0 01:05:48 Established        1
   ```
   ```
   <PE1> display bgp vpnv4 all peer
   ```
   ```
    BGP local router ID : 10.16.1.2
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2.2.2.2         4         100      180      180     0 02:33:25 Established       1
   
     Peer of IPv4-family for vpn instance :
   
     VPN-Instance vpn1, Router ID 10.16.1.2:
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down        State  PrefRcv
     10.1.1.1        4       65001       80       80     0 01:06:34 Established        1
   ```
4. Configure the inter-AS VPN Option B mode.
   
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
   
   # Configure ASBR1 to establish an MP-EBGP peer with ASBR2, and disable ASBR1 from filtering received VPNv4 routes based on VPN targets.
   
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
   
   The configuration of ASBR2 is similar to that of ASBR1. For configuration details, see the configuration file.
5. Verify the configuration.
   
   
   
   After the configurations are complete, the CEs can learn routes to the loopback interface of each other, and can ping each other.
   
   The following example uses the command output on CE1.
   
   ```
   <CE1> display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ```
   ```
   ------------------------------------------------------------------------------
   ```
   ```
   Routing Table: _public_
   ```
   ```
            Destinations : 9        Routes : 9
   ```
   ```
   Destination/Mask    Proto  Pre  Cost      Flags  NextHop         Interface
   ```
   ```
           5.5.5.5/32  Direct 0    0             D  127.0.0.1       LoopBack1
   ```
   ```
          6.6.6.6/32  EBGP   255  0             D  10.1.1.2        GigabitEthernet0/1/0
   ```
   ```
          10.1.1.0/24  Direct 0    0             D  10.1.1.1        GigabitEthernet0/1/0
   ```
   ```
          10.1.1.1/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
   ```
   ```
        10.1.1.255/32  Direct 0    0             D  127.0.0.1       GigabitEthernet0/1/0
   ```
   ```
         127.0.0.0/8   Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
         127.0.0.1/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
   127.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
   255.255.255.255/32  Direct 0    0             D  127.0.0.1       InLoopBack0
   ```
   ```
   <CE1> ping -a 5.5.5.5 6.6.6.6
   ```
   ```
     PING 6.6.6.6: 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 6.6.6.6: bytes=56 Sequence=1 ttl=252 time=120 ms
   ```
   ```
       Reply from 6.6.6.6: bytes=56 Sequence=2 ttl=252 time=73 ms
   ```
   ```
       Reply from 6.6.6.6: bytes=56 Sequence=3 ttl=252 time=111 ms
   ```
   ```
       Reply from 6.6.6.6: bytes=56 Sequence=4 ttl=252 time=86 ms
   ```
   ```
       Reply from 6.6.6.6: bytes=56 Sequence=5 ttl=252 time=110 ms
   ```
   ```
     --- 6.6.6.6 ping statistics ---
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
       round-trip min/avg/max = 73/100/120 ms 
   ```
   
   Run the **display bgp vpnv4 all routing-table** command on either ASBR to view information about VPNv4 routes.
   
   The following example uses the command output on ASBR1.
   
   ```
   <ASBR1> display bgp vpnv4 all routing-table
   ```
   ```
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total number of routes from all PE: 2
    Route Distinguisher: 100:1
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>i  5.5.5.5/32         1.1.1.1         0          100        0      65001i
    Route Distinguisher: 200:1
   
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   6.6.6.6/32         192.168.1.2                             0    200 65002i
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
  interface Loopback 1
   ip address 5.5.5.5 255.255.255.255
  #
  bgp 65001
   peer 10.1.1.2 as-number 100
   network 5.5.5.5 255.255.255.255
   #
   ipv4-family unicast
    undo synchronization
    peer 10.1.1.2 enable
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.16.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.1.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
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
   ipv4-family vpn-instance vpn1
    peer 10.1.1.1 as-number 65001
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.16.1.0 0.0.0.255
  #
  return
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.16.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 192.168.1.2 as-number 200
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.1.2 enable
    peer 1.1.1.1 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 192.168.1.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.16.1.0 0.0.0.255
  #
  return
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.17.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 200
   peer 192.168.1.1 as-number 100
   peer 4.4.4.4 as-number 200
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 192.168.1.1 enable
    peer 4.4.4.4 enable
   #
   ipv4-family vpnv4
    undo policy vpn-target
    peer 4.4.4.4 enable
    peer 192.168.1.1 enable
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.17.1.0 0.0.0.255
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
    route-distinguisher 200:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.17.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 10.2.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 200
   peer 3.3.3.3 as-number 200
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   ipv4-family vpnv4
    policy vpn-target
    peer 3.3.3.3 enable
  #
   ipv4-family vpn-instance vpn1
    peer 10.2.1.1 as-number 65002
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.17.1.0 0.0.0.255
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
  interface Loopback 1
   ip address 6.6.6.6 255.255.255.255
  #
  bgp 65002
   peer 10.2.1.2 as-number 200
   network 6.6.6.6 255.255.255.255
   #
   ipv4-family unicast
    undo synchronization
    peer 10.2.1.2 enable
  #
  return
  ```