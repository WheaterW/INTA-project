Example for Configuring EVPN L3VPNv6 H-VPN over MPLS
====================================================

This section provides an example for configuring EVPN L3VPNv6 H-VPN over MPLS to deliver network connectivity.

#### Networking Requirements

An IP bearer network generally uses L2VPN and L3VPN (HVPN) to carry Layer 2 and Layer 3 services, respectively. The protocols are complex. EVPN, in contrast, can carry both Layer 2 and Layer 3 services. To simplify service bearer protocols, many IP bearer networks will evolve to EVPN. Among them, L3VPNv6 HVPN that carries IPv6 Layer 3 services needs to evolve to EVPN L3VPNv6 HVPN. On the network shown in [Figure 1](#EN-US_TASK_0172370687__fig7904139358), an access layer network is deployed between the UPE and SPE, and an aggregation layer network is deployed between the SPE and NPE. Independent IGP protocols need to be deployed on the access layer network and aggregation layer network for connectivity. EVPN L3VPNv6 H-VPN needs to be deployed to implement E2E connectivity. On the EVPN L3VPNv6 H-VPN network, the UPE functions as an RR client to receive specific routes reflected by the SPE functioning as an RR. This mechanism facilitates route management and traffic control.

**Figure 1** EVPN L3VPNv6 H-VPN over MPLS networking![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001225120653.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Deploy an IGP between the UPE and SPE and between the SPE and NPE. In this example, deploy OSPF between the UPE and SPE and IS-IS between the SPE and NPE.
2. Configure MPLS LDP on the UPE, SPE, and NPE.
3. Create a VPN instance on the UPE and NPE.
4. Bind access-side interfaces to VPN instances on the UPE and NPE.
5. Deploy BGP EVPN between the UPE and SPE and between the SPE and NPE.
6. On the SPE, specify the UPE as an RR client, and configure the SPE to use its own address as the next hop of BGP EVPN routes to be advertised to the peer.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the UPE, SPE, and NPE: 1.1.1.1, 2.2.2.2, and 3.3.3.3
* VPN instance name (vpn1) and RD (100:1)
* VPN targets 2:2 for route import and export by the VPN instance

#### Procedure

1. Configure IP addresses, including loopback interface addresses, on the UPE, SPE, and NPE.
   
   
   
   For details about how to configure interface IP addresses and masks, see [Configuration Files](#EN-US_TASK_0172370687__dc_vrp_evpn_cfg_008601) in this section.
2. Deploy an IGP between the UPE and SPE and between the SPE and NPE. In this example, deploy OSPF between the UPE and SPE and IS-IS between the SPE and NPE.
   
   
   
   For details, see [Configuration Files](#EN-US_TASK_0172370687__dc_vrp_evpn_cfg_008601) in this section.
3. Configure MPLS LDP on the UPE, SPE, and NPE.
   
   
   
   For details, see [Configuration Files](#EN-US_TASK_0172370687__dc_vrp_evpn_cfg_008601) in this section.
4. Create a VPN instance on the UPE and NPE.
   
   
   
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
   [*NPE-vpn-instance-vpn1-af-ipv6] vpn-target 2:2 both evpn
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv6] evpn mpls routing-enable
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
6. Deploy BGP EVPN between the UPE and SPE and between the SPE and NPE.
   
   
   
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
   [*SPE-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*SPE-bgp] peer 3.3.3.3 connect-interface LoopBack1
   ```
   ```
   [*SPE-bgp] l2vpn-family evpn
   ```
   ```
   [*SPE-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*SPE-bgp-af-evpn] peer 3.3.3.3 enable
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
   [*NPE-bgp] l2vpn-family evpn
   ```
   ```
   [*NPE-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*NPE-bgp-af-evpn] quit
   ```
   ```
   [*NPE-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*NPE-bgp-6-vpn1] advertise l2vpn evpn
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
7. On the SPE, specify the UPE as an RR client, and configure the SPE to use its own IP address as the next hop of BGP EVPN routes to be advertised to the peer.
   
   
   
   # Configure the SPE.
   
   ```
   [~SPE] bgp 100
   ```
   ```
   [*SPE-bgp] l2vpn-family evpn
   ```
   ```
   [*SPE-bgp-af-evpn] peer 1.1.1.1 reflect-client
   ```
   ```
   [*SPE-bgp-af-evpn] peer 1.1.1.1 next-hop-local
   ```
   ```
   [*SPE-bgp-af-evpn] peer 3.3.3.3 reflect-client
   ```
   ```
   [*SPE-bgp-af-evpn] peer 3.3.3.3 next-hop-local
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
8. Verify the configuration.
   
   
   
   Run the **display bgp evpn all routing-table** command on the NPE and UPE. The command output shows EVPN routes received from the remote end. The following example uses the command output on the NPE.
   
   ```
   [~NPE] display bgp evpn all routing-table
   ```
   ```
    Local AS number : 100
   
    BGP Local router ID is 10.2.1.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
    
    EVPN address family:
    Number of Ip Prefix Routes: 2
    Route Distinguisher: 100:1
          Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
    *>i   0:[2001:DB8:20::]:64                                   2.2.2.2
    *>    0:[2001:DB8:30::]:64                                   0.0.0.0
       
   
   ```
   
   Run the **display ipv6 routing-table vpn-instance vpn1** command on the NPE and UPE. The command output shows VPN routes received from the remote end. The following example uses the command output on the NPE.
   
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
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 1.1.1.1 next-hop-local
    peer 3.3.3.3 enable
    peer 3.3.3.3 reflect-client
    peer 3.3.3.3 next-hop-local
  #               
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
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
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 2:2 import-extcommunity evpn
    evpn mpls routing-enable
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
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:30::1/64
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   isis enable 1
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
   isis enable 1
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
  return
  ```