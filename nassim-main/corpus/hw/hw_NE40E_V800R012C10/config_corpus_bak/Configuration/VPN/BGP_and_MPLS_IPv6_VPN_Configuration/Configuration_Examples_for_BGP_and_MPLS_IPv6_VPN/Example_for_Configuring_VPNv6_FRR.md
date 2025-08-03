Example for Configuring VPNv6 FRR
=================================

This section provides an example for configuring VPNv6 FRR in a CE multi-homing scenario. If a PE fails, VPNv6 FRR can quickly switch IPv6 VPN traffic to the backup route.

#### Networking Requirements

VPNv6 FRR can be deployed in the CE dual-homing networking. If the primary route between PEs fails, VPNv6 FRR can quickly switch IPv6 VPN traffic to the backup route.

On the network shown in [Figure 1](#EN-US_TASK_0172369738__fig_dc_vrp_mpls-l3vpn-v6_cfg_204401), PE1 learns two routes with the same prefix to the CE from PE2 and PE3. It is required that PE3 be configured as a backup next hop for the IPv6 route on PE1. In this manner, VPN traffic can be quickly switched to PE3 if PE2 becomes faulty.

**Figure 1** Network diagram of configuring VPNv6 FRR![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](figure/en-us_image_0285385105.png)

#### Configuration Notes

* A CE is dual-homed to two PEs, and VPN instances with different RDs are configured on the PEs.
* In a VPN FRR scenario, after the primary path recovers, traffic switches back to this path. Because the order in which nodes undergo IGP convergence differs, packet loss may occur during the switchback. To resolve this problem, run the [**route-select delay**](cmdqueryname=route-select+delay) *delay-value* command to configure a route selection delay so that traffic is switched back only after forwarding entries on the devices along the primary path are updated. The delay specified using *delay-value* depends on various factors, such as the number of routes on the devices. Set a proper delay as needed.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF on the MPLS backbone network for communication between PE1, PE2, and PE3.
2. Configure basic MPLS functions and MPLS LDP on the MPLS backbone network to establish LDP LSPs.
3. Configure an IPv6-address-family-enabled VPN instance on PE1, PE2, and PE3, and bind the interface that connects a PE to the CE to the VPN instance on that PE.
4. Establish an EBGP peer relationship between the CE and PEs for IPv6 VPN route import, and establish MP-IBGP peer relationships between PEs.
5. Configure static BFD for LDP LSP on PE1 and PE2.
6. Enable VPNv6 auto FRR on PE1.

#### Data Preparation

To complete the configuration, you need the following data:

* AS numbers of the PEs and CE
* Name of the VPN instance configured on each PE as well as other attributes of the VPN instance IPv6 address family, such as the RD and VPN targets
* Names of the route-policy and IP prefix configured on PE1
* BFD configuration name, local discriminator, and remote discriminator

#### Procedure

1. Configure IPv4 addresses for interfaces on the VPN backbone network and IPv6 addresses for interfaces at the VPN site. For detailed configurations, see Configuration Files.
2. Configure OSPF on the MPLS backbone network for communication between PEs on the backbone network. For detailed configurations, see Configuration Files.
3. Configure basic MPLS functions and MPLS LDP on the MPLS backbone network to establish LDP LSPs.
   
   
   
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
   [*PE1] interface gigabitEthernet0/2/0
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE1] interface gigabitEthernet0/3/0
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] mpls ldp
   ```
   ```
   [*PE1-GigabitEthernet0/3/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   <PE2> system-view
   ```
   ```
   [~PE2] mpls lsr-id 2.2.2.2
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
   [*PE2] interface gigabitEthernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] mpls ldp
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   <PE3> system-view
   ```
   ```
   [~PE3] mpls lsr-id 3.3.3.3
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
   [*PE3] interface gigabitEthernet0/1/0
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
   
   Run the **display mpls lsp** command on PEs. The command output shows that LSPs have been set up between PE1 and PE2, and between PE1 and PE3. The following example uses the command output on PE1.
   
   ```
   [~PE1] display mpls lsp
   ```
   ```
   2021-04-09 01:14:17.813                                                                                                             
   Flag after Out IF: (I) - RLFA Iterated LSP, (I*) - Normal and RLFA Iterated LSP                                                     
   Flag after LDP FRR: (L) - Logic FRR LSP
   -------------------------------------------------------------------------------
                    LSP Information: LDP LSP
   -------------------------------------------------------------------------------
   FEC                In/Out Label  In/Out IF                      Vrf Name
   1.1.1.1/32         3/NULL        -/-
   2.2.2.2/32         NULL/3        -/GE0/2/0
   2.2.2.2/32         1025/3        -/GE0/2/0
   3.3.3.3/32         NULL/3        -/GE0/3/0
   3.3.3.3/32         1024/3        -/GE0/3/0
   ```
4. Configure an IPv6-address-family-enabled VPN instance on each PE and configure the CE to access PE2 and PE3.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] ip vpn-instance vpn1
   ```
   ```
   [*PE1-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv6] vpn-target 111:1
   ```
   ```
   [*PE1-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*PE1-vpn-instance-vpn1] quit
   ```
   ```
   [*PE1] interface loopback2
   ```
   ```
   [*PE1-Loopback2] ip binding vpn-instance vpn1
   ```
   ```
   [*PE1-Loopback2] ipv6 enable
   ```
   ```
   [*PE1-Loopback2] ipv6 address 2001:DB8:8::1 64
   ```
   ```
   [*PE1-Loobpack2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] ip vpn-instance vpn1
   ```
   ```
   [*PE2-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:2
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv6] vpn-target 111:1
   ```
   ```
   [*PE2-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*PE2-vpn-instance-vpn1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/2/0
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] ipv6 address 2001:DB8:1::2 64
   ```
   ```
   [*PE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] ip vpn-instance vpn1
   ```
   ```
   [*PE3-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*PE3-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:3
   ```
   ```
   [*PE3-vpn-instance-vpn1-af-ipv6] vpn-target 111:1
   ```
   ```
   [*PE3-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*PE3-vpn-instance-vpn1] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] ipv6 address 2001:DB8:3::2 64
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE3] commit
   ```
5. Establish an EBGP peer relationship between PE2 and the CE, and between PE3 and the CE.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*PE2-bgp6-vpn1] peer 2001:DB8:1::1 as-number 65410
   ```
   ```
   [*PE2-bgp6-vpn1] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*PE3-bgp6-vpn1] peer 2001:DB8:3::1 as-number 65410
   ```
   ```
   [*PE3-bgp6-vpn1] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure the CE.
   
   ```
   <CE> system-view
   ```
   ```
   [~CE] bgp 65410
   ```
   ```
   [*CE-bgp] router-id 10.10.10.10
   ```
   ```
   [*CE-bgp] peer 2001:DB8:1::2 as-number 100
   ```
   ```
   [*CE-bgp] peer 2001:DB8:3::2 as-number 100
   ```
   ```
   [*CE-bgp] ipv6-family unicast
   ```
   ```
   [*CE-bgp-af-ipv6] peer 2001:DB8:1::2 enable
   ```
   ```
   [*CE-bgp-af-ipv6] peer 2001:DB8:3::2 enable
   ```
   ```
   [*CE-bgp-af-ipv6] network 2001:DB8:0:1:2::1 128
   ```
   ```
   [*CE-bgp-af-ipv6] quit
   ```
   ```
   [*CE-bgp] quit
   ```
   ```
   [*CE] commit
   ```
   
   After the configuration is complete, run the **display bgp vpnv6 vpn-instance vpn1 peer** command on PE2 and PE3. The command output shows that the status of the EBGP peer relationships between the PEs and CE is **Established**.
   
   The following example uses the command output on PE2.
   
   ```
   [~PE2] display bgp vpnv6 vpn-instance vpn1 peer
   ```
   ```
    BGP local router ID : 2.2.2.2
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
     Peer            V    AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv
     2001:DB8:1::1   4 65001       46       46     0 00:08:36 Established     5
   ```
6. Establish an MP-IBGP peer relationship between PEs.
   
   
   
   # Configure PE1.
   
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
   [*PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] ipv6-family vpnv6
   ```
   ```
   [*PE1-bgp-af-vpnv6] peer 2.2.2.2 enable
   ```
   ```
   [*PE1-bgp-af-vpnv6] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-vpnv6] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] bgp 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE2-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] ipv6-family vpnv6
   ```
   ```
   [*PE2-bgp-af-vpnv6] peer 1.1.1.1 enable
   ```
   ```
   [*PE2-bgp-af-vpnv6] quit
   ```
   ```
   [*PE2-bgp] quit
   ```
   ```
   [*PE2-bgp] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] bgp 100
   ```
   ```
   [*PE3-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*PE3-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] ipv6-family vpnv6
   ```
   ```
   [*PE3-bgp-af-vpnv6] peer 1.1.1.1 enable
   ```
   ```
   [*PE3-bgp-af-vpnv6] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
   
   After the configuration is complete, run the **display bgp vpnv6 all peer** command on PEs. The command output shows that the status of the MP-IBGP peer relationship between the PEs is **Established**.
   
   The following example uses the command output on PE1.
   
   ```
   [~PE1] display bgp vpnv6 all peer
   ```
   ```
    BGP local router ID : 10.10.1.1
    Local AS number : 100
    Total number of peers : 2                 Peers in established state : 2
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2.2.2.2         4         100       29       26     0 00:20:08 Established       2
     3.3.3.3         4         100       18       17     0 00:11:32 Established       1
   ```
7. Configure static BFD for LDP LSP.
   
   
   
   # Configure static BFD for LDP LSP on PE1.
   
   ```
   [~PE1] bfd
   ```
   ```
   [*PE1-bfd] quit
   ```
   ```
   [*PE1] bfd for_ldp_lsp bind ldp-lsp peer-ip 2.2.2.2 nexthop 10.10.1.2 interface gigabitethernet0/2/0
   ```
   ```
   [*PE1-bfd-session-for_ldp_lsp] discriminator local 10
   ```
   ```
   [*PE1-bfd-session-for_ldp_lsp] discriminator remote 20
   ```
   ```
   [*PE1-bfd-session-for_ldp_lsp] process-pst
   ```
   ```
   [*PE1-bfd-session-for_ldp_lsp] commit
   ```
   ```
   [~PE1-bfd-session-for_ldp_lsp] quit
   ```
   
   # Configure static BFD for LDP LSP on PE2.
   
   ```
   [~PE2] bfd
   ```
   ```
   [*PE2-bfd] quit
   ```
   ```
   [*PE2] bfd for_ldp_lsp bind ldp-lsp peer-ip 1.1.1.1 nexthop 10.10.1.1 interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-bfd-session-for_ldp_lsp] discriminator local 20
   ```
   ```
   [*PE2-bfd-session-for_ldp_lsp] discriminator remote 10
   ```
   ```
   [*PE2-bfd-session-for_ldp_lsp] commit
   ```
   ```
   [~PE2-bfd-session-for_ldp_lsp] quit
   ```
   
   # After the configuration is complete, run the **display bfd session all verbose** command on PE1 and PE2. The command output shows that **State** is **Up**, and **BFD Bind Type** is **LDP\_LSP**.
8. Enable VPNv6 auto FRR.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [~PE1-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*PE1-bgp6-vpn1] auto-frr
   ```
   ```
   [*PE1-bgp6-vpn1] route-select delay 300
   ```
   ```
   [*PE1-bgp6-vpn1] quit
   ```
   ```
   [*PE1-bgp] quit
   ```
   ```
   [*PE1] commit
   ```
9. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display ipv6 routing-table vpn-instance verbose** command on PE1. The command output shows the backup next hop, backup label, and backup tunnel ID of the IPv6 VPN route.
   
   ```
   [~PE1] display ipv6 routing-table vpn-instance vpn1 2001:DB8:2::1 128 verbose
   ```
   ```
   Routing Table : vpn1
   Summary Count : 1
   
   Destination  : 2001:DB8:2::1                           PrefixLength : 128
   NextHop      : 2.2.2.2                                 Preference   : 255
   Neighbour    : ::                                      ProcessID    : 0
   Label        : 4099                                    Protocol     : IBGP
   State        : Active Adv Relied                       Cost         : 0
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0
   Priority     : low                                     Age          : 450sec
   IndirectID   : 0x5A00006E
   RelayNextHop : ::                                      TunnelID     : 0x0000000001004c4b42
   Interface    : LDP LSP                                 Flags        : RD
   BkNextHop   : 3.3.3.3                                 BkInterface  : LDP LSP
   BkLabel     : 4098                                    BkTunnelID   : 0x0
   BkPETunnelID: 0x0000000001004c4b43                    BkIndirectID : 0x5A000070
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  bfd
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.10.1.1 255.255.255.252
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.20.1.1 255.255.255.252
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  interface LoopBack2
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:8::1/64
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
   ipv6-family vpnv6
    policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
  #
   ipv6-family vpn-instance vpn1
   auto-frr
   route-select delay 300
  #
  ospf 1
   area 0.0.0.0
    network 10.10.1.0 0.0.0.3
    network 10.20.1.0 0.0.0.3
    network 1.1.1.1 0.0.0.0
  #
  bfd for_ldp_lsp bind ldp-lsp peer-ip 2.2.2.2 nexthop 10.10.1.2 interface gigabitethernet0/2/0
   discriminator local 10
   discriminator remote 20
   process-pst
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
    route-distinguisher 100:2
    apply-label per-instance
    vpn-target 111:1 export-extcommunity
    vpn-target 111:1 import-extcommunity
  #
  bfd
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.10.1.2 255.255.255.252
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable 
   ip binding vpn-instance vpn1
   ipv6 address 2001:DB8:1::2/64
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
  #
   ipv6-family vpnv6
    policy vpn-target
    peer 1.1.1.1 enable
  #
   ipv6-family vpn-instance vpn1
    peer 2001:DB8:1::1 as-number 65410
    import-route direct
  #
  ospf 1
   area 0.0.0.0
    network 10.10.1.0 0.0.0.3
    network 2.2.2.2 0.0.0.0
  #
  bfd for_ldp_lsp bind ldp-lsp peer-ip 1.1.1.1 nexthop 10.10.1.1 interface gigabitethernet0/1/0
   discriminator local 20
   discriminator remote 10
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  ip vpn-instance vpn1
   ipv6-family
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
   ip address 10.20.1.2 255.255.255.252
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable 
   ip binding vpn-instance vpn1
   ipv6 address 2001:DB8:3::2/64
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100 
   peer 1.1.1.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
  #
   ipv6-family vpnv6
    policy vpn-target
    peer 1.1.1.1 enable
  #
   ipv6-family vpn-instance vpn1
    peer 2001:DB8:3::1 as-number 65410
  #
  ospf 1
   area 0.0.0.0
    network 10.20.1.0 0.0.0.3
    network 3.3.3.3 0.0.0.0
  #
  Return
  ```
* CE configuration file
  
  ```
  #
  sysname CE
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:2::1/128
  #
  bgp 65410
   router-id 10.10.10.10
   peer 2001:DB8:1::2 as-number 100
   peer 2001:DB8:3::2 as-number 100
   #
   ipv4-family unicast
    undo synchronization
   #
    ipv6-family unicast
     undo synchronization
     network 2001:DB8:0:1:2::1 128
     peer 2001:DB8:1::2 enable
     peer 2001:DB8:3::2 enable
  #
  return
  ```