Example for Configuring BGP4+ AS Number Substitution
====================================================

If the AS numbers of different sites in a VPN are the same and EBGP peer relationships are set up between PEs and CEs, AS number substitution needs to be enabled on PEs. Otherwise, CEs will discard the VPN routes that carry the same AS information as their local AS information. As a result, users of the same VPN cannot communicate with each other.

#### Networking Requirements

If different IPv6 VPN sites have the same AS number, and EBGP connections are established between PEs and CEs, you need to enable BGP4+ AS number substitution on the PEs that the VPN sites access.

On the network shown in [Figure 1](#EN-US_TASK_0172369705__fig_dc_vrp_mpls-l3vpn-v6_cfg_204101), the AS numbers of CE1 and CE2 are both 65410; EBGP is used to exchange routes between PE1 and CE1, and between PE2 and CE2.

The AS number 65410 is contained in the AS\_Path attribute of the BGP routes learned by PE1 from CE1. PE2 learns BGP routes from PE1 and checks the AS\_Path attribute of the routes before using EBGP to send them to CE2. Finding that the AS number 65410 in the AS\_Path attribute of the routes is the same as the AS number of CE2, PE2 does not send the routes to CE2. As a result, CE1 and CE2 cannot communicate with each other.

If BGP4+ AS number substitution is configured, PE2 will replace the AS number (65410) in the AS\_Path attribute of VPN routes with its own AS number (100). In this manner, the routes can pass the AS number check provided by BGP and reach CE2, and the two VPN sites can then access each other.

**Figure 1** Configuring BGP4+ AS number substitution![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v6_cfg_204101.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a basic BGP/MPLS IPv6 VPN.
2. Configure EBGP on CEs and PEs to exchange VPN routing information.
3. Configure BGP4+ AS number substitution on PEs.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of PEs and the P
* VPN instances configured on PE1 and PE2
* Same AS number of CE1 and CE2 (which differs from the AS number of the backbone network)

#### Procedure

1. Configure a basic BGP/MPLS IPv6 VPN.
   
   
   
   For configuration details, see [Example for Configuring Basic BGP/MPLS IPv6 VPN](dc_vrp_mpls-l3vpn-v6_cfg_2040.html). The main configurations are listed as follows:
   
   * Configure OSPF on the MPLS backbone network so that the PEs can learn the routes to each other's loopback interface.
   * Configure MPLS and MPLS LDP both globally and per interface on each node of the MPLS backbone network and establish LDP LSPs between PEs.
   * Establish a VPNv6 peer relationship between the PEs.
   * Configure an IPv6-address-family-supporting VPN instance on each PE and bind the interface that connects a PE to a CE to the VPN instance on that PE.
   * Configure BGP on CEs and PEs to exchange routing information.
   
   After completing the configurations, run the **display ipv6 routing-table** command on CE2. The command output shows that CE2 has learned a route to the network segment 2001:db8:1::1/64 where the interface that connects CE1 to PE1 resides, but CE2 does not have a route to 2001:db8:8::1/64, the loopback interface of CE1. CE1 is in a similar situation.
   
   ```
   <CE2> display ipv6 routing-table
   ```
   ```
   Routing Table : _public_
            Destinations : 9        Routes : 9
   
    Destination  : ::1                             PrefixLength : 128
    NextHop      : ::1                             Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : InLoopBack0                     Flags        : D
   
    Destination  : ::FFFF:127.0.0.0                PrefixLength : 104
    NextHop      : ::FFFF:127.0.0.1                Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : InLoopBack0                     Flags        : D
    
    Destination  : ::FFFF:127.0.0.1                PrefixLength : 128
    NextHop      : ::1                             Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : InLoopBack0                     Flags        : D 
   
    Destination  : 2001:db8:9::                    PrefixLength : 64
    NextHop      : 2001:db8:9::1                   Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : LoopBack1                       Flags        : D
   
    Destination  : 2001:db8:9::1                   PrefixLength : 128
    NextHop      : ::1                             Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : LoopBack1                       Flags        : D
   
    Destination  : 2001:db8:1::                  PrefixLength : 64
    NextHop      : 2001:db8:2::2                   Preference   : 255
    Cost         : 0                               Protocol     : EBGP
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : GigabitEthernet0/1/0            Flags        : D
   
    Destination  : 2001:db8:2::                    PrefixLength : 64
    NextHop      : 2001:db8:2::1                   Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : GigabitEthernet0/1/0          Flags        : D
   
    Destination  : 2001:db8:2::1                   PrefixLength : 128
    NextHop      : ::1                             Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : GigabitEthernet0/1/0            Flags        : D
   
    Destination  : FE80::                          PrefixLength : 10
    NextHop      : ::                              Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : NULL0                           Flags        : D 
   ```
   
   Run the **display ipv6 routing-table vpn-instance** command on PE2. The command output shows that there is a route to 2001:db8:8::1/64, the loopback address of the remote CE, in the routing table of the VPN instance IPv6 address family.
   
   ```
   <PE2> display ipv6 routing-table vpn-instance vpna
   ```
   ```
   Routing Table : vpna
            Destinations : 6        Routes : 6
   
    Destination  : 2001:db8:8::                  PrefixLength : 64
    NextHop      : ::FFFF:1.1.1.9                  Preference   : 255
    Cost         : 0                               Protocol     : IBGP
    RelayNextHop : ::FFFF:192.168.2.1              TunnelID     : 0x800007
    Interface    : GigabitEthernet0/2/0            Flags        : RD
   
    Destination  : 2001:db8:9::                    PrefixLength : 64
    NextHop      : 2001:db8:2::1                   Preference   : 255
    Cost         : 0                               Protocol     : EBGP
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : GigabitEthernet0/1/0            Flags        : D
   
    Destination  : 2001:db8:1::                    PrefixLength : 64
    NextHop      : ::FFFF:1.1.1.9                  Preference   : 255
    Cost         : 0                               Protocol     : IBGP
    RelayNextHop : ::FFFF:192.168.2.1              TunnelID     : 0x800007
    Interface    : GigabitEthernet0/2/0            Flags        : RD
   
    Destination  : 2001:db8:2::                    PrefixLength : 64
    NextHop      : 2001:db8:2::2                   Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : GigabitEthernet0/1/0            Flags        : D
   
    Destination  : 2001:db8:2::2                   PrefixLength : 128
    NextHop      : ::1                             Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : GigabitEthernet0/1/0            Flags        : D
   
    Destination  : FE80::                          PrefixLength : 10
    NextHop      : ::                              Preference   : 0
    Cost         : 0                               Protocol     : Direct
    RelayNextHop : ::                              TunnelID     : 0x0
    Interface    : NULL0                           Flags        : D
   ```
   
   Run the **display bgp ipv6 routing-table peer received-routes** command on CE2. The command output shows that CE2 has not received a route with the prefix 2001:db8:8::1/64.
   
   ```
   [~CE2] display bgp ipv6 routing-table peer 2001:db8:2::2 received-routes
   ```
   ```
    BGP Local router ID is 30.30.30.30
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 2
    *>  Network  : 2001:db8:1::                             PrefixLen : 64
        NextHop  : 2001:db8:2::2                            LocPrf    :
        MED      :                                          PrefVal   : 0
        Label    :
        Path/Ogn : 100  ?
        Network  : 2001:db8:2::                             PrefixLen : 64
        NextHop  : 2001:db8:2::2                            LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : 100  ? 
   ```
2. Configure BGP4+ AS number substitution on PEs.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv6-family vpn-instance vpna
   ```
   ```
   [*PE2-bgp6-vpna] peer 2001:db8:2::1 substitute-as
   ```
   ```
   [*PE2-bgp6-vpna] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   Run the **display bgp ipv6 routing-table peer received-routes** command on CE2 to check the routing information received from the EBGP peer. The command output shows that CE2 has received a route to 2001:db8:8::1/64 from PE2, and the value in the Path/Ogn field is 100 100. It indicates that the AS number has been replaced.
   
   ```
   [~CE2] display bgp ipv6 routing-table peer 2001:db8:2::2 received-routes
   ```
   ```
    BGP Local router ID is 30.30.30.30
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 3
    *>  Network  : 2001:db8:8::                           PrefixLen : 64
        NextHop  : 2001:db8:2::2                            LocPrf    :
        MED      :                                          PrefVal   : 0
        Label    :
        Path/Ogn : 100 100  i
    *>  Network  : 2001:db8:1::                             PrefixLen : 64
        NextHop  : 2001:db8:2::2                            LocPrf    :
        MED      :                                          PrefVal   : 0
        Label    :
        Path/Ogn : 100  ?
        Network  : 2001:db8:2::                             PrefixLen : 64
        NextHop  : 2001:db8:2::2                            LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : 100  ?
   ```
   
   After BGP4+ AS number substitution is configured on PE1, the ping (with the source address specified in the **ping** command) between CE1 and CE2 succeeds.
   
   ```
   [~CE2] ping ipv6 -a 2001:db8:9::1 2001:db8:8::1
   ```
   ```
     PING 2001:db8:8::1 : 56  data bytes, press CTRL_C to break
       Reply from 2001:db8:8::1
       bytes=56 Sequence=1 hop limit=62  time = 140 ms
       Reply from 2001:db8:8::1
       bytes=56 Sequence=2 hop limit=62  time = 140 ms
       Reply from 2001:db8:8::1
       bytes=56 Sequence=3 hop limit=62  time = 150 ms
       Reply from 2001:db8:8::1
       bytes=56 Sequence=4 hop limit=62  time = 170 ms
       Reply from 2001:db8:8::1
       bytes=56 Sequence=5 hop limit=62  time = 140 ms
   
     --- 2001:db8:8::1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 140/148/170 ms
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
   ipv6 address 2001:db8:1::1 64
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:8::1/64
  #
  bgp 65410
   router-id 10.10.10.10
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
  ip vpn-instance vpna
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
   ipv6 enable
   ip binding vpn-instance vpna
   ipv6 address 2001:db8:1::2 64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 20.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.9 255.255.255.255
  #
  bgp 100
   peer 3.3.3.9 as-number 100
   peer 3.3.3.9 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.9 enable
   #
   ipv6-family vpnv6
    policy vpn-target
    peer 3.3.3.9 enable
  #
   ipv6-family vpn-instance vpna
    peer 2001:db8:1::1 as-number 65410
    peer 2001:db8:1::1 substitute-as
    import-route direct
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.9 0.0.0.0
    network 20.1.1.0 0.0.0.255
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 2.2.2.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 20.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 30.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.9 255.255.255.255
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.9 0.0.0.0
    network 20.1.1.0 0.0.0.255
    network 30.1.1.0 0.0.0.255
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  ip vpn-instance vpna
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 3.3.3.9
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ip binding vpn-instance vpna
   ipv6 address 2001:db8:2::2 64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 30.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.9 255.255.255.255
  #
  bgp 100
   peer 1.1.1.9 as-number 100
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
   ipv6-family vpn-instance vpna
    peer 2001:db8:2::1 as-number 65410
    peer 2001:db8:2::1 substitute-as
    import-route direct
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.9 0.0.0.0
    network 30.1.1.0 0.0.0.255
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
   ipv6 address 2001:db8:2::1 64
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:db8:9::1/64
  #
  bgp 65410
   router-id 30.30.30.30
   peer 2001:db8:2::2 as-number 100
   #
   ipv6-family unicast
    undo synchronization
    import-route direct
    peer 2001:db8:2::2 enable
  #
  return
  ```