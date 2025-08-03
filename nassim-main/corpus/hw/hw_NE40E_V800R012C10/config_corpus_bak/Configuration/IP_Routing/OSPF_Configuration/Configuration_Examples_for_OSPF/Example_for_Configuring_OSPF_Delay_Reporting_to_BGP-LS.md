Example for Configuring OSPF Delay Reporting to BGP-LS
======================================================

Border Gateway Protocol-Link State (BGP-LS) can be used to summarize topology information collected by IGPs and send the information to the upper-layer controller.

#### Networking Requirements

BGP-LS is a new method of collecting network topology information. The topology information discovered by IGPs is summarized and reported to an upper-layer controller through BGP. With powerful routing capabilities of BGP, BGP-LS has the following advantages:

* Lowers the requirements on the controller's computing and IGP capabilities.
* Facilitates route selection and computation on the controller by using BGP to summarize process or AS topology information and report the complete information to the controller.
* Requires only one routing protocol (BGP) to report topology information to the controller.

In [Figure 1](#EN-US_TASK_0000001449229378__fig_dc_vrp_bgp_cfg_409701), DeviceC is connected to the controller and reports topology information to the controller. DeviceA, DeviceB, DeviceC, and DeviceD use OSPF to implement IP network interworking. The two interfaces connecting DeviceC and DeviceD belong to area 20, and the interfaces connecting DeviceA, DeviceB, and DeviceC belong to area 10.

**Figure 1** Configuring BGP-LS![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent GigabitEthernet0/1/1, GigabitEthernet0/1/2, GigabitEthernet0/1/3, and GigabitEthernet0/1/4, respectively.


  
![](figure/en-us_image_0000001449389118.png)

#### Precautions

To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for each interface on each Router.
2. Configure basic OSPF functions.
3. Deploy BGP-LS on DeviceC and the controller.
4. Configure DeviceA and DeviceC as the TWAMP sender and receiver, respectively.
5. Configure delay advertisement on DeviceA.

#### Data Preparation

To complete the configuration, you need the following data:

* IP addresses and areas of interfaces on DeviceA, DeviceB, DeviceC, and DeviceD
* BGP-LS ID in OSPF on DeviceC
* BGP AS numbers, BGP-LS domain AS numbers, and BGP-LS domain IDs of DeviceC and the controller

#### Procedure

1. Assign an IP address to each interface on each Router. For configuration details, see [Configuration Files](#EN-US_TASK_0000001449229378__section_dc_vrp_bgp_cfg_409705) in this section.
2. Configure basic OSPF functions.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospf 1 router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospf-1] area 0.0.0.10
   ```
   ```
   [*DeviceA-ospf-1-area-0.0.0.10] quit
   ```
   ```
   [*DeviceA-ospf-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ospf enable 1 area 0.0.0.10
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] ospf network-type p2p
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospf 1 router-id 2.2.2.2
   ```
   ```
   [*DeviceB-ospf-1] area 0.0.0.10
   ```
   ```
   [*DeviceB-ospf-1-area-0.0.0.10] quit
   ```
   ```
   [*DeviceB-ospf-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/4
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/4] ospf enable 1 area 0.0.0.10
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/4] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/4] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospf 1 router-id 3.3.3.3
   ```
   ```
   [*DeviceC-ospf-1] area 0.0.0.10
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.10] quit
   ```
   ```
   [*DeviceC-ospf-1] area 0.0.0.20
   ```
   ```
   [*DeviceC-ospf-1-area-0.0.0.20] quit
   ```
   ```
   [*DeviceC-ospf-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] ospf enable 1 area 0.0.0.10
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] ospf network-type p2p
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/3] ospf enable 1 area 0.0.0.20
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/4
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/4] ospf enable 1 area 0.0.0.10
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/4] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/4] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] ospf 1 router-id 4.4.4.4
   ```
   ```
   [*DeviceD-ospf-1] area 0.0.0.20
   ```
   ```
   [*DeviceD-ospf-1-area-0.0.0.20] quit
   ```
   ```
   [*DeviceD-ospf-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] ospf enable 1 area 20
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceD] interface LoopBack0
   ```
   ```
   [*DeviceD-LoopBack0] ospf enable 1 area 20
   ```
   ```
   [*DeviceD-LoopBack0] commit
   ```
   ```
   [~DeviceD-LoopBack0] quit
   ```
   
   # Check OSPF routing information on each Router. The following example uses the command output on DeviceC.
   
   ```
   [~DeviceC] display ospf routing
   ```
   ```
     
              OSPF Process 1 with Router ID 3.3.3.3
                      Routing Tables
    
    Routing for Network
    Destination        Cost     Type       NextHop         AdvRouter       Area
    10.1.1.0/24        1        Direct     10.1.1.1        3.3.3.3         0.0.0.10
    10.1.2.0/24        1        Direct     10.1.2.1        3.3.3.3         0.0.0.10
    172.16.1.1/32      1        Stub       192.168.0.2     4.4.4.4         0.0.0.20
    192.168.0.0/24     1        Direct     192.168.0.1     3.3.3.3         0.0.0.20
    
    Total Nets: 4
    Intra Area: 4  Inter Area: 0  ASE: 0  NSSA: 0
   ```
3. Deploy BGP-LS on DeviceC and the controller.
   
   
   
   # Enable OSPF topology advertisement on DeviceC.
   
   ```
   [~DeviceC] ospf 1
   ```
   ```
   [*DeviceC-ospf-1] bgp-ls enable
   ```
   ```
   [*DeviceC-ospf-1] bgp-ls identifier 20
   ```
   ```
   [*DeviceC-ospf-1] commit
   ```
   ```
   [~DeviceC-ospf-1] quit
   ```
   
   # Enable BGP-LS on DeviceC and establish a BGP-LS peer relationship with the controller.
   
   ```
   [~DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] peer 1.1.1.2 as-number 100
   ```
   ```
   [*DeviceC-bgp] link-state-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ls] peer 1.1.1.2 enable
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
   [*Controller-bgp] peer 1.1.1.1 as-number 100
   ```
   ```
   [*Controller-bgp] link-state-family unicast
   ```
   ```
   [*Controller-bgp-af-ls] peer 1.1.1.1 enable
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
4. Configure DeviceA and DeviceC as the TWAMP sender and receiver, respectively.
   
   
   
   # Configure DeviceA as the TWAMP client and sender.
   
   ```
   [~DeviceA] nqa twamp-light
   ```
   ```
   [*DeviceA-twamp-light] client
   ```
   ```
   [*DeviceA-twamp-light-client] test-session 1 sender-ip 10.1.1.2 reflector-ip 10.1.1.1 sender-port 862 reflector-port 862
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
   
   # Configure DeviceC as the TWAMP receiver.
   
   ```
   [~DeviceC] nqa twamp-light
   ```
   ```
   [*DeviceC-twamp-light] responder
   ```
   ```
   [*DeviceC-twamp-light-responder] test-session 1 local-ip 10.1.1.1 remote-ip 10.1.1.2 local-port 862 remote-port 862
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
5. Configure delay advertisement on DeviceA.
   
   
   ```
   [~DeviceA] ospf 1 router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospf-1] metric-delay advertisement enable
   ```
   ```
   [*DeviceA-ospf-1] commit
   ```
6. Verify the configuration.
   
   
   
   # Display information about BGP-LS peers and their status on DeviceC.
   
   ```
   [~DeviceC] display bgp link-state unicast peer
   ```
   ```
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
    
     Peer                             V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     1.1.1.2                          4         100        5        9     0 00:00:55 Established        0
   ```
   
   # Check the delay sub-TLVs carried in OSPF Opaque LSAs on DeviceC.
   
   ```
   [~DeviceC] display ospf lsdb opaque-area
   ```
   ```
             OSPF Process 1 with Router ID 3.3.3.3
                             Area: 0.0.0.10
                     Link State Database
    
    
     Type      : Opq-Area
     Ls id     : 8.0.0.0
     Adv rtr   : 1.1.1.1
     Ls age    : 55
     Len       : 48
     Options   :  E
     seq#      : 80000002
     chksum    : 0x365e
     Opaque Type: 8
     Opaque Id: 0
     OSPFv2 Extended Link Opaque LSA TLV information:
       OSPFv2 Extended Link TLV:
         Link Type: P-2-P
         Link ID: 3.3.3.3
         Link Data: 10.1.1.2
         Min/Max Unidirectional Link Delay Sub-TLV:
           Anomalous (A) Bit: 0
           Min Delay: 786 (us)
   ```
   
   # Check BGP-LS routes on DeviceC.
   
   ```
   [~DeviceC] display bgp link-state unicast routing-table [LINK][OSPFv2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier1.1.1.1][ospf-area-id0.0.0.10][igp-router-id1.1.1.1]][REMOTE[as100][bgp-ls-identifier1.1.1.1][ospf-area-id0.0.0.10][igp-router-id3.3.3.3]][LINK[if-address10.1.1.2][peer-address10.1.1.1][if-address::][peer-address::]]
   ```
   ```
    BGP Local router ID is 10.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    
    BGP local router ID : 1.1.1.1
    Local AS number : 100
    Paths:   1 available, 1 best, 1 select
    BGP routing table entry information of [LINK][OSPFv2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier1.1.1.1][ospf-area-id0.0.0.10][igp-router-id1.1.1.1]][REMOTE[as100][bgp-ls-identifier1.1.1.1][ospf-area-id0.0.0.10][igp-router-id3.3.3.3]][LINK[if-address10.1.1.2][peer-address10.1.1.1][if-address::][peer-address::]]:
    Imported route.
    From: 0.0.0.0 (0.0.0.0)
    Route Duration: 0d00h09m59s
    Direct Out-interface:
    Original nexthop: 0.0.0.0
    AS-path Nil, origin incomplete, MED 0, pref-val 0, valid, local, best, select, pre 255
    Link-state Route Type: LINK
    Protocol: OSPFv2
    Identifier: 20
    Local Node Descriptor:
     AS Number: 100
     BGP Identifier: 1.1.1.1
     OSPF Area ID: 0.0.0.10
     IGP Router ID: 1.1.1.1
    Remote Node Descriptor:
     AS Number: 100
     BGP Identifier: 1.1.1.1
     OSPF Area ID: 0.0.0.10
     IGP Router ID: 3.3.3.3
    Link Descriptor:
     IPv4 interface address: 10.1.1.2
     IPv4 neighbor address: 10.1.1.1
     IPv6 interface address: ::
     IPv6 neighbor address: ::
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
       1.1.1.2
   
   ```
   
   The preceding command output shows that DeviceC obtains the topology information on the whole OSPF network. DeviceC can use BGP-LS routes to report the topology information to its BGP-LS peer (the controller).

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  ospf 1 router-id 1.1.1.1
   metric-delay advertisement enable 
   area 0.0.0.10 
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   ospf network-type p2p 
   ospf enable 1 area 0.0.0.10 
  #
  nqa twamp-light 
   client 
    test-session 1 sender-ip 10.1.1.2 reflector-ip 10.1.1.1 sender-port 862 reflector-port 862 
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
  ospf 1 router-id 2.2.2.2 
   area 0.0.0.10 
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   ospf enable 1 area 0.0.0.10
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  ospf 1 router-id 3.3.3.3
   bgp-ls enable
   bgp-ls identifier 20 
   area 0.0.0.10
   area 0.0.0.20
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 1.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   ospf network-type p2p
   ospf enable 1 area 0.0.0.10
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 192.168.0.1 255.255.255.0
   ospf enable 1 area 0.0.0.20
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   ospf enable 1 area 0.0.0.10
  #
  bgp 100
   peer 1.1.1.2 as-number 100
   #
   ipv4-family unicast
    undo synchronization 
    peer 1.1.1.2 enable
   #
   link-state-family unicast
    peer 1.1.1.2 enable
  #
  nqa twamp-light 
   responder 
    test-session 1 local-ip 10.1.1.1 remote-ip 10.1.1.2 local-port 862 remote-port 862 
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  ospf 1 router-id 4.4.4.4 
   area 0.0.0.20 
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 192.168.0.2 255.255.255.0
   ospf enable 1 area 0.0.0.20 
  #
  interface LoopBack0
   ip address 172.16.1.1 255.255.255.255
   ospf enable 1 area 0.0.0.20
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
   ip address 1.1.1.2 255.255.255.0
  #
  bgp 100
   peer 1.1.1.1 as-number 100
   #
   ipv4-family unicast
    undo synchronization 
    peer 1.1.1.1 enable
   #
   link-state-family unicast
    peer 1.1.1.1 enable
  #
  return
  ```