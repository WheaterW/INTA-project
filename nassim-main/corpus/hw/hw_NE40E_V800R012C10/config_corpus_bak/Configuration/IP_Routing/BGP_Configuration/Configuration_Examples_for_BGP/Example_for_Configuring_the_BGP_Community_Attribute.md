Example for Configuring the BGP Community Attribute
===================================================

By setting the community attribute, you can flexibly control BGP route selection.

#### Networking Requirements

Enterprises A, B, and C belong to different ASs, and enterprise B's network communicates with the networks of the other two enterprises through EBGP connections. Enterprise A and C are rivals, and enterprise A requires that the routes it sends to enterprise B be transmitted only within enterprise B. In this situation, you can configure the community attribute on the router in enterprise A that sends routes to enterprise B.

In [Figure 1](#EN-US_TASK_0172366379__fig_dc_vrp_bgp_cfg_407701), EBGP connections are established between Device B and Device A, and between Device B and Device C. It is required that the routes advertised from AS 10 to AS 20 are not advertised to other ASs by AS 20. In this situation, configure the community attribute No\_Export on Device A.

**Figure 1** Configuring the BGP community attribute![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example are GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_bgp_cfg_407701.png)

#### Precautions

To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish EBGP connections between Device A andDevice B, and between Device B and Device C.
2. Configure a routing policy on Device A to advertise the community attribute No\_Export.

#### Data Preparation

To complete the configuration, you need the following data:

* Router ID and AS number of Device A
* Router ID and AS number of Device B
* Router ID and AS number of Device C

#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172366379__section_dc_vrp_bgp_cfg_407705) in this section.
2. Configure EBGP connections.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bgp 10
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 10.1.2.2 as-number 20
   ```
   ```
   [*DeviceA-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv4] network 10.5.1.0 255.255.255.0
   ```
   ```
   [*DeviceA-bgp-af-ipv4] commit
   ```
   ```
   [~DeviceA-bgp-af-ipv4] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 20
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 10.1.2.1 as-number 10
   ```
   ```
   [*DeviceB-bgp] peer 10.1.3.2 as-number 30
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
   
   # Configure Device C.
   
   ```
   [~DeviceC] bgp 30
   ```
   ```
   [*DeviceC-bgp] router-id 3.3.3.3 
   ```
   ```
   [*DeviceC-bgp] peer 10.1.3.1 as-number 20
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
   
   # Check the routing table of Device B.
   
   ```
   [~DeviceB] display bgp routing-table 10.5.1.0
   
   BGP local router ID : 2.2.2.2
    Local AS number : 20
    Paths:   1 available, 1 best, 1 select
    BGP routing table entry information of 10.5.1.0/24:
    From: 10.1.2.1 (1.1.1.1)
    Route Duration: 0d00h00m37s
    Direct Out-interface: GigabitEthernet0/2/0
    Original nexthop: 10.1.2.1
    Qos information : 0x0
    AS-path 10, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255
    Advertised to such 2 peers:
       10.1.2.1
       10.1.3.2
   ```
   
   The command output shows that Device B advertises the received routes to Device C in AS 30.
   
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
   
    *>   10.5.1.0/24        10.1.3.1                             0      20 10i
   ```
   
   In the routing table, you can view that Device C learns the route to 10.5.1.0/24 from Device B.
3. Configure the BGP community attribute.
   
   
   
   # Configure a routing policy on Device A to ensure that the routes advertised by Device A to Device B are not advertised by Device B to any other AS.
   
   ```
   [~DeviceA] route-policy comm_policy permit node 10
   ```
   ```
   [*DeviceA-route-policy] apply community no-export
   ```
   ```
   [*DeviceA-route-policy] commit
   ```
   ```
   [~DeviceA-route-policy] quit
   ```
   
   # Apply the routing policy.
   
   ```
   [~DeviceA] bgp 10
   ```
   ```
   [*DeviceA-bgp] ipv4-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv4] peer 10.1.2.2 route-policy comm_policy export
   ```
   ```
   [*DeviceA-bgp-af-ipv4] peer 10.1.2.2 advertise-community
   ```
   ```
   [*DeviceA-bgp-af-ipv4] commit
   ```
   
   # Check the routing table of Device B.
   
   ```
   [~DeviceB] display bgp routing-table 10.5.1.0
   
   BGP local router ID : 2.2.2.2
    Local AS number : 20
    Paths:   1 available, 1 best, 1 select
    BGP routing table entry information of 10.5.1.0/24:
    From: 10.1.2.1 (1.1.1.1)
    Route Duration: 0d00h00m12s
    Direct Out-interface: GigabitEthernet0/2/0
    Original nexthop: 10.1.2.1
    Qos information : 0x0
    Community:no-export
    AS-path 10, origin igp, MED 0, pref-val 0, valid, external, best, select, pre 255
    Not advertised to any peers yet
   ```
   
   The command output on DeviceB shows the configured community attribute and that the route to 10.5.1.0/24 has not been advertised to DeviceC.

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
   ip address 10.5.1.1 255.255.255.0
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
  bgp 10
  ```
  ```
   router-id 1.1.1.1
  ```
  ```
   peer 10.1.2.2 as-number 20
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    network 10.5.1.0 255.255.255.0
  ```
  ```
    peer 10.1.2.2 enable
  ```
  ```
    peer 10.1.2.2 route-policy comm_policy export
  ```
  ```
    peer 10.1.2.2 advertise-community
  ```
  ```
  #
  ```
  ```
  route-policy comm_policy permit node 10
  ```
  ```
   apply community no-export
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
  bgp 20
  ```
  ```
   router-id 2.2.2.2
  ```
  ```
   peer 10.1.2.1 as-number 10
  ```
  ```
   peer 10.1.3.2 as-number 30
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    peer 10.1.2.1 enable
  ```
  ```
    peer 10.1.3.2 enable
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
  bgp 30
  ```
  ```
   router-id 3.3.3.3
  ```
  ```
   peer 10.1.3.1 as-number 20
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
    peer 10.1.3.1 enable
  ```
  ```
  #
  ```
  ```
  return
  ```