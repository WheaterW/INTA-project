Example for Configuring Interworking Between EVPN L3VPNv6 HoVPN over MPLS and Common L3VPNv6
============================================================================================

This section provides an example for configuring interworking between EVPN L3VPNv6 HoVPN over MPLS and common L3VPNv6.

#### Networking Requirements

An IP bearer network generally uses L2VPN and L3VPN (HVPN) to carry Layer 2 and Layer 3 services, respectively. The protocols are complex. EVPN, in contrast, can carry both Layer 2 and Layer 3 services. To simplify service bearer protocols, many IP bearer networks will evolve to EVPN. Among them, L3VPN HVPN that carries Layer 3 services needs to evolve to EVPN L3VPN HVPN. During evolution, if a lot of devices are deployed on the network, both the L3VPNv6 and EVPN may be used to carry IPv6 services. On the network shown in [Figure 1](#EN-US_TASK_0172370688__fig148010918154), the UPE and SPE are connected at the access layer, and the SPE and NPE are connected at the aggregation layer. Independent IGPs are deployed at the access and aggregation layers to ensure communication at different layers. EVPN L3VPNv6 HoVPN is deployed between the UPE and SPE, and L3VPNv6 is deployed between the SPE and NPE. The SPE advertises only default EVPN routes to the UPE. Upon receipt of specific routes from the UPE, the SPE re-encapsulates the EVPN routes into VPNv6 routes and advertises these VPNv6 routes to the NPE.

**Figure 1** Configuring interworking between EVPN L3VPN HoVPN over MPLS and common L3VPN![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001179250248.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Deploy an IGP between the UPE and SPE and between the SPE and NPE. In this example, deploy OSPF between the UPE and SPE and IS-IS between the SPE and NPE.
2. Configure MPLS LDP on the UPE, SPE, and NPE.
3. Create a VPN instance on the UPE, SPE, and NPE.
4. Bind access-side interfaces to VPN instances on the UPE and NPE.
5. Configure a default static VPN route on the SPE.
6. Configure a route-policy on the NPE to prevent the NPE from receiving default routes.
7. Configure BGP VPNv6 on the SPE and NPE.
8. Configure BGP EVPN on the UPE and SPE, specify the UPE as a lower-level PE of the SPE, and configure the import of default VPN routes.
9. Configure route regeneration on the SPE.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the UPE, SPE, and NPE: 1.1.1.1, 2.2.2.2, and 3.3.3.3
* VPN instance name (vpn1) and RD (100:1)
* VPN targets 1:1 and 2:2 for route import and export by the VPN instance

#### Procedure

1. Configure IP addresses, including loopback interface addresses, on the UPE, SPE, and NPE.
   
   
   
   For details about how to configure interface IP addresses and masks, see [Configuration Files](#EN-US_TASK_0172370688__dc_vrp_evpn_cfg_008801) in this section.
2. Deploy an IGP between the UPE and SPE and between the SPE and NPE. In this example, deploy OSPF between the UPE and SPE and IS-IS between the SPE and NPE.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172370688__dc_vrp_evpn_cfg_008801) in this section.
3. Configure MPLS LDP on the UPE, SPE, and NPE.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172370688__dc_vrp_evpn_cfg_008801) in this section.
4. Create a VPN instance on the UPE, SPE, and NPE.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] ip vpn-instance vpn1
   ```
   ```
   [*UPE-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv6] vpn-target 2:2 both evpn
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv6] evpn mpls routing-enable
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*UPE-vpn-instance-vpn1] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the SPE.
   
   ```
   [~SPE] ip vpn-instance vpn1
   ```
   ```
   [*SPE-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv6] vpn-target 1:1 both
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv6] vpn-target 2:2 both evpn
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv6] evpn mpls routing-enable
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*SPE-vpn-instance-vpn1] quit
   ```
   ```
   [*SPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] ip vpn-instance vpn1
   ```
   ```
   [*NPE-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv6] vpn-target 1:1 both
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*NPE-vpn-instance-vpn1] quit
   ```
   ```
   [*NPE] commit
   ```
5. Bind access-side interfaces to VPN instances on the UPE and NPE.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] interface GigabitEthernet 0/2/0
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] ipv6 address 2001:DB8:20::1 64
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] interface GigabitEthernet 0/2/0
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] ipv6 address 2001:DB8:30::1 64
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*NPE] commit
   ```
6. Configure a default static route on the SPE.
   
   
   ```
   [~SPE] ipv6 route-static vpn-instance vpn1 :: 0 2001:DB8:3::2
   ```
   ```
   [*SPE] commit
   ```
7. Configure a route-policy on the NPE to prevent the NPE from receiving default routes.
   
   
   ```
   [~NPE] ip ipv6-prefix default index 10 permit :: 0
   ```
   ```
   [*NPE] route-policy p1 deny node 10
   ```
   ```
   [*NPE-route-policy] if-match ipv6 address prefix-list default
   ```
   ```
   [*NPE-route-policy] quit
   ```
   ```
   [*NPE] route-policy p1 permit node 20
   ```
   ```
   [*NPE-route-policy] quit
   ```
   ```
   [*NPE] ip vpn-instance vpn1
   ```
   ```
   [*NPE-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv6] import route-policy p1
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*NPE-vpn-instance-vpn1] quit
   ```
   ```
   [*NPE] commit
   ```
8. Configure BGP VPNv6 on the SPE and NPE.
   
   
   
   # Configure the SPE.
   
   ```
   [~SPE] bgp 100
   ```
   ```
   [*SPE-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*SPE-bgp] peer 3.3.3.3 connect-interface LoopBack1
   ```
   ```
   [*SPE-bgp] ipv6-family vpnv6
   ```
   ```
   [*SPE-bgp-af-vpnv6] peer 3.3.3.3 enable
   ```
   ```
   [*SPE-bgp-af-vpnv6] quit
   ```
   ```
   [*SPE-bgp] quit
   ```
   ```
   [*SPE] commit
   ```
   
   # Configure the NPE.
   
   ```
   [~NPE] bgp 100
   ```
   ```
   [*NPE-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*NPE-bgp] peer 2.2.2.2 connect-interface LoopBack1
   ```
   ```
   [*NPE-bgp] ipv6-family vpnv6
   ```
   ```
   [*NPE-bgp-af-vpnv6] peer 2.2.2.2 enable
   ```
   ```
   [*NPE-bgp-af-vpnv6] quit
   ```
   ```
   [*NPE-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*NPE-bgp-6-vpn1] import-route direct
   ```
   ```
   [*NPE-bgp-6-vpn1] quit
   ```
   ```
   [*NPE-bgp] quit
   ```
   ```
   [*NPE] commit
   ```
9. Configure BGP EVPN on the UPE and SPE, specify the UPE as a lower-level PE of the SPE, and configure the import of default VPN routes.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] bgp 100
   ```
   ```
   [*UPE-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*UPE-bgp] peer 2.2.2.2 connect-interface LoopBack1
   ```
   ```
   [*UPE-bgp] l2vpn-family evpn
   ```
   ```
   [*UPE-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*UPE-bgp-af-evpn] quit
   ```
   ```
   [*UPE-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*UPE-bgp-6-vpn1] advertise l2vpn evpn
   ```
   ```
   [*UPE-bgp-6-vpn1] import-route direct
   ```
   ```
   [*UPE-bgp-6-vpn1] quit
   ```
   ```
   [*UPE-bgp] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure the SPE.
   
   ```
   [~SPE] bgp 100
   ```
   ```
   [*SPE-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*SPE-bgp] peer 1.1.1.1 connect-interface LoopBack1
   ```
   ```
   [*SPE-bgp] l2vpn-family evpn
   ```
   ```
   [*SPE-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*SPE-bgp-af-evpn] peer 1.1.1.1 upe
   ```
   ```
   [*SPE-bgp-af-evpn] quit
   ```
   ```
   [*SPE-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*SPE-bgp-6-vpn1] network :: 0
   ```
   ```
   [*SPE-bgp-6-vpn1] advertise l2vpn evpn
   ```
   ```
   [*SPE-bgp-6-vpn1] quit
   ```
   ```
   [*SPE-bgp] quit
   ```
   ```
   [*SPE] commit
   ```
10. Configure route regeneration on the SPE.
    
    
    
    # Configure the SPE.
    
    ```
    [~SPE] bgp 100
    ```
    ```
    [*SPE-bgp] ipv6-family vpnv6
    ```
    ```
    [*SPE-bgp-af-vpnv6] peer 3.3.3.3 advertise route-reoriginated evpn ipv6
    ```
    ```
    [*SPE-bgp-af-vpnv6] quit
    ```
    ```
    [*SPE-bgp] l2vpn-family evpn
    ```
    ```
    [*SPE-bgp-af-evpn] peer 1.1.1.1 import reoriginate
    ```
    ```
    [*SPE-bgp-af-evpn] quit
    ```
    ```
    [*SPE-bgp] quit
    ```
    ```
    [*SPE] commit
    ```
11. Verify the configuration.
    
    
    
    Run the **display ipv6 routing-table vpn-instance vpn1** command on the NPE. The command output shows VPN route information.
    
    ```
    [~NPE] display ipv6 routing-table vpn-instance vpn1
    ```
    ```
    Routing Table : vpn1
             Destinations : 4        Routes : 4         
    
    Destination  : 2001:DB8:20::                           PrefixLength : 64
    NextHop      : ::FFFF:2.2.2.2                          Preference   : 255
    Cost         : 0                                       Protocol     : IBGP
    RelayNextHop : ::FFFF:10.2.1.1                         TunnelID     : 0x0000000001004c4b42
    Interface    : GigabitEthernet0/1/0                    Flags        : RD
    
    Destination  : 2001:DB8:30::                           PrefixLength : 64
    NextHop      : 2001:DB8:30::1                          Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : GigabitEthernet0/2/0                    Flags        : D
    
    Destination  : 2001:DB8:30::1                          PrefixLength : 128
    NextHop      : ::1                                     Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : GigabitEthernet0/2/0                    Flags        : D
    
    Destination  : FE80::                                  PrefixLength : 10
    NextHop      : ::                                      Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : NULL0                                   Flags        : DB
    ```
    
    Run the **display bgp evpn all routing-table** command on the UPE. The command output shows the default EVPN routes received from the SPE.
    
    ```
    [~UPE] display bgp evpn all routing-table
    ```
    ```
     Local AS number : 100
    
     BGP Local router ID is 10.1.1.1
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
     
     EVPN address family:
     Number of Ip Prefix Routes: 2
     Route Distinguisher: 100:1
           Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
     *>i   0:[::]:0                                               2.2.2.2
     *>    0:[2001:DB8:20::]:64                                   0.0.0.0
        
    
    ```
    
    Run the **display ipv6 routing-table vpn-instance vpn1** command on the UPE to view the default VPN routes received from the SPE.
    
    ```
    [~UPE] display ipv6 routing-table vpn-instance vpn1
    ```
    ```
    Routing Table : vpn1
             Destinations : 4        Routes : 4         
    
    Destination  : ::                                      PrefixLength : 0
    NextHop      : ::FFFF:2.2.2.2                          Preference   : 255
    Cost         : 0                                       Protocol     : IBGP
    RelayNextHop : ::FFFF:10.1.1.2                         TunnelID     : 0x0000000001004c4b42
    Interface    : GigabitEthernet0/1/0                    Flags        : RD
    
    Destination  : 2001:DB8:20::                           PrefixLength : 64
    NextHop      : 2001:DB8:20::1                          Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : GigabitEthernet0/2/0                    Flags        : D
    
    Destination  : 2001:DB8:20::1                          PrefixLength : 128
    NextHop      : ::1                                     Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : GigabitEthernet0/2/0                    Flags        : D
    
    Destination  : FE80::                                  PrefixLength : 10
    NextHop      : ::                                      Preference   : 0
    Cost         : 0                                       Protocol     : Direct
    RelayNextHop : ::                                      TunnelID     : 0x0
    Interface    : NULL0                                   Flags        : DB
    ```

#### Configuration Files

* UPE configuration file
  
  ```
  #
  sysname UPE
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 1.1.1.1
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
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:20::1/64
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
   ipv6-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* SPE configuration file
  
  ```
  #
  sysname SPE
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
    vpn-target 1:1 export-extcommunity
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity
    vpn-target 2:2 import-extcommunity evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
   isis enable 1
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 3.3.3.3 enable
   #
   ipv6-family vpnv6
    undo policy vpn-target
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise route-reoriginated evpn ipv6
   #
   ipv6-family vpn-instance vpn1
    network :: 0
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 upe
    peer 1.1.1.1 import reoriginate
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  ipv6 route-static vpn-instance vpn1 :: 0 2001:DB8:3::2
  #
  return
  ```
* NPE configuration file
  
  ```
  #
  sysname NPE
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 100:1
    apply-label per-instance
    import route-policy p1
    vpn-target 1:1 export-extcommunity
    vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
  #
  mpls ldp
  #
  isis 1
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:30::1/64
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
  #
  interface LoopBack2
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:3::2/64
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
  ip ipv6-prefix default index 10 permit :: 0
  #
   ipv6-family vpn-instance vpn1
    import-route direct
  #
  route-policy p1 deny node 10
   if-match ipv6 address prefix-list default
  #
  route-policy p1 permit node 20
  #
  return
  ```