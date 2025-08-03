Example for Configuring Routing Loop Detection for BGP Routes Imported to OSPF
==============================================================================

This section describes how to configure routing loop detection for routes imported from BGP to OSPF.

#### Networking Requirements

On the live network, OSPF routes can be imported to a BGP process for redistribution. In such a scenario, routing policies are usually configured on multiple devices to prevent routing loops. If routing policies are incorrectly configured on the devices that import routes, routing loops may occur. To prevent this problem, configure routing loop detection for the routes imported to OSPF.

On the network shown in [Figure 1](#EN-US_TASK_0000001211171423__fig1261541011544), DeviceA, DeviceB, DeviceC, and DeviceD establish IBGP peer relationships, and an OSPF process is configured on DeviceC and DeviceD. OSPF is configured on DeviceC to import BGP routes, and BGP is configured on DeviceD to import OSPF routes.

**Figure 1** Routing loop detection for routes imported from BGP to OSPF![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001230985383.png)

#### Precautions

To improve security, OSPF area authentication or interface authentication is recommended. For details, see "Improving OSPF Network Security." OSPF area authentication is used as an example. For details, see "Example for Configuring Basic OSPF Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on each device.
2. Enable OSPF and BGP, and configure basic OSPF and BGP functions.
3. Configure route import to construct a routing loop.
4. Check whether a routing loop occurs.
5. Enable routing loop detection to check whether the routing loop is eliminated.

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   DeviceA is used as an example.
   
   ```
   <DeviceA> system-view
   [~DeviceA] interface 100GE1/0/1 
   [*DeviceA-100GE1/0/1] ip address 10.12.1.1 24
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   The configurations of other devices are similar to those of DeviceA. For configuration details, see [Configuration Scripts](#EN-US_TASK_0000001211171423__section_dc_vrp_isis_cfg_201205) in this section.
   
   In addition, configure a static route on DeviceA to simulate a looped route.
   
   ```
   [~DeviceA] ip route-static 10.0.0.0 255.255.255.255 NULL0
   [*DeviceA] commit
   ```
2. Enable OSPF and BGP, and configure basic OSPF and BGP functions to implement intra-AS communication.
   
   
   
   # Enable BGP on DeviceA and establish an IBGP peer relationship between DeviceA and DeviceB.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] router-id 10.11.1.1
   [*DeviceA-bgp] peer 10.12.1.2 as-number 100
   [*DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] peer 10.12.1.2 enable
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Enable BGP on DeviceB, and establish IBGP peer relationships between DeviceB and DeviceA, between DeviceB and DeviceC, and between DeviceB and DeviceD.
   
   ```
   [~DeviceB] bgp 100
   [*DeviceB-bgp] router-id 10.22.2.2
   [*DeviceB-bgp] peer 10.12.1.1 as-number 100
   [*DeviceB-bgp] peer 10.23.1.3 as-number 100
   [*DeviceB-bgp] peer 10.24.1.4 as-number 100
   [*DeviceB-bgp] ipv4-family unicast
   [*DeviceB-bgp-af-ipv4] peer 10.12.1.1 enable
   [*DeviceB-bgp-af-ipv4] peer 10.23.1.3 enable
   [*DeviceB-bgp-af-ipv4] peer 10.24.1.4 enable
   [*DeviceB-bgp-af-ipv4] peer 10.23.1.3 reflect-client
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Enable BGP on DeviceC and establish an IBGP peer relationship between DeviceC and DeviceB.
   
   ```
   [~DeviceC] bgp 100
   [*DeviceC-bgp] router-id 10.33.3.3
   [*DeviceC-bgp] peer 10.23.1.2 as-number 100
   [*DeviceC-bgp] ipv4-family unicast
   [*DeviceC-bgp-af-ipv4] peer 10.23.1.2 enable
   [*DeviceC-bgp] quit
   [*DeviceC] commit
   ```
   
   # Enable BGP on DeviceD and establish an IBGP peer relationship between DeviceD and DeviceB.
   
   ```
   [~DeviceD] bgp 100
   [*DeviceD-bgp] router-id 10.44.4.4
   [*DeviceD-bgp] peer 10.24.1.2 as-number 100
   [*DeviceD-bgp] ipv4-family unicast
   [*DeviceD-bgp-af-ipv4] peer 10.24.1.2 enable
   [*DeviceD-bgp] quit
   [*DeviceD] commit
   ```
   
   # Configure OSPF on DeviceC and DeviceD. The configuration on DeviceC is used as an example.
   
   ```
   [~DeviceC] ospf 1 router-id 10.33.3.3
   [*DeviceC-ospf-1] area 0
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.34.1.0 0.0.0.255
   [*DeviceC-ospf-1-area-0.0.0.0] quit
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
3. Configure route import.
   
   
   
   # Configure OSPF on DeviceC to import BGP routes.
   
   
   
   ```
   [~DeviceC] ospf 1 router-id 10.33.3.3
   [*DeviceC-ospf-1] import-route bgp permit-ibgp
   [*DeviceC-ospf-1] opaque-capability enable
   [*DeviceC-ospf-1] quit
   [*DeviceC] commit
   ```
   
   # Configure BGP on DeviceD to import OSPF routes.
   
   ```
   [~DeviceD] bgp 100
   [*DeviceD-bgp] ipv4-family unicast
   [*DeviceD-bgp-af-ipv4] import-route ospf 1
   [*DeviceD-bgp] quit
   [*DeviceD] commit
   ```
4. Display the routing table on each device to check whether a routing loop occurs.
   
   
   
   # Check BGP peer information on DeviceB.
   
   ```
   [~DeviceB] display bgp peer
   ```
   ```
    BGP local router ID : 10.22.2.2
    Local AS number : 100
    Total number of peers : 3                 Peers in established state : 3
   
     Peer                              V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State   PrefRcv
     10.12.1.1                         4         100      453      458     0 06:30:47 Established        1
     10.23.1.3                         4         100      452      458     0 06:30:46 Established        0
     10.24.1.4                         4         100      451      457     0 06:29:39 Established        3
   ```
   
   # Check OSPF neighbor information on DeviceC.
   
   ```
   [~DeviceC] display ospf peer
   ```
   ```
   (M) Indicates MADJ neighbor
   
   
             OSPF Process 1 with Router ID 10.33.3.3
                   Neighbors
   
    Area 0.0.0.0 interface 10.34.1.3 (100GE1/0/1)'s neighbors
    Router ID: 10.44.4.4             Address: 10.34.1.4
      State: Full           Mode:Nbr is Master     Priority: 1
      DR: 10.34.1.4          BDR: 10.34.1.3          MTU: 0
      Dead timer due in  31  sec
      Retrans timer interval: 5
      Neighbor is up for 06h28m21s
      Neighbor Up Time : 2021-08-27 02:59:32
      Authentication Sequence: [ 0 ]
   ```
   
   # Check OSPF neighbor information on DeviceD.
   
   ```
   [~DeviceD] display ospf peer
   ```
   ```
   (M) Indicates MADJ neighbor
   
   
             OSPF Process 1 with Router ID 10.44.4.4
                   Neighbors
   
    Area 0.0.0.0 interface 10.34.1.4 (100GE1/0/2)'s neighbors
    Router ID: 10.33.3.3             Address: 10.34.1.3
      State: Full           Mode:Nbr is Slave      Priority: 1
      DR: 10.34.1.4          BDR: 10.34.1.3          MTU: 0
      Dead timer due in  32  sec
      Retrans timer interval: 5
      Neighbor is up for 06h28m25s
      Neighbor Up Time : 2021-08-27 02:59:32
      Authentication Sequence: [ 0 ]
   ```
   
   The preceding command outputs show that BGP peer relationships and OSPF neighbor relationships have been established between the devices.
   
   # Check the BGP routing table of DeviceB.
   
   ```
   [~DeviceB] display bgp routing-table 10.0.0.0
   ```
   ```
    BGP local router ID : 10.22.2.2
    Local AS number : 100
    Paths:   2 available, 1 best, 1 select, 0 best-external, 0 add-path
    BGP routing table entry information of 10.0.0.0/32:
    RR-client route.
    From: 10.24.1.4 (10.44.4.4)
    Route Duration: 0d00h00m52s
    Relay IP Nexthop: 10.24.1.4
    Relay IP Out-Interface: 100GE1/0/1
    Original nexthop: 10.24.1.4
    Qos information : 0x0
    AS-path Nil, origin incomplete, MED 1, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Advertised to such 3 peers:
       10.23.1.3
       10.24.1.4
       10.12.1.1
   
    BGP routing table entry information of 10.0.0.0/32:
    From: 10.12.1.1 (10.11.1.1)
    Route Duration: 0d22h53m22s
    Relay IP Nexthop: 10.12.1.1
    Relay IP Out-Interface:100GE1/0/2
    Original nexthop: 10.12.1.1
    Qos information : 0x0
    AS-path 10, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, pre 255, not preferred for AS-Path
    Not advertised to any peer yet
   ```
   
   The preceding command output shows that DeviceB has learned the BGP route advertised by DeviceD.
   
   # Check the BGP routing table of DeviceC.
   
   ```
   [~DeviceC] display bgp routing-table 10.0.0.0
   ```
   ```
    BGP local router ID : 10.33.3.3
    Local AS number : 100
    Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
    BGP routing table entry information of 10.0.0.0/32:
    From: 10.23.1.2 (10.22.2.2)
    Route Duration: 0d07h12m30s
    Relay IP Nexthop: 0.0.0.0
    Relay IP Out-Interface: NULL0
    Original nexthop: 10.12.1.1
    Qos information : 0x0
    AS-path 10, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Originator: 10.11.1.1
    Cluster list: 10.22.2.2
    Not advertised to any peer yet
   ```
   
   The preceding command output shows that DeviceC has learned the BGP route advertised by DeviceB.
   
   # Check the routing table of DeviceD.
   
   ```
   [~DeviceD] display ospf routing 10.0.0.0
   ```
   ```
             OSPF Process 1 with Router ID 10.44.4.4
   
    Destination    : 10.0.0.0/32
    AdverRouter    : 10.33.3.3                 Tag                 : 1
    Cost           : 1                        Type                : Type2
    NextHop        : 10.34.1.3               Interface           : 100GE1/0/2
    Priority       : Medium                   Age                 : 01h31m18s
   ```
   
   The preceding command output shows that DeviceD has learned the OSPF route distributed by DeviceC.
   
   
   
   In this case, a routing loop occurs on DeviceB, DeviceC, and DeviceD.
5. Enable routing loop detection on each device.
   
   
   
   # Enable routing loop detection for routes imported into OSPF and BGP. DeviceA is used as an example.
   
   ```
   [*DeviceA] route loop-detect ospf enable
   [*DeviceA] route loop-detect bgp enable
   [*DeviceA] commit
   ```
   
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   In the case of inter-protocol route import, if a routing protocol with a higher priority detects a routing loop, although this protocol increases the cost of the corresponding route, the cost increase will not render the route inactive. As a result, the routing loop cannot be eliminated. If a routing protocol with a lower preference detects a routing loop and increases the cost of the corresponding route, this route will not be preferred over the originally received route. In this case, the routing loop can be eliminated. OSPF has a higher preference than BGP. Therefore, to eliminate the routing loop, you need to reduce the preference of the corresponding BGP route.
6. Check whether the routing loop is eliminated.
   
   
   
   # Check the BGP routing table of DeviceB.
   
   ```
   [~DeviceB] display bgp routing-table 10.0.0.0
   ```
   ```
    BGP local router ID : 10.22.2.2
    Local AS number : 100
    Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
    BGP routing table entry information of 10.0.0.0/32:
    From: 10.12.1.1 (10.11.1.1)
    Route Duration: 1d00h10m02s
    Relay IP Nexthop: 10.12.1.1
    Relay IP Out-Interface: 100GE1/0/2
    Original nexthop: 10.12.1.1
    Qos information : 0x0
    AS-path 10, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, select, pre 255
    Advertised to such 2 peers:
       10.23.1.3
       10.24.1.4
   ```
   
   The preceding command output shows that DeviceB has learned the route distributed by DeviceA and no longer preferentially selects the route distributed by DeviceD. This means that the routing loop on DeviceB, DeviceC, and DeviceD is resolved.

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.12.1.1 255.255.255.0
  #
  bgp 100
   router-id 10.11.1.1
   private-4-byte-as enable
   peer 10.12.1.2 as-number 100
   #
   ipv4-family unicast
    import-route static
    peer 10.12.1.2 enable
  #
  ip route-static 10.0.0.0 255.255.255.255 NULL0
  #
  route loop-detect ospf enable
  #
  route loop-detect bgp enable
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.12.1.2 255.255.255.0
  #
  interface 100GE1/0/3
   undo portswitch
   ip address 10.24.1.2 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.23.1.2 255.255.255.0
  #
  bgp 100
   router-id 10.22.2.2
   private-4-byte-as enable
   peer 10.12.1.1 as-number 100
   peer 10.23.1.3 as-number 100
   peer 10.24.1.4 as-number 100
   #
   ipv4-family unicast
    peer 10.12.1.1 enable
    peer 10.23.1.3 enable
    peer 10.23.1.3 reflect-client
    peer 10.24.1.4 enable
    peer 10.24.1.4 reflect-client
  #
  route loop-detect ospf enable
  #
  route loop-detect bgp enable
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.34.1.3 255.255.255.0
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.23.1.3 255.255.255.0
  #
  bgp 100
   router-id 10.33.3.3
   private-4-byte-as enable
   peer 10.23.1.2 as-number 100
   #
   ipv4-family unicast
    peer 10.23.1.2 enable
  #
  ospf 1 router-id 10.33.3.3
   import-route bgp permit-ibgp
   opaque-capability enable
   area 0.0.0.0
    network 10.34.1.0 0.0.0.255
  #
  route loop-detect ospf enable
  #
  route loop-detect bgp enable
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  interface 100GE1/0/2
   undo portswitch
   ip address 10.34.1.4 255.255.255.0
  #
  interface 100GE1/0/1
   undo portswitch
   ip address 10.24.1.4 255.255.255.0
  #
  bgp 100
   router-id 10.44.4.4
   private-4-byte-as enable
   peer 10.24.1.2 as-number 100
   #
   ipv4-family unicast
    import-route ospf 1
    peer 10.24.1.2 enable
  #
  ospf 1 router-id 10.44.4.4
   opaque-capability enable
   area 0.0.0.0
    network 10.34.1.0 0.0.0.255
  #
  route loop-detect ospf enable
  #
  route loop-detect bgp enable
  #
  return
  ```