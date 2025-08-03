Example for Configuring Interworking Between a Common L3VPN and an EVPN L3VPN over MPLS
=======================================================================================

This section provides an example for configuring interworking between a common L3VPN and an EVPN L3VPN to implement communication between the two networks.

#### Networking Requirements

Many metro networks deployed with L3VPN are evolving towards EVPN. If a metro network involves a large number of devices, E2E evolution may not be completed at one time. If this is the case, co-existence of L3VPN and EVPN arises. On the network shown in [Figure 1](#EN-US_TASK_0172370655__fig6836194111119), an L3VPN is deployed between the UPE and NPE1, and an EVPN is deployed between NPE1 and NPE2. To allow communication between the L3VPN and EVPN, configure the border device NPE1 between the two networks.

**Figure 1** Configuring interworking between common L3VPN and EVPN L3VPN over MPLS![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001224889809.png)  

**Table 1** Interface IP addresses
| Device | Interface | IP Address |
| --- | --- | --- |
| UPE | GigabitEthernet 0/1/0 | 10.1.1.1/24 |
| GigabitEthernet 0/2/0 | 192.168.20.1/24 |
| LoopBack1 | 1.1.1.1/32 |
| NPE1 | GigabitEthernet 0/1/0 | 10.1.1.2/24 |
| GigabitEthernet 0/2/0 | 10.2.1.1/24 |
| LoopBack1 | 2.2.2.2/32 |
| NPE2 | GigabitEthernet 0/1/0 | 10.2.1.2/24 |
| GigabitEthernet 0/2/0 | 192.168.30.1/24 |
| LoopBack1 | 3.3.3.3/32 |



#### Configuration Roadmap

The configuration roadmap is as follows:

1. Deploy IGPs on the UPE, NPE1, and NPE2. In this example, OSPF runs between the UPE and NPE1, and IS-IS runs between NPE1 and NPE2.
2. Configure MPLS LDP on the UPE, NPE1, and NPE2.
3. Configure L3VPN instances on the UPE and NPE1, and establish a BGP VPNv4 connection between them.
4. Establish a BGP EVPN connection between NPE1 and NPE2.
5. Configure an L3VPN instance and binding it to a physical interface on NPE2 to access Layer 3 services.
6. Enable NPE1 to re-originate routes.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the UPE and NPEs
* VPN instance RD
* VPN targets used for route import and export by the VPN instance

#### Procedure

1. Configure IP addresses, including loopback interface addresses, on the UPE, NPE1, and NPE2.
   
   
   
   For details about how to configure interface IP addresses and masks, see [Configuration Files](#EN-US_TASK_0172370655__dc_vrp_evpn_cfg_007001) in this section.
2. Deploy IGPs on the UPE, NPE1, and NPE2. In this example, OSPF runs between the UPE and NPE1, and IS-IS runs between NPE1 and NPE2.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172370655__dc_vrp_evpn_cfg_007001) in this section.
3. Configure MPLS LDP on the UPE, NPE1, and NPE2.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172370655__dc_vrp_evpn_cfg_007001) in this section.
4. Configure L3VPN instances on the UPE and NPE1, and establish a BGP VPNv4 connection between them.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] ip vpn-instance vpn1
   ```
   ```
   [*UPE-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv4] route-distinguisher 10:1
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*UPE-vpn-instance-vpn1] quit
   ```
   ```
   [*UPE] interface GigabitEthernet 0/2/0
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] ip address 192.168.20.1 255.255.255.0
   ```
   ```
   [*UPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*UPE] bgp 100
   ```
   ```
   [*UPE-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*UPE-bgp] peer 2.2.2.2 connect-interface LoopBack1
   ```
   ```
   [*UPE-bgp] ipv4-family vpnv4
   ```
   ```
   [*UPE-bgp-af-vpnv4] peer 2.2.2.2 enable
   ```
   ```
   [*UPE-bgp-af-vpnv4] quit
   ```
   ```
   [*UPE-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*UPE-bgp-vpn1] import-route direct
   ```
   ```
   [*UPE-bgp-vpn1] quit
   ```
   ```
   [*UPE] commit
   ```
   
   # Configure NPE1.
   
   ```
   [~NPE1] ip vpn-instance vpn1
   ```
   ```
   [*NPE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*NPE1-vpn-instance-vpn1-af-ipv4] route-distinguisher 10:2
   ```
   ```
   [*NPE1-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both
   ```
   ```
   [*NPE1-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*NPE1-vpn-instance-vpn1] quit
   ```
   ```
   [*NPE1] bgp 100
   ```
   ```
   [*NPE1-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*NPE1-bgp] peer 1.1.1.1 connect-interface LoopBack1
   ```
   ```
   [*NPE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*NPE1-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*NPE1-bgp-af-vpnv4] quit
   ```
   ```
   [*NPE1] commit
   ```
5. Establish a BGP EVPN connection between NPE1 and NPE2.
   
   
   
   # Configure NPE1.
   
   ```
   [~NPE1] bgp 100
   ```
   ```
   [*NPE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*NPE1-bgp] peer 3.3.3.3 connect-interface LoopBack1
   ```
   ```
   [*NPE1-bgp] l2vpn-family evpn
   ```
   ```
   [*NPE1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*NPE1-bgp-af-evpn] quit
   ```
   ```
   [*NPE1-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*NPE1-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*NPE1] commit
   ```
   
   # Configure NPE2.
   
   ```
   [~NPE2] bgp 100
   ```
   ```
   [*NPE2-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*NPE2-bgp] peer 2.2.2.2 connect-interface LoopBack1
   ```
   ```
   [*NPE2-bgp] l2vpn-family evpn
   ```
   ```
   [*NPE2-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*NPE2-bgp-af-evpn] quit
   ```
   ```
   [*NPE2] commit
   ```
6. Configure an L3VPN instance and binding it to a physical interface on NPE2 to access Layer 3 services.
   
   
   ```
   [~NPE2] ip vpn-instance vpn1
   ```
   ```
   [*NPE2-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*NPE2-vpn-instance-vpn1-af-ipv4] route-distinguisher 20:2
   ```
   ```
   [*NPE2-vpn-instance-vpn1-af-ipv4] vpn-target 2:2 both evpn
   ```
   ```
   [*NPE2-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*NPE2-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*NPE2-vpn-instance-vpn1] quit
   ```
   ```
   [*NPE2] interface GigabitEthernet 0/2/0
   ```
   ```
   [*NPE2-GigabitEthernet0/2/0] ip binding vpn-instance vpn1
   ```
   ```
   [*NPE2-GigabitEthernet0/2/0] ip address 192.168.30.1 24
   ```
   ```
   [*NPE2-GigabitEthernet0/2/0] quit
   ```
   ```
   [*NPE2] bgp 100
   ```
   ```
   [*NPE2-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*NPE2-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*NPE2-bgp-vpn1] import-route direct
   ```
   ```
   [*NPE2-bgp-vpn1] quit
   ```
   ```
   [*NPE2-bgp] quit
   ```
   ```
   [*NPE2] commit
   ```
7. Enable NPE1 to re-originate routes.
   
   
   ```
   [~NPE1] ip vpn-instance vpn1
   ```
   ```
   [*NPE1-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*NPE1-vpn-instance-vpn1-af-ipv4] vpn-target 2:2 both evpn
   ```
   ```
   [*NPE1-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*NPE1-pn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*NPE1-vpn-instance-vpn1] quit
   ```
   ```
   [*NPE1] bgp 100
   ```
   ```
   [*NPE1-bgp] ipv4-family vpnv4
   ```
   ```
   [*NPE1-bgp-af-vpnv4] peer 1.1.1.1 reflect-client
   ```
   ```
   [*NPE1-bgp-af-vpnv4] peer 1.1.1.1 import reoriginate
   ```
   ```
   [*NPE1-bgp-af-vpnv4] peer 1.1.1.1 advertise route-reoriginated evpn mac-ip
   ```
   ```
   [*NPE1-bgp-af-vpnv4] peer 1.1.1.1 advertise route-reoriginated evpn ip
   ```
   ```
   [*NPE1-bgp-af-vpnv4] quit
   ```
   ```
   [*NPE1-bgp] l2vpn-family evpn
   ```
   ```
   [*NPE1-bgp-af-evpn] peer 3.3.3.3 advertise irb
   ```
   ```
   [*NPE1-bgp-af-evpn] peer 3.3.3.3 reflect-client
   ```
   ```
   [*NPE1-bgp-af-evpn] peer 3.3.3.3 import reoriginate
   ```
   ```
   [*NPE1-bgp-af-evpn] peer 3.3.3.3 advertise route-reoriginated vpnv4
   ```
   ```
   [*NPE1-bgp-af-evpn] quit
   ```
   ```
   [*NPE1-bgp] quit
   ```
   ```
   [*NPE1] commit
   ```
8. Verify the configuration.
   
   
   
   Run the **display bgp evpn all routing-table** command on NPE2. The command output shows EVPN routes received from the UPE.
   
   ```
   [~NPE2] display bgp evpn all routing-table
   ```
   ```
    Local AS number : 100
   
    BGP Local router ID is 3.3.3.3
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
   
    EVPN address family:
    Number of Ip Prefix Routes: 4
    Route Distinguisher: 10:1
          Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
    *>i   0:192.168.20.0:24                                   2.2.2.2
    Route Distinguisher: 10:2
          Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
    *>i   0:192.168.20.0:24                                   2.2.2.2
    *>    0:192.168.30.0:24                                      0.0.0.0
    *>    0:192.168.30.1:32                                      0.0.0.0
       
   ```
   
   Run the **display ip routing-table vpn-instance vpn1** command on NPE2. The command output shows VPN route information.
   
   ```
   [~NPE2] display ip routing-table vpn-instance vpn1
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : vpn1
            Destinations : 5        Routes : 5         
   
   Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
   
      192.168.20.0/24  IBGP    255  0             RD  2.2.2.2         GigabitEthernet0/1/0
      192.168.30.0/24  Direct  0    0             D   192.168.30.1    GigabitEthernet0/2/0
      192.168.30.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
    192.168.30.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
   255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
   ```

#### Configuration Files

* UPE configuration file
  
  ```
  #
  sysname UPE
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 10:1
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
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip binding vpn-instance vpn1
   ip address 192.168.20.1 255.255.255.0
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
    import-route direct
    peer 192.168.20.2 as-number 65410
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* NPE1 configuration file
  
  ```
  #
  sysname NPE1
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 10:2
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
   ipv4-family vpnv4
    policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 1.1.1.1 import reoriginate
    peer 1.1.1.1 advertise route-reoriginated evpn mac-ip
    peer 1.1.1.1 advertise route-reoriginated evpn ip
   #
   ipv4-family vpn-instance vpn1
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise irb
    peer 3.3.3.3 reflect-client
    peer 3.3.3.3 import reoriginate
    peer 3.3.3.3 advertise route-reoriginated vpnv4
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  return
  ```
* NPE2 configuration file
  
  ```
  #
  sysname NPE2
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 20:2
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
   ip address 192.168.30.1 255.255.255.0
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
   ipv4-family vpn-instance vpn1
    import-route direct
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 2.2.2.2 advertise irb
  #
  return
  ```