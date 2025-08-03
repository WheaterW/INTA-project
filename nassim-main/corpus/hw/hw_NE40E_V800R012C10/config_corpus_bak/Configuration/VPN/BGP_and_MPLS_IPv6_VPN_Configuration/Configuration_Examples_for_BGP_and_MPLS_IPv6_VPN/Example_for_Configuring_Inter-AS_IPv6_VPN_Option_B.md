Example for Configuring Inter-AS IPv6 VPN Option B
==================================================

An MP-EBGP peer relationship can be established between the ASBRs with only one hop to exchange VPNv6 routes.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369717__fig_dc_vrp_mpls-l3vpn-v6_cfg_205001), CE1 and CE2 belong to the same VPN. CE1 is connected to PE1 in AS 100, and CE2 is connected to PE2 in AS 200. It is required that an MP-EBGP peer relationship be established between the ASBRs to transmit VPNv6 routes, thus implementing inter-AS VPN Option B.

**Figure 1** Networking diagram of inter-AS IPv6 VPN Option B![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_mpls-l3vpn-v6_cfg_205001.png)

#### Configuration Notes

When configuring inter-AS IPv6 VPN Option B, note the following:

* An MP-EBGP peer relationship is established between ASBR1 and ASBR2, and the ASBRs do not filter received VPNv6 routes based on VPN targets.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IGP on the MPLS backbone network to implement interworking of the ASBR and PE in the same AS, and set up an MPLS LDP LSP between the ASBR and PE in the same AS.
2. Set up EBGP peer relationships between the PEs and CEs and set up MP-IBGP peer relationships between the PEs and ASBRs.
3. Configure VPN instances on the PEs rather than ASBRs.
4. Enable MPLS on the interface that connects one ASBR to the other ASBR, set up an MP-EBGP peer relationship between the ASBRs, and configure the ASBRs not to filter received VPNv6 routes based on VPN targets.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the PEs and ASBRs
* Names, RDs, and VPN targets of the VPN instances of the PEs

#### Procedure

1. On the MPLS backbone networks in AS 100 and AS 200, configure an IGP to interconnect the PE and ASBR on each network.
   
   
   
   In this example, OSPF is used as an IGP. For configuration details, see [Configuration Files](#EN-US_TASK_0172369717__example535610981214051) in this section.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The 32-bit IP address of the loopback interface that functions as the LSR ID needs to be advertised by using OSPF.
   
   After the configuration, the OSPF neighbor relationship can be established between the ASBR and PE in the same AS. Run the **display ospf peer** command. The command output shows that the neighbor relationship is in the **Full** state.
   
   The ASBR and PE in the same AS can learn and successfully ping the IP address of the loopback interface of each other.
2. Configure MPLS and MPLS LDP, and set up MPLS LDP LSPs on the MPLS backbone networks in AS 100 and AS 200.
   
   
   
   For configuration details, see [Example for Configuring Inter-AS IPv6 VPN Option A](dc_vrp_mpls-l3vpn-v6_cfg_2049.html).
3. Configure the basic BGP/MPLS IPv6 VPN functions on PE1 and PE2.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The VPN targets of the VPN instances of PE1 and PE2 must be the same.
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172369717__example535610981214051) in this section.
4. Configure inter-AS VPN Option B.
   
   
   
   # Configure ASBR1. Enable MPLS on GE 0/2/0 connected to ASBR2.
   
   ```
   [~ASBR1] interface gigabitEthernet 0/2/0
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
   
   # Configure ASBR1. Establish MP-EBGP peer with ASBR2 and perform no VPN-Target filtering on the received VPNv6 routes, and then enable ASBR1 to allocate labels based on the next hop.
   
   ```
   [~ASBR1] bgp 100
   ```
   ```
   [*ASBR1-bgp] peer 192.168.1.2 as-number 200
   ```
   ```
   [*ASBR1-bgp] ipv6-family vpnv6
   ```
   ```
   [*ASBR1-bgp-af-vpnv6] peer 192.168.1.2 enable
   ```
   ```
   [*ASBR1-bgp-af-vpnv6] undo policy vpn-target
   ```
   ```
   [*ASBR1-bgp-af-vpnv6] quit
   ```
   ```
   [*ASBR1-bgp] quit
   ```
   ```
   [*ASBR1] commit
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The configurations of ASBR2 are similar to those of ASBR1. For configuration details, see [Configuration Files](#EN-US_TASK_0172369717__example535610981214051) in this section.
5. Verify the configuration.
   
   
   
   After the configuration, CEs can learn routes to the interface of each other, and CE1 and CE2 can ping each other successfully.
   
   The following example uses the command output on CE1.
   
   ```
   <CE1> display ipv6 routing-table
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
   
   Destination  : 2001:db8:2::                           PrefixLength : 64
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
   <CE1> ping ipv6 2001:db8:2::1
   ```
   ```
     PING 2001:db8:2::1 : 56  data bytes, press CTRL_C to break
   ```
   ```
       Reply from 2001:db8:2::1
   ```
   ```
       bytes=56 Sequence=1 hop limit=62  time = 125 ms
   ```
   ```
       Reply from 2001:db8:2::1
   ```
   ```
       bytes=56 Sequence=2 hop limit=62  time = 109 ms
   ```
   ```
       Reply from 2001:db8:2::1
   ```
   ```
       bytes=56 Sequence=3 hop limit=62  time = 109 ms
   ```
   ```
       Reply from 2001:db8:2::1
   ```
   ```
       bytes=56 Sequence=4 hop limit=62  time = 109 ms
   ```
   ```
       Reply from 2001:db8:2::1
   ```
   ```
       bytes=56 Sequence=5 hop limit=62  time = 110 ms
   
   
   ```
   ```
     --- 2001:db8:2::1 ping statistics ---
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
       round-trip min/avg/max = 109/112/125 ms
   ```
   
   Run the **display bgp vpnv6 all routing-table** command on an ASBR. The command output shows the VPNv6 routes on the ASBR.
   
   The following example uses the command output on ASBR1.
   
   ```
   <ASBR1> display bgp vpnv6 all routing-table
   ```
   ```
    
    BGP Local router ID is 192.168.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
    
    Total number of routes from all PE: 2
    Route Distinguisher: 100:1
   
    *>i Network  : 2001:db8:1::                             PrefixLen : 64  
        NextHop  : ::FFFF:1.1.1.1                           LocPrf    : 100 
        MED      : 0                                        PrefVal   : 0
        Label    : 21/23
        Path/Ogn : 65001?
    Route Distinguisher: 200:2
   
    *>  Network  : 2001:db8:2::                            PrefixLen : 64  
        NextHop  : ::FFFF:192.168.1.2                         LocPrf    :   
        MED      :                                          PrefVal   : 0
        Label    : 25/25
        Path/Ogn : 200 65002?
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
   router-id 10.10.10.10
   peer 2001:db8:1::2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
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
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
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
   ipv6-family vpnv6
    policy vpn-target
    peer 2.2.2.2 enable
  #
   ipv6-family vpn-instance vpn1
    peer 2001:db8:1::1 as-number 65001
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 172.16.1.0 0.0.0.255
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
   ipv6-family vpnv6
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 192.168.1.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 172.16.1.0 0.0.0.255
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
   ip address 10.1.1.1 255.255.255.0
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
   ipv6-family vpnv6
    undo policy vpn-target
    peer 4.4.4.4 enable
    peer 192.168.1.1 enable
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
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
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
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
   ipv6-family vpnv6
    policy vpn-target
    peer 3.3.3.3 enable
  #
   ipv6-family vpn-instance vpn1
    peer 2001:db8:2::1 as-number 65002
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.1.1.0 0.0.0.255
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
   router-id 11.11.11.11
   peer 2001:db8:2::2 as-number 200
   #
    ipv4-family unicast
    undo synchronization
   #
   ipv6-family unicast
    undo synchronization
    import-route direct
    peer 2001:db8:2::2 enable
  #
  return
  ```