Example for Configuring IPv6 FRR
================================

Example for Configuring IPv6 FRR

#### Networking Requirements

On the network shown in [Figure 1](#EN-US_TASK_0000001351890102__fig_dc_vrp_ip-route_cfg_002801), it is required that a backup outbound interface and a backup next hop be configured on DeviceT so that Link B functions as the backup of Link A. If Link A fails, traffic is rapidly switched to Link B, improving network reliability.

**Figure 1** Configuring public network IPv6 FRR![](public_sys-resources/note_3.0-en-us.png) 

In this example, Interface1, Interface2, and Interface3 represent 100GE1/0/1, 100GE1/0/2, and 100GE1/0/3, respectively.


  
![](figure/en-us_image_0000001404144765.png)

#### Configuration Roadmap

The configuration roadmap is as follows:

1. Enable basic OSPFv3 functions on DeviceT, DeviceA, and DeviceC.
2. Enable basic IPv6 IS-IS functions on DeviceT, DeviceB, and DeviceC.
3. Enable public network IPv6 FRR on DeviceT, and then check information about the backup outbound interface and backup next hop.
4. Disable IPv6 FRR, and then check information about the backup outbound interface and backup next hop.

#### Procedure

1. Assign an IPv6 address to each interface. For detailed configurations, see [Configuration Scripts](#EN-US_TASK_0000001351890102__postreq8302349163615).
2. Configure OSPFv3 on DeviceT, DeviceA, and DeviceC. For details, see [Configuration Scripts](#EN-US_TASK_0000001351890102__postreq8302349163615).
3. Configure IPv6 IS-IS on DeviceT, DeviceB, and DeviceC. For details, see [Configuration Scripts](#EN-US_TASK_0000001351890102__postreq8302349163615).
4. Check routing information.
   
   
   
   # Check routes destined for 2001:db8:20::1 on DeviceT.
   
   
   
   ```
   <DeviceT> display ipv6 routing-table 2001:db8:20::1 64 verbose
   Routing Table : _public_
   Summary Count : 2
   
   Destination  : 2001:db8:20::                          PrefixLength : 64
   NextHop      : 2001:db8:200::2                         Preference   : 10
   Neighbour    : ::                                      ProcessID    : 1
   Label        : NULL                                    Protocol     : OSPFv3
   State        : Active Adv                              Cost         : 3
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0
   IndirectID   : 0x69                                    Age          : 269sec
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/2                   Flags        : D
   
   Destination  : 2001:db8:20::                          PrefixLength : 64
   NextHop      : 2001:db8:100::2                              Preference   : 15
   Neighbour    : ::                                      ProcessID    : 1
   Label        : NULL                                    Protocol     : ISIS
   State        : Inactive Adv                            Cost         : 30
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0
   IndirectID   : 0xb5                                    Age          : 201sec
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/3                   Flags        : 0
   ```
   
   The preceding command output shows that there are two routes to 2001:db8:20::1/64 and that the route with 2001:db8:200::2 as the next hop is optimal because the OSPFv3 route priority is higher than the IPv6 IS-IS route priority.
5. Enable public network IPv6 FRR.
   
   
   
   # Enable IPv6 FRR on DeviceT.
   
   ```
   [~DeviceT] ipv6 frr
   [*DeviceT] commit
   ```
   
   # Check the backup outbound interface and the backup next hop on DeviceT.
   
   ```
   <DeviceT> display ipv6 routing-table 2001:db8:20::1 64 verbose
   Routing Table : _public_
   Summary Count : 2
   
   Destination  : 2001:db8:20::                           PrefixLength : 64
   NextHop      : 2001:db8:200::2                         Preference  : 10
   Neighbour    : ::                                      ProcessID    : 1
   Label        : NULL                                    Protocol    : OSPFv3
   State        : Active Adv                              Cost         : 3
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0
   IndirectID   : 0x69                                    Age          : 553sec
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/2                   Flags        : D
   BkNextHop   : 2001:db8:100::2                         BkInterface : 100GE1/0/3
   BkLabel      : NULL                                    BkTunnelID   : 0x0
   BkPETunnelID : 0x0                                     BkIndirectID : 0xb5
   
   Destination  : 2001:db8:20::                           PrefixLength : 64
   NextHop      : 2001:db8:100::2                         Preference  : 15
   Neighbour    : ::                                      ProcessID    : 1
   Label        : NULL                                    Protocol     : ISIS
   State        : Inactive Adv                            Cost         : 30
   Entry ID     : 0                                       EntryFlags   : 0x00000000
   Reference Cnt: 0                                       Tag          : 0
   IndirectID   : 0xb5                                    Age          : 485sec
   RelayNextHop : ::                                      TunnelID     : 0x0
   Interface    : 100GE1/0/3                  Flags        : 0
   ```
   
   The preceding command output shows that the route to 2001:db8:20::1/64 has a backup outbound interface and a backup next hop and that the IS-IS route is the backup route.

#### Verifying the Configuration

# Simulate a link fault on DeviceT.

```
[~DeviceT] interface 100GE1/0/2
[~DeviceT-100GE1/0/2] shutdown
[*DeviceT-100GE1/0/2] commit
[~DeviceT-100GE1/0/2] quit
```

# On DeviceT, check the routes to 2001:db8:20::1/64.

```
<DeviceT> display ipv6 routing-table 2001:db8:20::1 64 verbose
Routing Table : _public_
Summary Count : 1

Destination  : 2001:db8:20::                           PrefixLength : 64
NextHop      : 2001:db8:100:2                          Preference   : 15
Neighbour    : ::                                      ProcessID    : 1
Label        : NULL                                    Protocol    : ISIS
State        : Active Adv                              Cost         : 30
Entry ID     : 0                                       EntryFlags   : 0x00000000
Reference Cnt: 0                                       Tag          : 0
IndirectID   : 0xb5                                    Age          : 1279sec
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : 100GE1/0/3                   Flags        : D
```

The preceding command output shows that traffic is switched to Link B after Link A fails.


#### Configuration Scripts

* DeviceT
  ```
  # 
  sysname DeviceT
  #
  ipv6 frr
  #
  isis 1
   is-level level-1 
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0001.00
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
   area 0.0.0.1
  # 
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:10::1/64
   ospfv3 1 area 0.0.0.1
   isis ipv6 enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:200::1/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:100::1/64
   isis enable 1
   isis ipv6 enable 1
  return
  ```

* DeviceA
  ```
  # 
  sysname DeviceA
  #
  ospfv3 1
   router-id 2.2.2.2
   area 0.0.0.0
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:200::2/64
   ospfv3 1 area 0.0.0.0
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:201::2/64
   ospfv3 1 area 0.0.0.0
  return
  ```

* DeviceB
  ```
  # 
  sysname DeviceB
  #
  isis 1
   is-level level-1 
   ipv6 enable topology ipv6
   network-entity 10.0000.0000.0002.00
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:100::2/64
   isis ipv6 enable 1 
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:101::2/64
   isis ipv6 enable 1 
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
   ipv6 enable topology ipv6 
   network-entity 10.0000.0000.0003.00
  #
  ospfv3 1
   router-id 1.1.1.1
   area 0.0.0.0
   area 0.0.0.2
  #
  interface 100GE1/0/1
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:20::1/64
   isis enable 1
  #
  interface 100GE1/0/2
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:201::1/64
   ospfv3 1 area 0.0.0.2
  #
  interface 100GE1/0/3
   undo portswitch
   ipv6 enable
   ipv6 address 2001:db8:101::1/64
   isis enable 1
   isis ipv6 enable 1 
  #
  return
  ```