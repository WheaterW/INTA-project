Example for Configuring IPv6 GRE Static Routes
==============================================

This section provides an example for configuring IPv6 GRE static routes. The configuration allows traffic between users to be transmitted over IPv6 GRE tunnels. Static routes are required between a device and its connected clients.

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0172369125__fig_dc_vrp_gre_cfg_205301), DeviceA, DeviceB, and DeviceC belong to the VPN backbone network, and OSPFv3 runs among them.

It is required that a direct link be established between DeviceA and DeviceC. To meet such a requirement, configure an IPv6 GRE tunnel between DeviceA and DeviceC and specify the tunnel interface as the outbound interface of a static route, so that PC1 and PC2 can communicate with each other.

PC1 and PC2 respectively use DeviceA and DeviceC as their default gateways.

**Figure 1** Networking for configuring IPv6 GRE static routes![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and Tunnel1, respectively.


  
![](images/fig_dc_vrp_gre_cfg_205301.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Configure a dynamic routing protocol for Routers to communicate.
2. Create tunnel interfaces on DeviceA and DeviceC, and specify the source and destination addresses of the tunnel interfaces. The tunnel source address is the IP address of the interface that sends packets, and the tunnel destination address is the IP address of the interface that receives packets.
3. To enable the tunnel to support routes, configure a network address for the tunnel interfaces.
4. To transmit traffic between PC1 and PC2 through the IPv6 GRE tunnel, configure a static route to PC2 on DeviceA and a static route to PC1 on DeviceC, and specify the local tunnel interface as the outbound interface of the corresponding static route.

#### Data Preparation

To complete the configuration, you need the following data:

* Data for OSPFv3
* IPv6 GRE tunnel's source and destination addresses and tunnel interface address

#### Procedure

1. Configure interface IP addresses.
   
   
   
   # Configure DeviceA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::1/64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/2/0
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [~DeviceA-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] ipv6 address 2001:db8:3::1/64
   ```
   ```
   [*DeviceA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceB
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8:1::2/64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] interface GigabitEthernet 0/2/0
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [~DeviceB-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ipv6 address 2001:db8:2::2/64
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceC
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [~DeviceC-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ipv6 address 2001:db8:2::1/64
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] interface GigabitEthernet 0/2/0
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] undo shutdown
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 address 2001:db8:4::1/64
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
2. Configure an IGP on the VPN backbone network.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ospfv3 1
   ```
   ```
   [*DeviceA-ospfv3-1] router-id 1.1.1.1
   ```
   ```
   [*DeviceA-ospfv3-1] area 0.0.0.0
   ```
   ```
   [*DeviceA-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceA-ospfv3-1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ospfv3 1 area 0.0.0.0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceB.
   
   ```
   [~DeviceB] ospfv3 1
   ```
   ```
   [*DeviceB-ospfv3-1] router-id 2.2.2.2
   ```
   ```
   [*DeviceB-ospfv3-1] area 0.0.0.0
   ```
   ```
   [*DeviceB-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceB-ospfv3-1] quit
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ospfv3 1 area 0.0.0.0
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   ```
   [~DeviceB] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] ospfv3 1 area 0.0.0.0
   ```
   ```
   [*DeviceB-GigabitEthernet0/2/0] quit
   ```
   ```
   [*DeviceB] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ospfv3 1
   ```
   ```
   [*DeviceC-ospfv3-1] router-id 3.3.3.3
   ```
   ```
   [*DeviceC-ospfv3-1] area 0.0.0.0
   ```
   ```
   [*DeviceC-ospfv3-1-area-0.0.0.0] quit
   ```
   ```
   [*DeviceC-ospfv3-1] quit
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] ospfv3 1 area 0.0.0.0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   After the configuration is complete, run the **display ipv6 routing-table** command on DeviceA and DeviceC. The command output shows that they have learned the OSPFv3 route to the network segment of each other's interconnection interface.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ipv6 routing-table
   ```
   ```
   Routing Table : _public_
            Destinations : 9        Routes : 9
   
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
   
   Destination  : 2001:DB8:1::                            PrefixLength : 64
   NextHop      : 2001:DB8:1::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8:1::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8:2::                            PrefixLength : 64
   NextHop      : FE80::3A00:10FF:FE03:0                  Preference   : 10
   Cost         : 2                                       Protocol     : OSPFv3
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8:3::                            PrefixLength : 64
   NextHop      : 2001:DB8:3::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : 2001:DB8:3::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : D      
   ```
3. Configure tunnel interfaces.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] binding tunnel gre
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceA] commit
   ```
   ```
   [~DeviceA] interface tunnel 1
   ```
   ```
   [*DeviceA-Tunnel1] tunnel-protocol gre ipv6
   ```
   ```
   [*DeviceA-Tunnel1] ipv6 enable
   ```
   ```
   [*DeviceA-Tunnel1] ipv6 address 2001:db8:5::1/64
   ```
   ```
   [*DeviceA-Tunnel1] source 2001:db8:1::1
   ```
   ```
   [*DeviceA-Tunnel1] destination 2001:db8:2::1
   ```
   ```
   [*DeviceA-Tunnel1] quit
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] binding tunnel gre
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] commit
   ```
   ```
   [~DeviceC] interface tunnel 1
   ```
   ```
   [*DeviceC-Tunnel1] tunnel-protocol gre ipv6
   ```
   ```
   [*DeviceC-Tunnel1] ipv6 enable
   ```
   ```
   [*DeviceC-Tunnel1] ipv6 address 2001:db8:5::2/64
   ```
   ```
   [*DeviceC-Tunnel1] source 2001:db8:2::1
   ```
   ```
   [*DeviceC-Tunnel1] destination 2001:db8:1::1
   ```
   ```
   [*DeviceC-Tunnel1] quit
   ```
   ```
   [*DeviceC] commit
   ```
   
   After the configuration is complete, the tunnel interfaces go up and can ping each other.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ipv6 interface Tunnel1
   ```
   ```
   Tunnel1 current state : UP
   IPv6 protocol current state : UP
   IPv6 is enabled, link-local address is FE80::200:174:A191:F872
     Global unicast address(es):
       2001:DB8:5::1, subnet is 2001:DB8:5::/64
     Joined group address(es):
       FF02::1:FF00:1
       FF02::1:FF91:F872
       FF02::2
       FF02::1
     MTU is 1448 bytes
     ND DAD is enabled, number of DAD attempts: 1
     ND reachable time is 1200000 milliseconds
     ND retransmit interval is 1000 milliseconds
     Hosts use stateless autoconfig for addresses
   ```
   ```
   [~DeviceA] ping ipv6 -a 2001:db8:5::1 2001:db8:5::2
   ```
   ```
     PING 2001:DB8:5::2 : 56  data bytes, press CTRL_C to break
       Reply from 2001:DB8:5::2
       bytes=56 Sequence=1 hop limit=64 time=6 ms
       Reply from 2001:DB8:5::2
       bytes=56 Sequence=2 hop limit=64 time=5 ms
       Reply from 2001:DB8:5::2
       bytes=56 Sequence=3 hop limit=64 time=5 ms
       Reply from 2001:DB8:5::2
       bytes=56 Sequence=4 hop limit=64 time=6 ms
       Reply from 2001:DB8:5::2
       bytes=56 Sequence=5 hop limit=64 time=4 ms
   
     --- 2001:DB8:5::2 ping statistics---
       5 packet(s) transmitted
       5 packet(s) received
       0.00% packet loss
       round-trip min/avg/max=4/5/6 ms 
   ```
4. Configure IPv6 static routes.
   
   
   
   # Configure DeviceA.
   
   ```
   [~DeviceA] ipv6 route-static 2001:db8:4:: 64 tunnel1
   ```
   ```
   [*DeviceA] commit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ipv6 route-static 2001:db8:3:: 64 tunnel1
   ```
   ```
   [*DeviceC] commit
   ```
5. Verify the configuration.
   
   
   
   After the configuration is complete, run the **display ipv6 routing-table** command on DeviceA and DeviceC. The command output shows the static route from the local tunnel interface to the user-side network segment of the peer.
   
   # The following example uses the command output on DeviceA.
   
   ```
   [~DeviceA] display ipv6 routing-table
   ```
   ```
   Routing Table : _public_
            Destinations : 12       Routes : 12
   
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
   
   Destination  : 2001:DB8:1::                            PrefixLength : 64
   NextHop      : 2001:DB8:1::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8:1::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8:2::                            PrefixLength : 64
   NextHop      : FE80::3A00:10FF:FE03:0                  Preference   : 10
   Cost         : 2                                       Protocol     : OSPFv3
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/1/0                    Flags        : D
   
   Destination  : 2001:DB8:3::                            PrefixLength : 64
   NextHop      : 2001:DB8:3::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : 2001:DB8:3::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : GigabitEthernet0/2/0                    Flags        : D
   
   Destination  : 2001:DB8:4::                            PrefixLength : 64
   NextHop      : 2001:DB8:5::1                           Preference   : 60
   Cost         : 0                                       Protocol     : Static
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : Tunnel1                                 Flags        : D
   
   Destination  : 2001:DB8:5::                            PrefixLength : 64
   NextHop      : 2001:DB8:5::1                           Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : Tunnel1                                 Flags        : D
   
   Destination  : 2001:DB8:5::1                           PrefixLength : 128
   NextHop      : ::1                                     Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : Tunnel1                                 Flags        : D
   
   Destination  : FE80::                                  PrefixLength : 10
   NextHop      : ::                                      Preference   : 0
   Cost         : 0                                       Protocol     : Direct
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : NULL0                                   Flags        : D       
   ```

#### Configuration Files

* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0  
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::1/64
   ospfv3 1 area 0.0.0.0
   binding tunnel gre 
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:3::1/64
  #
  interface Tunnel1
   ipv6 enable
   ipv6 address 2001:DB8:5::1/64
   tunnel-protocol gre ipv6
   source 2001:DB8:1::1
   destination 2001:DB8:2::1    
  #
  ipv6 route-static 2001:DB8:4:: 64 Tunnel1 
  #
  return
  
  ```
* DeviceB configuration file
  
  ```
  #
  sysname DeviceB
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0  
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:1::2/64
   ospfv3 1 area 0.0.0.0 
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::2/64
   ospfv3 1 area 0.0.0.0
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  ospfv3 1
   router-id 3.3.3.3
   area 0.0.0.0   
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:2::1/64
   ospfv3 1 area 0.0.0.0
   binding tunnel gre
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:DB8:4::1/64 
  #
  interface Tunnel1
   ipv6 enable
   ipv6 address 2001:DB8:5::2/64
   tunnel-protocol gre ipv6
   source 2001:DB8:2::1
   destination 2001:DB8:1::1   
  #
  ipv6 route-static 2001:DB8:3:: 64 Tunnel1 
  #
  return
  ```