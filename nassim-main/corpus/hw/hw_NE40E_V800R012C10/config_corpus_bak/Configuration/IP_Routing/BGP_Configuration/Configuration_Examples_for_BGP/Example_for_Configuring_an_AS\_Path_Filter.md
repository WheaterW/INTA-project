Example for Configuring an AS\_Path Filter
==========================================

AS\_Path filters can be used to improve network performance.

#### Networking Requirements

Enterprises A, B, and C belong to different ASs. The network of enterprise B communicates with the networks of the other two enterprises through EBGP. Due to the competition relationship, enterprises A and C require that the routes that they advertise to enterprise B be not learned by each other. In this situation, configure an AS\_Path filter on enterprise B.

In [Figure 1](#EN-US_TASK_0172366370__fig_dc_vrp_bgp_cfg_408801), Device B establish EBGP connections with Devices A and C. To disable devices in AS 10 from communicating with devices in AS 30, you can configure an AS\_Path filter on Device B to prevent devices in AS 20 from advertising routes of AS 30 to AS 10 or routes of AS 10 to AS 30.

**Figure 1** Configuring BGP route filtering![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 2 in this example are GE 0/1/0 and GE 0/2/0, respectively.


  
![](images/fig_dc_vrp_bgp_cfg_408801.png)

#### Precautions

During the configuration process, note the following:

* The relationship between multiple filtering rules in the same filter is OR.
* To improve security, you are advised to deploy BGP security measures. For details, see "Configuring BGP Security." Keychain authentication is used as an example. For details, see "Example for Configuring BGP Keychain."

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Establish EBGP connections between Device A and Device B, and between Device B and Device C, and then import direct routes.
2. Configure an AS\_Path filter on Device B and then apply its filtering rules.

#### Data Preparation

To complete the configuration, you need the following data:

* Router IDs and AS numbers of Device A, Device B, and Device C
* Number of the AS\_Path filter

#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172366370__section_dc_vrp_bgp_cfg_408805) in this section.
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
   [*DeviceA-bgp] import-route direct
   ```
   ```
   [*DeviceA-bgp] commit
   ```
   
   # Configure Device B.
   
   ```
   [*DeviceB] bgp 20
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
   [*DeviceB-bgp] import-route direct
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
   [*DeviceC-bgp] import-route direct
   ```
   ```
   [*DeviceC-bgp] commit
   ```
   ```
   [~DeviceC-bgp] quit
   ```
   
   # Display the routing table advertised by Device B. Use the routes advertised by Device B to Device C as an example. You can view that Device B advertises the routes destined for the network segment between Device A and Device C.
   
   ```
   <DeviceB> display bgp routing-table peer 10.1.3.2 advertised-routes
   
   
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 3
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     10.1.2.0/24        10.1.3.1                       0                     0      20?
    *>     10.1.3.0/24        10.1.3.1                       0                     0      20?
    *>     10.1.4.0/24       10.1.3.1                      0                     0      20 10?
   ```
   
   Check the routing table of Device C. The command output shows that Device C has learned the two routes advertised by Device B.
   
   ```
   <DeviceC> display bgp routing-table
   
    BGP Local router ID is 3.3.3.3
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 7
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     10.1.2.0/24        10.1.3.1                       0                     0      20?
    *>     10.1.3.0/24        0.0.0.0                        0                     0       ?
                              10.1.3.1                       0                     0      20?
    *>     10.1.3.2/32        0.0.0.0                        0                     0       ?
    *>     10.1.4.0/24        0.0.0.0                        0                     0       ?
    *                         10.1.3.1                                             0      20 10?
    *>     10.1.4.2/32        0.0.0.0                        0                     0       ?
   ```
3. Configure the AS\_Path filter on Device B and then apply the filter on the outbound interface of Device B.
   
   
   
   # Create AS\_Path filter 1 to deny the routes carrying AS 30. The regular expression "\_30\_" indicates any AS list that contains AS 30 and "\*" matches any character.
   
   ```
   [~DeviceB] ip as-path-filter 1 deny _30_
   ```
   ```
   [*DeviceB] ip as-path-filter 1 permit .*
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Create AS\_Path filter 2 to deny the routes carrying AS 10. The regular expression "\_10\_" indicates any AS list that contains AS 10 and "\*" matches any character.
   
   ```
   [~DeviceB] ip as-path-filter 2 deny _10_
   ```
   ```
   [*DeviceB] ip as-path-filter 2 permit .*
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Apply the AS\_Path filter on two outbound interfaces of Device B.
   
   ```
   [~DeviceB] bgp 20
   ```
   ```
   [*DeviceB-bgp] peer 10.1.2.1 as-path-filter 1 export
   ```
   ```
   [*DeviceB-bgp] peer 10.1.3.2 as-path-filter 2 export
   ```
   ```
   [*DeviceB-bgp] commit
   ```
   ```
   [~DeviceB-bgp] quit
   ```
4. Verify the configuration.
   
   
   
   # Display the routing table advertised by Device B. The command output shows that the advertised routes to the network segment between Device A and Device C do not exist. Use the routes advertised by Device B to Device C as an example.
   
   ```
   <DeviceB> display bgp routing-table peer 10.1.3.2 advertised-routes
   
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 2
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     10.1.2.0/24        10.1.3.1                       0                     0      20?
    *>     10.1.3.0/24        10.1.3.1                       0                     0      20?
   ```
   
   Similarly, the BGP routing table of Device C does not have these routes.
   
   ```
   <DeviceC> display bgp routing-table
   
    BGP Local router ID is 3.3.3.3
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 6
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     10.1.2.0/24        10.1.3.1                       0                     0      20?
    *>     10.1.3.0/24        0.0.0.0                        0                     0       ?
                              10.1.3.1                       0                     0      20?
    *>     10.1.3.2/32        0.0.0.0                        0                     0       ?
    *>     10.1.4.0/24        0.0.0.0                        0                     0       ?
    *>     10.1.4.2/32        0.0.0.0                        0                     0       ?
   ```
   
   Check the routing table advertised by Device B, and you can view that the advertised routes to the network segment between Device A and Device C do not exist. Use the routes advertised by Device B to Device A as an example.
   
   ```
   <DeviceB> display bgp routing-table peer 10.1.2.1 advertised-routes
   
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 2
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     10.1.2.0/24        10.1.2.2                       0                     0      20?
    *>     10.1.3.0/24        10.1.2.2                       0                     0      20?
   ```
   
   Similarly, the BGP routing table of Device A does not have these routes.
   
   ```
   <DeviceA> display bgp routing-table
   
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
   
    Total Number of Routes: 6
           Network            NextHop                       MED        LocPrf    PrefVal Path/Ogn
   
    *>     10.1.2.0/24        0.0.0.0                        0                     0       ?
                              10.1.2.2                       0                     0      20?
    *>     10.1.2.1/32        0.0.0.0                        0                     0       ?
    *>     10.1.3.0/24        10.1.2.2                       0                     0      20?
    *>     10.1.4.0/24        0.0.0.0                        0                     0       ?
    *>     10.1.4.1/32        0.0.0.0                        0                     0       ?
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
   ip address 10.1.4.1 255.255.255.0
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
    import-route direct
  ```
  ```
    peer 10.1.2.2 enable
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
   ip address 10.1.3.1 255.255.255.0
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
    import-route direct
  ```
  ```
    peer 10.1.2.1 enable
  ```
  ```
    peer 10.1.2.1 as-path-filter 1 export
  ```
  ```
    peer 10.1.3.2 enable
  ```
  ```
    peer 10.1.3.2 as-path-filter 2 export
  ```
  ```
  #
  ```
  ```
   ip as-path-filter 1 deny _30_
  ```
  ```
   ip as-path-filter 1 permit .*
  ```
  ```
   ip as-path-filter 2 deny _10_
  ```
  ```
   ip as-path-filter 2 permit .*
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
  interface GigabitEthernet0/1/0
  ```
  ```
   undo shutdown
  ```
  ```
   ip address 10.1.4.2 255.255.255.0
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
    import-route direct
  ```
  ```
    peer 10.1.3.1 enable
  ```
  ```
  #
  ```
  ```
  return
  ```