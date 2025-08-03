Example for Configuring Inter-AS IPv6 VPN Option C (Solution 1)
===============================================================

After establishing a multi-hop MP-EBGP peer relationship between PEs of different ASs, you can implement the inter-AS IPv6 VPN Option C solution.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369720__fig_dc_vrp_mpls-l3vpn-v6_cfg_209701), CE1 and CE2 belong to the same VPN; CE1 accesses the network through PE1 in AS100; CE2 accesses the network through PE2 in AS200.

It is required that inter-AS BGP/MPLS IPv6 VPN be implemented in Option C mode.

**Figure 1** Inter-AS IPv6 VPN Option C (solution 1)![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v6_cfg_209701.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Set up an MP-EBGP peer relationship between PEs in different ASs and configure the maximum number of hops between PEs.
2. Configure a routing policy on ASBRs, so that each ASBR assigns MPLS labels to the loopback routes received from the PE in the local AS before advertising the routes to the remote ASBR and assigns new MPLS labels to the routes advertised to the PE in the local AS if they are labeled IPv4 routes.
3. Configure the PE and ASBR in the same AS to exchange labeled IPv4 routes.
4. Configure the ASBRs to exchange labeled IPv4 routes.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of PE1 (1.1.1.9), ASBR1 (2.2.2.9), ASBR2 (3.3.3.9), and PE2 (4.4.4.9)
* Name (vpn1), RD (100:1), and export and import VPN targets (1:1) of the VPN instance on each PE
* Route-policies (policy1 and policy2) configured on the ASBR

#### Procedure

1. Configure an IGP on the MPLS backbone network in AS100 and AS200, so that the PE and ASBR in the same AS can communicate.
   
   
   
   This example uses OSPF as the IGP.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The 32-bit loopback interface address used as the LSR ID should be advertised by OSPF.
   
   After the configurations are complete, the OSPF neighbor relationship can be established between the ASBR and PE in the same AS. Run the **display ospf peer** command. The command output shows that the status of the OSPF neighbor relationship is **Full**.
   
   The following example uses the command output on PE1.
   
   ```
   <PE1> display ospf peer
   (M) Indicates MADJ neighbor
   
   
             OSPF Process 1 with Router ID 1.1.1.9
                   Neighbors
   
    Area 0.0.0.0 interface 10.10.1.2 (GE0/1/0)'s neighbors
    Router ID: 10.10.1.1            Address: 10.10.1.1        
      State: Full           Mode:Nbr is Master     Priority: 1
      DR: 10.10.1.2         BDR: 10.10.1.1         MTU: 0
      Dead timer due in  34  sec
      Retrans timer interval: 5
      Neighbor is up for 00h09m56s
      Neighbor Up Time : 2020-03-03 11:55:21
      Authentication Sequence: [ 0 ]
   ```
   
   The ASBR and PE in the same AS can learn the routes to each other's Loopback1 interface and ping each other.
2. Configure MPLS and MPLS LDP both globally and per interface on each node of the MPLS backbone networks in AS100 and AS200 and set up LDP LSPs.
   
   
   
   For configuration details, see the configuration files.
3. Set up IBGP peer relationships between the PEs and ASBRs in each AS.
   
   
   
   For configuration details, see the configuration files.
4. Configure the VPN instance on the PE and configure the CE to access the PE.
   
   
   
   For configuration details, see the configuration files.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The import VPN target configured on PE1 must be the same as the export VPN target configured on PE2; the export VPN target configured on PE1 must be the same as the import VPN target configured on PE2.
5. Configure the function to exchange labeled IPv4 routes.
   
   
   
   # Configure PE1 to exchange labeled IPv4 routes with ASBR1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 2.2.2.9 label-route-capability
   ```
   ```
   [*PE1-bgp] commit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Enable MPLS on GE 0/2/0 that connects ASBR1 to ASBR2.
   
   ```
   [~ASBR1] interface gigabitethernet0/2/0
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] ip address 10.21.1.1 24
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*ASBR1-GigabitEthernet0/2/0] commit
   ```
   ```
   [~ASBR1-GigabitEthernet0/2/0] quit
   ```
   
   # Configure routing policies on ASBR1.
   
   ```
   [~ASBR1] route-policy policy1 permit node 1
   ```
   ```
   [*ASBR1-route-policy] apply mpls-label
   ```
   ```
   [*ASBR1-route-policy] quit
   ```
   ```
   [*ASBR1] route-policy policy2 permit node 1
   ```
   ```
   [*ASBR1-route-policy] if-match mpls-label
   ```
   ```
   [*ASBR1-route-policy] apply mpls-label
   ```
   ```
   [*ASBR1-route-policy] commit
   ```
   ```
   [~ASBR1-route-policy] quit
   ```
   
   # Apply the routing policies to the routes advertised to PE1 and enable ASBR1 to exchange label IPv4 routes with PE1.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.9 route-policy policy2 export
   ```
   ```
   [*ASBR1-bgp] peer 1.1.1.9 label-route-capability
   ```
   ```
   [*ASBR1-bgp] commit
   ```
   
   # Apply the routing policies to the routes advertised to ASBR2 and enable ASBR1 to exchange label IPv4 routes with ASBR2.
   
   ```
   [~ASBR1-bgp] peer 10.21.1.2 as-number 200
   ```
   ```
   [*ASBR1-bgp] peer 10.21.1.2 route-policy policy1 export
   ```
   ```
   [*ASBR1-bgp] peer 10.21.1.2 label-route-capability
   ```
   ```
   [*ASBR1-bgp] commit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
   
   # Configure ASBR1 to advertise the loopback routes of PE1 to ASBR2, and then to PE2.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [~ASBR1-bgp] network 1.1.1.9 32
   ```
   ```
   [*ASBR1-bgp] commit
   ```
   ```
   [~ASBR1-bgp] quit
   ```
   
   The configurations of PE2 and ASBR2 are similar to the configurations of PE1 and ASBR1, respectively. For configuration details, see the configuration files.
6. Establish an MP-EBGP peer relationship between PE1 and PE2.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 4.4.4.9 as-number 200
   ```
   ```
   [*PE1-bgp] peer 4.4.4.9 connect-interface LoopBack 1
   ```
   ```
   [*PE1-bgp] peer 4.4.4.9 ebgp-max-hop 10
   ```
   ```
   [*PE1-bgp] ipv6-family vpnv6
   ```
   ```
   [*PE1-bgp-af-vpnv6] peer 4.4.4.9 enable
   ```
   ```
   [*PE1-bgp-af-vpnv6] quit
   ```
   ```
   [*PE1-bgp] commit
   ```
   ```
   [~PE1-bgp] quit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 200
   ```
   ```
   [*PE2-bgp] peer 1.1.1.9 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.9 connect-interface LoopBack 1
   ```
   ```
   [*PE2-bgp] peer 1.1.1.9 ebgp-max-hop 10
   ```
   ```
   [*PE2-bgp] ipv6-family vpnv6
   ```
   ```
   [*PE2-bgp-af-vpnv6] peer 1.1.1.9 enable
   ```
   ```
   [*PE2-bgp-af-vpnv6] quit
   ```
   ```
   [*PE2-bgp] commit
   ```
   ```
   [~PE2-bgp] quit
   ```
7. Verify the configuration.
   
   
   
   After the configurations are complete, the CEs can learn routes to each other's interface and can ping through each other.
   
   The following example uses the command output on CE1.
   
   ```
   [~CE1] display ipv6 routing-table
   ```
   ```
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
   ```
   ```
     PING 2001:db8:2::1 : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8:2::1
       bytes=56 Sequence=1 hop limit=60 time=6 ms
       Reply from 2001:db8:2::1
       bytes=56 Sequence=2 hop limit=60 time=3 ms
       Reply from 2001:db8:2::1
       bytes=56 Sequence=3 hop limit=60 time=3 ms
       Reply from 2001:db8:2::1
       bytes=56 Sequence=4 hop limit=60 time=2 ms
       Reply from 2001:db8:2::1
       bytes=56 Sequence=5 hop limit=60 time=2 ms
   
     ---2001:db8:2::1 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=2/3/6 ms
   ```
   
   ASBRs do not have VPNv6 routes. Run the **display bgp routing-table label** command on an ASBR. The command output shows the label information of the routes.
   
   The following example uses the command output on ASBR1.
   
   ```
   [~ASBR1] display bgp routing-table label
   ```
   ```
    BGP Local router ID is 10.10.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 2
           Network                       NextHop                       In/Out Label
   
    *>     1.1.1.9                       0.0.0.0                       48062/NULL             
    *>     4.4.4.9                       10.21.1.2                     48063/48060
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
    import-route direct
    peer 2001:db8:1::2 enable
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
   ip address 10.10.1.2 255.255.255.0
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
   peer 2.2.2.9 as-number 100
   peer 2.2.2.9 connect-interface LoopBack1
   peer 4.4.4.9 as-number 200
   peer 4.4.4.9 ebgp-max-hop 10
   peer 4.4.4.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 2.2.2.9 enable
    peer 2.2.2.9 label-route-capability
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
    network 10.10.1.0 0.0.0.255
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
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  bgp 100
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 connect-interface LoopBack1
   peer 10.21.1.2 as-number 200
   #
   ipv4-family unicast
    undo synchronization
    network 1.1.1.9 255.255.255.255
    peer 1.1.1.9 enable
    peer 1.1.1.9 route-policy policy2 export
    peer 1.1.1.9 label-route-capability
    peer 10.21.1.2 enable
    peer 10.21.1.2 route-policy policy1 export
    peer 10.21.1.2 label-route-capability
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 10.10.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  route-policy policy2 permit node 1
   if-match mpls-label
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
   ip address 3.3.3.9 255.255.255.255
  #
  bgp 200
   peer 4.4.4.9 as-number 200
   peer 4.4.4.9 connect-interface LoopBack1
   peer 10.21.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization
    network 4.4.4.9 255.255.255.255
    peer 4.4.4.9 enable
    peer 4.4.4.9 route-policy policy2 export
    peer 4.4.4.9 label-route-capability
    peer 10.21.1.1 enable
    peer 10.21.1.1 route-policy policy1 export
    peer 10.21.1.1 label-route-capability
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 10.40.1.0 0.0.0.255
  #
  route-policy policy1 permit node 1
   apply mpls-label
  #
  route-policy policy2 permit node 1
   if-match mpls-label
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
    route-distinguisher 200:1
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
   ip address 10.40.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
  #
  interface LoopBack1
   ip address 4.4.4.9 255.255.255.255
  #
  bgp 200
   peer 1.1.1.9 as-number 100
   peer 1.1.1.9 ebgp-max-hop 10
   peer 1.1.1.9 connect-interface LoopBack1
   peer 3.3.3.9 as-number 200
   peer 3.3.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.9 enable
    peer 3.3.3.9 enable
    peer 3.3.3.9 label-route-capability
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
    network 10.40.1.0 0.0.0.255
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