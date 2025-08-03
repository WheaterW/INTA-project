Example for Configuring OSPFv3 Delay Reporting to BGP-LS
========================================================

OSPFv3 delay is reported to BGP-LS, which summarizes the topology information collected by IGPs and sends the information to the upper-layer controller for delay-based path computation.

#### Networking Requirements

BGP-LS is a new method of collecting network topology information. The topology information discovered by IGPs is summarized and reported to an upper-layer controller through BGP. With powerful routing capabilities of BGP, BGP-LS has the following advantages:

* Lowers the requirements on the controller's computing capabilities and no longer requires IGP capabilities on the controller.
* Facilitates route selection and computation on the controller by using BGP to summarize process or AS topology information and report the complete information to the controller.
* Requires only one routing protocol (BGP) to report topology information to the controller.

In [Figure 1](#EN-US_TASK_0000001579446269__fig_dc_vrp_bgp_cfg_409701), DeviceC is connected to the controller and reports topology information to the controller. DeviceA, DeviceB, DeviceC, and DeviceD use OSPFv3 to implement IP network interworking. The two interfaces connecting DeviceC and DeviceD belong to area 20, and the interfaces connecting DeviceA, DeviceB, and DeviceC belong to area 10.

**Figure 1** Configuring BGP-LS![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, interface3, and interface4 in this example represent GigabitEthernet0/1/1, GigabitEthernet0/1/2, GigabitEthernet0/1/3, and GigabitEthernet0/1/4, respectively.


  
![](figure/en-us_image_0000001528846254.png)

#### Precautions

To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses for interfaces on each device.
2. Configure basic OSPFv3 functions.
3. Deploy BGP-LS on DeviceC and the controller.
4. Configure the TWAMP Light Controller and TWAMP Light Responder on DeviceA and DeviceC, respectively.
5. Configure the TE function.
6. Configure delay advertisement on DeviceA.

#### Data Preparation

To complete the configuration, you need the following data:

* IPv6 addresses and areas of interfaces on DeviceA, DeviceB, DeviceC, and DeviceD
* BGP-LS ID in OSPFv3 on DeviceC
* BGP AS numbers, BGP-LS domain AS numbers, and BGP-LS domain IDs of Device C and the controller

#### Procedure

1. Assign an IPv6 address to each interface on each device. For configuration details, see [Configuration Files](#EN-US_TASK_0000001579446269__section_dc_vrp_bgp_cfg_409705) in this section.
2. Configure basic OSPFv3 functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospfv3-1] area 0.0.0.10
   ```
   ```
   [*DeviceA-ospfv3-1-area-0.0.0.10] quit
   ```
   ```
   [*DeviceA-ospfv3-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ospfv3 1 area 0.0.0.10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ospfv3 network-type p2p
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospfv3 1
   ```
   ```
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-ospfv3-1] area 0.0.0.10
   ```
   ```
   [*DeviceB-ospfv3-1-area-0.0.0.10] quit
   ```
   ```
   [*DeviceB-ospfv3-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/4
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/4] ospfv3 1 area 0.0.0.10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/4] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/4] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospfv3 1
   ```
   ```
   [*DeviceC-ospfv3-1] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-ospfv3-1] area 0.0.0.10
   ```
   ```
   [*DeviceC-ospfv3-1-area-0.0.0.10] quit
   ```
   ```
   [*DeviceC-ospfv3-1] area 0.0.0.20
   ```
   ```
   [*DeviceC-ospfv3-1-area-0.0.0.20] quit
   ```
   ```
   [*DeviceC-ospfv3-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] ospfv3 1 area 0.0.0.10
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] ospfv3 network-type p2p
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/3] ospfv3 1 area 0.0.0.20
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/4
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/4] ospfv3 1 area 0.0.0.10
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/4] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/4] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] ospfv3 1
   ```
   ```
   [*DeviceD-ospfv3-1] router-id 4.4.4.4
   ```
   ```
   [*DeviceD-ospfv3-1] area 0.0.0.20
   ```
   ```
   [*DeviceD-ospfv3-1-area-0.0.0.20] quit
   ```
   ```
   [*DeviceD-ospfv3-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] ospfv3 1 area 0.0.0.20
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceD] interface LoopBack0
   ```
   ```
   [*DeviceD-LoopBack0] ospfv3 1 area 0.0.0.20
   ```
   ```
   [*DeviceD-LoopBack0] commit
   ```
   ```
   [~DeviceD-LoopBack0] quit
   ```
3. Deploy BGP-LS on DeviceC and the controller.
   
   
   
   # Enable OSPFv3 topology advertisement on DeviceC.
   
   ```
   [~DeviceC] ospfv3 1
   ```
   ```
   [*DeviceC-ospfv3-1] bgp-ls enable
   ```
   ```
   [*DeviceC-ospfv3-1] bgp-ls identifier 20
   ```
   ```
   [*DeviceC-ospfv3-1] commit
   ```
   ```
   [~DeviceC-ospfv3-1] quit
   ```
   
   # Enable BGP-LS on DeviceC and establish a BGP-LS peer relationship with the controller.
   
   ```
   [~DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] peer 10.0.0.2 as-number 100
   ```
   ```
   [*DeviceC-bgp] link-state-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ls] peer 10.0.0.2 enable
   ```
   ```
   [*DeviceC-bgp-af-ls] commit
   ```
   ```
   [~DeviceC-bgp-af-ls] quit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
   
   # Enable BGP-LS on the controller and establish a BGP-LS peer relationship with DeviceC.
   
   ```
   [~Controller] bgp 100
   ```
   ```
   [*Controller-bgp] peer 10.0.0.1 as-number 100
   ```
   ```
   [*Controller-bgp] link-state-family unicast
   ```
   ```
   [*Controller-bgp-af-ls] peer 10.0.0.1 enable
   ```
   ```
   [*Controller-bgp-af-ls] commit
   ```
   ```
   [~Controller-bgp-af-ls] quit
   ```
   ```
   [~Controller-bgp] quit
   ```
4. Configure the TWAMP Light Controller and TWAMP Light Responder on DeviceA and DeviceC, respectively.
   
   
   
   # Configure the TWAMP Light Controller on DeviceA.
   
   ```
   [~DeviceA] nqa twamp-light
   ```
   ```
   [*DeviceA-twamp-light] client
   ```
   ```
   [*DeviceA-twamp-light-client] test-session 1 sender-ipv6 2001:db8:13::1 reflector-ipv6 2001:db8:13::3 sender-port 862 reflector-port 862
   ```
   ```
   [*DeviceA-twamp-light-client] test-session 1 bind interface GigabitEthernet 0/1/2
   ```
   ```
   [*DeviceA-twamp-light-client] quit
   ```
   ```
   [*DeviceA-twamp-light] sender
   ```
   ```
   [*DeviceA-twamp-light-sender] test start-continual test-session 1 period 1000
   ```
   ```
   [*DeviceA-twamp-light-sender] commit
   ```
   ```
   [~DeviceA-twamp-light-sender] quit
   ```
   ```
   [~DeviceA-twamp-light] quit
   ```
   
   # Configure the TWAMP Light Responder on DeviceC.
   
   ```
   [~DeviceC] nqa twamp-light
   ```
   ```
   [*DeviceC-twamp-light] responder
   ```
   ```
   [*DeviceC-twamp-light-responder] test-session 1 local-ipv6 2001:db8:13::3 remote-ipv6 2001:db8:13::1 local-port 862 remote-port 862
   ```
   ```
   [*DeviceC-twamp-light-responder] commit
   ```
   ```
   [~DeviceC-twamp-light-responder] quit
   ```
   ```
   [~DeviceC-twamp-light] quit
   ```
5. Configure TE on DeviceA.
   
   
   ```
   [~DeviceA] te attribute enable
   ```
   ```
   [*DeviceA] commit
   ```
6. Enable TE for the OSPFv3 area on DeviceA.
   
   
   ```
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospfv3-1] area 0.0.0.10
   ```
   ```
   [*DeviceA-ospfv3-1-area-0.0.0.10] traffic-eng enable
   ```
   ```
   [*DeviceA-ospfv3-1-area-0.0.0.10] commit
   ```
7. Configure delay advertisement on DeviceA.
   
   
   ```
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospf-1] metric-delay advertisement enable
   ```
   ```
   [*DeviceA-ospf-1] commit
   ```
8. Verify the configuration.
   
   
   
   # Display information about BGP-LS peers and their status on DeviceC.
   
   ```
   [~DeviceC] display bgp link-state unicast peer
   ```
   ```
    BGP local router ID : 10.0.0.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
    
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     10.0.0.2                         4         100        5        9     0 00:00:55 Established        0
   ```
   
   # Check the delay information advertised by OSPFv3 on DeviceC.
   
   ```
   [~DeviceC] display ospfv3 traffic-eng
   ```
   ```
             OSPFv3 Process 1 with Router ID 3.3.3.3  
   
    Area ID                   : 0.0.0.10
   
    Traffic Engineering LSAs of the database
   
    ------------------------------------------------
   
    LSA  [1]
    Last Receive TimeStamp   : 0000-00-00 00:00:00
    Last Update TimeStamp    : 2023-04-21 01:27:50
    ------------------------------------------------
    Lsa  Type                : Intra-Area-TE                                          
    Link State Id            : 0.0.0.0                                                
    Advertising Router Id    : 1.1.1.1
    Length                   : 40
   
    Router IPv6 Address      : 2001:DB8:1::1  
   
    ------------------------------------------------
   
    LSA  [2]
    Last Receive TimeStamp   : 0000-00-00 00:00:00
    Last Update TimeStamp    : 2023-04-21 01:28:22
    ------------------------------------------------
    Lsa  Type                : Intra-Area-TE                                          
    Link State Id            : 0.0.0.1                                                
    Advertising Router Id    : 1.1.1.1
    Length                   : 160
    Link Type                : P2P                                    
    Neighbor Interface Id    : 14
    Neighbor Router Id       : 3.3.3.3
    Local Interface IPv6 Address  : 2001:db8:13::1
    TE Metric                : 1                                      
    Maximum Bandwidth        : 12500000 bytes/sec                                       
    Maximum Reservable BW    : 0 bytes/sec                                       
    Admin Group              : 0x0
    Global Pool              :
       Unreserved BW [ 0] =                        0  bytes/sec                                          
       Unreserved BW [ 1] =                        0  bytes/sec                                          
       Unreserved BW [ 2] =                        0  bytes/sec                                          
       Unreserved BW [ 3] =                        0  bytes/sec                                          
       Unreserved BW [ 4] =                        0  bytes/sec                                          
       Unreserved BW [ 5] =                        0  bytes/sec                                          
       Unreserved BW [ 6] =                        0  bytes/sec                                          
       Unreserved BW [ 7] =                        0  bytes/sec  
    Min/Max Unidirectional Link Delay:
       Anomalous (A) Bit: 0
       Min Delay: 2220 (us)
       Max Delay: 4240 (us)
   ```
   
   # Check BGP-LS routes on DeviceC.
   
   ```
   [~DeviceC] display bgp link-state unicast routing-table [LINK][OSPFv3][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.0.0.1][ospf-area-id0.0.0.10][igp-router-id1.1.1.1]][REMOTE[as100][bgp-ls-identifier10.0.0.1][ospf-area-id0.0.0.10][igp-router-id3.3.3.3]][LINK[if-address0.0.0.0][peer-address0.0.0.0][if-address2001:db8:13::1][peer-address2001:db8:13::3]]
   ```
   ```
    BGP Local router ID is 10.1.1.1 
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path, 
                  h - history,  i - internal, s - suppressed, S - Stale 
                  Origin : i - IGP, e - EGP, ? - incomplete 
   
    BGP local router ID : 3.3.3.3 
    Local AS number : 100 
    Paths:   1 available, 1 best, 1 select 
    BGP routing table entry information of [LINK][OSPFv3][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.0.0.1][ospf-area-id0.0.0.10][igp-router-id1.1.1.1]][REMOTE[as100][bgp-ls-identifier10.0.0.1][ospf-area-id0.0.0.10][igp-router-id3.3.3.3]][LINK[if-address0.0.0.0][peer-address0.0.0.0][if-address2001:db8:13::1][peer-address2001:db8:13::3]]: 
    Imported route. 
    From: 0.0.0.0 (0.0.0.0) 
    Route Duration: 0d00h09m59s 
    Direct Out-interface: 
    Original nexthop: 0.0.0.0 
    AS-path Nil, origin incomplete, MED 0, pref-val 0, valid, local, best, select, pre 255 
    Link-state Route Type: LINK 
    Protocol: OSPFv3 
    Identifier: 20 
    Local Node Descriptor: 
     AS Number: 100 
     BGP Identifier: 10.0.0.1 
     OSPF Area ID: 0.0.0.10 
     IGP Router ID: 1.1.1.1 
    Remote Node Descriptor: 
     AS Number: 100 
     BGP Identifier: 10.0.0.1 
     OSPF Area ID: 0.0.0.10 
     IGP Router ID: 3.3.3.3 
    Link Descriptor: 
     IPv4 interface address: 0.0.0.0 
     IPv4 neighbor address: 0.0.0.0 
     IPv6 interface address: 2001:db8:13::1 
     IPv6 neighbor address: 2001:db8:13::3 
    Link-state attribute: 
     IPv4 Router ID of Local Node: 
     IPv6 Router ID of Local Node: 
     IPv4 Router ID of Remote Node: 
     IPv6 Router ID of Remote Node: 
     Administrative group: 0x0 
     Maximum link bandwidth(kbits/sec): 0 
     Maximum reservable link bandwidth(kbits/sec): 0 
     Maximum Unreserved bandwidth(kbits/sec): 0 0 0 0 0 0 0 0 
     TE Default Metric: 0 
     Link Protection Type: Null 
     MPLS Protocol Mask: 0x0 
     IGP Metric: 1 
     Shared Risk Link Group: 
     Min/Max Unidirectional Link Delay(microseconds): 912/5503 
     Opaque link Properties: 
     Link Name: 
     Adjacency Segment Identifier(Flags/Weight/SID): 
     LAN Adjacency Segment Identifier(Flags/Weight/System-ID/SID): 
     SRv6 End.X SID(EndPoint Behavior/Flags/Algorithm/Weight/SID)(SID Structure): 
     SRv6 LAN End.X SID(EndPoint Behavior/Flags/Algorithm/Weight/Neighbor ID/SID)(SID Structure): 
     MSD([MSD Type, MSD Value]): 
    Advertised to such 1 peers: 
       10.0.0.2 
   ```
   
   The preceding command output shows that DeviceC obtains the topology information on the whole OSPFv3 network. DeviceC can use BGP-LS routes to report the topology information to its BGP-LS peer (the controller).

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  te attribute enable
  #
  ospfv3 1
   router-id 1.1.1.1
   metric-delay advertisement enable 
   area 0.0.0.10 
    traffic-eng enable
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:13::1/64
   ospfv3 network-type p2p 
   ospfv3 1 area 0.0.0.10 
  #
  nqa twamp-light 
   client 
    test-session 1 sender-ipv6 2001:db8:13::1 reflector-ipv6 2001:db8:13::3 sender-port 862 reflector-port 862 
    test-session 1 bind interface GigabitEthernet 0/1/2
   sender
    test start-continual test-session 1 period 1000 
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  ospfv3 1 
   router-id 2.2.2.2 
   area 0.0.0.10 
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:23::2/64
   ospfv3 1 area 0.0.0.10
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  ospfv3 1 
   router-id 3.3.3.3
   bgp-ls enable
   bgp-ls identifier 20 
   area 0.0.0.10
   area 0.0.0.20
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.0.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:13::3/64
   ospfv3 network-type p2p
   ospfv3 1 area 0.0.0.10
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:34::3/64
   ospfv3 1 area 0.0.0.20
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:23::3/64
   ospfv3 1 area 0.0.0.10
  #
  bgp 100
   peer 10.0.0.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization 
    peer 10.0.0.2 enable
   #
   link-state-family unicast
    peer 10.0.0.2 enable
  #
  nqa twamp-light 
   responder 
    test-session 1 local-ipv6 2001:db8:13::3 remote-ipv6 2001:db8:13::1 local-port 862 remote-port 862 
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  ospfv3 1
   router-id 4.4.4.4 
   area 0.0.0.20 
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable 
   ipv6 address 2001:db8:34::4/64 
   ospfv3 1 area 0.0.0.20 
  #
  interface LoopBack0
   ipv6 enable 
   ipv6 address 2001:db8:4::4/128 
   ospfv3 1 area 0.0.0.20 
  #
  return
  ```
* Controller configuration file
  
  ```
  #
  sysname Controller
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 10.0.0.2 255.255.255.0
  #
  bgp 100
   peer 10.0.0.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization 
    peer 10.0.0.1 enable
   #
   link-state-family unicast
    peer 10.0.0.1 enable
  #
  return
  ```