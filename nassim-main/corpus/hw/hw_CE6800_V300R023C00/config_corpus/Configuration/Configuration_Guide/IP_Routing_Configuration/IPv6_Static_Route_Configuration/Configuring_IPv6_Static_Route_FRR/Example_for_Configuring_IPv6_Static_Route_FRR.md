Example for Configuring IPv6 Static Route FRR
=============================================

Example for Configuring IPv6 Static Route FRR

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001176663221__fig_dc_vrp_static-route_disjoin_cfg_004701), two IPv6 static routes are configured on DeviceD. The next hop in one static route is set to DeviceA and that in the other static route is set to DeviceB. Link B backs up link A. If link A fails, traffic is rapidly switched to link B.

**Figure 1** Network diagram of IPv6 static route FRR![](public_sys-resources/note_3.0-en-us.png) 

In this example, interface 1, interface 2, and interface 3 represent 100GE 1/0/1, 100GE 1/0/2, and 100GE 1/0/3, respectively.


  
![](figure/en-us_image_0000001130623696.png)

#### Precautions

During the configuration, note the following:

* Ensure that there are at least two IPv6 static routes to the same destination address when configuring IPv6 static route FRR.

#### Configuration Roadmap

The configuration roadmap is as follows:

1. On DeviceD, configure an IPv6 static route with DeviceA as the next hop and another IPv6 static route with DeviceB as the next hop.
2. On DeviceD, set a smaller preference value for link A to ensure that link A becomes the active link.
3. On DeviceD, enable FRR for IPv6 static routes and check information about the backup outbound interface and backup next hop.
4. Configure dynamic BFD for IPv6 static route to speed up fault detection.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   To speed up fault detection, configure dynamic BFD for IPv6 static route or static BFD for IPv6 static route.

#### Procedure

1. Configure IPv6 addresses for interfaces on each device.
   
   
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   [~HUAWEI] sysname DeviceD
   [*HUAWEI] commit
   [~DeviceD] interface 100ge 1/0/1
   [~DeviceD-100GE1/0/1] undo portswitch
   [*DeviceD-100GE1/0/1] ipv6 enable
   [*DeviceD-100GE1/0/1] ipv6 address 2001:db8:2::1 64
   [*DeviceD-100GE1/0/1] quit
   [*DeviceD] interface 100ge 1/0/2
   [*DeviceD-100GE1/0/2] undo portswitch
   [*DeviceD-100GE1/0/2] ipv6 enable
   [*DeviceD-100GE1/0/2] ipv6 address 2001:db8:1::1 64
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] interface 100ge 1/0/3
   [*DeviceD-100GE1/0/3] undo portswitch
   [*DeviceD-100GE1/0/3] ipv6 enable
   [*DeviceD-100GE1/0/3] ipv6 address 2001:db8:5::1 64
   [*DeviceD-100GE1/0/3] quit
   [*DeviceD] commit
   ```
   
   The configurations of DeviceA, DeviceB, and DeviceC are similar to the configuration of DeviceD. For detailed configurations, see Configuration Scripts.
2. Configure IPv6 static routes.
   
   
   
   # On DeviceA, configure IPv6 static routes.
   
   ```
   [~DeviceA] ipv6 route-static 2001:db8:5:: 64 100ge 1/0/1 2001:db8:1::1
   [*DeviceA] ipv6 route-static 2001:db8:6:: 64 100ge 1/0/2 2001:db8:3::2
   [*DeviceA] commit
   ```
   
   # On DeviceB, configure IPv6 static routes.
   
   ```
   [~DeviceB] ipv6 route-static 2001:db8:5:: 64 100ge 1/0/1 2001:db8:2::1
   [*DeviceB] ipv6 route-static 2001:db8:6:: 64 100ge 1/0/2 2001:db8:4::2
   [*DeviceB] commit
   ```
   
   # On DeviceC, configure IPv6 static routes.
   
   ```
   [~DeviceC] ipv6 route-static 2001:db8:5:: 64 100ge 1/0/1 2001:db8:3::1
   [*DeviceC] ipv6 route-static 2001:db8:5:: 64 100ge 1/0/2 2001:db8:4::1
   [*DeviceC] ipv6 route-static 2001:db8:1:: 64 100ge 1/0/1 2001:db8:3::1
   [*DeviceC] ipv6 route-static 2001:db8:2:: 64 100ge 1/0/2 2001:db8:4::1
   [*DeviceC] commit
   ```
   
   # On DeviceD, configure IPv6 static routes.
   
   ```
   [~DeviceD] ipv6 route-static 2001:db8:6:: 64 100ge 1/0/2 2001:db8:1::2
   [*DeviceD] ipv6 route-static 2001:db8:6:: 64 100ge 1/0/1 2001:db8:2::2
   [*DeviceD] ipv6 route-static 2001:db8:3:: 64 100ge 1/0/2 2001:db8:1::2
   [*DeviceD] ipv6 route-static 2001:db8:4:: 64 100ge 1/0/1 2001:db8:2::2
   [*DeviceD] commit
   ```
   
   # Check the IPv6 routing table of DeviceD. The following command output shows that load balancing is performed between the two IPv6 static routes.
   
   ```
   [~DeviceD] display ipv6 routing-table
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
   Interface    : 100GE1/0/2                               Flags        : D
   
   Destination  : 2001:db8:1::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/2                               Flags        : D
   
   Destination  : 2001:DB8:2::                            PrefixLength : 64
   NextHop      : 2001:DB8:2::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                               Flags        : D
   
   Destination  : 2001:DB8:2::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                               Flags        : D
   
   Destination  : 2001:DB8:3::                            PrefixLength : 64
   NextHop      : 2001:DB8:1::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/2                               Flags        : D
   
   Destination  : 2001:DB8:4::                            PrefixLength : 64
   NextHop      : 2001:DB8:2::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                               Flags        : D
   
   Destination  : 2001:db8:5::                            PrefixLength : 64
   NextHop      : 2001:db8:5::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/3                               Flags        : D
   
   Destination  : 2001:db8:5::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/3                               Flags        : D
   
   Destination  : 2001:db8:6::                     PrefixLength : 64
   NextHop      : 2001:db8:2::2                    Preference   : 60 
   Cost         : 0                                Protocol     : Static 
   RelayNextHop : ::                               TunnelID     : 0x0 
   Interface    : 100GE1/0/1                        Flags        : D
   
   Destination  : 2001:db8:6::                     PrefixLength : 64
   NextHop      : 2001:db8:1::2                    Preference   : 60 
   Cost         : 0                                Protocol     : Static 
   RelayNextHop : ::                               TunnelID     : 0x0 
   Interface    : 100GE1/0/2                        Flags        : D
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : D   
   ```
3. Change the preference value of the IPv6 static routes.
   
   
   
   # Change the preference value of IPv6 static routes on DeviceD.
   
   ```
   [~DeviceD] ipv6 route-static 2001:db8:6:: 64 100ge 1/0/2 2001:db8:1::2 preference 40
   [*DeviceD] commit
   ```
   
   # Check the IPv6 routing table of DeviceD. The following command output shows that the preferences of IPv6 static routes have been changed.
   
   ```
   [~DeviceD] display ipv6 routing-table
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
   Interface    : 100GE1/0/2                               Flags        : D
   
   Destination  : 2001:db8:1::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/2                               Flags        : D
   
   Destination  : 2001:DB8:2::                            PrefixLength : 64
   NextHop      : 2001:DB8:2::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                               Flags        : D
   
   Destination  : 2001:DB8:2::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                               Flags        : D
   
   Destination  : 2001:DB8:3::                            PrefixLength : 64
   NextHop      : 2001:DB8:1::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/2                               Flags        : D
   
   Destination  : 2001:DB8:4::                            PrefixLength : 64
   NextHop      : 2001:DB8:2::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/1                               Flags        : D
   
   Destination  : 2001:db8:5::                            PrefixLength : 64
   NextHop      : 2001:db8:5::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/3                               Flags        : D
   
   Destination  : 2001:db8:5::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/3                               Flags        : D
   
   Destination  : 2001:db8:6::                      PrefixLength : 64
   NextHop      : 2001:db8:1::2                     Preference   : 40 
   Cost         : 0                                 Protocol     : Static 
   RelayNextHop : ::                                TunnelID     : 0x0 
   Interface    : 100GE1/0/2                         Flags        : D
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : D
   ```
4. Enable IPv6 static route FRR.
   
   
   
   # Enable IPv6 static route FRR on DeviceD.
   
   ```
   [~DeviceD] ipv6 route-static frr
   [*DeviceD] commit
   ```
   
   # Check the backup outbound interface and next-hop IP address on DeviceD.
   
   ```
   [~DeviceD] display ipv6 routing-table 2001:db8:6:: verbose
   Routing Table : _public_
   Summary Count : 1
   
   Destination  : 2001:db8:6::                           PrefixLength : 64
   NextHop      : 2001:db8:1::2                       Preference   : 40
   Neighbour    : ::                                      ProcessID    : 0
   Label        : NULL                                    Protocol     : Static
   State        : Active Adv                              Cost         : 0
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0
   Priority     : medium                                  Age          : 28sec
   IndirectID   : 0xFC000105
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/2                            Flags        : D
   BkNextHop    : 2001:db8:2::2                        BkInterface  : 100GE1/0/1
   BkLabel      : NULL                                    BkTunnelID   : 0x0
   BkPETunnelID : 0x0                                     BkIndirectID : 0xFC0001
   ```
5. Configure dynamic BFD for IPv6 static route.
   
   
   
   # On DeviceD, configure dynamic BFD for IPv6 static route.
   
   ```
   [~DeviceD] bfd
   [*DeviceD-bfd] quit
   [*DeviceD] ipv6 route-static bfd 2001:db8:3::2 local-address 2001:db8:1::1
   [*DeviceD] ipv6 route-static 2001:db8:6:: 64 2001:db8:1::1 bfd enable
   [*DeviceD] commit
   ```
   
   # On DeviceC, configure dynamic BFD for IPv6 static route.
   
   ```
   [~DeviceC] bfd
   [*DeviceC-bfd] quit
   [*DeviceC] ipv6 route-static bfd 2001:db8:1::1 local-address 2001:db8:3::2
   [*DeviceC] ipv6 route-static 2001:db8:5:: 64 2001:db8:1::2 bfd enable
   [*DeviceC] commit
   ```
6. # Simulate a fault on link A so that traffic is rapidly switched to link B.
   
   
   ```
   [~DeviceD] interface 100ge 1/0/2
   [~DeviceD-100GE1/0/2] shutdown
   [*DeviceD-100GE1/0/2] quit
   [*DeviceD] commit
   ```

#### Verifying the Configuration

# Check the routes to 2001:db8:6::/64 on DeviceD.

```
[~DeviceD] display ipv6 routing-table 2001:db8:6:: verbose
Routing Table : _public_
Summary Count : 1

Destination  : 2001:db8:6::                            PrefixLength : 64
NextHop    : 2001:db8:2::2                          Preference   : 60
Neighbour    : ::                                      ProcessID    : 0
Label        : NULL                                    Protocol     : Static
State        : Active Adv                              Cost         : 0
Entry ID     : 0                                       EntryFlags   : 0x00000000
Reference Cnt: 0                                       Tag          : 0
Priority     : medium                                  Age          : 43sec
IndirectID   : 0xFC000106
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/1                    Flags        : D
```

The command output shows that the outbound interface of 2001:db8:6::/64 has been changed to 2001:db8:2::2.


#### Configuration Scripts

* DeviceD
  
  ```
  #
  sysname DeviceD
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:5::1/64
  #
  ipv6 route-static frr
  ipv6 route-static 2001:db8:6:: 64 100GE1/0/2 2001:db8:1::2 preference 40 track bfd-session aa
  ipv6 route-static 2001:db8:6:: 64 100GE1/0/1 2001:db8:2::2
  ipv6 route-static 2001:db8:3:: 64 100GE1/0/2 2001:db8:1::2
  ipv6 route-static 2001:db8:4:: 64 100GE1/0/1 2001:db8:2::2
  #
  ipv6 route-static bfd 2001:db8:3::2 local-address 2001:db8:1::1
  ipv6 route-static 2001:db8:6:: 64 2001:db8:1::1 bfd enable
  #
  return
  ```
* DeviceA
  
  ```
  #
  sysname DeviceA
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:1::2/64
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
  #
  ipv6 route-static 2001:db8:5:: 64 100GE1/0/1 2001:db8:1::1
  ipv6 route-static 2001:db8:6:: 64 100GE1/0/2 2001:db8:3::2
  #
  return
  ```
* DeviceB
  
  ```
  #
  sysname DeviceB
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:2::2/64
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
  #
  ipv6 route-static 2001:db8:5:: 64 100GE1/0/1 2001:db8:2::1
  ipv6 route-static 2001:db8:6:: 64 100GE1/0/2 2001:db8:4::2
  #
  return
  ```
* DeviceC
  
  ```
  #
  sysname DeviceC
  #
  bfd
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:3::2/64
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:4::2/64
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:6::1/64
  #
  ipv6 route-static 2001:db8:5:: 64 100GE1/0/1 2001:db8:3::1
  ipv6 route-static 2001:db8:5:: 64 100GE1/0/2 2001:db8:4::1
  ipv6 route-static 2001:db8:1:: 64 100GE1/0/1 2001:db8:3::1
  ipv6 route-static 2001:db8:2:: 64 100GE1/0/2 2001:db8:4::1
  #
  ipv6 route-static bfd 2001:db8:1::1 local-address 2001:db8:3::2
  ipv6 route-static 2001:db8:5:: 64 2001:db8:1::2 bfd enable
  #
  return
  ```