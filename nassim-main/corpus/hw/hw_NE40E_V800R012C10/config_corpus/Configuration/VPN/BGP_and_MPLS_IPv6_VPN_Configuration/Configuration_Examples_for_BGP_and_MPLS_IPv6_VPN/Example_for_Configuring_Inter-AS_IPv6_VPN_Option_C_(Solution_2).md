Example for Configuring Inter-AS IPv6 VPN Option C (Solution 2)
===============================================================

If no MP-IBGP peer relationship is established between PEs and ASBRs, you can use LDP to allocate labels for BGP and implement the inter-AS IPv6 VPN Option C solution.

#### Networking Requirements

As shown in [Figure 1](#EN-US_TASK_0172369724__fig_dc_vrp_mpls-l3vpn-v6_cfg_209801), CE1 and CE2 belong to the same VPN. CE1 accesses AS100 through PE1, and CE2 accesses AS200 through PE2.

**Figure 1** Inter-AS IPv6 VPN Option C (solution 2)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v6_cfg_209801.png)

No IBGP peer relationship is needed between a PE and an ASBR. The ASBR learns the labeled BGP routes of the public network in the remote AS from the peer ASBR. These BGP routes are then imported to the IGP. In this manner, LDP can distribute labels for these routes and establish an inter-AS LDP LSP. The inter-AS BGP/MPLS IPv6 VPN can then be implemented in Option C mode.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Advertise the routes of the PEs within an AS to the remote ASBR through BGP, import these routes to the IGP on the remote ASBR, and then advertise these routes to the remote PE through the IGP.
2. Configure a routing policy on each ASBR, so that each ASBR assigns an MPLS label to the loopback interface route that is received from the PE in the same AS and is to be advertised to the remote ASBR and assigns new MPLS labels to the labeled IPv4 routes to be advertised to the PE in the same AS.
3. Exchange the labeled IPv4 routes between the local and remote ASBRs.
4. Configure LDP LSPs for the labeled BGP routes of the public network on ASBRs.
5. Establish an MP-EBGP peer relationship between the PEs of different ASs and specify the maximum hops allowed for an MP-EBGP connection between PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of PE1 (1.1.1.9), ASBR1 (2.2.2.9), ASBR2 (3.3.3.9), and PE2 (4.4.4.9)
* Name (vpn1), RD (100:1), and export and import VPN targets (1:1) of the VPN instance on each PE
* Route-policies (policy1 and policy2) configured on the ASBR

#### Procedure

1. Configure an IGP on the MPLS backbone networks in AS100 and AS200 so that PEs on each MPLS backbone network can communicate with ASBRs.
   
   
   
   This example uses OSPF as the IGP. For configuration details, see [Configuration Files](#EN-US_TASK_0172369724__example1695196732214051) in this section.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Advertise the 32-bit IP address of a loopback interface, that is, the LSR ID, using OSPF.
   
   After the configurations are complete, the OSPF neighbor relationship can be established between the ASBR and PE in the same AS. Run the **display ospf peer** command. The command output shows that the status of the OSPF neighbor relationship is **Full**.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display ospf peer
   ```
   ```
   (M) Indicates MADJ neighbor
   
   
             OSPF Process 1 with Router ID 1.1.1.9
                   Neighbors
   
    Area 0.0.0.0 interface 172.16.1.2 (GE0/1/0)'s neighbors
    Router ID: 2.2.2.9            Address: 172.16.1.1       
      State: Full           Mode:Nbr is Master     Priority: 1
      DR: 2.2.2.9        BDR: 1.1.1.9        MTU: 0
      Dead timer due in  31  sec
      Retrans timer interval: 5
      Neighbor is up for 00h21m46s
      Neighbor Up Time : 2020-03-04 06:56:08
      Authentication Sequence: [ 0 ]
   ```
   
   The ASBR and PE in the same AS can learn the IP address of each other's Loopback 1 interface and ping each other.
2. Establish an EBGP peer relationship between the ASBRs.
   
   
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] bgp 100
   [*ASBR1-bgp] peer 192.168.1.2 as-number 200
   [*ASBR1-bgp] commit
   [~ASBR1-bgp] quit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] bgp 200
   [*ASBR2-bgp] peer 192.168.1.1 as-number 100
   [*ASBR2-bgp] commit
   [~ASBR2-bgp] quit
   ```
   
   After completing the configurations, run the **display bgp peer** command on each ASBR. The command output shows that the status of the EBGP peer relationship is **Established**.
   
   The following example uses the command output on ASBR1.
   
   ```
   [~ASBR1] display bgp peer
   ```
   ```
    BGP local router ID : 172.16.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer        V  AS    MsgRcvd  MsgSent  OutQ  Up/Down       State       PrefRcv
   
     192.168.1.2 4 200        129      134     0 01:39:21 Established             1
   
   ```
3. Advertise the routes of the PE in an AS to the PE in another AS.
   
   
   
   # On ASBR1, advertise the loopback address of PE1 to ASBR2.
   
   ```
   [~ASBR1] bgp 100
   [~ASBR1-bgp] network 1.1.1.9 32
   [*ASBR1-bgp] commit
   [~ASBR1-bgp] quit
   ```
   
   # On ASBR2, advertise the loopback address of PE2 to ASBR1.
   
   ```
   [~ASBR2] bgp 200
   [~ASBR2-bgp] network 4.4.4.9 32
   [*ASBR2-bgp] commit
   [~ASBR2-bgp] quit
   ```
   
   # On ASBR1, import BGP routes to OSPF, and advertise the routes of PE2 to PE1 through OSPF.
   
   ```
   [~ASBR1] ospf 1
   [~ASBR1-ospf-1] import-route bgp
   [*ASBR1-ospf-1] commit
   [~ASBR1-ospf-1] quit
   ```
   
   # On ASBR2, import BGP routes to OSPF, and advertise the routes of PE1 to PE2 through OSPF.
   
   ```
   [~ASBR2] ospf 1
   [~ASBR2-ospf-1] import-route bgp
   [*ASBR2-ospf-1] commit
   [~ASBR2-ospf-1] quit
   ```
   
   After completing the configurations, run the **display ip routing-table** command on each PE. The command output shows routing table information. The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip routing-table
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
            Destinations : 10       Routes : 10
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
           1.1.1.9/32  Direct  0    0             D  127.0.0.1       LoopBack1
           2.2.2.9/32  OSPF    10   1             D  172.16.1.1      GigabitEthernet0/1/0
           4.4.4.9/32  O_ASE   150  1             D  172.16.1.1      GigabitEthernet0/1/0
         127.0.0.0/8   Direct  0    0             D  127.0.0.1       InLoopBack0
         127.0.0.1/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   127.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
        172.16.1.0/24  Direct  0    0             D  172.16.1.2      GigabitEthernet0/1/0
        172.16.1.2/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
      172.16.1.255/32  Direct  0    0             D  127.0.0.1       GigabitEthernet0/1/0
   255.255.255.255/32  Direct  0    0             D  127.0.0.1       InLoopBack0
   ```
4. Configure MPLS and MPLS LDP both globally and per interface on each node of the backbone networks in AS100 and AS200 to establish LDP LSPs.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] mpls lsr-id 1.1.1.9
   [*PE1] mpls
   [*PE1-mpls] quit
   [*PE1] mpls ldp
   [*PE1-mpls-ldp] quit
   [*PE1] interface gigabitethernet0/1/0
   [*PE1-GigabitEthernet0/1/0] mpls
   [*PE1-GigabitEthernet0/1/0] mpls ldp
   [*PE1-GigabitEthernet0/1/0] commit
   [~PE1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls lsr-id 2.2.2.9
   [*ASBR1] mpls
   [*ASBR1-mpls] quit
   [*ASBR1] mpls ldp
   [*ASBR1-mpls-ldp] quit
   [*ASBR1] interface gigabitethernet0/1/0
   [*ASBR1-GigabitEthernet0/1/0] mpls
   [*ASBR1-GigabitEthernet0/1/0] mpls ldp
   [*ASBR1-GigabitEthernet0/1/0] commit
   [~ASBR1-GigabitEthernet0/1/0] quit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] mpls lsr-id 3.3.3.9
   [*ASBR2] mpls
   [*ASBR2-mpls] quit
   [*ASBR2] mpls ldp
   [*ASBR2-mpls-ldp] quit
   [*ASBR2] interface gigabitethernet 0/1/0
   [*ASBR2-GigabitEthernet0/1/0] mpls
   [*ASBR2-GigabitEthernet0/1/0] mpls ldp
   [*ASBR2-GigabitEthernet0/1/0] commit
   [~ASBR2-GigabitEthernet0/1/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] mpls lsr-id 4.4.4.9
   [*PE2] mpls
   [*PE2-mpls] quit
   [*PE2] mpls ldp
   [*PE2-mpls-ldp] quit
   [*PE2] interface gigabitethernet0/1/0
   [*PE2-GigabitEthernet0/1/0] mpls
   [*PE2-GigabitEthernet0/1/0] mpls ldp
   [*PE2-GigabitEthernet0/1/0] commit
   [~PE2-GigabitEthernet0/1/0] quit
   ```
   
   After the configurations are complete, the LDP sessions between PE1 and the ASBR1, and between PE2 and ASBR2 are set up. Run the **display mpls ldp session** command. The command output shows that the LDP session status is **Operational**. Run the **display mpls ldp lsp** command. The command output shows whether LDP LSPs are set up.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls ldp session
   
    LDP Session(s) in Public Network
    Codes: LAM(Label Advertisement Mode), SsnAge Unit(DDDD:HH:MM)
    An asterisk (*) before a session means the session is being deleted.
   
   --------------------------------------------------------------------------
    PeerID             Status      LAM  SsnRole  SsnAge       KASent/Rcv
   --------------------------------------------------------------------------
    2.2.2.9:0          Operational DU   Passive  0000:00:10   43/43
   --------------------------------------------------------------------------
   TOTAL: 1 Session(s) Found.
   ```
   ```
   [~PE1] display mpls ldp lsp
   
    LDP LSP Information
    -------------------------------------------------------------------------------
    Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP
    -------------------------------------------------------------------------------
    DestAddress/Mask   In/OutLabel    UpstreamPeer    NextHop          OutInterface
    -------------------------------------------------------------------------------
    1.1.1.9/32          3/NULL         2.2.2.9         127.0.0.1        Loop1
   *1.1.1.9/32          Liberal/32828                  DS/2.2.2.9
    2.2.2.9/32          NULL/3         -               172.16.1.1       GigabitEthernet0/1/0
    2.2.2.9/32          32828/3        2.2.2.9         172.16.1.1       GigabitEthernet0/1/0
    4.4.4.9/32          NULL/32831     -               172.16.1.1       GigabitEthernet0/1/0
    4.4.4.9/32          32831/32831    2.2.2.9         172.16.1.1       GigabitEthernet0/1/0
    -------------------------------------------------------------------------------
    TOTAL: 5 Normal LSP(s) Found.
    TOTAL: 1 Liberal LSP(s) Found.
    TOTAL: 0 FRR LSP(s) Found.
    An asterisk (*) before an LSP means the LSP is not established
    An asterisk (*) before a Label means the USCB or DSCB is stale
    An asterisk (*) before an UpstreamPeer means the session is stale
    An asterisk (*) before a DS means the session is stale
    An asterisk (*) before a NextHop means the LSP is FRR LSP
   ```
5. Configure the function to exchange labeled IPv4 routes on ASBRs.
   
   
   
   # Enable MPLS on GE 0/2/0 that connects ASBR1 to ASBR2.
   
   ```
   [~ASBR1] interface gigabitethernet0/2/0
   [~ASBR1-GigabitEthernet0/2/0] ip address 192.168.1.1 24
   [*ASBR1-GigabitEthernet0/2/0] mpls
   [*ASBR1-GigabitEthernet0/2/0] commit
   [~ASBR1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure a routing policy on ASBR1.
   
   ```
   [~ASBR1] route-policy policy1 permit node 1
   [*ASBR1-route-policy] apply mpls-label
   [*ASBR1-route-policy] commit
   [~ASBR1-route-policy] quit
   ```
   
   # On ASBR1, apply the routing policy to the routes advertised to ASBR2 and enable the capability of exchanging labeled IPv4 routes with ASBR2.
   
   ```
   [~ASBR1] bgp 100
   [~ASBR1-bgp] peer 192.168.1.2 route-policy policy1 export
   [*ASBR1-bgp] peer 192.168.1.2 label-route-capability
   [*ASBR1-bgp] commit
   [~ASBR1-bgp] quit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configuration of ASBR2 is similar to the configuration of ASBR1. For configuration details, see [Configuration Files](#EN-US_TASK_0172369724__example1695196732214051) in this section.
6. Configure LDP LSPs for the labeled BGP routes of the public network on ASBRs.
   
   
   
   # Configure ASBR1.
   
   ```
   [~ASBR1] mpls
   [~ASBR1-mpls] lsp-trigger bgp-label-route
   [*ASBR1-mpls] commit
   [~ASBR1-mpls] quit
   ```
   
   # Configure ASBR2.
   
   ```
   [~ASBR2] mpls
   [~ASBR2-mpls] lsp-trigger bgp-label-route
   [*ASBR2-mpls] commit
   [~ASBR2-mpls] quit
   ```
7. Configure a VPN instance on each PE and bind the interface that connects a PE to a CE to the VPN instance on that PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpn1
   [*PE1-vpn-instance-vpn1] ipv6-family
   [*PE1-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
   [*PE1-vpn-instance-vpn1-af-ipv6] vpn-target 1:1 export-extcommunity
   [*PE1-vpn-instance-vpn1-af-ipv6] vpn-target 1:1 import-extcommunity
   [*PE1-vpn-instance-vpn1-af-ipv6] quit
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/2/0
   [*PE1-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   [*PE1-GigabitEthernet0/2/0] ipv6 enable
   [*PE1-GigabitEthernet0/2/0] ipv6 address 2001:db8:1::2 64
   [*PE1-GigabitEthernet0/2/0] commit
   [~PE1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpn1
   [*PE2-vpn-instance-vpn1] ipv6-family
   [*PE2-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
   [*PE2-vpn-instance-vpn1-af-ipv6] vpn-target 1:1 export-extcommunity
   [*PE2-vpn-instance-vpn1-af-ipv6] vpn-target 1:1 import-extcommunity
   [*PE2-vpn-instance-vpn1-af-ipv6] quit
   [*PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   [*PE2-GigabitEthernet0/2/0] ipv6 enable
   [*PE2-GigabitEthernet0/2/0] ipv6 address 2001:db8:2::2 64
   [*PE2-GigabitEthernet0/2/0] commit
   [~PE2-GigabitEthernet0/2/0] quit
   ```
   
   After completing the configurations, run the **display ip vpn-instance verbose** command on PEs to check VPN instance configurations. Each PE can ping its connected CE.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display ip vpn-instance verbose
    Total VPN-Instances configured      : 1
    Total IPv4 VPN-Instances configured : 0
    Total IPv6 VPN-Instances configured : 1
   
    VPN-Instance Name and ID : vpn1, 2
     Interfaces : GigabitEthernet0/2/0
    Address family ipv6
     Create date : 2027-06-04 23:23:53+00:00
     Up time : 0 days, 00 hours, 13 minutes and 38 seconds
     Vrf Status : UP
     Route Distinguisher : 100:1
     Export VPN Targets : 1:1
     Import VPN Targets : 1:1
     Label Policy : label per route
     The diffserv-mode Information is : uniform
     The ttl-mode Information is : pipe
   ```
   ```
   [~PE1] ping ipv6 vpn-instance vpn1 2001:db8:1::1
     PING 2001:db8:1::1 : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8:1::1
       bytes=56 Sequence=1 hop limit=64 time=25 ms
       Reply from 2001:db8:1::1
       bytes=56 Sequence=2 hop limit=64 time=1 ms
       Reply from 2001:db8:1::1
       bytes=56 Sequence=3 hop limit=64 time=2 ms
       Reply from 2001:db8:1::1
       bytes=56 Sequence=4 hop limit=64 time=1 ms
       Reply from 2001:db8:1::1
       bytes=56 Sequence=5 hop limit=64 time=1 ms
   
     ---2001:db8:1::1 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=1/6/25 ms
   ```
8. Establish an MP-EBGP peer relationship between PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [*PE1-bgp] peer 4.4.4.9 as-number 200
   [*PE1-bgp] peer 4.4.4.9 connect-interface LoopBack 1
   [*PE1-bgp] peer 4.4.4.9 ebgp-max-hop 10
   [*PE1-bgp] ipv6-family vpnv6
   [*PE1-bgp-af-vpnv6] peer 4.4.4.9 enable
   [*PE1-bgp-af-vpnv6] quit
   [*PE1-bgp] commit
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   [*PE2-bgp] peer 1.1.1.9 as-number 100
   [*PE2-bgp] peer 1.1.1.9 connect-interface LoopBack 1
   [*PE2-bgp] peer 1.1.1.9 ebgp-max-hop 10
   [*PE2-bgp] ipv6-family vpnv6
   [*PE2-bgp-af-vpnv6] peer 1.1.1.9 enable
   [*PE2-bgp-af-vpnv6] quit
   [*PE2-bgp] commit
   [~PE2-bgp] quit
   ```
9. Set up EBGP peer relationships between PEs and CEs to import VPN routes.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] bgp 65001
   [*CE1-bgp] ipv6-family unicast
   [*CE1-bgp-af-ipv6] peer 2001:db8:1::2 as-number 100
   [*CE1-bgp-af-ipv6] import-route direct
   [*CE1-bgp-af-ipv6] quit
   [*CE1-bgp] commit
   [~CE1-bgp] quit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] bgp 65002
   [*CE2-bgp] ipv6-family unicast
   [*CE2-bgp-af-ipv6] peer 2001:db8:2::2 as-number 200
   [*CE2-bgp-af-ipv6] import-route direct
   [*CE2-bgp-af-ipv6] quit
   [*CE2-bgp] commit
   [~CE2-bgp] quit
   ```
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   [*PE1-bgp] ipv6-family vpn-instance vpn1
   [*PE1-bgp-6-vpn1] peer 2001:db8:1::1 as-number 65001
   [*PE1-bgp-6-vpn1] import-route direct
   [*PE1-bgp-6-vpn1] quit
   [*PE1-bgp] commit
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   [*PE2-bgp] ipv6-family vpn-instance vpn1
   [*PE2-bgp-6-vpn1] peer 2001:db8:2::1 as-number 65002
   [*PE2-bgp-6-vpn1] import-route direct
   [*PE2-bgp-6-vpn1] quit
   [*PE2-bgp] commit
   [~PE2-bgp] quit
   ```
   
   After completing the configurations, run the **display bgp vpnv6 vpn-instance peer** command on each PE to view the BGP peer relationship between the PE and CE. The command output shows that the BGP peer relationship is in the **Established** state.
   
   The following example uses the peer relationship between PE1 and CE1.
   
   ```
   [~PE1] display bgp vpnv6 vpn-instance vpn1 peer
   
    BGP local router ID : 172.16.1.2
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:db8:1::1   4       65001       16       28     0 00:11:49 Established        0
   ```
10. Verify the configuration.
    
    
    
    After the configurations are complete, CEs can learn the routes to each other' interface and ping each other.
    
    The following example uses the command output on CE1.
    
    ```
    [~CE1] display ipv6 routing-table
    Routing Table : _public_
             Destinations : 7        Routes : 7
    
    Destination  : ::1                                     PrefixLength : 128
    NextHop      : ::1                                     Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : InLoopBack0                             Flags        : D
    
    Destination  : ::FFFF:127.0.0.0                        PrefixLength : 104
    NextHop      : ::FFFF:127.0.0.1                        Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : InLoopBack0                             Flags        : D
    
    Destination  : ::FFFF:127.0.0.1                        PrefixLength : 128
    NextHop      : ::1                                     Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : InLoopBack0                             Flags        : D
    
    Destination  : 2001:db8:1::                            PrefixLength : 64
    NextHop      : 2001:db8:1::1                           Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : GigabitEthernet0/1/0                    Flags        : D
    
    Destination  : 2001:db8:1::1                           PrefixLength : 128
    NextHop      : ::1                                     Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : GigabitEthernet0/1/0                    Flags        : D
    
    Destination  : 2001:db8:2::                            PrefixLength : 64
    NextHop      : 2001:db8:1::2                           Preference   : 255
    Cost         : 0                                       Protocol     : EBGP
    RelayNextHop : 2001:db8:1::2                           TunnelID     : 0x0
    Interface    : GigabitEthernet0/1/0                    Flags        : RD
    
    Destination  : FE80::                                  PrefixLength : 10
    NextHop      : ::                                      Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : NULL0                                   Flags        : D
    ```
    ```
    [~CE1] ping ipv6 2001:db8:2::1
      PING 2001:DB8:2::1 : 56  data bytes, press CTRL_C to break
        Reply from 2001:DB8:2::1
        bytes=56 Sequence=1 hop limit=60 time=318 ms
        Reply from 2001:DB8:2::1
        bytes=56 Sequence=2 hop limit=60 time=22 ms
        Reply from 2001:DB8:2::1
        bytes=56 Sequence=3 hop limit=60 time=21 ms
        Reply from 2001:DB8:2::1
        bytes=56 Sequence=4 hop limit=60 time=14 ms
        Reply from 2001:DB8:2::1
        bytes=56 Sequence=5 hop limit=60 time=22 ms
    
      --- 2001:DB8:2::1 ping statistics---
        5 packet(s) transmitted
        5 packet(s) received
        0.00% packet loss
        round-trip min/avg/max=14/79/318 ms
    ```
    
    After completing the configurations, run the **display ip routing-table** *dest-ip-address* **verbose** command on ASBR1. The command output shows that the routes from ASBR1 to PE2 are labeled BGP routes of the public network. The routing table is **Public**, the protocol type is **BGP**, and the label has a non-zero value.
    
    The following example uses the command output on ASBR1.
    
    ```
    [~ASBR1] display ip routing-table 4.4.4.9 verbose
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ------------------------------------------------------------------------------
    Routing Table : _public_
    Summary Count : 1
    
    Destination: 4.4.4.9/32
         Protocol: EBGP            Process ID: 0
       Preference: 255                   Cost: 1
          NextHop: 192.168.1.2        Neighbour: 0.0.0.0
            State: Active Adv Relied      Age: 00h18m41s
              Tag: 0                 Priority: low
            Label: NULL               QoSInfo: 0x0
       IndirectID: 0xA1000071
     RelayNextHop: 0.0.0.0          Interface: MPLS LOCAL IFNET
         TunnelID: 0x000000000c00030000 Flags: RD
    ```
    
    Run the **display mpls lsp protocol ldp include** *dest-ip-address* **verbose** on ASBR1 and PE2 respectively. The command output shows that an LDP LSP is established between ASBR1 and PE2. An ingress LDP LSP on a PE to the remote PE exists.
    
    ```
    [~ASBR1] display mpls lsp protocol ldp include 4.4.4.9 32 verbose
    -------------------------------------------------------------------------------
                     LSP Information: LDP LSP
    -------------------------------------------------------------------------------
      No                  :  1
      VrfIndex            :
      Fec                 :  4.4.4.9/32
      Nexthop             :  0.0.0.0
      In-Label            :  32831
      Out-Label           :  NULL
      In-Interface        :  ----------
      Out-Interface       :  ----------
      LspIndex            :  5000033
      Type                :  Primary
      OutSegmentIndex     :  4294967295
      LsrType             :  Egress
      Outgoing TunnelType :  BGP
      Outgoing TunnelID   :  0x1040020
      Label Operation     :  SWAPPUSH
      Mpls-Mtu            :  ------
      LspAge              :  1185 sec
      Ingress-ELC         :  ------
    ```

#### Configuration Files

* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
  #
  bgp 65001
   router-id 5.5.5.9
   peer 2001:db8:1::2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    peer 2001:db8:1::2 enable
    import-route direct
  #
  return
  ```
* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
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
   ip address 172.16.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #
  bgp 100
   peer 4.4.4.9 as-number 200
   peer 4.4.4.9 ebgp-max-hop 10
   peer 4.4.4.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 4.4.4.9 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 4.4.4.9 enable
   #
   ipv6-family vpn-instance vpn1
    import-route direct
    peer 2001:db8:1::1 as-number 65001
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  return
  ```
* ASBR1 configuration file
  
  ```
  #
  sysname ASBR1
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
   lsp-trigger bgp-label-route
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
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  bgp 100
   peer 192.168.1.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    network 1.1.1.9 255.255.255.255
    peer 192.168.1.2 enable
    peer 192.168.1.2 route-policy policy1 export
    peer 192.168.1.2 label-route-capability
  #
  ospf 1
   import-route bgp
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 172.16.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  return
  ```
* ASBR2 configuration file
  
  ```
  #
  sysname ASBR2
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
   lsp-trigger bgp-label-route
  #
  mpls ldp
   #
   ipv4-family
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
   ip address 3.3.3.9 255.255.255.255
  #
  bgp 200
   peer 192.168.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 4.4.4.9 255.255.255.255
    peer 192.168.1.1 enable
    peer 192.168.1.1 route-policy policy1 export
    peer 192.168.1.1 label-route-capability
  #
  ospf 1
   import-route bgp
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 10.162.1.0 0.0.0.255
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
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 4.4.4.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.162.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
  #
  bgp 200
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 ebgp-max-hop 10
   peer 1.1.1.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 1.1.1.9 enable
   #
   ipv6-family vpn-instance vpn1
    import-route direct
    peer 2001:db8:2::1 as-number 65002
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.9 0.0.0.0
    network 10.162.1.0 0.0.0.255
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
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
  #
  bgp 65002
   router-id 6.6.6.9
   peer 2001:db8:2::2 as-number 200
   #
   ipv6-family unicast
    undo synchronization
    import-route direct
    peer 2001:db8:2::2 enable
  #
  return
  ```