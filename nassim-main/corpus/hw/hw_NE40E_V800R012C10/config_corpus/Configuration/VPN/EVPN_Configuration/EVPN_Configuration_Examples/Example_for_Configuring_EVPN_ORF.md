Example for Configuring EVPN ORF
================================

This section provides an example for configuring EVPN ORF. This configuration reduces the EVPN route receiving pressure of devices and saves network resources.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172370612__fig154036585511), to enable different sites to communicate with each other over the backbone network, EVPN is deployed on the network so that PEs can exchange EVPN routes to transmit service traffic. Two EVPN instances named evrf1 and evrf2 are configured on PE1. The EVPN instance named evrf1 is configured on PE2, and the EVPN instance named evrf2 is configured on PE3. To allow each PE to receive only desired routes and minimize system resource consumption in processing unwanted routes, EVPN ORF can be configured.

**Figure 1** Configuring EVPN ORF![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GigabitEthernet0/1/0, GigabitEthernet0/2/0, and GigabitEthernet0/3/0, respectively.


  
![](figure/en-us_image_0000001218056152.png)  


#### Precautions

When configuring EVPN ORF, note the following:

* For the same EVPN instance, the export VPN target list of a site shares VPN targets with the import VPN target lists of the other sites; the import VPN target list of a site shares VPN targets with the export VPN target lists of the other sites.
* Using the local loopback interface address of each PE as the source address is recommended.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Assign an IP address to each PE interface, including the loopback interfaces.
2. Configure a routing protocol on each PE to ensure Layer 3 communication. OSPF is used in this example.
3. Configure MPLS LDP on each PE.
4. Configure EVPN instances on the PEs and bind each EVPN instance to a BD.
5. Configure a source address on each PE.
6. Configure each PE's sub-interface that connects to a CE.
7. Configure an ESI for each PE interface that connects to a CE.
8. Configure the CEs and PEs to communicate.
9. Configure BGP EVPN peer relationships between the PEs and RR, and configure the PEs as RR clients.
10. Configure EVPN ORF on each device.

#### Data Preparation

To complete the configuration, you need the following data:

* PE1's EVPN instance names: evrf1 and evrf2; PE2's EVPN instance name: evrf1; PE3's EVPN instance name: evrf2
* evrf1's RD (100:1) and RT (1:1); evrf2's RD (100:2) and RT (2:2)

#### Procedure

1. Assign an IP address to each PE interface, including the loopback interfaces.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370612__file1).
2. Configure a routing protocol on each PE to ensure Layer 3 communication. OSPF is used in this example.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370612__file1).
3. Configure MPLS LDP on each PE.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370612__file1).
4. Configure EVPN instances on the PEs and bind each EVPN instance to a BD.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
   ```
   ```
   [*PE1] evpn vpn-instance evrf2 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf2] route-distinguisher 100:2
   ```
   ```
   [*PE1-evpn-instance-evrf2] vpn-target 2:2
   ```
   ```
   [*PE1-evpn-instance-evrf2] quit
   ```
   ```
   [*PE1] bridge-domain 10
   ```
   ```
   [*PE1-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE1-bd10] quit
   ```
   ```
   [*PE1] bridge-domain 20
   ```
   ```
   [*PE1-bd20] evpn binding vpn-instance evrf2
   ```
   ```
   [*PE1-bd20] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE2-evpn-instance-evrf1] route-distinguisher 100:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] vpn-target 1:1
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] bridge-domain 10
   ```
   ```
   [*PE2-bd10] evpn binding vpn-instance evrf1
   ```
   ```
   [*PE2-bd10] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evrf2 bd-mode
   ```
   ```
   [*PE3-evpn-instance-evrf2] route-distinguisher 100:2
   ```
   ```
   [*PE3-evpn-instance-evrf2] vpn-target 2:2
   ```
   ```
   [*PE3-evpn-instance-evrf2] quit
   ```
   ```
   [*PE3] bridge-domain 20
   ```
   ```
   [*PE3-bd20] evpn binding vpn-instance evrf2
   ```
   ```
   [*PE3-bd20] quit
   ```
   ```
   [*PE3] commit
   ```
5. Configure a source address on each PE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn source-address 1.1.1.1
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] evpn source-address 2.2.2.2
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn source-address 4.4.4.4
   ```
   ```
   [*PE3] commit
   ```
6. Configure each PE's sub-interface that connects to a CE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet0/1/0.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] rewrite pop single
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] interface gigabitethernet0/1/0.2 mode l2
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] encapsulation dot1q vid 20
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] rewrite pop single
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] bridge-domain 20
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.2] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet0/1/0.1 mode l2
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] rewrite pop single
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] interface gigabitethernet0/2/0.1 mode l2
   ```
   ```
   [*PE3-GigabitEthernet0/2/0.1] encapsulation dot1q vid 20
   ```
   ```
   [*PE3-GigabitEthernet0/2/0.1] rewrite pop single
   ```
   ```
   [*PE3-GigabitEthernet0/2/0.1] bridge-domain 20
   ```
   ```
   [*PE3-GigabitEthernet0/2/0.1] quit
   ```
   ```
   [*PE3] commit
   ```
7. Configure an ESI for each PE interface that connects to a CE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet0/1/0
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] esi 0000.1111.1111.1111.1111
   ```
   ```
   [*PE1-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE1] commit
   ```
   
   # Configure PE2.
   
   ```
   [~PE2] interface gigabitethernet0/1/0
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] esi 0000.1111.2222.2222.2222
   ```
   ```
   [*PE2-GigabitEthernet0/1/0] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] interface gigabitethernet0/2/0
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] esi 0000.1111.3333.3333.3333
   ```
   ```
   [*PE3-GigabitEthernet0/2/0] quit
   ```
   ```
   [*PE3] commit
   ```
8. Configure the CEs and PEs to communicate.
   
   
   
   # Configure CE1.
   
   ```
   [~CE1] interface gigabitethernet0/1/0.1 mode l2
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] rewrite pop single
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE1] interface gigabitethernet0/1/0.2 mode l2
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.2] encapsulation dot1q vid 20
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.2] rewrite pop single
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.2] bridge-domain 20
   ```
   ```
   [*CE1-GigabitEthernet0/1/0.2] quit
   ```
   ```
   [*CE1] commit
   ```
   
   # Configure CE2.
   
   ```
   [~CE2] interface gigabitethernet0/1/0.1 mode l2
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] rewrite pop single
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [*CE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE2] commit
   ```
   
   # Configure CE3.
   
   ```
   [~CE3] interface gigabitethernet0/1/0.1 mode l2
   ```
   ```
   [*CE3-GigabitEthernet0/1/0.1] encapsulation dot1q vid 20
   ```
   ```
   [*CE3-GigabitEthernet0/1/0.1] rewrite pop single
   ```
   ```
   [*CE3-GigabitEthernet0/1/0.1] bridge-domain 20
   ```
   ```
   [*CE3-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*CE3] commit
   ```
9. Configure BGP EVPN peer relationships between the PEs and RR, and configure the PEs as RR clients.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] bgp 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE1-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*PE1-bgp-af-evpn] quit
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
   [*PE2-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE2-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE2-bgp] l2vpn-family evpn
   ```
   ```
   [*PE2-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*PE2-bgp-af-evpn] quit
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
   [*PE3-bgp] peer 3.3.3.3 as-number 100
   ```
   ```
   [*PE3-bgp] peer 3.3.3.3 connect-interface loopback 1
   ```
   ```
   [*PE3-bgp] l2vpn-family evpn
   ```
   ```
   [*PE3-bgp-af-evpn] peer 3.3.3.3 enable
   ```
   ```
   [*PE3-bgp-af-evpn] quit
   ```
   ```
   [*PE3-bgp] quit
   ```
   ```
   [*PE3] commit
   ```
   
   # Configure the RR.
   
   ```
   [~RR] bgp 100
   ```
   ```
   [*RR-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*RR-bgp] peer 1.1.1.1 connect-interface loopback 1
   ```
   ```
   [*RR-bgp] peer 2.2.2.2 as-number 100
   ```
   ```
   [*RR-bgp] peer 2.2.2.2 connect-interface loopback 1
   ```
   ```
   [*RR-bgp] peer 4.4.4.4 as-number 100
   ```
   ```
   [*RR-bgp] peer 4.4.4.4 connect-interface loopback 1
   ```
   ```
   [*RR-bgp] l2vpn-family evpn
   ```
   ```
   [*RR-bgp-af-evpn] peer 1.1.1.1 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 1.1.1.1 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] peer 2.2.2.2 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 2.2.2.2 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] peer 4.4.4.4 enable
   ```
   ```
   [*RR-bgp-af-evpn] peer 4.4.4.4 reflect-client
   ```
   ```
   [*RR-bgp-af-evpn] quit
   ```
   ```
   [*RR-bgp] quit
   ```
   ```
   [*RR] commit
   ```
   
   # Run the **display bgp evpn peer** command on the RR. The command output shows that BGP peer relationships have been established between the PEs and RR and are in the **Established** state.
   
   ```
   [~RR] display bgp evpn peer
   ```
   ```
     
    BGP local router ID : 3.3.3.3
    Local AS number : 100
    Total number of peers : 3                 Peers in established state : 3
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     1.1.1.1         4         100       10       33     0 00:00:19 Established        6
     2.2.2.2         4         100        8       33     0 00:00:20 Established        4
     4.4.4.4         4         100        8       33     0 00:00:21 Established        4
   ```
   
   # Run the **display bgp evpn all routing-table peer 2.2.2.2 advertised-routes** and **display bgp evpn all routing-table peer 4.4.4.4 advertised-routes** commands on the RR to view routes advertised to PE2 and PE3.
   
   ```
   [~RR] display bgp evpn all routing-table peer 2.2.2.2 advertised-routes
   ```
   ```
    Local AS number : 100
   
    BGP Local router ID is 3.3.3.3
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
    
    EVPN address family:
    Number of A-D Routes: 7
    Route Distinguisher: 100:1
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.1111.1111.1111:0                         1.1.1.1
    *>i   0000.1111.2222.2222.2222:0                             2.2.2.2
    Route Distinguisher: 100:2
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.1111.1111.1111:0                         1.1.1.1
    *>i   0000.1111.3333.3333.3333:0                         4.4.4.4
    Route Distinguisher: 1.1.1.1:0
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.1111.1111.1111:4294967295               1.1.1.1
    Route Distinguisher: 2.2.2.2:0
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.2222.2222.2222:4294967295                    2.2.2.2
    Route Distinguisher: 4.4.4.4:0
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.3333.3333.3333:4294967295               4.4.4.4
    
    EVPN address family:
    Number of Inclusive Multicast Routes: 4
    Route Distinguisher: 100:1
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>i   0:32:1.1.1.1                                         1.1.1.1
    *>i   0:32:2.2.2.2                                           2.2.2.2
    Route Distinguisher: 100:2
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>i   0:32:1.1.1.1                                         1.1.1.1
    *>i   0:32:4.4.4.4                                         4.4.4.4
    
    EVPN address family:
    Number of ES Routes: 3
    Route Distinguisher: 1.1.1.1:0
          Network(ESI)                                           NextHop
    *>i   0000.1111.1111.1111.1111                           1.1.1.1
    Route Distinguisher: 2.2.2.2:0
          Network(ESI)                                           NextHop
    *>i   0000.1111.2222.2222.2222                               2.2.2.2
    Route Distinguisher: 4.4.4.4:0
          Network(ESI)                                           NextHop
    *>i   0000.1111.3333.3333.3333                           4.4.4.4
   ```
   ```
   [~RR] display bgp evpn all routing-table peer 4.4.4.4 advertised-routes
   ```
   ```
    Local AS number : 100
   
    BGP Local router ID is 3.3.3.3
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
    
    EVPN address family:
    Number of A-D Routes: 7
    Route Distinguisher: 100:1
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.1111.1111.1111:0                         1.1.1.1
    *>i   0000.1111.2222.2222.2222:0                         2.2.2.2
    Route Distinguisher: 100:2
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.1111.1111.1111:0                         1.1.1.1
    *>i   0000.1111.3333.3333.3333:0                             4.4.4.4
    Route Distinguisher: 1.1.1.1:0
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.1111.1111.1111:4294967295               1.1.1.1
    Route Distinguisher: 2.2.2.2:0
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.2222.2222.2222:4294967295               2.2.2.2
    Route Distinguisher: 4.4.4.4:0
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.1111.3333.3333.3333:4294967295                    4.4.4.4
    
    EVPN address family:
    Number of Inclusive Multicast Routes: 4
    Route Distinguisher: 100:1
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>i   0:32:1.1.1.1                                         1.1.1.1
    *>i   0:32:2.2.2.2                                         2.2.2.2
    Route Distinguisher: 100:2
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>i   0:32:1.1.1.1                                         1.1.1.1
    *>i   0:32:4.4.4.4                                           4.4.4.4
    
    EVPN address family:
    Number of ES Routes: 3
    Route Distinguisher: 1.1.1.1:0
          Network(ESI)                                           NextHop
    *>i   0000.1111.1111.1111.1111                           1.1.1.1
    Route Distinguisher: 2.2.2.2:0
          Network(ESI)                                           NextHop
    *>i   0000.1111.2222.2222.2222                           2.2.2.2
    Route Distinguisher: 4.4.4.4:0
          Network(ESI)                                           NextHop
    *>i   0000.1111.3333.3333.3333                               4.4.4.4
   ```
   
   The command output shows that the RR reflects all routes to PE2 and PE3. However, PE2 and PE3 do not have to receive all the routes. To resolve this problem, configure EVPN ORF on each device.
10. Configure EVPN ORF on each device.
    
    
    
    # Configure PE1.
    
    ```
    [~PE1] bgp 100
    ```
    ```
    [*PE1-bgp] ipv4-family vpn-target
    ```
    ```
    [*PE1-bgp-af-vpn-target] peer 3.3.3.3 enable
    ```
    ```
    [*PE1-bgp-af-vpn-target] quit
    ```
    ```
    [*PE1-bgp] l2vpn-family evpn
    ```
    ```
    [*PE1-bgp-af-evpn] vpn-orf enable
    ```
    ```
    [*PE1-bgp-af-evpn] quit
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
    [*PE2-bgp] ipv4-family vpn-target
    ```
    ```
    [*PE2-bgp-af-vpn-target] peer 3.3.3.3 enable
    ```
    ```
    [*PE2-bgp-af-vpn-target] quit
    ```
    ```
    [*PE2-bgp] l2vpn-family evpn
    ```
    ```
    [*PE2-bgp-af-evpn] vpn-orf enable
    ```
    ```
    [*PE2-bgp-af-evpn] quit
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
    [*PE3-bgp] ipv4-family vpn-target
    ```
    ```
    [*PE3-bgp-af-vpn-target] peer 3.3.3.3 enable
    ```
    ```
    [*PE3-bgp-af-vpn-target] quit
    ```
    ```
    [*PE3-bgp] l2vpn-family evpn
    ```
    ```
    [*PE3-bgp-af-evpn] vpn-orf enable
    ```
    ```
    [*PE3-bgp-af-evpn] quit
    ```
    ```
    [*PE3-bgp] quit
    ```
    ```
    [*PE3] commit
    ```
    
    # Configure the RR.
    
    ```
    [~RR] bgp 100
    ```
    ```
    [*RR-bgp] ipv4-family vpn-target
    ```
    ```
    [*RR-bgp-af-vpn-target] peer 1.1.1.1 enable
    ```
    ```
    [*RR-bgp-af-vpn-target] peer 1.1.1.1 reflect-client
    ```
    ```
    [*RR-bgp-af-vpn-target] peer 2.2.2.2 enable
    ```
    ```
    [*RR-bgp-af-vpn-target] peer 2.2.2.2 reflect-client
    ```
    ```
    [*RR-bgp-af-vpn-target] peer 4.4.4.4 enable
    ```
    ```
    [*RR-bgp-af-vpn-target] peer 4.4.4.4 reflect-client
    ```
    ```
    [*RR-bgp-af-vpn-target] quit
    ```
    ```
    [*RR-bgp] l2vpn-family evpn
    ```
    ```
    [*RR-bgp-af-evpn] vpn-orf enable
    ```
    ```
    [*RR-bgp-af-evpn] quit
    ```
    ```
    [*RR-bgp] quit
    ```
    ```
    [*RR] commit
    ```
11. Verify the configuration.
    
    
    
    Run the **display bgp vpn-target routing-table** command on the RR. The command output shows that the RR has received ORF routes.
    
    ```
    [~RR] display bgp vpn-target routing-table
    ```
    ```
     
     Total number of routes from all PE: 7
    
     BGP Local router ID is 10.1.1.2
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
    
     Origin AS: 100
    
     Total Number of Routes: 7
            Network                  NextHop        MED        LocPrf    PrefVal Path/Ogn
     *>i    RT <1 : 1>               1.1.1.1         0          100        0       ?
     * i                             2.2.2.2         0          100        0       ?
     *>i    RT <2 : 2>               1.1.1.1         0          100        0       ?
     * i                             4.4.4.4         0          100        0       ?
     *>i    RT <0011-1111-1111>      1.1.1.1         0          100        0       ?
     *>i    RT <0011-1122-2222>      2.2.2.2         0          100        0       ?
     *>i    RT <0011-1133-3333>      4.4.4.4         0          100        0       ?
    ```
    
    Run the **display bgp evpn all routing-table peer 2.2.2.2 advertised-routes** and **display bgp evpn all routing-table peer 4.4.4.4 advertised-routes** commands on the RR again. The command output shows that the RR has advertised only requested routes to PE2 and PE3.
    
    ```
    [~RR] display bgp evpn all routing-table peer 2.2.2.2 advertised-routes
    ```
    ```
     Local AS number : 100
    
     BGP Local router ID is 10.1.1.2
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
     
     EVPN address family:
     Number of A-D Routes: 2
     Route Distinguisher: 100:1
           Network(ESI/EthTagId)                                  NextHop
     *>i   0000.1111.1111.1111.1111:0                             1.1.1.1
     Route Distinguisher: 1.1.1.1:0
           Network(ESI/EthTagId)                                  NextHop
     *>i   0000.1111.1111.1111.1111:4294967295                    1.1.1.1
     
     EVPN address family:
     Number of Inclusive Multicast Routes: 1
     Route Distinguisher: 100:1
           Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
     *>i   0:32:1.1.1.1                                           1.1.1.1
    ```
    ```
    [~RR] display bgp evpn all routing-table peer 4.4.4.4 advertised-routes
    ```
    ```
     Local AS number : 100
    
     BGP Local router ID is 10.1.1.2
     Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                   h - history,  i - internal, s - suppressed, S - Stale
                   Origin : i - IGP, e - EGP, ? - incomplete
    
     
     EVPN address family:
     Number of A-D Routes: 2
     Route Distinguisher: 100:2
           Network(ESI/EthTagId)                                  NextHop
     *>i   0000.1111.1111.1111.1111:0                             1.1.1.1
     Route Distinguisher: 1.1.1.1:0
           Network(ESI/EthTagId)                                  NextHop
     *>i   0000.1111.1111.1111.1111:4294967295                    1.1.1.1
     
     EVPN address family:
     Number of Inclusive Multicast Routes: 1
     Route Distinguisher: 100:2
           Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
     *>i   0:32:1.1.1.1                                           1.1.1.1
    ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 100:2
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #               
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   esi 0000.1111.1111.1111.1111
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/0.2 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #               
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    vpn-orf enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
  #
  evpn source-address 1.1.1.1
  #
  return
  ```
* PE2 configuration file
  
  ```
  #
  sysname PE2
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 100:1
   vpn-target 1:1 export-extcommunity
   vpn-target 1:1 import-extcommunity
  #
  mpls lsr-id 2.2.2.2
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #               
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   esi 0000.1111.2222.2222.2222
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 2.2.2.2 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    vpn-orf enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.2.1.0 0.0.0.255
  #
  evpn source-address 2.2.2.2
  #
  return
  ```
* PE3 configuration file
  
  ```
  #
  sysname PE3
  #
  evpn vpn-instance evrf2 bd-mode
   route-distinguisher 100:2
   vpn-target 2:2 export-extcommunity
   vpn-target 2:2 import-extcommunity
  #
  mpls lsr-id 4.4.4.4
  #
  mpls
  #
  bridge-domain 20
   evpn binding vpn-instance evrf2
  #               
  mpls ldp
  #
  interface GigabitEthernet0/1/0
   undo shutdown  
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   esi 0000.1111.3333.3333.3333
  #
  interface GigabitEthernet0/2/0.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  interface LoopBack1
   ip address 4.4.4.4 255.255.255.255
  #
  bgp 100
   peer 3.3.3.3 as-number 100
   peer 3.3.3.3 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 3.3.3.3 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    vpn-orf enable
    peer 3.3.3.3 enable
   #
   ipv4-family vpn-target
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 4.4.4.4 0.0.0.0
    network 10.3.1.0 0.0.0.255
  #
  evpn source-address 4.4.4.4
  #
  return
  ```
* RR configuration file
  
  ```
  #
  sysname RR
  #
  mpls lsr-id 3.3.3.3
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
   ip address 10.2.1.2 255.255.255.0
   mpls           
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.3.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   peer 4.4.4.4 as-number 100
   peer 4.4.4.4 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
    peer 4.4.4.4 enable
   #
   l2vpn-family evpn
    undo policy vpn-target
    vpn-orf enable
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 4.4.4.4 enable
    peer 4.4.4.4 reflect-client
   #
   ipv4-family vpn-target
    peer 1.1.1.1 enable
    peer 1.1.1.1 reflect-client
    peer 2.2.2.2 enable
    peer 2.2.2.2 reflect-client
    peer 4.4.4.4 enable
    peer 4.4.4.4 reflect-client
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #               
  return
  ```
* CE1 configuration file
  
  ```
  #
  sysname CE1
  #
  bridge-domain 10
  #
  bridge-domain 20
  #
  interface Vbdif10
   ip address 192.168.1.11 255.255.255.0
  #
  interface Vbdif20
   ip address 192.168.2.11 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  interface GigabitEthernet0/1/0.2 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  return
  ```
* CE2 configuration file
  
  ```
  #
  sysname CE2
  #
  bridge-domain 10
  #
  interface Vbdif10
   ip address 192.168.1.12 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   rewrite pop single
   bridge-domain 10
  #
  return
  ```
* CE3 configuration file
  
  ```
  #
  sysname CE3
  #
  bridge-domain 20
  #
  interface Vbdif20
   ip address 192.168.2.12 255.255.255.0
  #
  interface GigabitEthernet0/1/0
   undo shutdown
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 20
   rewrite pop single
   bridge-domain 20
  #
  return
  ```