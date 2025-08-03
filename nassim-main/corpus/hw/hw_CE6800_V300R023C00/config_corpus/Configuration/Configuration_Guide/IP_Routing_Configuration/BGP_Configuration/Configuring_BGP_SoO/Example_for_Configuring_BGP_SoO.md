Example for Configuring BGP SoO
===============================

Example for Configuring BGP SoO

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001481981392__fig168879525502), DeviceA and DeviceB reside in different ASs, are connected to Server, and establish EBGP peer relationships with Leaf and Server to transmit public network unicast routes. To reduce redundant routes, configure the SoO function on DeviceA and DeviceB. When DeviceA advertises a route to Leaf, it adds the SoO attribute to the route. After receiving the route forwarded by Leaf, DeviceB checks the SoO attribute carried in the route. If the SoO attribute is the same as that configured on DeviceB, DeviceB does not accept this route, reducing memory usage and route selection costs.

**Figure 1** BGP SoO application on an IPv4 public network  
![](figure/en-us_image_0000001485105592.png)

#### Precautions

During the configuration, note the following:

* During the establishment of a peer relationship, if the IP address of the specified peer is a loopback interface address or a sub-interface address, the **peer connect-interface** command must be run on both ends to ensure correct connection.
* If there is no directly connected physical link between EBGP peers, run the **peer ebgp-max-hop** command to allow the EBGP peers to establish a TCP connection through multiple hops.

#### Configuration Roadmap

1. Assign IP addresses to interfaces.
2. Configure basic OSPF functions.
3. Establish EBGP connections between Server and DeviceA, between Server and DeviceB, between Leaf and DeviceA, and between Leaf and DeviceB.
4. Configure an IPv4 static route on Server and import it to the BGP routing table.
5. Configure BGP SoO on DeviceA and DeviceB.

#### Procedure

1. Assign IP addresses to interfaces. The following uses DeviceA as an example. The configurations of other devices are similar to that on DeviceA. For details, see [Configuration Scripts](#EN-US_TASK_0000001481981392__postreq1873214154377).
   
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface loopback0
   [~DeviceA-LoopBack0] ip address 10.1.3.1 24
   [*DeviceA-LoopBack0] quit
   [*DeviceA] interface loopback1
   [*DeviceA-LoopBack1] ip address 10.1.1.1 24
   [*DeviceA-LoopBack1] quit
   [*DeviceA] interface meth0/0/0
   [*DeviceA-MEth0/0/0] ip address 10.10.1.2 24
   [*DeviceA-MEth0/0/0] quit
   [*DeviceA] commit
   ```
2. Configure OSPF for interworking within the IGP domain.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1
   [*DeviceA-ospf-1] area 0
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.1.3.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   [*DeviceA-ospf-1-area-0.0.0.0] quit
   [*DeviceA-ospf-1] quit
   [*DeviceA] commit
   ```
   
   # Configure Leaf.
   
   ```
   [~Leaf] ospf 1
   [*Leaf-ospf-1] area 0
   [*Leaf-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   [*Leaf-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   [*Leaf-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   [*Leaf-ospf-1-area-0.0.0.0] quit
   [*Leaf-ospf-1] quit
   [*Leaf] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf 1
   [*DeviceB-ospf-1] area 0
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.4.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   [*DeviceB-ospf-1-area-0.0.0.0] quit
   [*DeviceB-ospf-1] quit
   [*DeviceB] commit
   ```
   
   # Configure Server.
   
   ```
   [~Server] ospf 1
   [*Server-ospf-1] area 0
   [*Server-ospf-1-area-0.0.0.0] network 10.1.3.0 0.0.0.255
   [*Server-ospf-1-area-0.0.0.0] network 10.1.4.0 0.0.0.255
   [*Server-ospf-1-area-0.0.0.0] network 10.10.1.0 0.0.0.255
   [*Server-ospf-1-area-0.0.0.0] quit
   [*Server-ospf-1] quit
   [*Server] commit
   ```
3. Configure EBGP.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] router-id 11.11.11.11
   [*DeviceA-bgp] peer 10.1.1.2 as-number 200  
   [*DeviceA-bgp] peer 10.1.1.2 ebgp-max-hop 10
   [*DeviceA-bgp] peer 10.1.1.2 connect-interface LoopBack1
   [*DeviceA-bgp] peer 10.1.3.2 as-number 400
   [*DeviceA-bgp] peer 10.1.3.2 ebgp-max-hop 10
   [*DeviceA-bgp] peer 10.1.3.2 connect-interface LoopBack0
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure Leaf.
   
   ```
   [~Leaf] bgp 200
   [*Leaf-bgp] router-id 22.22.22.22
   [*Leaf-bgp] peer 10.1.1.1 as-number 100
   [*Leaf-bgp] peer 10.1.1.1 ebgp-max-hop 10
   [*Leaf-bgp] peer 10.1.1.1 connect-interface LoopBack0
   [*Leaf-bgp] peer 10.1.2.1 as-number 300
   [*Leaf-bgp] peer 10.1.2.1 ebgp-max-hop 10
   [*Leaf-bgp] peer 10.1.2.1 connect-interface LoopBack1
   [*Leaf-bgp] quit
   [*Leaf] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 300
   [*DeviceB-bgp] router-id 33.33.33.33
   [*DeviceB-bgp] peer 10.1.2.2 as-number 200
   [*DeviceB-bgp] peer 10.1.2.2 ebgp-max-hop 10
   [*DeviceB-bgp] peer 10.1.2.2 connect-interface LoopBack0
   [*DeviceB-bgp] peer 10.1.4.2 as-number 400
   [*DeviceB-bgp] peer 10.1.4.2 ebgp-max-hop 10
   [*DeviceB-bgp] peer 10.1.4.2 connect-interface LoopBack1
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Configure Server.
   
   ```
   [~Server] bgp 400
   [*Server-bgp] router-id 44.44.44.44
   [*Server-bgp] peer 10.1.3.1 as-number 100
   [*Server-bgp] peer 10.1.3.1 ebgp-max-hop 10
   [*Server-bgp] peer 10.1.3.1 connect-interface LoopBack0
   [*Server-bgp] peer 10.1.4.1 as-number 300
   [*Server-bgp] peer 10.1.4.1 ebgp-max-hop 10
   [*Server-bgp] peer 10.1.4.1 connect-interface LoopBack1
   [*Server-bgp] quit
   [*Server] commit
   ```
   
   # Check the connection status of BGP peers. The following uses DeviceA as an example.
   
   ```
   [~DeviceA] display bgp peer
   Status codes: * - Dynamic
    BGP local router ID        : 11.11.11.11
    Local AS number            : 100
    Total number of peers      : 2
    Peers in established state : 2
    Total number of dynamic peers : 0
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.1.1.2                         4         200       32       38     0 00:22:34 Established       0
     10.1.3.2                         4         400       34       35     0 00:26:22 Established       0
   ```
4. Configure an IPv4 static route on Server and run the **network** command to import it.
   
   
   ```
   [~Server] ip route-static 1.1.1.1 255.255.255.255 NULL0
   [*Server] commit
   [~Server] bgp 400
   [*Server-bgp] ipv4-family unicast
   [*Server-bgp-af-ipv4] network 1.1.1.1 32
   [*Server-bgp-af-ipv4] quit
   [*Server-bgp] quit
   [*Server] commit
   ```
5. Configure the BGP SoO function.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] ipv4-family unicast
   [*DeviceA-bgp-af-ipv4] peer 10.1.1.2 soo-reverse 10:10
   [*DeviceA-bgp-af-ipv4] peer 10.1.1.2 advertise-ext-community  
   [*DeviceA-bgp-af-ipv4] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure Leaf.
   
   ```
   [~Leaf] bgp 200
   [*Leaf-bgp] peer 10.1.2.1 advertise-ext-community 
   [*Leaf-bgp] quit
   [*Leaf] commit
   ```
   
   # Check the BGP routing table of DeviceA. The command output shows that the SoO attribute 10:10 has been added to the route sent by DeviceA.
   
   ```
   [~DeviceA] display bgp routing-table peer 10.1.1.2 advertised-routes 1.1.1.1
   
    BGP local router ID : 11.11.11.11
    Local AS number : 100
    BGP routing table entry information of 1.1.1.1/32:
    From: 10.1.3.2 (10.1.3.2)
    Route Duration: 0d00h07m50s
    Relay IP Nexthop: 10.10.1.1
    Relay IP Out-Interface: MEth0/0/0
    Original nexthop: 10.1.3.2
    Advertised nexthop: 10.1.1.1
    Qos information : 0x0
    Ext-Community: SoO <10 : 10>
    AS-path 100 400, origin igp, pref-val 0, valid, external, best, select, pre 255, IGP cost 1
    Advertised to such 1 peers:
       10.1.1.2
   ```
   
   # Check the routing table of DeviceB. The command output shows that DeviceB receives the route 1.1.1.1/32 that carries the SoO attribute.
   
   ```
   [~DeviceB] display bgp routing-table peer 10.1.2.2 received-routes 1.1.1.1
   
    BGP local router ID : 33.33.33.33
    Local AS number : 300
    BGP routing table entry information of 1.1.1.1/32:
    From: 10.1.2.2 (10.10.1.3)  
    Route Duration: 0d00h00m57s
    Relay IP Nexthop: 10.10.1.3
    Relay IP Out-Interface: MEth0/0/0
    Original nexthop: 10.1.2.2
    Qos information : 0x0
    Ext-Community: SoO <10 : 10>
    AS-path 200 100 400, origin igp, pref-val 0, valid, external, pre 255, IGP cost 1, not preferred for AS-Path
    Not advertised to any peer yet
   ```
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 300
   [*DeviceB-bgp] ipv4-family unicast
   [*DeviceB-bgp-af-ipv4] peer 10.1.2.2 soo-reverse 10:10
   [*DeviceB-bgp-af-ipv4] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the BGP routing table of DeviceB. The **display bgp routing-table peer 10.1.2.2 received-routes 1.1.1.1** command output has no route information displayed. According to the **display bgp routing-table 1.1.1.1** command output, DeviceB discards the route received from 10.1.2.2 and accepts the route received from 10.1.4.2 after the BGP SoO attribute is configured.
```
[~DeviceB] display bgp routing-table 1.1.1.1 32

 BGP local router ID : 33.33.33.33
 Local AS number : 300
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 1.1.1.1/32:
 From: 10.1.4.2 (10.1.3.2)
 Route Duration: 0d00h07m01s
 Relay IP Nexthop: 10.10.1.1
 Relay IP Out-Interface: MEth0/0/0
 Original nexthop: 10.1.4.2
 Qos information : 0x0
 AS-path 400, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255, IGP cost 1
 Advertised to such 1 peers:
    10.1.2.2
```


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface MEth0/0/0
   ip address 10.10.1.2 255.255.255.0 
  #
  interface LoopBack0
   ip address 10.1.3.1 255.255.255.0
  #
  interface LoopBack1
   ip address 10.1.1.1 255.255.255.0
  #
  bgp 100
   private-4-byte-as enable
   peer 10.1.1.2 as-number 200
   peer 10.1.1.2 ebgp-max-hop 10                 
   peer 10.1.1.2 connect-interface LoopBack1     
   peer 10.1.3.2 as-number 400
   peer 10.1.3.2 ebgp-max-hop 10
   peer 10.1.3.2 connect-interface LoopBack0
   #
   ipv4-family unicast
    peer 10.1.1.2 enable
    peer 10.1.1.2 soo-reverse 10:10
    peer 10.1.1.2 advertise-ext-community   
    peer 10.1.3.2 enable
  # 
  ospf 1                             
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.3.0 0.0.0.255
    network 10.10.1.0 0.0.0.255
  #
  return
  ```
* Leaf
  
  ```
  #
  sysname Leaf
  #
  interface MEth0/0/0
   ip address 10.10.1.3 255.255.255.0
  #
  interface LoopBack0
   ip address 10.1.1.2 255.255.255.0
  #
  interface LoopBack1
   ip address 10.1.2.2 255.255.255.0
  #
  bgp 200
   private-4-byte-as enable
   peer 10.1.1.1 as-number 100
   peer 10.1.1.1 ebgp-max-hop 10
   peer 10.1.1.1 connect-interface LoopBack0
   peer 10.1.2.1 as-number 300
   peer 10.1.2.1 ebgp-max-hop 10
   peer 10.1.2.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 10.1.1.1 enable
    peer 10.1.2.1 enable
    peer 10.1.2.1 advertise-ext-community  
  #
  ospf 1
   area 0.0.0.0
    network 10.1.1.0 0.0.0.255
    network 10.1.2.0 0.0.0.255
    network 10.10.1.0 0.0.0.255
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  interface MEth0/0/0
   ip address 10.10.1.4 255.255.255.0
  #
  interface LoopBack0
   ip address 10.1.2.1 255.255.255.0
  #
  interface LoopBack1
   ip address 10.1.4.1 255.255.255.0
  #
  bgp 300
   private-4-byte-as enable
   peer 10.1.2.2 as-number 200
   peer 10.1.2.2 ebgp-max-hop 10
   peer 10.1.2.2 connect-interface LoopBack0
   peer 10.1.4.2 as-number 400
   peer 10.1.4.2 ebgp-max-hop 10
   peer 10.1.4.2 connect-interface LoopBack1
   #
   ipv4-family unicast
    peer 10.1.2.2 enable
    peer 10.1.2.2 soo-reverse 10:10
    peer 10.1.4.2 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.1.2.0 0.0.0.255
    network 10.1.4.0 0.0.0.255
    network 10.10.1.0 0.0.0.255
  #
  return
  ```
* Server
  
  ```
  #
  sysname Server
  #
  interface MEth0/0/0
   ip address 10.10.1.1 255.255.255.0
  #
  interface LoopBack0
   ip address 10.1.3.2 255.255.255.0
  #
  interface LoopBack1
   ip address 10.1.4.2 255.255.255.0
  #
  bgp 400
   private-4-byte-as enable
   peer 10.1.3.1 as-number 100
   peer 10.1.3.1 ebgp-max-hop 10
   peer 10.1.3.1 connect-interface LoopBack0
   peer 10.1.4.1 as-number 300
   peer 10.1.4.1 ebgp-max-hop 10
   peer 10.1.4.1 connect-interface LoopBack1
   #
   ipv4-family unicast
    network 1.1.1.1 255.255.255.255  
    peer 10.1.3.1 enable
    peer 10.1.4.1 enable
  #
  ospf 1
   area 0.0.0.0
    network 10.1.3.0 0.0.0.255
    network 10.1.4.0 0.0.0.255
    network 10.10.1.0 0.0.0.255
  #
  ip route-static 1.1.1.1 255.255.255.255 NULL0
  #
  return
  ```