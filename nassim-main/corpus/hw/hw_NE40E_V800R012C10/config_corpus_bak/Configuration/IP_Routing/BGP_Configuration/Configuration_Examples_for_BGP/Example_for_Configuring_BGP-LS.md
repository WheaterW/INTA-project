Example for Configuring BGP-LS
==============================

BGP-link state (LS) enables BGP to report topology information collected by IGPs to the controller.

#### Networking Requirements

BGP-LS is a new method of collecting topology information. With powerful routing capabilities of BGP, BGP-LS has the following advantages:

* Reduces computing capability requirements and spares the necessity of IGPs on the controller.
* Facilitates route selection and calculation on the controller by using BGP to summarize process or AS topology information and report the complete information to the controller.
* Requires only one routing protocol (BGP) to report topology information to the controller.

In [Figure 1](#EN-US_TASK_0172366412__fig_dc_vrp_bgp_cfg_409701), Device C is connected to the controller and reports topology information to the controller. Device A, Device B, Device C, and Device D use IS-IS to communicate with each other at the network layer. Device A, Device B, and Device C reside in area 10, whereas Device D resides in area 20. Device A and Device B are Level-1 devices, Device C is a Level-1-2 device, and Device D is a Level-2 device.

**Figure 1** Configuring BGP-LS![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1, interface2, interface3, and interface4 in this example represent GigabitEthernet0/1/1, GigabitEthernet0/1/2, GigabitEthernet0/1/3, and GigabitEthernet0/1/4, respectively.


  
![](images/fig_dc_vrp_bgp_cfg_409701.png)

#### Precautions

To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure an IP address for each interface on each Router.
2. Configure basic IS-IS functions.
3. Deploy BGP-LS on Device C and the controller.

#### Data Preparation

To complete the configuration, you need the following data:

* Area addresses of Device A, Device B, Device C, and Device D
* Levels of Device A, Device B, Device C, and Device D
* BGP-LS identifier of Device C in IS-IS
* BGP AS numbers, BGP-LS domain AS numbers, and BGP-LS domain IDs of Device C and the controller

#### Procedure

1. Assign an IP address to each interface on each Router. For configuration details, see [Configuration Files](#EN-US_TASK_0172366412__section_dc_vrp_bgp_cfg_409705) in this section.
2. Configure basic IS-IS functions.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] isis 1
   ```
   ```
   [*DeviceA-isis-1] is-level level-1
   ```
   ```
   [*DeviceA-isis-1] network-entity 10.0000.0000.0001.00
   ```
   ```
   [*DeviceA-isis-1] quit
   ```
   ```
   [*DeviceA] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] isis enable 1
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/2] quit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] isis 1
   ```
   ```
   [*DeviceB-isis-1] is-level level-1
   ```
   ```
   [*DeviceB-isis-1] network-entity 10.0000.0000.0002.00
   ```
   ```
   [*DeviceB-isis-1] quit
   ```
   ```
   [*DeviceB] interface gigabitethernet 0/1/4
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/4] isis enable 1
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/4] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/4] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   ```
   ```
   [*DeviceC-isis-1] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/2
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/2] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/3] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceC] interface gigabitethernet 0/1/4
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/4] isis enable 1
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/4] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/4] quit
   ```
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] isis 1
   ```
   ```
   [*DeviceD-isis-1] is-level level-2
   ```
   ```
   [*DeviceD-isis-1] network-entity 20.0000.0000.0004.00
   ```
   ```
   [*DeviceD-isis-1] quit
   ```
   ```
   [*DeviceD] interface gigabitethernet 0/1/3
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] isis enable 1
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/3] quit
   ```
   ```
   [*DeviceD] interface LoopBack0
   ```
   ```
   [*DeviceD-LoopBack0] isis enable 1
   ```
   ```
   [*DeviceD-LoopBack0] commit
   ```
   ```
   [~DeviceD-LoopBack0] quit
   ```
   
   # Check IS-IS routing information on each Router. The following example uses the command output on Device C.
   
   ```
   [~DeviceC] display isis route
                            Route information for ISIS(1)
                            -----------------------------
   
                           ISIS(1) Level-1 Forwarding Table
                           --------------------------------
   
   IPV4 Destination   IntCost    ExtCost ExitInterface     NextHop         Flags
   -------------------------------------------------------------------------------
   1.1.1.0/24         10         NULL    GE0/1/1           Direct          D/-/L/-
   10.1.1.0/24        10         NULL    GE0/1/2           Direct          D/-/L/-
   10.1.2.0/24        10         NULL    GE0/1/4           Direct          D/-/L/-
   192.168.0.0/24     10         NULL    GE0/1/3           Direct          D/-/L/-
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                  U-Up/Down Bit Set
   
   
                           ISIS(1) Level-2 Forwarding Table
                           --------------------------------
   
   IPV4 Destination   IntCost    ExtCost ExitInterface     NextHop         Flags
   -------------------------------------------------------------------------------
   1.1.1.0/24         10         NULL    GE0/1/1           Direct          D/-/L/-
   10.1.1.0/24        10         NULL    GE0/1/2           Direct          D/-/L/-
   10.1.2.0/24        10         NULL    GE0/1/4           Direct          D/-/L/-
   172.16.1.1/32      10         NULL    GE0/1/3           192.168.0.2     A/-/-/-
   192.168.0.0/24     10         NULL    GE0/1/3           Direct          D/-/L/-
        Flags: D-Direct, A-Added to URT, L-Advertised in LSPs, S-IGP Shortcut,
                                  U-Up/Down Bit Set
   ```
3. Deploy BGP-LS on Device C and the controller.
   
   
   
   # Enable IS-IS topology advertisement to BGP on Device C.
   
   ```
   [~DeviceC] isis 1
   ```
   ```
   [*DeviceC-isis-1] bgp-ls enable level-1-2
   ```
   ```
   [*DeviceC-isis-1] bgp-ls identifier 20
   ```
   ```
   [*DeviceC-isis-1] commit
   ```
   ```
   [~DeviceC-isis-1] quit
   ```
   
   # Enable BGP-LS on Device C and configure the controller as a BGP-LS peer of Device C.
   
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
   
   # Enable BGP-LS on the controller and configure Device C as a BGP-LS peer of the controller.
   
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
4. Verify the configuration.
   
   
   
   # Display information about BGP-LS peers and their status on Device C.
   
   ```
   [~DeviceC] display bgp link-state unicast peer
    BGP local router ID : 10.1.1.1
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State  PrefRcv
     1.1.1.2         4         100       27       48     0 00:29:11 Established       17
   ```
   
   # Display BGP-LS routes on Device C.
   
   ```
   [~DeviceC] display bgp link-state unicast routing-table
    BGP Local router ID is 10.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
   
   
    Total Number of Node Routes: 6
    *>     Network  : [NODE][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0002.00]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [NODE][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [NODE][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [NODE][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0004.00]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [NODE][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.02]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [NODE][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0004.01]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
   
    Total Number of Link Routes: 8
    *>     Network  : [LINK][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0002.00]][REMOTE[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.02]][LINK[if-address0.0.0.0][peer-address0.0.0.0][if-address::][peer-address::]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [LINK][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][REMOTE[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.02]][LINK[if-address0.0.0.0][peer-address0.0.0.0][if-address::][peer-address::]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [LINK][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.02]][REMOTE[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0002.00]][LINK[if-address0.0.0.0][peer-address0.0.0.0][if-address::][peer-address::]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [LINK][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.02]][REMOTE[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][LINK[if-address0.0.0.0][peer-address0.0.0.0][if-address::][peer-address::]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [LINK][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][REMOTE[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0004.01]][LINK[if-address0.0.0.0][peer-address0.0.0.0][if-address::][peer-address::]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [LINK][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0004.00]][REMOTE[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0004.01]][LINK[if-address0.0.0.0][peer-address0.0.0.0][if-address::][peer-address::]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [LINK][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0004.01]][REMOTE[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][LINK[if-address0.0.0.0][peer-address0.0.0.0][if-address::][peer-address::]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [LINK][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0004.01]][REMOTE[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0004.00]][LINK[if-address0.0.0.0][peer-address0.0.0.0][if-address::][peer-address::]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
   
    Total Number of IPv4 Prefix Routes: 11
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0002.00]][PREFIX[ospf-route-type0][prefix10.1.2.0/24]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][PREFIX[ospf-route-type0][prefix1.1.1.0/24]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][PREFIX[ospf-route-type0][prefix10.1.1.0/24]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][PREFIX[ospf-route-type0][prefix10.1.2.0/24]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-1][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][PREFIX[ospf-route-type0][prefix192.168.0.0/24]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][PREFIX[ospf-route-type0][prefix1.1.1.0/24]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][PREFIX[ospf-route-type0][prefix10.1.1.0/24]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][PREFIX[ospf-route-type0][prefix10.1.2.0/24]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0003.00]][PREFIX[ospf-route-type0][prefix192.168.0.0/24]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0004.00]][PREFIX[ospf-route-type0][prefix192.168.0.0/24]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
    *>     Network  : [IPV4-PREFIX][ISIS-LEVEL-2][IDENTIFIER20][LOCAL[as100][bgp-ls-identifier10.1.1.1][ospf-area-id0.0.0.0][igp-router-id0000.0000.0004.00]][PREFIX[ospf-route-type0][prefix172.16.1.1/32]]
           NextHop  : 0.0.0.0                                  LocPrf    :
           MED      : 0                                        PrefVal   : 0
           Path/Ogn :  ?
   ```
   
   The preceding command output shows that Device C obtains the topology information on the whole IS-IS network. Device C can use BGP-LS routes to report the topology information to its BGP-LS peer (the controller).

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0001.00
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.2 255.255.255.0
   isis enable 1
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  isis 1
   is-level level-1
   network-entity 10.0000.0000.0002.00
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ip address 10.1.2.2 255.255.255.0
   isis enable 1
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  isis 1
   bgp-ls enable level-1-2
   bgp-ls identifier 20 
   network-entity 10.0000.0000.0003.00
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ip address 1.1.1.1 255.255.255.0
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ip address 10.1.1.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 192.168.0.1 255.255.255.0
   isis enable 1
  #
  interface GigabitEthernet0/1/4
   undo shutdown
   ip address 10.1.2.1 255.255.255.0
   isis enable 1
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
  return
  ```
* Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  isis 1
   is-level level-2
   network-entity 20.0000.0000.0004.00
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ip address 192.168.0.2 255.255.255.0
   isis enable 1
  #
  interface LoopBack0
   ip address 172.16.1.1 255.255.255.255
   isis enable 1
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