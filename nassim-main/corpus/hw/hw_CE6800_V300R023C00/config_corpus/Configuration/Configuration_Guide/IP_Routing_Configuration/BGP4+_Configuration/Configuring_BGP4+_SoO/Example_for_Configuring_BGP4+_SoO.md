Example for Configuring BGP4+ SoO
=================================

Example for Configuring BGP4+ SoO

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001484849888__fig141211449172212), DeviceA and DeviceB reside in different ASs, are connected to Server, and establish EBGP peer relationships with Leaf and Server to transmit public network unicast routes. To reduce redundant routes, configure the SoO function on DeviceA and DeviceB. When DeviceA advertises a route to Leaf, it adds the SoO attribute to the route. After receiving the route forwarded by Leaf, DeviceB checks the SoO attribute carried in the route. If the SoO attribute is the same as that configured on DeviceB, DeviceB does not accept this route, reducing memory usage and route selection costs.

**Figure 1** BGP4+ SoO application in a public network IPv6 scenario![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 represents 100GE1/0/1.


  
![](figure/en-us_image_0000001539291877.png)

#### Precautions

Note the following during the configuration:

* During the establishment of a peer relationship, if the IPv6 address of the specified peer is a loopback interface address or a sub-interface IPv6 address, the **peer connect-interface** command must be run on both ends to ensure correct connection.
* If there is no directly connected physical link between EBGP peers, run the **peer ebgp-max-hop** command to allow the EBGP peers to establish a TCP connection through multiple hops.

#### Configuration Roadmap

1. Assign an IPv6 address to each interface.
2. Enable IS-IS, configure the level, and specify a NET on each device.
3. Establish EBGP connections between Server and DeviceA, between Server and DeviceB, between Leaf and DeviceA, and between Leaf and DeviceB.
4. Configure an IPv6 static route on Server and import it to the BGP4+ routing table.
5. Configure BGP4+ SoO on DeviceA and DeviceB.

#### Procedure

1. Enable IPv6 forwarding and configure an IPv6 address for each interface.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceA
   [*HUAWEI] commit
   [~DeviceA] interface loopback0     
   [~DeviceA-LoopBack0] ipv6 enable
   [*DeviceA-LoopBack0] ipv6 address 2001:db8:10::2 128        
   [*DeviceA-LoopBack0] quit
   [*DeviceA] interface loopback1
   [*DeviceA-LoopBack1] ipv6 enable
   [*DeviceA-LoopBack1] ipv6 address 2001:db8:20::1 128
   [*DeviceA-LoopBack1] quit
   [*DeviceA] interface 100GE1/0/1
   [*DeviceA-100GE1/0/1] undo portswitch
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:1::1 64
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure Leaf.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname Leaf
   [*HUAWEI] commit
   [~Leaf] interface loopback0
   [~Leaf-LoopBack0] ipv6 enable
   [*Leaf-LoopBack0] ipv6 address 2001:DB8:30::2 128
   [*Leaf-LoopBack0] quit
   [*Leaf] interface loopback1
   [*Leaf-LoopBack1] ipv6 enable
   [*Leaf-LoopBack1] ipv6 address 2001:DB8:20::2 128
   [*Leaf-LoopBack1] quit
   [*Leaf] interface 100GE1/0/1
   [*Leaf-100GE1/0/1] undo portswitch
   [*Leaf-100GE1/0/1] ipv6 enable
   [*Leaf-100GE1/0/1] ipv6 address 2001:db8:1::3 64
   [*Leaf-100GE1/0/1] quit
   [*Leaf] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceB
   [*HUAWEI] commit
   [~DeviceB] interface loopback0
   [~DeviceB-LoopBack0] ipv6 enable
   [*DeviceB-LoopBack0] ipv6 address 2001:DB8:30::1 128
   [*DeviceB-LoopBack0] quit
   [*DeviceB] interface loopback1
   [*DeviceB-LoopBack1] ipv6 enable
   [*DeviceB-LoopBack1] ipv6 address 2001:DB8:40::2 128
   [*DeviceB-LoopBack1] quit
   [~DeviceB] interface 100GE1/0/1
   [*DeviceB-100GE1/0/1] undo portswitch
   [*DeviceB-100GE1/0/1] ipv6 enable
   [*DeviceB-100GE1/0/1] ipv6 address 2001:db8:1::4 64
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure Server.
   
   ```
   <HUAWEI> system-view
   [*HUAWEI] sysname Server
   [*HUAWEI] commit
   [~Server] interface loopback0
   [~Server-LoopBack0] ipv6 enable
   [*Server-LoopBack0] ipv6 address 2001:DB8:10::1 128
   [*Server-LoopBack0] quit
   [*Server] interface loopback1
   [*Server-LoopBack1] ipv6 enable
   [*Server-LoopBack1] ipv6 address 2001:DB8:40::1 128
   [*Server-LoopBack1] quit
   [*Server] interface 100GE1/0/1
   [*Server-100GE1/0/1] undo portswitch
   [*Server-100GE1/0/1] ipv6 enable
   [*Server-100GE1/0/1] ipv6 address 2001:db8:1::2 64
   [*Server-100GE1/0/1] quit
   [*Server] commit
   ```
2. Enable IS-IS.
   
   
   
   # Configure DeviceA.
   
   
   
   ```
   [~DeviceA] isis 1
   [*DeviceA-isis-1] cost-style wide
   [*DeviceA-isis-1] network-entity 10.0000.0000.0000.0001.00
   [*DeviceA-isis-1] ipv6 enable topology standard
   [*DeviceA-isis-1] quit
   [*DeviceA] interface loopback0
   [*DeviceA-LoopBack0] isis ipv6 enable 1
   [*DeviceA-LoopBack0] quit
   [*DeviceA] interface loopback1
   [*DeviceA-LoopBack1] isis ipv6 enable 1
   [*DeviceA-LoopBack1] quit
   [*DeviceA] interface 100GE1/0/1
   [*DeviceA-100GE1/0/1] isis ipv6 enable 1
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] commit
   ```
   
   # Configure Leaf.
   
   ```
   [~Leaf] isis 1
   [*Leaf-isis-1] cost-style wide
   [*Leaf-isis-1] network-entity 10.0000.0000.0000.0003.00
   [*Leaf-isis-1] ipv6 enable topology standard
   [*Leaf-isis-1] quit
   [*Leaf] interface loopback0
   [*Leaf-LoopBack0] isis ipv6 enable 1
   [*Leaf-LoopBack0] quit
   [*Leaf] interface loopback1
   [*Leaf-LoopBack1] isis ipv6 enable 1
   [*Leaf-LoopBack1] quit
   [*Leaf] interface 100GE1/0/1
   [*Leaf-100GE1/0/1] isis ipv6 enable 1
   [*Leaf-100GE1/0/1] quit
   [*Leaf] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   [*DeviceB-isis-1] cost-style wide
   [*DeviceB-isis-1] network-entity 10.0000.0000.0000.0004.00
   [*DeviceB-isis-1] ipv6 enable topology standard
   [*DeviceB-isis-1] quit
   [*DeviceB] interface loopback0
   [*DeviceB-LoopBack0] isis ipv6 enable 1
   [*DeviceB-LoopBack0] quit
   [*DeviceB] interface loopback1
   [*DeviceB-LoopBack1] isis ipv6 enable 1
   [*DeviceB-LoopBack1] quit
   [*DeviceB] interface 100GE1/0/1
   [*DeviceB-100GE1/0/1] isis ipv6 enable 1
   [*DeviceB-100GE1/0/1] quit
   [*DeviceB] commit
   ```
   
   # Configure Server.
   
   ```
   [~Server] isis 1
   [*Server-isis-1] cost-style wide
   [*Server-isis-1] network-entity 10.0000.0000.0000.0002.00
   [*Server-isis-1] ipv6 enable topology standard
   [*Server-isis-1] quit
   [*Server] interface loopback0
   [*Server-LoopBack0] isis ipv6 enable 1
   [*Server-LoopBack0] quit
   [*Server] interface loopback1
   [*Server-LoopBack1] isis ipv6 enable 1
   [*Server-LoopBack1] quit
   [*Server] interface 100GE1/0/1
   [*Server-100GE1/0/1] isis ipv6 enable 1
   [*Server-100GE1/0/1] quit
   [*Server] commit
   ```
3. Configure EBGP.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] router-id 11.11.11.11
   [*DeviceA-bgp] peer 2001:db8:20::2 as-number 200  
   [*DeviceA-bgp] peer 2001:db8:20::2 ebgp-max-hop 10
   [*DeviceA-bgp] peer 2001:db8:20::2 connect-interface LoopBack1
   [*DeviceA-bgp] peer 2001:db8:10::1 as-number 400
   [*DeviceA-bgp] peer 2001:db8:10::1 ebgp-max-hop 10
   [*DeviceA-bgp] peer 2001:db8:10::1 connect-interface LoopBack0
   [*DeviceA-bgp] ipv6-family unicast
   [*DeviceA-bgp-af-ipv6] peer 2001:db8:20::2 enable
   [*DeviceA-bgp-af-ipv6] peer 2001:db8:10::1 enable
   [*DeviceA-bgp-af-ipv6] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure Leaf.
   
   ```
   [~Leaf] bgp 200
   [*Leaf-bgp] router-id 22.22.22.22
   [*Leaf-bgp] peer 2001:db8:20::1 as-number 100
   [*Leaf-bgp] peer 2001:db8:20::1 ebgp-max-hop 10
   [*Leaf-bgp] peer 2001:db8:20::1 connect-interface LoopBack0
   [*Leaf-bgp] peer 2001:db8:30::1 as-number 300
   [*Leaf-bgp] peer 2001:db8:30::1 ebgp-max-hop 10
   [*Leaf-bgp] peer 2001:db8:30::1 connect-interface LoopBack1
   [*Leaf-bgp] ipv6-family unicast
   [*Leaf-bgp-af-ipv6] peer 2001:db8:20::1 enable
   [*Leaf-bgp-af-ipv6] peer 2001:db8:30::1 enable
   [*Leaf-bgp-af-ipv6] quit
   [*Leaf-bgp] quit
   [*Leaf] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 300
   [*DeviceB-bgp] router-id 33.33.33.33
   [*DeviceB-bgp] peer 2001:db8:30::2 as-number 200
   [*DeviceB-bgp] peer 2001:db8:30::2 ebgp-max-hop 10
   [*DeviceB-bgp] peer 2001:db8:30::2 connect-interface LoopBack0
   [*DeviceB-bgp] peer 2001:db8:40::1 as-number 400
   [*DeviceB-bgp] peer 2001:db8:40::1 ebgp-max-hop 10
   [*DeviceB-bgp] peer 2001:db8:40::1 connect-interface LoopBack1
   [*DeviceB-bgp] ipv6-family unicast
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:30::2 enable
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:40::1 enable
   [*DeviceB-bgp-af-ipv6] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```
   
   # Configure Server.
   
   ```
   [~Server] bgp 400
   [*Server-bgp] router-id 44.44.44.44
   [*Server-bgp] peer 2001:db8:10::2 as-number 100
   [*Server-bgp] peer 2001:db8:10::2 ebgp-max-hop 10
   [*Server-bgp] peer 2001:db8:10::2 connect-interface LoopBack0
   [*Server-bgp] peer 2001:db8:40::2 as-number 300
   [*Server-bgp] peer 2001:db8:40::2 ebgp-max-hop 10
   [*Server-bgp] peer 2001:db8:40::2 connect-interface LoopBack1
   [*Server-bgp] ipv6-family unicast
   [*Server-bgp-af-ipv6] peer 2001:db8:10::2 enable
   [*Server-bgp-af-ipv6] peer 2001:db8:40::2 enable
   [*Server-bgp-af-ipv6] quit
   [*Server-bgp] quit
   [*Server] commit
   ```
   
   # Check the connection status of BGP peers. The following uses DeviceA as an example.
   
   ```
   [~DeviceA] display bgp ipv6 peer
   Status codes: * - Dynamic
    BGP local router ID        : 11.11.11.11
    Local AS number            : 100
    Total number of peers      : 2
    Peers in established state : 2
    Total number of dynamic peers : 0
   
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     2001:DB8:10::1                   4         400       20       21     0 00:14:33 Established       0
     2001:DB8:20::2                   4         200       17       23     0 00:09:32 Established       0
   ```
4. Configure an IPv6 static route on Server and run the **network** command to import it.
   
   
   ```
   [~Server] ipv6 route-static 2001:db8:1::1 128 NULLO
   [*Server] commit
   [~Server] bgp 400
   [*Server-bgp] ipv6-family unicast
   [*Server-bgp-af-ipv6] network 2001:db8:1::1 128
   [*Server-bgp-af-ipv6] quit
   [*Server-bgp] quit
   [*Server] commit
   ```
5. Configure the BGP4+ SoO function.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] bgp 100
   [*DeviceA-bgp] ipv6-family unicast
   [*DeviceA-bgp-af-ipv6] peer 2001:db8:20::2 soo-reverse 10:10
   [*DeviceA-bgp-af-ipv6] peer 2001:db8:20::2 advertise-ext-community  
   [*DeviceA-bgp-af-ipv6] quit
   [*DeviceA-bgp] quit
   [*DeviceA] commit
   ```
   
   # Configure Leaf.
   
   ```
   [~Leaf] bgp 200
   [*Leaf-bgp] ipv6-family unicast
   [*Leaf-bgp-af-ipv6] peer 2001:db8:30::1 advertise-ext-community
   [*Leaf-bgp-af-ipv6] quit
   [*Leaf-bgp] quit
   [*Leaf] commit
   ```
   
   # Check the BGP4+ routing table of DeviceA. The command output shows that the SoO attribute 10:10 has been added to the route sent by DeviceA.
   
   ```
   [~DeviceA] display bgp ipv6 routing-table peer 2001:db8:20::2 advertised-routes 2001:db8:1::1
   
    BGP local router ID : 11.11.11.11
    Local AS number : 100
    BGP routing table entry information of 2001:db8:1::1/128:
    From: 2001:db8:10::1 (2001:db8:10::1)
    Route Duration: 0d00h14m11s
    Relay IP Nexthop: FE80::3A71:1FF:FE41:300
    Relay IP Out-Interface: 100GE1/0/1
    Original nexthop: 2001:DB8:10::1
    Advertised nexthop: 2001:DB8:20::1
    Ext-Community: SoO <10 : 10>
    AS-path 100 400, origin igp, pref-val 0, valid, external, best, select, pre 255, IGP cost 10
    Advertised to such 1 peers:
       2001:DB8:20::2
   ```
   
   # Check whether DeviceB can receive the route 2001:db8:1::1/128 that carries the SoO attribute.
   
   ```
   [~DeviceB] display bgp routing-table peer 2001:db8:30::2 received-routes 2001:db8:1::1
   
    BGP local router ID : 33.33.33.33
    Local AS number : 300
    BGP routing table entry information of 2001:db8:1::1/128:
    From: 2001:db8:30::2 (2001:db8:30::2)  
    Relay IP Nexthop: FE80::3A71:1FF:FE21:300
    Relay IP Out-Interface: 100GE1/0/1
    Original nexthop: 2001:DB8:30::2
    Qos information : 0x0
    Ext-Community: SoO <10 : 10>
    AS-path 200 100 400, origin igp, pref-val 0, valid, external, pre 255, IGP cost 10, not preferred for AS-Path
    Not advertised to any peer yet
   ```
   
   
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] bgp 300
   [*DeviceB-bgp] ipv6-family unicast
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:30::2 soo-reverse 10:10
   [*DeviceB-bgp-af-ipv6] quit
   [*DeviceB-bgp] quit
   [*DeviceB] commit
   ```

#### Verifying the Configuration

# Check the BGP4+ routing table of DeviceB. The **display bgp routing-table peer 2001:db8:30::2 received-routes 2001:db8:1::1** command output has no route information displayed. According to the **display bgp routing-table 2001:db8:1::1** command output, DeviceB discards the route received from 2001:db8:30::2 and accepts the route received from 2001:db8:40::1 after the BGP4+ SoO attribute is configured.
```
[~DeviceB] display bgp routing-table 2001:db8:1::1 128

 BGP local router ID : 33.33.33.33
 Local AS number : 300
 Paths:   1 available, 1 best, 1 select, 0 best-external, 0 add-path
 BGP routing table entry information of 2001:db8:1::1/128:
 From: 2001:DB8:40::1 (2001:DB8:40::1)
 Route Duration: 0d00h06m39s
 Relay IP Nexthop: FE80::3A71:1FF:FE41:300
 Relay IP Out-Interface: 100GE1/0/1
 Original nexthop: 2001:DB8:40::1
 Qos information : 0x0
 AS-path 400, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255, IGP cost 10
 Advertised to such 1 peers:
    2001:DB8:30::2
```


#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0000.0001.00
   #
   ipv6 enable topology standard
   #
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64       
   isis ipv6 enable 1        
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:db8:10::2/128
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:20::1/128
   isis ipv6 enable 1
  #
  bgp 100
   private-4-byte-as enable
   peer 2001:DB8:10::1 as-number 400
   peer 2001:DB8:10::1 ebgp-max-hop 10
   peer 2001:DB8:10::1 connect-interface LoopBack0
   peer 2001:DB8:20::2 as-number 200
   peer 2001:DB8:20::2 ebgp-max-hop 10
   peer 2001:DB8:20::2 connect-interface LoopBack1
   #
   ipv4-family unicast
   #
   ipv6-family unicast
    peer 2001:DB8:10::1 enable
    peer 2001:DB8:20::2 enable
    peer 2001:DB8:20::2 soo-reverse 10:10
    peer 2001:DB8:20::2 advertise-ext-community
  #
  return
  ```
* Leaf
  
  ```
  #
  sysname Leaf
  #
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0000.0003.00
   #
   ipv6 enable topology standard
   #
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::3/64       
   isis ipv6 enable 1 
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:30::2/128
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:20::2/128
   isis ipv6 enable 1
  #
  bgp 200
   private-4-byte-as enable
   peer 2001:DB8:20::1 as-number 100
   peer 2001:DB8:20::1 ebgp-max-hop 10
   peer 2001:DB8:20::1 connect-interface LoopBack1
   peer 2001:DB8:30::1 as-number 300
   peer 2001:DB8:30::1 ebgp-max-hop 10
   peer 2001:DB8:30::1 connect-interface LoopBack0
   #
   ipv4-family unicast
   #
   ipv6-family unicast
    peer 2001:DB8:20::1 enable
    peer 2001:DB8:30::1 enable
    peer 2001:DB8:30::1 advertise-ext-community
  #
  return
  ```
* DeviceB
  ```
  #
  sysname DeviceB
  #
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0000.0004.00
   #
   ipv6 enable topology standard
   #
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::4/64      
   isis ipv6 enable 1
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:30::1/128
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:40::2/128
   isis ipv6 enable 1
  #
  bgp 300
   private-4-byte-as enable
   peer 2001:DB8:30::2 as-number 200
   peer 2001:DB8:30::2 ebgp-max-hop 10
   peer 2001:DB8:30::2 connect-interface LoopBack0
   peer 2001:DB8:40::1 as-number 400
   peer 2001:DB8:40::1 ebgp-max-hop 10
   peer 2001:DB8:40::1 connect-interface LoopBack1
   #
   ipv4-family unicast
   #
   ipv6-family unicast
    peer 2001:DB8:30::2 enable
    peer 2001:DB8:30::2 soo-reverse 10:10
    peer 2001:DB8:40::1 enable
  #
  return
  ```
* Server
  
  ```
  #
  sysname Server
  #
  isis 1
   cost-style wide
   network-entity 10.0000.0000.0000.0002.00
   #
   ipv6 enable topology standard
   #
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::2/64   
   isis ipv6 enable 1
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:DB8:10::1/128
   isis ipv6 enable 1
  #
  interface LoopBack1
   ipv6 enable
   ipv6 address 2001:DB8:40::1/128
   isis ipv6 enable 1
  #
  bgp 400
   private-4-byte-as enable
   peer 2001:DB8:10::2 as-number 100
   peer 2001:DB8:10::2 ebgp-max-hop 10
   peer 2001:DB8:10::2 connect-interface LoopBack0
   peer 2001:DB8:40::2 as-number 300
   peer 2001:DB8:40::2 ebgp-max-hop 10
   peer 2001:DB8:40::2 connect-interface LoopBack1
   #
   ipv4-family unicast
   #
   ipv6-family unicast
    network 2001:db8:1::1 128            
    peer 2001:DB8:10::2 enable
    peer 2001:DB8:40::2 enable
  #
  ipv6 route-static 2001:db8:1::1 128 NULL0   
  #
  return
  ```