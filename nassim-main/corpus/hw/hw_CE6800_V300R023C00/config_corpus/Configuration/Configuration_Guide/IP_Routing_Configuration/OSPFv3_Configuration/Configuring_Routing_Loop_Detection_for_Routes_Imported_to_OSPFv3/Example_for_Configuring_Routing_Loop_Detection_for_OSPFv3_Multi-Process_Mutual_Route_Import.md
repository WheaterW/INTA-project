Example for Configuring Routing Loop Detection for OSPFv3 Multi-Process Mutual Route Import
===========================================================================================

This section provides an example for configuring routing loop detection for OSPFv3 multi-process mutual route import.

#### Networking Requirements

On the live network, routes of an OSPFv3 process can be imported to another OSPFv3 process for redistribution. In such a scenario, routing policies are usually configured on multiple devices to prevent routing loops. If routing policies are incorrectly configured on the devices that import routes, routing loops may occur. To prevent this problem, configure routing loop detection for the routes imported to OSPFv3.

In [Figure 1](#EN-US_TASK_0000001178508042__fig1261541011544), an IS-IS process is configured on DeviceC, DeviceD, and DeviceE. OSPFv3 process 1 is configured on DeviceB, DeviceC, DeviceE, and DeviceF. OSPFv3 process 2 is configured on DeviceA, DeviceB, and DeviceF. DeviceC is configured to import routes from the IS-IS process to OSPFv3 process 1. DeviceB is configured to import routes from OSPFv3 process 1 to OSPFv3 process 2. DeviceF is configured to import routes from OSPFv3 process 2 to OSPFv3 process 1.

**Figure 1** Routing loop detection for OSPFv3 multi-process mutual route import![](../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, and interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001229116017.png)

#### Precautions

To improve security, you are advised to deploy OSPFv3 authentication. For details, see "Configuring OSPFv3 Authentication." OSPFv3 area authentication is used as an example. For details, see "Example for Configuring Basic OSPFv3 Functions."


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IP addresses for interfaces on each device.
2. Enable IS-IS and OSPFv3 and configure basic functions.
3. Configure route import to construct a routing loop.
4. Check whether a routing loop occurs.
5. Enable routing loop detection to check whether the routing loop is eliminated.

#### Procedure

1. Assign an IP address to each interface.
   
   
   
   DeviceA is used as an example.
   
   ```
   <DeviceA> system-view
   [~DeviceA] interface 100GE1/0/1
   [*DeviceA-100GE1/0/1] ipv6 enable
   [*DeviceA-100GE1/0/1] ipv6 address 2001:db8:1::1 64
   [*DeviceA-100GE1/0/1] ipv6 address FE80::A:B link-local
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE1/0/2
   [*DeviceA-100GE1/0/2] ipv6 enable
   [*DeviceA-100GE1/0/2] ipv6 address 2001:db8:2::2 64
   [*DeviceA-100GE1/0/2] ipv6 address FE80::A:F link-local
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
   
   The configurations of other devices are similar to those of DeviceA. For configuration details, see [Configuration Scripts](#EN-US_TASK_0000001178508042__section_dc_vrp_isis_cfg_201205) in this section.
2. Enable OSPFv3 and IS-IS, and configure basic OSPFv3 and IS-IS functions to implement intra-area interworking.
   
   
   
   # Configure an IS-IS process on DeviceC, DeviceD, and DeviceE. DeviceC is used as an example.
   
   ```
   [~DeviceC] isis 1
   [*DeviceC-isis-1] cost-style wide
   [*DeviceC-isis-1] network-entity 10.0000.0000.0003.00
   [*DeviceC-isis-1] ipv6 enable topology standard
   [*DeviceC-isis-1] quit
   [*DeviceC] interface 100GE1/0/2
   [*DeviceC-100GE1/0/2] isis ipv6 enable 1
   [*DeviceC-100GE1/0/2] quit
   [*DeviceC] interface 100GE1/0/3
   [*DeviceC-100GE1/0/3] isis ipv6 enable 1
   [*DeviceC-100GE1/0/3] quit
   [*DeviceC] commit
   ```
   
   # Configure OSPFv3 process 1 on DeviceB, DeviceC, DeviceE, and DeviceF. DeviceB is used as an example.
   
   ```
   [~DeviceB] ospfv3 1 
   [*DeviceB-ospfv3-1] router-id 10.2.2.1
   [*DeviceB-ospfv3-1] area 0
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   [*DeviceB-ospfv3-1] quit
   [*DeviceB] interface 100GE1/0/2
   [*DeviceB-100GE1/0/2] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/2] quit
   [*DeviceB] interface 100GE1/0/3
   [*DeviceB-100GE1/0/3] ospfv3 1 area 0.0.0.0
   [*DeviceB-100GE1/0/3] quit
   [*DeviceB] commit
   ```
   
   # Configure OSPFv3 process 2 on DeviceA, DeviceB, and DeviceF. DeviceA is used as an example.
   
   ```
   [~DeviceA] ospfv3 2 
   [*DeviceA-ospfv3-2] router-id 10.1.1.2
   [*DeviceA-ospfv3-2] area 0
   [*DeviceA-ospfv3-2-area-0.0.0.0] quit
   [*DeviceA-ospfv3-2] quit
   [*DeviceA] interface 100GE1/0/1
   [*DeviceA-100GE1/0/1] ospfv3 2 area 0.0.0.0
   [*DeviceA-100GE1/0/1] quit
   [*DeviceA] interface 100GE1/0/2
   [*DeviceA-100GE1/0/2] ospfv3 2 area 0.0.0.0
   [*DeviceA-100GE1/0/2] quit
   [*DeviceA] commit
   ```
3. Configure route import.
   
   
   
   # Configure OSPFv3 process 1 on DeviceC and DeviceE to import IS-IS routes. The configuration on DeviceC is used as an example.
   
   
   
   ```
   [~DeviceC] ospfv3 1
   [*DeviceC-ospfv3-1] router-id 10.3.3.1
   [*DeviceC-ospfv3-1] import-route isis 1
   [*DeviceC-ospfv3-1] quit
   [*DeviceC] commit
   ```
   
   # Configure OSPFv3 process 2 on DeviceB to import routes from OSPFv3 process 1.
   
   ```
   [~DeviceB] ospfv3 2 
   [*DeviceB-ospfv3-2] router-id 10.2.2.2
   [*DeviceB-ospfv3-2] import-route ospfv3 1
   [*DeviceB-ospfv3-2] quit
   [*DeviceB] commit
   ```
   
   # Configure OSPFv3 process 1 on DeviceF to import routes from OSPFv3 process 2.
   
   ```
   [~DeviceF] ospfv3 1 
   [*DeviceF-ospfv3-1] router-id 10.6.6.1
   [*DeviceF-ospfv3-1] import-route ospfv3 2
   [*DeviceF-ospfv3-1] quit
   [*DeviceF] commit
   ```
4. Display the routing table on each device to check whether a routing loop occurs.
   
   
   
   # Display OSPFv3 neighbor information on DeviceB.
   
   ```
   [~DeviceB] display ospfv3 peer
   ```
   ```
   OSPFv3 Process (1)
   Total number of peer(s): 2
    Peer(s) in full state: 2
   OSPFv3 Area (0.0.0.0)
   Neighbor ID      Pri State            Dead Time  Interface          Instance ID
   10.6.6.1            1 Full/DR          00:00:31    100GE1/0/2              0
   10.3.3.1            1 Full/DR          00:00:36    100GE1/0/3              0
   
   OSPFv3 Process (2)
   Total number of peer(s): 1
    Peer(s) in full state: 1
   OSPFv3 Area (0.0.0.0)
   Neighbor ID      Pri State            Dead Time  Interface          Instance ID
   10.1.1.2            1 Full/Backup      00:00:36    100GE1/0/1              0
   ```
   
   The command output shows that OSPFv3 neighbor relationships have been established between devices.
   
   # Display the routing table of DeviceB.
   
   ```
   [~DeviceB] display ipv6 routing-table 2001:db8:44::44
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 2
   
   Destination  : 2001:db8:44::44                         PrefixLength : 64
   NextHop      : FE80::F:B                            Preference   : 150
   Cost         : 1                                       Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/2                             Flags        : D
   
   Destination  : 2001:db8:44::44                         PrefixLength : 64
   NextHop      : FE80::C:B                            Preference   : 150
   Cost         : 1                                       Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/3                             Flags        : D
   ```
   
   The command output shows that the next hops of the route displayed on DeviceB are DeviceF and DeviceC, and DeviceF and DeviceC work in load balancing mode.
   
   # Display the routing table of DeviceA.
   
   ```
   [~DeviceA] display ipv6 routing-table 2001:db8:44::44
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:44::44                         PrefixLength : 64
   NextHop      : FE80::B:A                            Preference   : 150
   Cost         : 1                                       Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                            Flags        : D
   ```
   
   The command output shows that the next hop of the route displayed on DeviceA is DeviceB.
   
   # Display the routing table of DeviceF.
   
   ```
   [~DeviceF] display ipv6 routing-table 2001:db8:44::44
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 2
   
   Destination  : 2001:db8:44::44                         PrefixLength : 64
   NextHop      : FE80::E:F                            Preference   : 150
   Cost         : 1                                       Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/3                               Flags        : D
   
   Destination  : 2001:db8:44::44                         PrefixLength : 64
   NextHop      : FE80::A:F                            Preference   : 150
   Cost         : 1                                       Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                           Flags        : D
   ```
   
   The command output shows that the next hops of the route displayed on DeviceF are DeviceA and DeviceE, and DeviceA and DeviceE work in load balancing mode.
   
   
   
   In this case, a routing loop is formed on DeviceB, DeviceA, and DeviceF.
5. Enable routing loop detection on each device.
   
   
   
   # Enable routing loop detection for routes imported to OSPFv3. DeviceA is used as an example.
   
   ```
   [~DeviceA] route loop-detect ospfv3 enable
   [*DeviceA] commit
   ```
6. Check whether the routing loop is eliminated.
   
   
   
   # Display the routing table of DeviceB.
   
   ```
   [~DeviceB] display ipv6 routing-table 2001:db8:44::44
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:44::44                         PrefixLength : 64
   NextHop      : FE80::C:B                            Preference   : 150
   Cost         : 1                                       Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/3                           Flags        : D
   ```
   
   The command output shows that the next hop of the route displayed on DeviceB is DeviceC.
   
   # Display the routing table of DeviceA.
   
   ```
   [~DeviceA] display ipv6 routing-table 2001:db8:44::44
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:44::44                         PrefixLength : 64
   NextHop      : FE80::B:A                            Preference   : 150
   Cost         : 1                                       Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                            Flags        : D
   ```
   
   The command output shows that the next hop of the route displayed on DeviceA is DeviceB.
   
   # Display the routing table of DeviceF.
   
   ```
   [~DeviceF] display ipv6 routing-table 2001:db8:44::44
   ```
   ```
   Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
   ------------------------------------------------------------------------------
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:44::44                         PrefixLength : 64
   NextHop      : FE80::E:F                            Preference   : 150
   Cost         : 1                                       Protocol     : OSPFv3ASE
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/3                           Flags        : D
   ```
   
   The command output shows that the next hop of the route displayed on DeviceF is DeviceE. The routing loop on DeviceB, DeviceA, and DeviceF has been removed.

#### Configuration Scripts

* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  ospfv3 2
   router-id 10.1.1.2
   area 0.0.0.0
  #
  route loop-detect ospfv3 enable
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
   ipv6 address FE80::A:B link-local
   ospfv3 2 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
   ipv6 address FE80::A:F link-local
   ospfv3 2 area 0.0.0.0
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  ospfv3 1
   router-id 10.2.2.1
   area 0.0.0.0
  #
  ospfv3 2
   router-id 10.2.2.2
   import-route ospfv3 1
   area 0.0.0.0
  #
  route loop-detect ospfv3 enable
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
   ipv6 address FE80::B:A link-local
   ospfv3 2 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:5::2/64
   ipv6 address FE80::B:F link-local
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
   ipv6 address FE80::B:C link-local
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0003.00
   #
   ipv6 enable topology standard
   #
  #
  ospfv3 1
   router-id 10.3.3.1
   import-route isis 1
   area 0.0.0.0
  #
  route loop-detect ospfv3 enable
  #
  interface 100GE1/0/1         
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
   ipv6 address FE80::C:B link-local
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2          
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:7::2/64
   ospfv3 1 area 0.0.0.0
   isis ipv6 enable 1
  #
  interface 100GE1/0/3           
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:6::2/64 
   isis ipv6 enable 1
  #
  return
  ```
* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0004.00
   #
   ipv6 enable topology standard
   #
  #
  route loop-detect ospfv3 enable
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:6::1/64
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:9::2/64
   isis ipv6 enable 1
  #
  interface LoopBack0
   ipv6 enable
   ipv6 address 2001:db8:44::44/128
   isis ipv6 enable 1
  #
  return
  ```
* DeviceE
  
  ```
  #
  sysname DeviceE
  #
  isis 1
   is-level level-1
   cost-style wide
   network-entity 10.0000.0000.0005.00
   #
   ipv6 enable topology standard
   #
  #
  ospfv3 1
   router-id 10.5.5.1
   import-route isis 1
   area 0.0.0.0
  #
  route loop-detect ospfv3 enable
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
   ipv6 address FE80::E:F link-local
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:7::1/64
   ospfv3 1 area 0.0.0.0
   isis ipv6 enable 1
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:9::1/64
   isis ipv6 enable 1
  #
  return
  ```
* DeviceF
  
  ```
  #
  sysname DeviceF
  #
  ospfv3 1
   router-id 10.6.6.1
   import-route ospfv3 2
   area 0.0.0.0
  #
  ospfv3 2
   router-id 10.6.6.2
   area 0.0.0.0
  #
  route loop-detect ospfv3 enable
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
   ipv6 address FE80::F:A link-local
   ospfv3 2 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:5::1/64
   ipv6 address FE80::F:B link-local
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::2/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```