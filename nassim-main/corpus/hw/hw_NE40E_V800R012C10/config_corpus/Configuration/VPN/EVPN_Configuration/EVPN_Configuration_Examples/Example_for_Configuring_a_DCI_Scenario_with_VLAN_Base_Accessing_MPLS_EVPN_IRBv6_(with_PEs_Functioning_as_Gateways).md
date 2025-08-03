Example for Configuring a DCI Scenario with VLAN Base Accessing MPLS EVPN IRBv6 (with PEs Functioning as Gateways)
==================================================================================================================

Underlay VLAN accessing DCI uses different cloud management platforms, and Ethernet sub-interfaces are associated with VLANs for access to the DCI backbone network. DCI-PEs and DC GWs are integrated to form DCI-PE-GWs. BGP EVPN is deployed between DCI-PE-GWs to transmit IRBv6 routes, ensuring service communication.

#### Networking Requirements

A device functions as both a DC GW and a DCI-PE and directly connects to a DC device. On the network shown in [Figure 1](#EN-US_TASK_0172370690__fig_dc_vrp_dci_cfg_003201), a DCI-PE-GW functions as both a DC GW and a DCI-PE. A DCI-PE-GW connects to the P on the DCI backbone network on one side and directly connects to a DC device on the other side. A VXLAN tunnel is established in each DC to implement intra-DC VM communication. To implement inter-DC VM communication, create L3VPN and EVPN instances on DCI-PE-GWs and deploy BGP EVPN between the DCI-PE-GWs on the DCI backbone network.

**Figure 1** Configuring a DCI scenario with VLAN base accessing MPLS EVPN IRBv6 (PEs also functioning as gateways)![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and sub-interface1.1 represent GE0/1/0, GE0/2/0, and GE0/1/0.1, respectively.


  
![](images/fig_dc_vrp_dci_cfg_003201.png)  

**Table 1** Interface IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| DCI-PE1-GW1 | GigabitEthernet 0/1/0.1 | - |
| GigabitEthernet 0/2/0 | 192.168.1.1/24 |
| LoopBack1 | 1.1.1.1/32 |
| P | GigabitEthernet 0/1/0 | 192.168.1.2/24 |
| GigabitEthernet 0/2/0 | 192.168.10.1/24 |
| LoopBack1 | 2.2.2.2/32 |
| DCI-PE2-GW2 | GigabitEthernet 0/1/0.1 | - |
| GigabitEthernet 0/2/0 | 192.168.10.2/24 |
| LoopBack1 | 3.3.3.3/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure OSPF on the DCI backbone network to implement communication between DCI-PE-GWs.
2. Configure an MPLS TE tunnel on the DCI backbone network.
3. Configure VPN instances on DCI-PE-GWs and apply tunnel policies to these VPN instances.
4. Create VBDIF interfaces and bind these interfaces to VPN instances on DCI-PE-GWs.
5. Configure DCI-PE-GWs to advertise IPv6 prefix routes.
6. Configure EVPN instances on DCI-PE-GWs, establish a BGP EVPN peer relationship between the DCI-PE-GWs, and advertise IRBv6 routes.
7. Configure a source address on each DCI-PE-GW.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the DCI-PE-GWs and P
* VPN instance RD
* VPN targets used for route import and export by the VPN instance
* EVPN instance RD
* VPN targets used for route import and export by the EVPN instance

#### Procedure

1. Configure interface IP addresses, including loopback interface addresses, on each node.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370690__dc_vrp_dci_cfg_0012_section).
2. Configure an IGP on the DCI backbone network. OSPF is used in this example.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370690__dc_vrp_dci_cfg_0012_section).
3. Configure an MPLS TE tunnel on the DCI backbone network.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370690__dc_vrp_dci_cfg_0012_section).
4. Configure VPN instances on DCI-PE-GWs and apply tunnel policies to these VPN instances.
   
   
   
   # Configure DCI-PE1-GW1.
   
   ```
   [~DCI-PE1-GW1] tunnel-policy te-lsp1
   ```
   ```
   [*DCI-PE1-GW1-tunnel-policy-te-lsp1] tunnel select-seq cr-lsp load-balance-number 1
   ```
   ```
   [*DCI-PE1-GW1-tunnel-policy-te-lsp1] quit
   ```
   ```
   [*DCI-PE1-GW1] ip vpn-instance vpn1
   ```
   ```
   [*DCI-PE1-GW1-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*DCI-PE1-GW1-vpn-instance-vpn1-af-ipv6] route-distinguisher 11:11
   ```
   ```
   [*DCI-PE1-GW1-vpn-instance-vpn1-af-ipv6] tnl-policy te-lsp1 evpn
   ```
   ```
   [*DCI-PE1-GW1-vpn-instance-vpn1-af-ipv6] vpn-target 11:1 both evpn
   ```
   ```
   [*DCI-PE1-GW1-vpn-instance-vpn1-af-ipv6] evpn mpls routing-enable
   ```
   ```
   [*DCI-PE1-GW1-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*DCI-PE1-GW1-vpn-instance-vpn1] quit
   ```
   ```
   [*DCI-PE1-GW1] commit
   ```
   
   # Configure DCI-PE2-GW2.
   
   ```
   [~DCI-PE2-GW2] tunnel-policy te-lsp1
   ```
   ```
   [*DCI-PE2-GW2-tunnel-policy-te-lsp1] tunnel select-seq cr-lsp load-balance-number 1
   ```
   ```
   [*DCI-PE2-GW2-tunnel-policy-te-lsp1] quit
   ```
   ```
   [*DCI-PE2-GW2] ip vpn-instance vpn1
   ```
   ```
   [*DCI-PE2-GW2-vpn-instance-vpn1] ipv6-family
   ```
   ```
   [*DCI-PE2-GW2-vpn-instance-vpn1-af-ipv6] route-distinguisher 11:11
   ```
   ```
   [*DCI-PE2-GW2-vpn-instance-vpn1-af-ipv6] tnl-policy te-lsp1 evpn
   ```
   ```
   [*DCI-PE2-GW2-vpn-instance-vpn1-af-ipv6] vpn-target 11:1 both evpn
   ```
   ```
   [*DCI-PE2-GW2-vpn-instance-vpn1-af-ipv6] evpn mpls routing-enable
   ```
   ```
   [*DCI-PE2-GW2-vpn-instance-vpn1-af-ipv6] quit
   ```
   ```
   [*DCI-PE2-GW2-vpn-instance-vpn1] quit
   ```
   ```
   [*DCI-PE2-GW2] commit
   ```
5. Configure DCI-PE-GWs to advertise IP prefix routes.
   
   
   
   # Configure DCI-PE1-GW1.
   
   ```
   [~DCI-PE1-GW1] bgp 100
   ```
   ```
   [*DCI-PE1-GW1-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*DCI-PE1-GW1-bgp-6-vpn1] import-route direct
   ```
   ```
   [*DCI-PE1-GW1-bgp-6-vpn1] advertise l2vpn evpn
   ```
   ```
   [*DCI-PE1-GW1-bgp-6-vpn1] quit
   ```
   ```
   [*DCI-PE1-GW1] commit
   ```
   
   # Configure DCI-PE2-GW2.
   
   ```
   [~DCI-PE2-GW2] bgp 100
   ```
   ```
   [*DCI-PE2-GW2-bgp] ipv6-family vpn-instance vpn1
   ```
   ```
   [*DCI-PE2-GW2-bgp-6-vpn1] import-route direct
   ```
   ```
   [*DCI-PE2-GW2-bgp-6-vpn1] advertise l2vpn evpn
   ```
   ```
   [*DCI-PE2-GW2-bgp-6-vpn1] quit
   ```
   ```
   [*DCI-PE2-GW2] commit
   ```
6. Configure EVPN instances on DCI-PE-GWs, establish a BGP EVPN peer relationship between the DCI-PE-GWs, and advertise IRBv6 routes.
   
   
   
   # Configure DCI-PE1-GW1.
   
   ```
   [~DCI-PE1-GW1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*DCI-PE1-GW1-evpn-instance-evrf1] route-distinguisher 10:1
   ```
   ```
   [*DCI-PE1-GW1-evpn-instance-evrf1] vpn-target 11:1
   ```
   ```
   [*DCI-PE1-GW1-evpn-instance-evrf1] tnl-policy te-lsp1
   ```
   ```
   [*DCI-PE1-GW1-evpn-instance-evrf1] quit
   ```
   ```
   [*DCI-PE1-GW1] bridge-domain 10
   ```
   ```
   [*DCI-PE1-GW1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*DCI-PE1-GW1-bd10] quit
   ```
   ```
   [*DCI-PE1-GW1] bgp 100
   ```
   ```
   [*DCI-PE1-GW1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*DCI-PE1-GW1-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*DCI-PE1-GW1-bgp] l2vpn-family evpn
   ```
   ```
   [*DCI-PE1-GW1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*DCI-PE1-GW1-bgp-af-evpn] peer 3.3.3.3 advertise irbv6
   ```
   ```
   [*DCI-PE1-GW1-bgp-af-evpn] quit
   ```
   ```
   [*DCI-PE1-GW1-bgp] quit
   ```
   ```
   [*DCI-PE1-GW1] commit
   ```
   
   # Configure DCI-PE2-GW2.
   
   ```
   [~DCI-PE2-GW2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*DCI-PE2-GW2-evpn-instance-evrf1] route-distinguisher 10:1
   ```
   ```
   [*DCI-PE2-GW2-evpn-instance-evrf1] vpn-target 11:1
   ```
   ```
   [*DCI-PE2-GW1-evpn-instance-evrf1] tnl-policy te-lsp1
   ```
   ```
   [*DCI-PE2-GW2-evpn-instance-evrf1] quit
   ```
   ```
   [*DCI-PE2-GW2] bridge-domain 10
   ```
   ```
   [*DCI-PE2-GW2-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*DCI-PE2-GW2-bd10] quit
   ```
   ```
   [*DCI-PE2-GW2] bgp 100
   ```
   ```
   [*DCI-PE2-GW2-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*DCI-PE2-GW2-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*DCI-PE2-GW2-bgp] l2vpn-family evpn
   ```
   ```
   [*DCI-PE2-GW2-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*DCI-PE2-GW2-bgp-af-evpn] peer 1.1.1.1 advertise irbv6
   ```
   ```
   [*DCI-PE2-GW2-bgp-af-evpn] quit
   ```
   ```
   [*DCI-PE2-GW2-bgp] quit
   ```
   ```
   [*DCI-PE2-GW2] commit
   ```
7. Create VBDIF interfaces on DCI-PE-GWs.
   
   
   
   # Configure DCI-PE1-GW1.
   
   ```
   [~DCI-PE1-GW1] interface gigabitethernet 0/1/0.1 mode l2
   ```
   ```
   [*DCI-PE1-GW1-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*DCI-PE1-GW1-GigabitEthernet0/1/0.1] rewrite pop single
   ```
   ```
   [*DCI-PE1-GW1-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [*DCI-PE1-GW1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*DCI-PE1-GW1] interface Vbdif10
   ```
   ```
   [*DCI-PE1-GW1-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*DCI-PE1-GW1-Vbdif10] ipv6 enable
   ```
   ```
   [*DCI-PE1-GW1-Vbdif10] ipv6 address 2001:DB8:10::1 64
   ```
   ```
   [*DCI-PE1-GW1-Vbdif10] ipv6 nd collect host enable
   ```
   ```
   [*DCI-PE1-GW1-Vbdif10] quit
   ```
   ```
   [*DCI-PE1-GW1] commit
   ```
   
   # Configure DCI-PE2-GW2.
   
   ```
   [~DCI-PE2-GW2] interface gigabitethernet 0/1/0.1 mode l2
   ```
   ```
   [*DCI-PE2-GW2-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*DCI-PE2-GW2-GigabitEthernet0/1/0.1] rewrite pop single
   ```
   ```
   [*DCI-PE2-GW2-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [*DCI-PE2-GW2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*DCI-PE2-GW2] interface Vbdif10
   ```
   ```
   [*DCI-PE2-GW2-Vbdif10] ip binding vpn-instance vpn1
   ```
   ```
   [*DCI-PE1-GW2-Vbdif10] ipv6 enable
   ```
   ```
   [*DCI-PE1-GW2-Vbdif10] ipv6 address 2001:DB8:20::1 64
   ```
   ```
   [*DCI-PE2-GW2-Vbdif10] ipv6 nd collect host enable
   ```
   ```
   [*DCI-PE2-GW2-Vbdif10] quit
   ```
   ```
   [*DCI-PE2-GW2] commit
   ```
8. Configure a source address on each DCI-PE-GW.
   
   
   
   # Configure DCI-PE-GW1.
   
   ```
   [~DCI-PE-GW1] evpn source-address 1.1.1.1
   ```
   ```
   [*DCI-PE-GW1] commit
   ```
   
   # Configure DCI-PE-GW2.
   
   ```
   [~DCI-PE-GW2] evpn source-address 3.3.3.3
   ```
   ```
   [*DCI-PE-GW2] commit
   ```
9. Verify the configuration.
   
   
   
   Run the **display bgp evpn all routing-table** command on a DCI-PE-GW. The command output shows that the DCI-PE-GW has received EVPN IRBv6 routes from the remote DCI-PE-GW. The following example uses the command output on DCI-PE1-GW1.
   
   ```
   [~DCI-PE1-GW1] display bgp evpn all routing-table
   ```
   ```
    Local AS number : 100
   
    BGP Local router ID is 192.168.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
    
    EVPN address family:
    Number of Mac Routes: 4
    Route Distinguisher: 10:1
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>i   0:48:00e0-fc12-3456:0:0.0.0.0                          3.3.3.3
    *>i   0:48:00e0-fc12-3456:32:20.1.1.1                        3.3.3.3
    *>    0:48:00e0-fc12-7890:0:0.0.0.0                          0.0.0.0
    *>    0:48:00e0-fc12-7890:32:10.1.1.1                        0.0.0.0
       
       
   
    EVPN-Instance evrf1:
    Number of Mac Routes: 4
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>i   0:48:00e0-fc12-3456:0:0.0.0.0                          3.3.3.3
    *>i   0:48:00e0-fc12-3456:32:20.1.1.1                        3.3.3.3
    *>    0:48:00e0-fc12-7890:0:0.0.0.0                          0.0.0.0
    *>    0:48:00e0-fc12-7890:32:10.1.1.1                        0.0.0.0
    
    EVPN address family:
    Number of Inclusive Multicast Routes: 2
    Route Distinguisher: 10:1
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:1.1.1.1                                           127.0.0.1
    *>i   0:32:3.3.3.3                                           3.3.3.3
       
   
    EVPN-Instance evrf1:
    Number of Inclusive Multicast Routes: 2
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:1.1.1.1                                           127.0.0.1
    *>i   0:32:3.3.3.3                                           3.3.3.3
    
    EVPN address family:
    Number of Ip Prefix Routes: 2
    Route Distinguisher: 11:11
          Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
    *>    0:10.1.1.0:24                                          0.0.0.0
    *>i   0:10.2.1.0:24                                          3.3.3.3
       
   
   ```
   
   Run the **display ipv6 routing-table vpn-instance** command on a DCI-PE-GW. The command output shows that the DCI-PE-GW has received VPN routes from the remote DCI-PE-GW. The following example uses the command output on DCI-PE1-GW1.
   
   ```
   [~DCI-PE1-GW1] display ipv6 routing-table vpn-instance vpn1
   ```
   ```
   Routing Table : vpn1
            Destinations : 4        Routes : 4         
   
   Destination  : 2001:DB8:10::                           PrefixLength : 64
   NextHop      : 2001:DB8:10::1                          Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : Vbdif10                                 Flags        : D
   
   Destination  : 2001:DB8:10::1                          PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : Vbdif10                                 Flags        : D
   
   Destination  : 2001:DB8:20::                           PrefixLength : 64
   NextHop      : ::FFFF:3.3.3.3                          Preference   : 255
   Cost         : 0                                       Protocol     : IBGP
   RelayNextHop : ::FFFF:0.0.0.0                          TunnelID     : 0x000000000300000001
   Interface    : Tunnel1                                 Flags        : RD
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : DB
   ```

#### Configuration Files

* DCI-PE1-GW1 configuration file
  
  ```
  #
  sysname DCI-PE1-GW1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   tnl-policy te-lsp1
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 11:11
    apply-label per-instance
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
    tnl-policy te-lsp1 evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:10::1/64
   ipv6 nd collect host enable
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.1.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 3.3.3.3
   mpls te tunnel-id 100
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   ipv6-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise irbv6
  #               
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 192.168.1.0 0.0.0.255
    mpls-te enable
  #
  tunnel-policy te-lsp1
   tunnel select-seq cr-lsp load-balance-number 1
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* P configuration file
  
  ```
  #
  sysname P
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ip address 192.168.1.2 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.10.1 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 192.168.1.0 0.0.0.255
    network 192.168.10.0 0.0.0.255
    mpls-te enable
  #
  return
  ```
* DCI-PE2-GW2 configuration file
  
  ```
  #
  sysname DCI-PE2-GW2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   tnl-policy te-lsp1
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  ip vpn-instance vpn1
   ipv6-family
    route-distinguisher 11:11
    apply-label per-instance
    vpn-target 11:1 export-extcommunity evpn
    vpn-target 11:1 import-extcommunity evpn
    tnl-policy te-lsp1 evpn
    evpn mpls routing-enable
  #
  mpls lsr-id 3.3.3.3
  #
  mpls
   mpls te
   mpls rsvp-te
   mpls te cspf
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  interface Vbdif10
   ip binding vpn-instance vpn1
   ipv6 enable
   ipv6 address 2001:DB8:20::1/64
   ipv6 nd collect host enable
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 192.168.10.2 255.255.255.0
   mpls
   mpls te
   mpls rsvp-te
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  interface Tunnel1
   ip address unnumbered interface LoopBack1
   tunnel-protocol mpls te
   destination 1.1.1.1
   mpls te tunnel-id 100
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
   #
   ipv6-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 advertise irbv6
  #               
  ospf 1
   opaque-capability enable
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 192.168.10.0 0.0.0.255
    mpls-te enable
  #
  tunnel-policy te-lsp1
   tunnel select-seq cr-lsp load-balance-number 1
  #
  evpn source-address 3.3.3.3
  #
  return
  ```
* Device1 configuration file
  
  See the configuration file of a DC device.
* Device2 configuration file
  
  See the configuration file of a DC device.