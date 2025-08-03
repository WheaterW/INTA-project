Example for Configuring IPv6 Static Routes
==========================================

You can configure IPv6 static routes to interconnect any two devices on an IPv6 network.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172365490__fig_dc_vrp_static-route_disjoin_cfg_002201), the prefix of all the IPv6 addresses is 64. It is required that IPv6 static routes be configured between Routers to ensure that all hosts communicate with Routers. GE interfaces on Routers use IPv6 link-local addresses.

**Figure 1** Networking for configuring IPv6 static routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE0/1/0, GE0/2/0, and GE0/3/0, respectively.


  
![](images/fig_dc_vrp_static-route_disjoin_cfg_002201.png)

#### Precautions

When configuring an IPv6 static route, specify a next hop address if the outbound interface is of the broadcast type.


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure IPv6 addresses for GE interfaces on each Router.
2. Configure the IPv6 static route and the default route on each Router.
3. Configure the IPv6 default gateway on each host so that any two hosts can communicate with each other.

#### Data Preparation

To complete the configuration, you need the following data:

* Default route with GE 0/1/0 as the outbound interface on Device A
* Static route to 2001:db8:1:: 64 with GE 0/1/0 as the outbound interface on Device B
* Static route to 2001:db8:3:: 64 with GE 0/2/0 as the outbound interface on Device B
* Default route with GE 0/1/0 as the outbound interface on Device C
* Default gateways of PC1, PC2, and PC3

#### Procedure

1. Configure an IPv6 address for each interface. For configuration details, see [Configuration Files](#EN-US_TASK_0172365490__section_dc_vrp_static-route_disjoin_cfg_002205) in this section.
2. Configure IPv6 static routes.
   
   
   
   # Configure an IPv6 default route on Device A.
   
   ```
   [~DeviceA] ipv6 route-static :: 0 gigabitethernet 0/1/0 2001:db8:4::2
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure two IPv6 static routes on Device B.
   
   ```
   [~DeviceB] ipv6 route-static 2001:db8:1:: 64 gigabitethernet 0/1/0 2001:db8:4::1
   ```
   ```
   [*DeviceB] ipv6 route-static 2001:db8:3:: 64 gigabitethernet 0/2/0 2001:db8:5::1
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure an IPv6 default route on Device C.
   
   ```
   [~DeviceC] ipv6 route-static :: 0 gigabitethernet 0/1/0 2001:db8:5::2
   ```
   ```
   [*DeviceC] commit
   ```
3. Configure host addresses and gateways.
   
   
   
   Configure IPv6 addresses for hosts, and then configure the default gateways of PC1, PC2, and PC3 as 2001:db8:1::1, 2001:db8:2::1, and 2001:db8:3::1, respectively.
4. Verify the configuration.
   
   
   
   # Check the IPv6 routing table of Device A.
   
   ```
   [~DeviceA] display ipv6 routing-table
   ```
   ```
   Routing Table : _public_
            Destinations : 9        Routes : 9
   
   Destination  : ::                                      PrefixLength : 0
   NextHop      : 2001:DB8:4::2                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8::1                             PrefixLength : 128
   NextHop      : 2001:DB8::1                             Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : InLoopBack0                             Flags        : D
   
   Destination  : ::FFFF:127.0.0.0                        PrefixLength : 104
   NextHop      : ::FFFF:127.0.0.1                        Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : InLoopBack0                             Flags        : D
   
   Destination  : ::FFFF:127.0.0.1                        PrefixLength : 128
   NextHop      : 2001:DB8::1                             Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : InLoopBack0                             Flags        : D
   
   Destination  : 2001:DB8:1::                            PrefixLength : 64
   NextHop      : 2001:DB8:1::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : 2001:DB8:1::1                           PrefixLength : 128
   NextHop      : 2001:DB8::1                             Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : 2001:DB8:4::                            PrefixLength : 64
   NextHop      : 2001:DB8:4::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8:4::1                           PrefixLength : 128
   NextHop      : 2001:DB8::1                             Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : D
   
   ```
   
   # Run the **ping** command to verify the connectivity.
   
   ```
   [~DeviceA] ping ipv6 2001:db8:3::1
   ```
   ```
     PING 2001:DB8:3::1 : 56  data bytes, press CTRL_C to break
       Reply from 2001:DB8:3::1
       bytes=56 Sequence=1 hop limit=63 time=6 ms
       Reply from 2001:DB8:3::1
       bytes=56 Sequence=2 hop limit=63 time=2 ms
       Reply from 2001:DB8:3::1
       bytes=56 Sequence=3 hop limit=63 time=1 ms
       Reply from 2001:DB8:3::1
       bytes=56 Sequence=4 hop limit=63 time=1 ms
       Reply from 2001:DB8:3::1
       bytes=56 Sequence=5 hop limit=63 time=1 ms
   
     --- 2001:DB8:3::1 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=1/2/6 ms 
   ```
   
   # Run the **tracert** command to verify the connectivity.
   
   ```
   [~DeviceA] tracert ipv6 2001:db8:3::1
   ```
   ```
     traceroute to 2001:DB8:3::1  30 hops max,60 bytes packet
    1 2001:DB8:4::2 5 ms  1 ms  1 ms
    2 2001:DB8:3::1 7 ms  2 ms  3 ms
   ```

#### Configuration Files

* Device A configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:1::1/64
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:4::1/64
  #
  ipv6 route-static :: 0 GigabitEthernet 0/1/0 2001:db8:4::2
  #
  return
  ```
* Device B configuration file
  
  ```
  #
  sysname DeviceB
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:4::2/64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:5::2/64
  #
  interface GigabitEthernet0/3/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2::1/64
  #
  ipv6 route-static 2001:db8:1:: 64 GigabitEthernet0/1/0 2001:db8:4::1
  ipv6 route-static 2001:db8:3:: 64 GigabitEthernet0/2/0 2001:db8:5::1
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
   ipv6 address 2001:db8:5::1/64
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:3::1/64
  #
  ipv6 route-static :: 0 GigabitEthernet0/1/0 2001:db8:5::2
  #
  return
  ```