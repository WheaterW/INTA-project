Example for Configuring Basic BGP4+ Functions
=============================================

Before building BGP4+ networks, you need to configure basic BGP4+ functions.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172366516__fig_dc_vrp_bgp6_cfg_006501), there are two ASs: AS 65008 and AS 65009. Device A is in AS 65008, and Device B, Device C, and Device D are in AS 65009. BGP4+ must be configured to exchange routing information between the two ASs.

**Figure 1** Configuring basic BGP4+ functions![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, and interface4 represent GE 0/1/0, GE 0/2/0, GE 0/3/0, and GE 0/1/8, respectively.


  
![](images/fig_dc_vrp_bgp6_cfg_006501.png)  


#### Precautions

To improve security, you are advised to deploy BGP4+ security measures. For details, see "Configuring BGP4+ Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP4+ Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IBGP connections between Device B, Device C, and Device D.
2. Configure an EBGP relationship between Device A and Device B.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs of Device A, Device B, Device C, and Device D
* AS numbers of Device A, Device B, Device C, and Device D

#### Procedure

1. Configure an IPv6 address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172366516__section_dc_vrp_bgp6_cfg_006505) in this section.
2. Configure IBGP connections.
   
   
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 65009
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 2001:db8:9:1::2 as-number 65009
   ```
   ```
   [*DeviceB-bgp] peer 2001:db8:9:3::2 as-number 65009
   ```
   ```
   [*DeviceB-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:9:1::2 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:9:3::2 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6] network 2001:db8:9:1:: 64
   ```
   ```
   [*DeviceB-bgp-af-ipv6] network 2001:db8:9:3:: 64
   ```
   ```
   [*DeviceB-bgp-af-ipv6] commit
   ```
   ```
   [~DeviceB-bgp-af-ipv6] quit
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
   [*DeviceC-bgp] peer 2001:db8:9:3::1 as-number 65009
   ```
   ```
   [*DeviceC-bgp] peer 2001:db8:9:2::2 as-number 65009
   ```
   ```
   [*DeviceC-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:db8:9:3::1 enable
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:db8:9:2::2 enable
   ```
   ```
   [*DeviceC-bgp-af-ipv6] network 2001:db8:9:3:: 64
   ```
   ```
   [*DeviceC-bgp-af-ipv6] network 2001:db8:9:2:: 64
   ```
   ```
   [*DeviceC-bgp-af-ipv6] commit
   ```
   ```
   [~DeviceC-bgp-af-ipv6] quit
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
   [*DeviceD-bgp] peer 2001:db8:9:1::1 as-number 65009
   ```
   ```
   [*DeviceD-bgp] peer 2001:db8:9:2::1 as-number 65009
   ```
   ```
   [*DeviceD-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceD-bgp-af-ipv6] peer 2001:db8:9:1::1 enable
   ```
   ```
   [*DeviceD-bgp-af-ipv6] peer 2001:db8:9:2::1 enable
   ```
   ```
   [*DeviceD-bgp-af-ipv6] network 2001:db8:9:2:: 64
   ```
   ```
   [*DeviceD-bgp-af-ipv6] network 2001:db8:9:1:: 64
   ```
   ```
   [*DeviceD-bgp-af-ipv6] commit
   ```
   ```
   [~DeviceD-bgp-af-ipv6] quit
   ```
   ```
   [~DeviceD-bgp] quit
   ```
3. Configure an EBGP connection.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bgp 65008
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 2001:db8:10::1 as-number 65009
   ```
   ```
   [*DeviceA-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv6] peer 2001:db8:10::1 enable
   ```
   ```
   [*DeviceA-bgp-af-ipv6] network 2001:db8:10:: 64
   ```
   ```
   [*DeviceA-bgp-af-ipv6] network 2001:db8:8:: 64
   ```
   ```
   [*DeviceA-bgp-af-ipv6] commit
   ```
   ```
   [~DeviceA-bgp-af-ipv6] quit
   ```
   ```
   [~DeviceA-bgp] quit
   ```
   
   # Configure Device B.
   
   ```
   [~DeviceB] bgp 65009
   ```
   ```
   [*DeviceB-bgp] peer 2001:db8:10::2 as-number 65008
   ```
   ```
   [*DeviceB-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:10::2 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6] network 2001:db8:10:: 64
   ```
   ```
   [*DeviceB-bgp-af-ipv6] commit
   ```
   ```
   [~DeviceB-bgp-af-ipv6] quit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
4. Verify the configuration.
   
   
   
   # Check the status of BGP4+ connections.
   
   ```
   [~DeviceB] display bgp ipv6 peer
   
    BGP local router ID : 2.2.2.2
    Local AS number : 65009
    Total number of peers : 3                 Peers in established state : 3
   
     Peer            V    AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv
   
     2001:db8:9:1::2 4 65009        8        9     0 00:05:37 Established       2
     2001:db8:9:3::2 4 65009        2        2     0 00:00:09 Established       2
     2001:db8:10::2  4 65008        9        7     0 00:05:38 Established       2
   ```
   
   The preceding command output shows that BGP4+ connections have been established between Device B and other Routers.
   
   # Display the routing table of Device A.
   
   ```
   [~DeviceA] display bgp ipv6 routing-table
   
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 6
    *>  Network  : 2001:db8:8::                             PrefixLen : 64
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : i
    *>  Network  : 2001:db8:9:1::                           PrefixLen : 64
        NextHop  : 2001:db8:10::1                           LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : 65009 i
    *>  Network  : 2001:db8:9:2::                           PrefixLen : 64
        NextHop  : 2001:db8:10::1                           LocPrf    :
        MED      :                                          PrefVal   : 0
        Label    :
        Path/Ogn : 65009 i
    *>  Network  : 2001:db8:9:3::                           PrefixLen : 64
        NextHop  : 2001:db8:10::1                           LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : 65009 i
    *>  Network  : 2001:db8:10::                            PrefixLen : 64
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : i
     *
        NextHop  : 2001:db8:10::1                           LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : 65009 i   
   ```
   
   The preceding command output shows that Device A has learned routes from its peer in AS 65009. AS 65008 and AS 65009 can exchange routing information.

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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:8::1/64
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:10::2/64
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
   peer 2001:db8:10::1 as-number 65009
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
   #
  ```
  ```
   ipv6-family unicast
  ```
  ```
    network 2001:db8:8:: 64
  ```
  ```
    network 2001:db8:10:: 64
  ```
  ```
    peer 2001:db8:10::1 enable
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:9:1::1/64
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:10::1/64
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:9:3::1/64
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
   peer 2001:db8:9:1::2 as-number 65009
  ```
  ```
   peer 2001:db8:9:3::2 as-number 65009
  ```
  ```
   peer 2001:db8:10::2 as-number 65008
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
   #
  ```
  ```
   ipv6-family unicast
  ```
  ```
    network 2001:db8:9:1:: 64
  ```
  ```
    network 2001:db8:9:3:: 64
  ```
  ```
    network 2001:db8:10:: 64
  ```
  ```
    peer 2001:db8:9:1::2 enable
  ```
  ```
    peer 2001:db8:9:3::2 enable
  ```
  ```
    peer 2001:db8:10::2 enable
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:9:2::1/64
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:9:3::2/64
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
   peer 2001:db8:9:2::2 as-number 65009
  ```
  ```
   peer 2001:db8:9:3::1 as-number 65009
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
   #
  ```
  ```
   ipv6-family unicast
  ```
  ```
    network 2001:db8:9:2:: 64
  ```
  ```
    network 2001:db8:9:3:: 64
  ```
  ```
    peer 2001:db8:9:2::2 enable
  ```
  ```
    peer 2001:db8:9:3::1 enable
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:9:1::2/64
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
   ipv6 enable
  ```
  ```
   ipv6 address 2001:db8:9:2::2/64
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
   peer 2001:db8:9:1::1 as-number 65009
  ```
  ```
   peer 2001:db8:9:2::1 as-number 65009
  ```
  ```
   #
  ```
  ```
   ipv4-family unicast
  ```
  ```
    undo synchronization 
   #
  ```
  ```
   ipv6-family unicast
  ```
  ```
    network 2001:db8:9:1:: 64
  ```
  ```
    network 2001:db8:9:2:: 64
  ```
  ```
    peer 2001:db8:9:1::1 enable
  ```
  ```
    peer 2001:db8:9:2::1 enable
  ```
  ```
  #
  ```
  ```
  return
  ```