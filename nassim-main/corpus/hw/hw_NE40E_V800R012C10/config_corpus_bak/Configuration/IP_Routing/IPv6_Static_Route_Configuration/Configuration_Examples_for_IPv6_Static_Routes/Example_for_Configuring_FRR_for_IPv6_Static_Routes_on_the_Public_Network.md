Example for Configuring FRR for IPv6 Static Routes on the Public Network
========================================================================

FRR for IPv6 static routes on the public network can fast detect link failures.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365505__fig_dc_vrp_static-route_disjoin_cfg_004701), it is required that two IPv6 static routes with Device A and Device B as the next hops be configured on Device D and that Link B function as the backup of Link A. If Link A fails, traffic is switched to the Link B immediately.

**Figure 1** Networking for configuring FRR for IPv6 static routes on the public network![](../../../../public_sys-resources/note_3.0-en-us.png) 

In this example, interface1, interface2, interface3, interface4, and interface5 represent GE 0/1/1, GE 0/1/2, GE 0/1/3, GE 0/2/3, and GE 0/3/3, respectively.


  
![](images/fig_dc_vrp_static-route_disjoin_cfg_004701.png)  


#### Precautions

When configuring FRR for IPv6 static routes on the public network, ensure that there are at least two IPv6 static routes to the same destination address.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure two IPv6 static routes with Device A and Device B as the next hops on Device D.
2. On Device D, set a higher priority for Link A to ensure that Link A becomes the primary link.
3. Enable FRR for IPv6 static routes on Device D, and check the backup outbound interface and the backup next hop.
4. Configure static BFD for IPv6 static routes to speed up fault detection.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   To speed up fault detection, configure dynamic or static BFD for IPv6 static routes. In this example, static BFD for IPv6 static routes is used. This is because it is more commonly used on the live network.
5. Disable FRR for IPv6 static routes, and check the backup outbound interface and the backup next hop.

#### Data Preparation

To complete the configuration, you need preference values of IPv6 static routes.


#### Procedure

1. Configure an IP address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365505__section_dc_vrp_static-route_disjoin_cfg_004705) in this section.
2. Configure IPv6 static routes.
   
   
   
   # On Device A, configure IPv6 static routes.
   
   ```
   [~DeviceA] ipv6 route-static 2001:db8:5:: 64 GigabitEthernet0/1/2 2001:db8:1::1
   ```
   ```
   [*DeviceA] ipv6 route-static 2001:db8:6:: 64 GigabitEthernet0/2/3 2001:db8:3::2
   ```
   ```
   [*DeviceA] commit
   ```
   
   # On Device B, configure IPv6 static routes.
   
   ```
   [~DeviceB] ipv6 route-static 2001:db8:5:: 64 GigabitEthernet0/1/1 2001:db8:2::1
   ```
   ```
   [*DeviceB] ipv6 route-static 2001:db8:6:: 64 GigabitEthernet0/3/3 2001:db8:4::2
   ```
   ```
   [*DeviceB] commit
   ```
   
   # On Device C, configure IPv6 static routes.
   
   ```
   [~DeviceC] ipv6 route-static 2001:db8:5:: 64 GigabitEthernet0/2/3 2001:db8:3::1
   ```
   ```
   [*DeviceC] ipv6 route-static 2001:db8:5:: 64 GigabitEthernet0/3/3 2001:db8:4::1
   ```
   ```
   [*DeviceC] ipv6 route-static 2001:db8:1:: 64 GigabitEthernet0/2/3 2001:db8:3::1
   ```
   ```
   [*DeviceC] ipv6 route-static 2001:db8:2:: 64 GigabitEthernet0/3/3 2001:db8:4::1
   ```
   ```
   [*DeviceC] commit
   ```
   
   # On Device D, configure IPv6 static routes.
   
   ```
   [~DeviceD] ipv6 route-static 2001:db8:6:: 64 GigabitEthernet0/1/2 2001:db8:1::2
   ```
   ```
   [*DeviceD] ipv6 route-static 2001:db8:6:: 64 GigabitEthernet0/1/1 2001:db8:2::2
   ```
   ```
   [*DeviceD] ipv6 route-static 2001:db8:3:: 64 GigabitEthernet0/1/2 2001:db8:1::2
   ```
   ```
   [*DeviceD] ipv6 route-static 2001:db8:4:: 64 GigabitEthernet0/1/1 2001:db8:2::2
   ```
   ```
   [*DeviceD] commit
   ```
   ```
   [~DeviceD] quit
   ```
   
   # Check the IP routing table of Device D. The following command output shows that load balancing is performed between the two IPv6 static routes.
   
   ```
   <DeviceD> display ipv6 routing-table
   ```
   ```
   Routing Table : _public_
            Destinations : 13        Routes : 13
   
   Destination  : ::1                                     PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : InLoopBack0                             Flags        : D
   
   Destination  : ::FFFF:127.0.0.0                        PrefixLength : 104
   NextHop      : ::FFFF:127.0.0.1                        Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : InLoopBack0                             Flags        : D
   
   Destination  : ::FFFF:127.0.0.1                        PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : InLoopBack0                             Flags        : D
   
   Destination  : 2001:db8:1::                            PrefixLength : 64
   NextHop      : 2001:db8:1::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/2                    Flags        : D
   
   Destination  : 2001:db8:1::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/2                    Flags        : D
   
   Destination  : 2001:DB8:2::                            PrefixLength : 64
   NextHop      : 2001:DB8:2::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/1                           Flags        : D
   
   Destination  : 2001:DB8:2::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/1                           Flags        : D
   
   Destination  : 2001:DB8:3::                            PrefixLength : 64
   NextHop      : 2001:DB8:1::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/2                           Flags        : D
   
   Destination  : 2001:DB8:4::                            PrefixLength : 64
   NextHop      : 2001:DB8:2::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/1                           Flags        : D
   
   Destination  : 2001:db8:5::                            PrefixLength : 64
   NextHop      : 2001:db8:5::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/3                    Flags        : D
   
   Destination  : 2001:db8:5::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/3                    Flags        : D
   
   Destination  : 2001:db8:6::                            PrefixLength : 64
   NextHop      : 2001:db8:2::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/1                    Flags        : D
   
   Destination  : 2001:db8:6::                            PrefixLength : 64
   NextHop      : 2001:db8:1::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/2                    Flags        : D
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : D   
   ```
3. Change the priorities of the IPv6 static routes.
   
   
   
   # Change the preference value of the IPv6 static route on Device D.
   
   ```
   <DeviceD> system-view
   ```
   ```
   [~DeviceD] ipv6 route-static 2001:db8:6:: 64 GigabitEthernet0/1/2 2001:db8:1::2 preference 40
   ```
   ```
   [*DeviceD] commit
   ```
   ```
   [~DeviceD] quit
   ```
   
   # Check the routing table of Device D. The following command output shows that the preference value of the IPv6 static route has been changed.
   
   ```
   <DeviceD> display ipv6 routing-table
   ```
   ```
   Routing Table : _public_
            Destinations : 13        Routes : 13
   
   Destination  : ::1                                     PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : InLoopBack0                             Flags        : D
   
   Destination  : ::FFFF:127.0.0.0                        PrefixLength : 104
   NextHop      : ::FFFF:127.0.0.1                        Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : InLoopBack0                             Flags        : D
   
   Destination  : ::FFFF:127.0.0.1                        PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : InLoopBack0                             Flags        : D
   
   Destination  : 2001:db8:1::                            PrefixLength : 64
   NextHop      : 2001:db8:1::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/2                    Flags        : D
   
   Destination  : 2001:db8:1::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/2                    Flags        : D
   
   Destination  : 2001:DB8:2::                            PrefixLength : 64
   NextHop      : 2001:DB8:2::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/1                           Flags        : D
   
   Destination  : 2001:DB8:2::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/1                           Flags        : D
   
   Destination  : 2001:DB8:3::                            PrefixLength : 64
   NextHop      : 2001:DB8:1::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/2                           Flags        : D
   
   Destination  : 2001:DB8:4::                            PrefixLength : 64
   NextHop      : 2001:DB8:2::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/1                           Flags        : D
   
   Destination  : 2001:db8:5::                            PrefixLength : 64
   NextHop      : 2001:db8:5::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/3                    Flags        : D
   
   Destination  : 2001:db8:5::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/3                    Flags        : D
   
   Destination  : 2001:db8:6::                            PrefixLength : 64
   NextHop      : 2001:db8:1::2                           Preference   : 40
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/2                    Flags        : D
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : D
   ```
4. Enable FRR for IPv6 static routes.
   
   
   
   # Enable FRR for static route on Device D.
   
   ```
   <DeviceD> system-view
   ```
   ```
   [~DeviceD] ipv6 route-static frr
   ```
   ```
   [*DeviceD] commit
   ```
   ```
   [~DeviceD] quit
   ```
   
   # Check the backup outbound interface and the backup next hop on Device D.
   
   ```
   <DeviceD> display ipv6 routing-table 2001:db8:6:: verbose
   ```
   ```
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:6::                            PrefixLength : 64
   NextHop      : 2001:db8:1::2                           Preference   : 40
   Neighbour    : ::                                      ProcessID    : 0
   Label        : NULL                                    Protocol     : Static
   State        : Active Adv                              Cost         : 0
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0
   Priority     : medium                                  Age          : 28sec
   IndirectID   : 0xFC000105
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/2                    Flags        : D
   BkNextHop    : 2001:db8:2::2                           BkInterface  : GigabitEthernet0/1/1
   BkLabel      : NULL                                    BkTunnelID   : 0x0
   BkPETunnelID : 0x0                                     BkIndirectID : 0xFC0001
   ```
5. Configure static BFD for IPv6 static routes.
   
   
   * Configure a BFD session.
     
     # On Device D, configure a BFD session between Device D and Device C.
     
     ```
     <DeviceD> system-view
     ```
     ```
     [~DeviceD] bfd
     ```
     ```
     [*DeviceD-bfd] quit
     ```
     ```
     [*DeviceD] bfd aa bind peer-ipv6 2001:db8:3::2 source-ipv6 2001:db8:1::1
     ```
     ```
     [*DeviceD-bfd-session-aa] discriminator local 10
     ```
     ```
     [*DeviceD-bfd-session-aa] discriminator remote 20
     ```
     ```
     [*DeviceD-bfd-session-aa] commit
     ```
     ```
     [~DeviceD-bfd-session-aa] quit
     ```
     
     # On Device C, configure a BFD session between Device C and Device D.
     
     ```
     <DeviceC> system-view
     ```
     ```
     [~DeviceC] bfd
     ```
     ```
     [*DeviceC-bfd] quit
     ```
     ```
     [*DeviceC] bfd ab bind peer-ipv6 2001:db8:1::1 source-ipv6 2001:db8:3::2
     ```
     ```
     [*DeviceC-bfd-session-ab] discriminator local 20
     ```
     ```
     [*DeviceC-bfd-session-ab] discriminator remote 10
     ```
     ```
     [*DeviceC-bfd-session-ab] commit
     ```
     ```
     [~DeviceC-bfd-session-ab] quit
     ```
   * Configure a static route and bind it to the BFD session.
     
     # On Device D, configure a static route and bind it to the BFD session named **aa**.
     
     ```
     [~DeviceD] ipv6 route-static 2001:db8:6:: 64 GigabitEthernet0/1/2 2001:db8:1::2 preference 40 track bfd-session aa
     ```
6. Simulate a fault on Link A.
   
   
   ```
   [~DeviceD] interface GigabitEthernet0/1/2
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/2] shutdown
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/2] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/2] quit
   ```
   ```
   [~DeviceD] quit
   ```
   
   # Check the routes to 2001:db8:6::/64 on Device D.
   
   ```
   <DeviceD> display ipv6 routing-table 2001:db8:6:: verbose
   ```
   ```
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:6::                            PrefixLength : 64
   NextHop      : 2001:db8:2::2                           Preference   : 60
   Neighbour    : ::                                      ProcessID    : 0
   Label        : NULL                                    Protocol     : Static
   State        : Active Adv                              Cost         : 0
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0
   Priority     : medium                                  Age          : 43sec
   IndirectID   : 0xFC000106
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/1                    Flags        : D
   ```

#### Configuration Files

* Device D configuration file
  
  ```
  #
  sysname DeviceD
  #
  bfd
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
  #
  interface GigabitEthernet0/1/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:5::1/64
  #
  bfd aa bind peer-ipv6 2001:db8:3::2 source-ipv6 2001:db8:1::1
   discriminator local 10
   discriminator remote 20
  #
  ipv6 route-static frr
  ipv6 route-static 2001:db8:6:: 64 GigabitEthernet0/1/2 2001:db8:1::2 preference 40 track bfd-session aa
  ipv6 route-static 2001:db8:6:: 64 GigabitEthernet0/1/1 2001:db8:2::2
  ipv6 route-static 2001:db8:3:: 64 GigabitEthernet0/1/2 2001:db8:1::2
  ipv6 route-static 2001:db8:4:: 64 GigabitEthernet0/1/1 2001:db8:2::2
  #
  return
  ```
* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
  #
  interface GigabitEthernet0/2/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
  #
  ipv6 route-static 2001:db8:5:: 64 GigabitEthernet0/1/2 2001:db8:1::1
  ipv6 route-static 2001:db8:6:: 64 GigabitEthernet0/2/3 2001:db8:3::2
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/1
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
  #
  interface GigabitEthernet0/3/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
  #
  ipv6 route-static 2001:db8:5:: 64 GigabitEthernet0/1/1 2001:db8:2::1
  ipv6 route-static 2001:db8:6:: 64 GigabitEthernet0/3/3 2001:db8:4::2
  #
  return
  ```
* Device C configuration file
  
  ```
  #
  sysname DeviceC
  #
  bfd
  #
  interface GigabitEthernet0/1/2
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:6::1/64
  #
  interface GigabitEthernet0/2/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
  #
  interface GigabitEthernet0/3/3
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:4::2/64
  #
  bfd ab bind peer-ipv6 2001:db8:1::1 source-ipv6 2001:db8:3::2
   discriminator local 20
   discriminator remote 10
  #
  ipv6 route-static 2001:db8:5:: 64 GigabitEthernet0/2/3 2001:db8:3::1
  ipv6 route-static 2001:db8:5:: 64 GigabitEthernet0/3/3 2001:db8:4::1
  ipv6 route-static 2001:db8:1:: 64 GigabitEthernet0/2/3 2001:db8:3::1
  ipv6 route-static 2001:db8:2:: 64 GigabitEthernet0/3/3 2001:db8:4::1
  #
  return
  ```