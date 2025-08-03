Example for Configuring BGP4+ Route Reflection
==============================================

Configuring BGP4+ RRs simplifies the network configuration because IBGP peers do not need to be fully meshed.

#### Networking Requirements

In [Figure 1](#EN-US_TASK_0172366519__fig_dc_vrp_bgp6_cfg_006601), Device B receives an Update packet from its EBGP peer and forwards it to Device C. Device C is an RR and has two clients: Device B and Device D.

Device B and Device D do not need to establish an IBGP connection. After receiving a route update message from Device B, Device C reflects it to Device D. Similarly, after receiving a route update message from Device D, Device C reflects it to Device B.

**Figure 1** Network diagram of configuring BGP4+ route reflection![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1 and interface2 represent GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_bgp6_cfg_006601.png)  


#### Precautions

To improve security, you are advised to deploy BGP4+ security measures. For details, see "Configuring BGP4+ Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP4+ Keychain."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure basic BGP4+ functions on each Router.
2. Configure an RR and its clients to establish IBGP connections.
3. Configure Device C as an RR, and then check its routing information.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs of Device A, Device B, Device C, and Device D
* AS numbers of Device A, Device B, Device C, and Device D

#### Procedure

1. Configure an IPv6 address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172366519__section_dc_vrp_bgp6_cfg_006605) in this section.
2. Configure basic BGP4+ functions.
   
   
   
   # Configure Device A.
   
   ```
   [~DeviceA] bgp 100
   ```
   ```
   [*DeviceA-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-bgp] peer 2001:db8:100::2 as-number 200
   ```
   ```
   [*DeviceA-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceA-bgp-af-ipv6] peer 2001:db8:100::2 enable
   ```
   ```
   [*DeviceA-bgp-af-ipv6] network 2001:db8:1:: 64
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
   [~DeviceB] bgp 200
   ```
   ```
   [*DeviceB-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-bgp] peer 2001:db8:100::1 as-number 100
   ```
   ```
   [*DeviceB-bgp] peer 2001:db8:101::1 as-number 200
   ```
   ```
   [*DeviceB-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:100::1 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:101::1 enable
   ```
   ```
   [*DeviceB-bgp-af-ipv6] peer 2001:db8:101::1 next-hop-local
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
   [~DeviceC] bgp 200
   ```
   ```
   [*DeviceC-bgp] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-bgp] peer 2001:db8:101::2 as-number 200
   ```
   ```
   [*DeviceC-bgp] peer 2001:db8:102::2 as-number 200
   ```
   ```
   [*DeviceC-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:db8:101::2 enable
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:db8:102::2 enable
   ```
   ```
   [*DeviceC-bgp-af-ipv6] network 2001:db8:101:: 96
   ```
   ```
   [*DeviceC-bgp-af-ipv6] network 2001:db8:102:: 96
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
   [~DeviceD] bgp 200
   ```
   ```
   [*DeviceD-bgp] router-id 4.4.4.4
   ```
   ```
   [*DeviceD-bgp] peer 2001:db8:102::1 as-number 200
   ```
   ```
   [*DeviceD-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceD-bgp-af-ipv6] peer 2001:db8:102::1 enable
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
3. Configure an RR.
   
   
   
   # Configure Device C as an RR, with Device B and Device D as its clients.
   
   ```
   [~DeviceC-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:db8:101::2 reflect-client
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:db8:102::2 reflect-client
   ```
   ```
   [*DeviceC-bgp-af-ipv6] commit
   ```
4. Verify the configuration.
   
   
   
   # Check the routing table of Device B.
   
   ```
   [~DeviceB] display bgp ipv6 routing-table
   
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 3
    *>  Network  : 2001:db8:1::                             PrefixLen : 64  
        NextHop  : 2001:db8:100::1                          LocPrf    :   
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn : 100i
      i Network  : 2001:db8:101::                           PrefixLen : 96  
        NextHop  : 2001:db8:101::1                          LocPrf    : 100 
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn :  i
    *>i Network  : 2001:db8:102::                           PrefixLen : 96  
        NextHop  : 2001:db8:101::1                          LocPrf    : 100 
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn :  i
   ```
   
   # Display the routing table of Device D.
   
   ```
   [~DeviceD] display bgp ipv6 routing-table
   ```
   ```
    BGP Local router ID is 4.4.4.4
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 3
    *>i Network  : 2001:db8:1::                             PrefixLen : 64  
        NextHop  : 2001:db8:101::2                          LocPrf    : 100 
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn : 100i
    *>i Network  : 2001:db8:101::                           PrefixLen : 96  
        NextHop  : 2001:db8:102::1                          LocPrf    : 100 
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn :  i
      i Network  : 2001:db8:102::                           PrefixLen : 96  
        NextHop  : 2001:db8:102::1                          LocPrf    : 100 
        MED      : 0                                        PrefVal   : 0
        Label    : 
        Path/Ogn :  i
   ```
   
   The preceding command output shows that Device D has learned from Device C the routes advertised by Device A.

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:100::1/96
  #
  bgp 100
   router-id 1.1.1.1
   peer 2001:db8:100::2 as-number 200
   #
   ipv6-family unicast
    undo synchronization 
    network 2001:db8:1:: 64
    peer 2001:db8:100::2 enable
  #
  return
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:101::2/96
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:100::2/96
  #
  bgp 200
   router-id 2.2.2.2
   peer 2001:db8:100::1 as-number 100
   peer 2001:db8:101::1 as-number 200
   #
   ipv6-family unicast
    undo synchronization 
    peer 2001:db8:100::1 enable
    peer 2001:db8:101::1 enable
    peer 2001:db8:101::1 next-hop-local
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:102::1/96
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:101::1/96
  #
  bgp 200
   router-id 3.3.3.3
   peer 2001:db8:101::2 as-number 200
   peer 2001:db8:102::2 as-number 200
   #
   ipv6-family unicast
    undo synchronization 
    network 2001:db8:101:: 96
    network 2001:db8:102:: 96
    peer 2001:db8:101::2 enable
    peer 2001:db8:101::2 reflect-client
    peer 2001:db8:102::2 enable
    peer 2001:db8:102::2 reflect-client
  #
  return
  ```
* Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:102::2/96
  #
  bgp 200
   router-id 4.4.4.4
   peer 2001:db8:102::1 as-number 200
   #
   ipv4-family unicast
    undo synchronization 
   #
   ipv6-family unicast
    undo synchronization 
    peer 2001:db8:102::1 enable
  #
  return
  ```