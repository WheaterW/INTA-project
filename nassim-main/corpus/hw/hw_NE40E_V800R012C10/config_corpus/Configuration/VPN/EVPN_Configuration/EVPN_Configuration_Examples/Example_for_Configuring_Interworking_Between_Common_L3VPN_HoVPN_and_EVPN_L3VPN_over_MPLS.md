Example for Configuring Interworking Between Common L3VPN HoVPN and EVPN L3VPN over MPLS
========================================================================================

This section provides an example for configuring interworking between L3VPN HoVPN and EVPN L3VPN to deliver network connectivity.

#### Networking Requirements

An IP bearer network generally uses L2VPN and L3VPN (HVPN) to carry Layer 2 and Layer 3 services, respectively. The protocols used in this scenario are complex. EVPN, in contrast, can carry both Layer 2 and Layer 3 services. To simplify service bearer protocols, many IP bearer networks will evolve to EVPN. Among them, L3VPN HVPN that carries Layer 3 services needs to evolve to EVPN L3VPN HVPN. During evolution, if a lot of devices are deployed on the network, end-to-end evolution may not be implemented at a time. As a result, co-existence of the L3VPN and EVPN L3VPN occurs. On the network shown in [Figure 1](#EN-US_TASK_0172370666__fig399810401128), the UPE and SPE are connected at the access layer, and the SPE and NPE are connected at the aggregation layer. Independent IGPs are deployed at the access and aggregation layers to ensure communication at different layers. An L3VPN HoVPN is deployed between the UPE and SPE, and an EVPN L3VPN is deployed between the SPE and NPE. The SPE advertises only default L3VPN routes to the UPE. After receiving specific routes (L3VPN routes) from the UPE, the SPE encapsulates these routes into EVPN routes and advertises them to the NPE.

**Figure 1** Configuring interworking between common L3VPN HoVPN and EVPN L3VPN over MPLS![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 and 2 in this example represent GE0/1/0 and GE0/2/0, respectively.


  
![](figure/en-us_image_0000001224808243.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Deploy an IGP between the UPE and SPE and between the SPE and NPE. In this example, deploy OSPF between the UPE and SPE and IS-IS between the SPE and NPE.
2. Configure MPLS LDP on the UPE, SPE, and NPE.
3. Create a VPN instance on the UPE, SPE, and NPE.
4. Bind access-side interfaces to VPN instances on the UPE and NPE.
5. Configure a default static VPN route on the SPE.
6. Configure a route-policy on the NPE to prevent the NPE from receiving default routes.
7. Configure a BGP EVPN peer relationship between the SPE and NPE.
8. Configure a BGP VPNv4 peer relationship between the UPE and SPE, specify the UPE as the lower-level PE of the SPE, and configure the UPE to import the default VPN route.
9. Configure route regeneration on the SPE.

#### Data Preparation

To complete the configuration, you need the following data:

* MPLS LSR IDs of the UPE, SPE, and NPE: 1.1.1.1, 2.2.2.2, and 3.3.3.3
* VPN instance name (vpn1) and RD (100:1)
* VPN targets 1:1 and 2:2 for route import and export by the VPN instance

#### Procedure

1. Configure IP addresses, including loopback interface addresses, on the UPE, SPE, and NPE.
   
   
   
   For details about how to configure interface IP addresses and masks, see [Configuration Files](#EN-US_TASK_0172370666__dc_vrp_evpn_cfg_008701) in this section.
2. Deploy an IGP between the UPE and SPE and between the SPE and NPE. In this example, deploy OSPF between the UPE and SPE and IS-IS between the SPE and NPE.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172370666__dc_vrp_evpn_cfg_008701) in this section.
3. Configure MPLS LDP on the UPE, SPE, and NPE.
   
   
   
   For configuration details, see [Configuration Files](#EN-US_TASK_0172370666__dc_vrp_evpn_cfg_008701) in this section.
4. Create a VPN instance on the UPE, SPE, and NPE.
   
   
   
   # Configure the UPE.
   
   ```
   [~UPE] ip vpn-instance vpn1
   ```
   ```
   [*UPE-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*UPE-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
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
   [*UPE] commit
   ```
   
   # Configure the SPE.
   
   ```
   [~SPE] ip vpn-instance vpn1
   ```
   ```
   [*SPE-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv4] vpn-target 2:2 both evpn
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*SPE-vpn-instance-vpn1-af-ipv4] quit
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
   [*NPE-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] vpn-target 1:1 both
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] vpn-target 2:2 both evpn
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] evpn mpls routing-enable
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] quit
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
   [*UPE-GigabitEthernet0/2/0] ip address 192.168.20.1 255.255.255.0
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
   [*NPE-GigabitEthernet0/2/0] ip address 192.168.30.1 255.255.255.0
   ```
   ```
   [*NPE-GigabitEthernet0/2/0] quit
   ```
   ```
   [*NPE] commit
   ```
6. Configure a default static route on the SPE.
   
   
   ```
   [~SPE] ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 33.33.33.33
   ```
   ```
   [*SPE] commit
   ```
7. Configure a route-policy on the NPE to prevent the NPE from receiving default routes.
   
   
   ```
   [~NPE] ip ip-prefix default index 10 permit 0.0.0.0 0
   ```
   ```
   [*NPE] route-policy SPE deny node 10
   ```
   ```
   [*NPE-route-policy] if-match ip-prefix default
   ```
   ```
   [*NPE-route-policy] quit
   ```
   ```
   [*NPE] route-policy SPE permit node 20
   ```
   ```
   [*NPE-route-policy] quit
   ```
   ```
   [*NPE] ip vpn-instance vpn1
   ```
   ```
   [*NPE-vpn-instance-vpn1] ipv4-family
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] import route-policy SPE evpn
   ```
   ```
   [*NPE-vpn-instance-vpn1-af-ipv4] quit
   ```
   ```
   [*NPE-vpn-instance-vpn1] quit
   ```
   ```
   [*NPE] commit
   ```
8. Configure a BGP EVPN peer relationship between the SPE and NPE.
   
   
   
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
   [*SPE-bgp] l2vpn-family evpn
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
   [*NPE-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*NPE-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*NPE-bgp-vpn1] import-route direct
   ```
   ```
   [*NPE-bgp-vpn1] quit
   ```
   ```
   [*NPE-bgp] quit
   ```
   ```
   [*NPE] commit
   ```
9. Configure a BGP VPNv4 peer relationship between the UPE and SPE, specify the UPE as a lower-level PE of the SPE, and configure the import of default VPN routes.
   
   
   
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
   [*SPE-bgp] ipv4-family vpnv4
   ```
   ```
   [*SPE-bgp-af-vpnv4] peer 1.1.1.1 enable
   ```
   ```
   [*SPE-bgp-af-vpnv4] peer 1.1.1.1 upe
   ```
   ```
   [*SPE-bgp-af-vpnv4] quit
   ```
   ```
   [*SPE-bgp] ipv4-family vpn-instance vpn1
   ```
   ```
   [*SPE-bgp-vpn1] network 0.0.0.0 0
   ```
   ```
   [*SPE-bgp-vpn1] advertise l2vpn evpn
   ```
   ```
   [*SPE-bgp-vpn1] quit
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
    [*SPE-bgp] ipv4-family vpnv4
    ```
    ```
    [*SPE-bgp-af-vpnv4] peer 1.1.1.1 import reoriginate
    ```
    ```
    [*SPE-bgp-af-vpnv4] quit
    ```
    ```
    [*SPE-bgp] l2vpn-family evpn
    ```
    ```
    [*SPE-bgp-af-evpn] undo policy vpn-target
    ```
    ```
    [*SPE-bgp-af-evpn] peer 3.3.3.3 advertise route-reoriginated vpnv4
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
    
    
    
    Run the **display bgp evpn all routing-table** command on the NPE. The command output shows EVPN routes received from the UPE.
    
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
     Number of Ip Prefix Routes: 3
     Route Distinguisher: 100:1
           Network(EthTagId/IpPrefix/IpPrefixLen)                 NextHop
     *>i   0:0.0.0.0:0                                            2.2.2.2
     *>i   0:192.168.20.0:24                                      2.2.2.2
     *>    0:192.168.30.0:24                                      0.0.0.0
        
    
    ```
    
    Run the **display ip routing-table vpn-instance vpn1** command on the NPE. The command output shows VPN routes received from the UPE.
    
    ```
    [~NPE] display ip routing-table vpn-instance vpn1
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ```
    ```
    ------------------------------------------------------------------------------
    Routing Table : vpn1
             Destinations : 5        Routes : 5         
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
    
       192.168.20.0/24  IBGP    255  0             RD  2.2.2.2         GigabitEthernet0/1/0
       192.168.30.0/24  Direct  0    0             RD  192.168.30.1    GigabitEthernet0/2/0
       192.168.30.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
     192.168.30.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/2/0
    255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0
    ```
    
    Run the **display ip routing-table vpn-instance vpn1** command on the UPE. The command output shows default VPN route information.
    
    ```
    [~UPE] display ip routing-table vpn-instance vpn1
    ```
    ```
    Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
    ```
    ```
    ------------------------------------------------------------------------------
    Routing Table : vpn1
             Destinations : 5        Routes : 5         
    
    Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface
    
            0.0.0.0/0   IBGP    255  0             RD  2.2.2.2         GigabitEthernet0/1/0
       192.168.20.0/24  Direct  0    0             RD  192.168.20.1    GigabitEthernet0/1/0
       192.168.20.1/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0
     192.168.20.255/32  Direct  0    0             D   127.0.0.1       GigabitEthernet0/1/0
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
   ipv4-family
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
   ipv4-family vpnv4
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 upe
    peer 1.1.1.1 import reoriginate
   #
   ipv4-family vpn-instance vpn1
    network 0.0.0.0
    advertise l2vpn evpn
   #
   l2vpn-family evpn
    undo policy vpn-target
    peer 3.3.3.3 enable
    peer 3.3.3.3 advertise route-reoriginated vpnv4
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  ip route-static vpn-instance vpn1 0.0.0.0 0.0.0.0 33.33.33.33
  #
  return
  ```
* NPE configuration file
  
  ```
  #
  sysname NPE
  #
  ip vpn-instance vpn1
   ipv4-family
    route-distinguisher 100:1
    apply-label per-instance
    import route-policy SPE evpn
    vpn-target 1:1 export-extcommunity
    vpn-target 2:2 export-extcommunity evpn
    vpn-target 1:1 import-extcommunity
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
  interface LoopBack2
   ip binding vpn-instance vpn1
   ip address 33.33.33.33 255.255.255.0
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
    policy vpn-target
    peer 2.2.2.2 enable
  #
  ip ip-prefix default index 10 permit 0.0.0.0 0
  #
  route-policy SPE deny node 10
   if-match ip-prefix default
  #
  route-policy SPE permit node 20
  #
  return
  ```