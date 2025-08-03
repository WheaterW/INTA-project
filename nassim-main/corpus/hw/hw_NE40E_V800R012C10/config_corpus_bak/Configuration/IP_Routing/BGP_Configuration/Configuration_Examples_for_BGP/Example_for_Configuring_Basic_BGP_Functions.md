Example for Configuring Basic BGP Functions
===========================================

Before building BGP networks, you need to configure basic BGP functions.

#### Networking Requirements

If multiple ASs want to access each other, these ASs must exchange their local routes. If multiple Routers exist in the ASs, a great deal of routing information will be exchanged between ASs, which consumes lots of bandwidth resources. To address this issue, you can configure basic BGP functions.

In [Figure 1](#EN-US_TASK_0172366356__fig_dc_vrp_bgp_cfg_407101), Device A is in AS 65008. Device B, Device C, and Device D are in AS 65009. The routing tables of these routers store many routes, and the routes change frequently. After BGP is enabled on the Routers, they can exchange routing information. If routes of one Router changes, the Router sends Update messages carrying only changed routing information to its peers, which greatly reduces bandwidth consumption.

**Figure 1** Configuring basic BGP functions![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example are GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_bgp_cfg_407101.png)

| Device Name | Interface | IP Address |
| --- | --- | --- |
| Device A | Loopback 0 | 1.1.1.1/32 |
| GE 0/1/0 | 172.16.0.1/16 |
| GE 0/2/0 | 192.168.0.1/24 |
| Device B | Loopback 0 | 2.2.2.2/32 |
| GE 0/1/0 | 10.1.1.1/24 |
| GE 0/2/0 | 192.168.0.2/24 |
| GE 0/3/0 | 10.1.3.1/24 |
| Device C | Loopback 0 | 3.3.3.3/32 |
| GE 0/2/0 | 10.1.2.1/24 |
| GE 0/3/0 | 10.1.3.2/24 |
| Device D | Loopback 0 | 4.4.4.4/32 |
| GE 0/1/0 | 10.1.1.2/24 |
| GE 0/2/0 | 10.1.2.2/24 |





#### Precautions

During the configuration, note the following:

* Before establishing a BGP peer relationship, ensure that BGP peers are reachable to each other through IGP routes. In this way, the BGP peers can exchange routing information.
* If the peer IP address specified during peer relationship establishment is a loopback interface address or a sub-interface IP address, you need to run the **peer connect-interface** command on both ends to ensure that the two ends are correctly connected.
* If there is no directly connected physical link between EBGP peers, run the **peer ebgp-max-hop** command to allow EBGP peers to establish TCP connections through multiple hops.
* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish IGP connections among Device B, Device C, and Device D. (OSPF is used as the IGP in this example.)
2. Establish IBGP connections between Device B, Device C, and Device D.
3. Establish an EBGP connection between Device A and Device B.
4. Run the **network** command on Device A to advertise routes, and then check the routing tables of Device A, Device B, and Device C.
5. Configure BGP on Device B to import direct routes, and then check the routing tables of Device A and Device C.

#### Data Preparation

To complete the configuration, you need the following data:

* Router ID and AS number of Device A
* Router IDs and AS numbers of Device B, Device C, and Device D

#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172366356__section_dc_vrp_bgp_cfg_407105) in this section.
2. Configure OSPF.
   
   
   
   # Configure Device B.
   
   ```
   [~DeviceB] ospf 1
   ```
   ```
   [*DeviceB-ospf-1] area 0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 10.1.3.0 0.0.0.255
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] network 2.2.2.2 0.0.0.0
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceB-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceB-ospf-1] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] ospf 1
   ```
   ```
   [*DeviceC-ospf-1] area 0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 10.1.3.0 0.0.0.255
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] network 3.3.3.3 0.0.0.0
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceC-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceC-ospf-1] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] ospf 1
   ```
   ```
   [*DeviceD-ospf-1] area 0
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] network 10.1.1.0 0.0.0.255
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] network 10.1.2.0 0.0.0.255
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] network 4.4.4.4 0.0.0.0
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.0] commit
   ```
   ```
   [~DeviceD-ospf-1-area-0.0.0.0] quit
   ```
   ```
   [~DeviceD-ospf-1] quit
   ```
3. Configure IBGP connections.
   
   
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 65009
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 3.3.3.3 as-number 65009
   ```
   ```
   [*DeviceB-bgp] peer 4.4.4.4 as-number 65009
   ```
   ```
   [*DeviceB-bgp] peer 3.3.3.3 connect-interface LoopBack0
   ```
   ```
   [*DeviceB-bgp] peer 4.4.4.4 connect-interface LoopBack0
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] bgp 65009
   ```
   ```
   [*DeviceC-bgp] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-bgp] peer 2.2.2.2 as-number 65009
   ```
   ```
   [*DeviceC-bgp] peer 4.4.4.4 as-number 65009
   ```
   ```
   [*DeviceC-bgp] peer 2.2.2.2 connect-interface LoopBack0
   ```
   ```
   [*DeviceC-bgp] peer 4.4.4.4 connect-interface LoopBack0
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
   
   # Configure Device D.
   
   ```
   [~DeviceD] bgp 65009
   ```
   ```
   [*DeviceD-bgp] router-id 4.4.4.4
   ```
   ```
   [*DeviceD-bgp] peer 2.2.2.2 as-number 65009
   ```
   ```
   [*DeviceD-bgp] peer 3.3.3.3 as-number 65009
   ```
   ```
   [*DeviceD-bgp] peer 2.2.2.2 connect-interface LoopBack0
   ```
   ```
   [*DeviceD-bgp] peer 3.3.3.3 connect-interface LoopBack0
   ```
   ```
   [*DeviceD-bgp] commit
   ```
   ```
   [~DeviceD-bgp] quit
   ```
4. Configure an EBGP connection.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bgp 65008
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 192.168.0.2 as-number 65009
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 65009
   ```
   ```
   [*DeviceB-bgp] peer 192.168.0.1 as-number 65008
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Check the status of BGP connections.
   
   ```
   [~DeviceB] display bgp peer
   
    BGP local router ID : 2.2.2.2
    Local AS number : 65009
    Total number of peers : 3                 Peers in established state : 3
   
     Peer            V    AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv
     3.3.3.3         4 65009        5        5     0 00:44:58 Established       0
     4.4.4.4         4 65009        4        4     0 00:40:54 Established       0
     192.168.0.1     4 65008        3        3     0 00:44:03 Established       0
   ```
   
   The command output shows that Device B has established BGP connections with other Routers and that the connection state is Established.
5. Configure Device A to advertise the route 172.16.0.0/16.
   
   
   
   # Configure Device A to advertise the route.
   
   ```
   [~DeviceA] bgp 65008
   ```
   ```
   [*DeviceA-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv4] network 172.16.0.0 255.255.0.0
   ```
   ```
   [*DeviceA-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceA-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Check the routing table of Device A.
   
   ```
   [~DeviceA] display bgp routing-table
   
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
    
   
    Total Number of Routes: 1
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   172.16.0.0          0.0.0.0         0                     0      i
   ```
   
   # Check the routing table of Device B.
   
   ```
   [~DeviceB] display bgp routing-table
   
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 1
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   172.16.0.0          192.168.0.1    0                     0      65008i
   ```
   
   # Check the routing table of Device C.
   
   ```
   [~DeviceC] display bgp routing-table
   
    BGP Local router ID is 3.3.3.3
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 1
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
      i  172.16.0.0          192.168.0.1    0          100        0      65008i
   ```
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The command output shows that Device C has learned the route 172.16.0.0 from AS 65008. However, this route is invalid because the next hop 192.168.0.1 is unreachable.
6. Configure BGP to import direct routes.
   
   
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 65009
   ```
   ```
   [*DeviceB-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv4] import-route direct
   ```
   ```
   [*DeviceB-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceB-bgp-af-ipv4] quit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Check the BGP routing table of Device A.
   
   ```
   [~DeviceA] display bgp routing-table
   
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 5
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
    *>   2.2.2.2/32         192.168.0.2     0                     0      65009?
    *>   172.16.0.0          0.0.0.0         0                     0      i
    *>   10.1.1.0/24        192.168.0.2     0                     0      65009?
    *>   10.1.3.0/24        192.168.0.2     0                     0      65009?
    *>   192.168.0.0        192.168.0.2     0                     0      65009?
   ```
   
   # Check the routing table of Device C.
   
   ```
   [~DeviceC] display bgp routing-table
   
    BGP Local router ID is 3.3.3.3
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 5
         Network            NextHop        MED        LocPrf    PrefVal Path/Ogn
   
      i  2.2.2.2/32         2.2.2.2         0          100        0      ?
    *>i  10.1.1.0/24        2.2.2.2         0          100        0      ?
    * i  10.1.3.0/24        2.2.2.2         0          100        0      ?
    *>i  172.16.0.0         192.168.0.1     0          100        0      65008i
    *>i  192.168.0.0        2.2.2.2         0          100        0      ?
   ```
   
   The command output shows that the route 172.16.0.0 becomes valid and that the next hop is the address of Device A.
   
   # Verify the configuration using the **ping** command.
   
   ```
   [~DeviceC] ping 172.16.0.1
     PING 172.16.0.1: 56  data bytes, press CTRL_C to break
       Reply from 172.16.0.1: bytes=56 Sequence=1 ttl=254 time=31 ms
       Reply from 172.16.0.1: bytes=56 Sequence=2 ttl=254 time=47 ms
       Reply from 172.16.0.1: bytes=56 Sequence=3 ttl=254 time=31 ms
       Reply from 172.16.0.1: bytes=56 Sequence=4 ttl=254 time=16 ms
       Reply from 172.16.0.1: bytes=56 Sequence=5 ttl=254 time=31 ms
     --- 172.16.0.1 ping statistics ---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max = 16/31/47 ms
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceA
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 172.16.0.1 255.255.0.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.0.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 1.1.1.1 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 65008
  ```
  ```
   router-id 1.1.1.1
  ```
  ```
   peer 192.168.0.2 as-number 65009
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    network 172.16.0.0 255.255.0.0
  ```
  ```
    peer 192.168.0.2 enable
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device B configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceB
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 192.168.0.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.3.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 2.2.2.2 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 65009
  ```
  ```
   router-id 2.2.2.2
  ```
  ```
   peer 3.3.3.3 as-number 65009
  ```
  ```
   peer 3.3.3.3 connect-interface LoopBack0
  ```
  ```
   peer 4.4.4.4 as-number 65009
  ```
  ```
   peer 4.4.4.4 connect-interface LoopBack0
  ```
  ```
   peer 192.168.0.1 as-number 65008
  ```
  ```
  #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    import-route direct
  ```
  ```
    peer 3.3.3.3 enable
  ```
  ```
    peer 4.4.4.4 enable 
  ```
  ```
    peer 192.168.0.1 enable
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 2.2.2.2 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.1.3.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device C configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceC
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.1 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/3/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.3.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 3.3.3.3 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 65009
  ```
  ```
   router-id 3.3.3.3
  ```
  ```
   peer 2.2.2.2 as-number 65009
  ```
  ```
   peer 2.2.2.2 connect-interface LoopBack0
  ```
  ```
   peer 4.4.4.4 as-number 65009
  ```
  ```
   peer 4.4.4.4 connect-interface LoopBack0
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    peer 2.2.2.2 enable
  ```
  ```
    peer 4.4.4.4 enable
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 3.3.3.3 0.0.0.0
  ```
  ```
    network 10.1.2.0 0.0.0.255
  ```
  ```
    network 10.1.3.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```
* Device D configuration file
  
  ```
  #
  ```
  ```
  sysname DeviceD
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.1.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface GigabitEthernet0/2/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.2.2 255.255.255.0
  ```
  ```
  #
  ```
  ```
  interface LoopBack0
  ```
  ```
   ip address 4.4.4.4 255.255.255.255
  ```
  ```
  #
  ```
  ```
  bgp 65009
  ```
  ```
   router-id 4.4.4.4
  ```
  ```
   peer 2.2.2.2 as-number 65009
  ```
  ```
   peer 2.2.2.2 connect-interface LoopBack0
  ```
  ```
   peer 3.3.3.3 as-number 65009
  ```
  ```
   peer 3.3.3.3 connect-interface LoopBack0
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    peer 2.2.2.2 enable
  ```
  ```
    peer 3.3.3.3 enable
  ```
  ```
  #
  ```
  ```
  ospf 1
  ```
  ```
   area 0.0.0.0
  ```
  ```
    network 4.4.4.4 0.0.0.0
  ```
  ```
    network 10.1.1.0 0.0.0.255
  ```
  ```
    network 10.1.2.0 0.0.0.255
  ```
  ```
  #
  ```
  ```
  return
  ```