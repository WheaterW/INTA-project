Example for Configuring EVPN E-Tree over MPLS
=============================================

This section provides an example for configuring EVPN E-Tree. This function isolates traffic between different interfaces in the same broadcast domain.

#### Networking Requirements

A user wants to deploy EVPN on the network shown in [Figure 1](#EN-US_TASK_0172370609__fig962918243284) to transmit services. Specifically, an EVPN instance (BD EVPN instance in this example) needs to be configured on PE1, PE2, and PE3, and a BGP EVPN peer relationship needs to be established between these devices. To improve network security, PE2 and PE3 can only interact with PE1, and PE2 and PE3 cannot send traffic to each other. To implement this function, the user can deploy EVPN E-Tree over the network.

**Figure 1** Configuring EVPN E-Tree![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GigabitEthernet0/1/0, GigabitEthernet0/2/0, and GigabitEthernet0/3/0, respectively.


  
![](figure/en-us_image_0000001229435519.png)  


#### Configuration Precautions

During the configuration process, note the following:

* For the same EVPN instance, the export VPN target list of one site shares VPN targets with the import VPN target lists of the other sites. Conversely, the import VPN target list of one site shares VPN targets with the export VPN target lists of the other sites.
* Using the local loopback interface address of each PE as the source address of the PE is recommended.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure interface IP addresses, including loopback interface addresses, on PEs.
2. Configure a routing protocol on each PE to ensure Layer 3 communication. OSPF is used in this example.
3. Configure MPLS LDP on each PE.
4. Create a BD EVPN instance and a BD on each PE, and bind the BD to the EVPN instance.
5. Configure each PE interface that connects to a CE.
6. Configure a source address on each PE.
7. Configure a BGP EVPN peer relationship between every two PEs.
8. Configure the access-side interfaces of PE2 and PE3 as leaf interfaces.

#### Data Preparation

To complete the configuration, you need the following data:

* EVPN instance name: evrf1
* EVPN instance **evrf1**'s RD (10:1) and RT (11:1) on each PE

#### Procedure

1. Configure interface IP addresses, including loopback interface addresses, on PEs.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370609__file1).
2. Configure a routing protocol on each PE to ensure Layer 3 communication. OSPF is used in this example.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370609__file1).
3. Configure MPLS LDP on each PE.
   
   
   
   For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370609__file1).
4. Create a BD EVPN instance and a BD on each PE, and bind the BD to the EVPN instance.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE1-evpn-instance-evrf1] route-distinguisher 10:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] vpn-target 11:1
   ```
   ```
   [*PE1-evpn-instance-evrf1] quit
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
   [*PE1] commit
   ```
   
   The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370609__file1).
5. Configure each PE interface that connects to a CE.
   
   
   
   # Configure PE1.
   
   ```
   [~PE1] interface gigabitethernet 0/1/0.1 mode l2
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] encapsulation dot1q vid 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] bridge-domain 10
   ```
   ```
   [*PE1-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE1] commit
   ```
   
   The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370609__file1).
6. Configure a source address on each PE.
   
   
   
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
   [~PE3] evpn source-address 3.3.3.3
   ```
   ```
   [*PE3] commit
   ```
7. Establish a BGP EVPN peer relationship between PEs.
   
   
   
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
   [*PE1-bgp] l2vpn-family evpn
   ```
   ```
   [*PE1-bgp-af-evpn] peer 2.2.2.2 enable
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
   
   The configurations of PE2 and PE3 are similar to that of PE1. For detailed configurations, see [Configuration Files](#EN-US_TASK_0172370609__file1).
8. Configure the access side interfaces of PE2 and PE3 as leaf interfaces.
   
   
   
   # Configure PE2.
   
   ```
   [~PE2] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE2-evpn-instance-evrf1] etree enable
   ```
   ```
   [*PE2-evpn-instance-evrf1] quit
   ```
   ```
   [*PE2] interface gigabitethernet0/1/0.1 mode l2
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] evpn e-tree-leaf
   ```
   ```
   [*PE2-GigabitEthernet0/1/0.1] quit
   ```
   ```
   [*PE2] commit
   ```
   
   # Configure PE3.
   
   ```
   [~PE3] evpn vpn-instance evrf1 bd-mode
   ```
   ```
   [*PE3-evpn-instance-evrf1] etree enable
   ```
   ```
   [*PE3-evpn-instance-evrf1] quit
   ```
   ```
   [*PE3] interface gigabitethernet0/3/0.1 mode l2
   ```
   ```
   [*PE3-GigabitEthernet0/3/0.1] evpn e-tree-leaf
   ```
   ```
   [*PE3-GigabitEthernet0/3/0.1] quit
   ```
   ```
   [*PE3] commit
   ```
9. Verify the configuration.
   
   
   
   Run the **display bgp evpn all routing-table** command on PE1 to view the leaf attribute in Ethernet auto-discovery and MAC routes.
   
   ```
   [~PE1] display bgp evpn all routing-table
   ```
   ```
    Local AS number : 100
   
    BGP Local router ID is 10.2.1.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
   
    EVPN address family:
    Number of A-D Routes: 2
    Route Distinguisher: 2.2.2.2:0
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.0000.0000.0000.0000:4294967295                    2.2.2.2
    Route Distinguisher: 3.3.3.3:0
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.0000.0000.0000.0000:4294967295                    3.3.3.3
       
   
    EVPN-Instance evrf1:
    Number of A-D Routes: 2
          Network(ESI/EthTagId)                                  NextHop
    *>i   0000.0000.0000.0000.0000:4294967295                    2.2.2.2
    * i                                                          3.3.3.3
   
    EVPN address family:
    Number of Mac Routes: 6
    Route Distinguisher: 10:1
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>    0:48:00e0-fc00-0001:0:0.0.0.0                          0.0.0.0
    *>i   0:48:00e0-fc00-0005:0:0.0.0.0                          2.2.2.2
    *>i   0:48:00e0-fc00-0004:0:0.0.0.0                          3.3.3.3
    *>i   0:48:00e0-fc00-0002:0:0.0.0.0                          2.2.2.2
    *>i   0:48:00e0-fc00-0003:0:0.0.0.0                          3.3.3.3
    *>    0:48:00e0-fc00-0006:0:0.0.0.0                          0.0.0.0
       
   
    EVPN-Instance evrf1:
    Number of Mac Routes: 6
          Network(EthTagId/MacAddrLen/MacAddr/IpAddrLen/IpAddr)  NextHop
    *>    0:48:00e0-fc00-0001:0:0.0.0.0                          0.0.0.0
    *>i   0:48:00e0-fc00-0005:0:0.0.0.0                          2.2.2.2
    *>i   0:48:00e0-fc00-0004:0:0.0.0.0                          3.3.3.3
    *>i   0:48:00e0-fc00-0002:0:0.0.0.0                          2.2.2.2
    *>i   0:48:00e0-fc00-0003:0:0.0.0.0                          3.3.3.3
    *>    0:48:00e0-fc00-0006:0:0.0.0.0                          0.0.0.0
   
    EVPN address family:
    Number of Inclusive Multicast Routes: 3
    Route Distinguisher: 10:1
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:1.1.1.1                                           127.0.0.1
    *>i   0:32:2.2.2.2                                           2.2.2.2
    *>i   0:32:3.3.3.3                                           3.3.3.3
       
   
    EVPN-Instance evrf1:
    Number of Inclusive Multicast Routes: 3
          Network(EthTagId/IpAddrLen/OriginalIp)                 NextHop
    *>    0:32:1.1.1.1                                           127.0.0.1
    *>i   0:32:2.2.2.2                                           2.2.2.2
    *>i   0:32:3.3.3.3                                           3.3.3.3
   ```
   ```
   [~PE1] display bgp evpn all routing-table ad-route 0000.0000.0000.0000.0000:4294967295
   ```
   ```
    BGP local router ID : 10.2.1.2
    Local AS number : 100
    Total routes of Route Distinguisher(2.2.2.2:0): 1
    BGP routing table entry information of 0000.0000.0000.0000.0000:4294967295:
    From: 2.2.2.2 (2.2.2.2) 
    Route Duration: 0d01h27m52s
    Relay IP Nexthop: 10.2.1.1
    Relay Tunnel Out-Interface: GigabitEthernet0/2/0
    Original nexthop: 2.2.2.2
    Qos information : 0x0            
    Ext-Community: RT <11 : 1>, SoO <2.2.2.2 : 0>, E-Tree <0 : 0 : 32915>
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 1
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
    ESI: 0000.0000.0000.0000.0000, Ethernet Tag ID: 4294967295
    Not advertised to any peer yet
    
    Total routes of Route Distinguisher(3.3.3.3:0): 1
    BGP routing table entry information of 0000.0000.0000.0000.0000:4294967295:
    From: 3.3.3.3 (3.3.3.3) 
    Route Duration: 0d01h25m59s
    Relay IP Nexthop: 10.1.1.2
    Relay Tunnel Out-Interface: GigabitEthernet0/3/0
    Original nexthop: 3.3.3.3
    Qos information : 0x0            
    Ext-Community: RT <11 : 1>, SoO <3.3.3.3 : 0>, E-Tree <0 : 0 : 32915>
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 1
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
    ESI: 0000.0000.0000.0000.0000, Ethernet Tag ID: 4294967295
    Not advertised to any peer yet
    
       
   
    EVPN-Instance evrf1:
    Number of A-D Routes: 2
    BGP routing table entry information of 0000.0000.0000.0000.0000:4294967295:
    Route Distinguisher: 2.2.2.2:0
    Remote-Cross route
    From: 2.2.2.2 (2.2.2.2) 
    Route Duration: 0d01h27m52s
    Relay Tunnel Out-Interface: GigabitEthernet0/2/0
    Original nexthop: 2.2.2.2
    Qos information : 0x0            
    Ext-Community: RT <11 : 1>, SoO <2.2.2.2 : 0>, E-Tree <0 : 0 : 32915>
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 1
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
    ESI: 0000.0000.0000.0000.0000, Ethernet Tag ID: 4294967295
    Not advertised to any peer yet
    
    BGP routing table entry information of 0000.0000.0000.0000.0000:4294967295:
    Route Distinguisher: 3.3.3.3:0
    Remote-Cross route
    From: 3.3.3.3 (3.3.3.3) 
    Route Duration: 0d01h25m59s
    Relay Tunnel Out-Interface: GigabitEthernet0/3/0
    Original nexthop: 3.3.3.3
    Qos information : 0x0            
    Ext-Community: RT <11 : 1>, SoO <3.3.3.3 : 0>, E-Tree <0 : 0 : 32915>
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, pre 255, IGP cost 1, not preferred for router ID
    Route Type: 1 (Ethernet Auto-Discovery (A-D) route)
    ESI: 0000.0000.0000.0000.0000, Ethernet Tag ID: 4294967295
    Not advertised to any peer yet
   ```
   ```
   [~PE1] display bgp evpn all routing-table mac-route 0:48:00e0-fc00-0005:0:0.0.0.0
   ```
   ```
    BGP local router ID : 10.2.1.2
    Local AS number : 100
    Total routes of Route Distinguisher(10:1): 1
    BGP routing table entry information of 0:48:00e0-fc00-0005:0:0.0.0.0:
    Label information (Received/Applied): 32912/NULL
    From: 2.2.2.2 (2.2.2.2) 
    Route Duration: 0d01h15m31s
    Relay IP Nexthop: 10.2.1.1
    Relay Tunnel Out-Interface: GigabitEthernet0/2/0
    Original nexthop: 2.2.2.2
    Qos information : 0x0            
    Ext-Community: RT <11 : 1>, SoO <2.2.2.2 : 0>, E-Tree <1 : 0 : 0>
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 1
    Route Type: 2 (MAC Advertisement Route)
    Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc00-0005/48, IP Address/Len: 0.0.0.0/0, ESI:0000.0000.0000.0000.0000
    Not advertised to any peer yet
    
       
   
    EVPN-Instance evrf1:
    Number of Mac Routes: 1
    BGP routing table entry information of 0:48:00e0-fc00-0005:0:0.0.0.0:
    Route Distinguisher: 10:1
    Remote-Cross route
    Label information (Received/Applied): 32912/NULL
    From: 2.2.2.2 (2.2.2.2) 
    Route Duration: 0d01h15m31s
    Relay Tunnel Out-Interface: GigabitEthernet0/2/0
    Original nexthop: 2.2.2.2
    Qos information : 0x0            
    Ext-Community: RT <11 : 1>, SoO <2.2.2.2 : 0>, E-Tree <1 : 0 : 0>
    AS-path Nil, origin incomplete, localpref 100, pref-val 0, valid, internal, best, select, pre 255, IGP cost 1
    Route Type: 2 (MAC Advertisement Route)
    Ethernet Tag ID: 0, MAC Address/Len: 00e0-fc00-0005/48, IP Address/Len: 0.0.0.0/0, ESI:0000.0000.0000.0000.0000
    Not advertised to any peer yet
   ```

#### Configuration Files

* PE1 configuration file
  
  ```
  #
  sysname PE1
  #
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  mpls lsr-id 1.1.1.1
  #
  mpls
  #
  bridge-domain 10
   evpn binding vpn-instance evrf1
  #
  mpls ldp
  #
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   mpls
   mpls ldp
  #
  interface LoopBack1
   ip address 1.1.1.1 255.255.255.255
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
   l2vpn-family evpn
    undo policy vpn-target
    peer 2.2.2.2 enable
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 1.1.1.1 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.2.1.0 0.0.0.255
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
   route-distinguisher 10:1
   etree enable
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
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
  interface GigabitEthernet0/1/0.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
   evpn e-tree-leaf
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.2.1.1 255.255.255.0
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
   ip address 2.2.2.2 255.255.255.255
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
    peer 3.3.3.3 enable
  #
  ospf 1
   area 0.0.0.0
    network 2.2.2.2 0.0.0.0
    network 10.2.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
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
  evpn vpn-instance evrf1 bd-mode
   route-distinguisher 10:1
   etree enable
   vpn-target 11:1 export-extcommunity
   vpn-target 11:1 import-extcommunity
  #
  mpls lsr-id 3.3.3.3
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
   ip address 10.1.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ip address 10.3.1.2 255.255.255.0
   mpls
   mpls ldp
  #
  interface GigabitEthernet0/3/0.1 mode l2
   encapsulation dot1q vid 10
   bridge-domain 10
   evpn e-tree-leaf
  #
  interface LoopBack1
   ip address 3.3.3.3 255.255.255.255
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   peer 1.1.1.1 connect-interface LoopBack1
   peer 2.2.2.2 as-number 100
   peer 2.2.2.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    undo synchronization
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
   #              
   l2vpn-family evpn
    undo policy vpn-target
    peer 1.1.1.1 enable
    peer 2.2.2.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 3.3.3.3 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.3.1.0 0.0.0.255
  #
  evpn source-address 3.3.3.3
  #
  return
  ```