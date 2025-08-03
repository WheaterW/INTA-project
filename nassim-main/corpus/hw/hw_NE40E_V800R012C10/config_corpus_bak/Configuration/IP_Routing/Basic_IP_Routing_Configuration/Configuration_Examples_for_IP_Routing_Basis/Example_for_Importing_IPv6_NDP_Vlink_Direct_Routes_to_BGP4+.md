Example for Importing IPv6 NDP Vlink Direct Routes to BGP4+
===========================================================

By importing IPv6 NDP Vlink direct routes to BGP4+, you can enable the remote device to obtain information about detailed routes in the VLAN, allowing precise control of data traffic.

#### Networking Requirements

As networks develop, the VLAN technology is widely used. If a user outside a VLAN needs to communicate with users within the VLAN, advertising routes destined for the network segment of the VLAN can achieve this purpose. When users outside the VLAN need to know the IPv6 NDP Vlink direct routes of the VLAN, and apply different traffic policies to routes of the VLAN users, advertising the routes destined for the network segment of the VLAN cannot meet this requirement.

In this case, you can enable the function of IPv6 NDP Vlink direct route advertisement. On the network shown in [Figure 1](#EN-US_TASK_0172365391__fig_dc_vrp_ip-route_cfg_005801), DeviceC is connected to two users through VLANIF interfaces. DeviceD needs to communicate with DeviceB, but not with DeviceA. In this case, you can enable the function of IPv6 NDP Vlink direct route advertisement on DeviceC, and use a route-policy to filter out subnet routes and the route to DeviceA.

**Figure 1** Networking diagram of importing IPv6 NDP Vlink direct routes to BGP4+![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces 1 through 3 in this example represent GE 0/1/0, GE 0/2/0, and GE 0/3/0, respectively.


  
![](images/fig_dc_vrp_ip-route_cfg_005801.png)  


#### Configuration Roadmap

The configuration roadmap is as follows:

1. Create VLANIF interfaces on SwitchA and DeviceC and assign IPv6 addresses to the VLANIF interfaces, and ensure that DeviceA, DeviceB, SwitchA, and DeviceC can communicate with each other.
2. Enable BGP4+ on DeviceC and DeviceD, ensuring that DeviceC and DeviceD are able to advertise IPv6 routes to each other.
3. Enable the function of IPv6 NDP Vlink direct route advertisement on DeviceC.
4. Configure a route-policy on DeviceC, allowing IPv6 routes only from DeviceB to pass through.
5. Enable BGP4+ on DeviceC and import IPv6 direct routes to BGP4+, and use the route-policy to import IPv6 routes only from DeviceB to BGP4+.
6. Associate BGP4+ with the route-policy on DeviceC to filter out the network segment route of the VLAN so that DeviceD cannot learn the network segment route and can communicate with VLAN users based only on IPv6 NDP Vlink direct routes.

#### Data Preparation

To complete the configuration, you need the following data:

* ID of the VLAN in which SwitchA and DeviceC reside (the VLAN ID is 10 in this example)
* Router IDs and AS numbers of Devices C and D (router ID of DeviceC is 1.1.1.1 and router ID of DeviceD is 2.2.2.2, and Devices C and D are in AS 100 in this example)
* Route-policy used to filter direct routes (the route-policy is policy1 in this example)
* Route-policy used to advertise BGP4+ routes on DeviceC (the route-policy is policy2 in this example)

#### Procedure

1. Configure an IP address for each interface.
   
   
   
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
   [*DeviceA-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] ipv6 address 2001:db8:2000::3 64
   ```
   ```
   [*DeviceA-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceA-GigabitEthernet0/1/0] quit
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
   [*DeviceB] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] undo shutdown
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] ipv6 address 2001:db8:2000::4 64
   ```
   ```
   [*DeviceB-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceB-GigabitEthernet0/1/0] quit
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
   [~DeviceC] interface GigabitEthernet 0/2/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 enable
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] ipv6 address 2001:db8:2001::1 64
   ```
   ```
   [*DeviceC-GigabitEthernet0/2/0] commit
   ```
   ```
   [~DeviceC-GigabitEthernet0/2/0] quit
   ```
   
   # Configure DeviceD.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname DeviceD
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~DeviceD] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] ipv6 enable
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] ipv6 address 2001:db8:2001::2 64
   ```
   ```
   [*DeviceD-GigabitEthernet0/1/0] commit
   ```
   ```
   [~DeviceD-GigabitEthernet0/1/0] quit
   ```
2. Configure basic VLAN functions. Create VLANIF 10 on SwitchA and DeviceC and assign IP addresses to the VLANIF interfaces.
   
   
   
   # Configure SwitchA.
   
   ```
   <HUAWEI> system-view
   ```
   ```
   [~HUAWEI] sysname SwitchA
   ```
   ```
   [*HUAWEI] commit
   ```
   ```
   [~SwitchA] vlan 10
   ```
   ```
   [*SwitchA-vlan10] quit
   ```
   ```
   [*SwitchA] interface GigabitEthernet 0/1/0
   ```
   ```
   [*SwitchA-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*SwitchA-GigabitEthernet0/1/0] port link-type access
   ```
   ```
   [*SwitchA-GigabitEthernet0/1/0] port default vlan 10
   ```
   ```
   [*SwitchA-GigabitEthernet0/1/0] quit
   ```
   ```
   [*SwitchA] interface GigabitEthernet 0/2/0
   ```
   ```
   [*SwitchA-GigabitEthernet0/2/0] portswitch
   ```
   ```
   [*SwitchA-GigabitEthernet0/2/0] port link-type access
   ```
   ```
   [*SwitchA-GigabitEthernet0/2/0] port default vlan 10
   ```
   ```
   [*SwitchA-GigabitEthernet0/2/0] quit
   ```
   ```
   [*SwitchA] interface GigabitEthernet 0/3/0
   ```
   ```
   [*SwitchA-GigabitEthernet0/3/0] portswitch
   ```
   ```
   [*SwitchA-GigabitEthernet0/3/0] port link-type access
   ```
   ```
   [*SwitchA-GigabitEthernet0/3/0] port default vlan 10
   ```
   ```
   [*SwitchA-GigabitEthernet0/3/0] quit
   ```
   ```
   [*SwitchA] interface Vlanif 10
   ```
   ```
   [*SwitchA-Vlanif10] ipv6 enable
   ```
   ```
   [*SwitchA-Vlanif10] ipv6 address 2001:db8:2000::2 64
   ```
   ```
   [*SwitchA-Vlanif10] commit
   ```
   ```
   [~SwitchA-Vlanif10] quit
   ```
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] vlan 10
   ```
   ```
   [*DeviceC-vlan10] quit
   ```
   ```
   [*DeviceC] interface GigabitEthernet 0/1/0
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] portswitch
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] port link-type access
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] port default vlan 10
   ```
   ```
   [*DeviceC-GigabitEthernet0/1/0] quit
   ```
   ```
   [*DeviceC] interface Vlanif 10
   ```
   ```
   [*DeviceC-Vlanif10] ipv6 enable
   ```
   ```
   [*DeviceC-Vlanif10] ipv6 address 2001:db8:2000::1 64
   ```
   ```
   [*DeviceC-Vlanif10] commit
   ```
   ```
   [~DeviceC-Vlanif10] quit
   ```
3. Configure BGP4+ between DeviceC and DeviceD.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] router-id 1.1.1.1
   ```
   ```
   [*DeviceC-bgp] peer 2001:db8:2001::2 as-number 100
   ```
   ```
   [*DeviceC-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:db8:2001::2 enable
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
   
   # Configure DeviceD.
   
   ```
   [~DeviceD] bgp 100
   ```
   ```
   [*DeviceD-bgp] router-id 2.2.2.2
   ```
   ```
   [*DeviceD-bgp] peer 2001:db8:2001::1 as-number 100
   ```
   ```
   [*DeviceD-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceD-bgp-af-ipv6] peer 2001:db8:2001::1 enable
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
   
   After the configuration is complete, run the **display bgp ipv6 peer** command to view status of BGP4+ peer relationships. The command output shows that the IBGP peer relationship has been established between DeviceC and DeviceD. Use the display on DeviceD as an example.
   
   ```
   [~DeviceD] display bgp ipv6 peer
   ```
   ```
    BGP local router ID : 2.2.2.2
    Local AS number : 100
    Total number of peers : 1                 Peers in established state : 1
   
     Peer            V          AS  MsgRcvd  MsgSent  OutQ  Up/Down       State PrefRcv
   
     2001:db8:2001::1         4         100       64       59     0 00:52:15 Established       0
   
   ```
4. Configure BGP4+ on DeviceC and import direct routes to BGP4+. Then view the routing tables of Devices C and D. 
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv6] import-route direct
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
   
   # Display the BGP4+ routing table of DeviceC.
   
   ```
   [~DeviceC] display bgp ipv6 routing-table
   ```
   ```
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 12
    *>  Network  : ::1                                      PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2000::                          PrefixLen : 64
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2000::1                         PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2000::2                         PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2001::                          PrefixLen : 64
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2001::1                         PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : FE80::                                   PrefixLen : 10
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : FE80::2E0:39FF:FE18:8300                 PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : FE80::2E0:91FF:FE4F:8100                 PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : FE80::2E0:9BFF:FE7E:7800                 PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
   
   ```
   
   # Display the BGP4+ routing table of DeviceD.
   
   ```
   [~DeviceD] display bgp ipv6 routing-table
   ```
   ```
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 2
    *>i Network  : 2001:db8:2000::                          PrefixLen : 64
        NextHop  : 2001:db8:2001::1                         LocPrf    : 100
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
      i Network  : 2001:db8:2001::                          PrefixLen : 64
        NextHop  : 2001:db8:2001::1                         LocPrf    : 100
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
   
   ```
   
   You can see that DeviceD has not learned the two IPv6 NDP Vlink direct routes 2001:db8:2000::3/128 and 2001:db8:2000::4/128.
5. Enable the function of IPv6 NDP Vlink direct route advertisement on DeviceC and configure the route-policy **policy1** to filter out the routes to the network segment of the VLAN and the IPv6 NDP Vlink direct route from DeviceA, 2001:db8:2000::3/128.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ip ipv6-prefix prefix1 index 10 permit 2001:db8:2000::4 128   
   ```
   ```
   [*DeviceC] route-policy policy1 permit node 10
   ```
   ```
   [*DeviceC-route-policy] if-match ipv6 address prefix-list prefix1
   ```
   ```
   [*DeviceC-route-policy] quit
   ```
   ```
   [*DeviceC] ipv6 nd vlink-direct-route advertise route-policy policy1
   ```
   ```
   [*DeviceC] commit
   ```
   
   # Display the BGP4+ routing table of DeviceC.
   
   ```
   [~DeviceC] display bgp ipv6 routing-table
   ```
   ```
    BGP Local router ID is 1.1.1.1
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 12
    *>  Network  : ::1                                      PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2000::                          PrefixLen : 64
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2000::1                         PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2000::2                         PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2000::3                         PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2000::4                         PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2001::                          PrefixLen : 64
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : 2001:db8:2001::1                         PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : FE80::                                   PrefixLen : 10
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : FE80::2E0:39FF:FE18:8300                 PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : FE80::2E0:91FF:FE4F:8100                 PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>  Network  : FE80::2E0:9BFF:FE7E:7800                 PrefixLen : 128
        NextHop  : ::                                       LocPrf    :
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
   
   ```
   
   # Display the BGP4+ routing table of DeviceD.
   
   ```
   [~DeviceD] display bgp ipv6 routing-table
   ```
   ```
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 3
    *>i Network  : 2001:db8:2000::                          PrefixLen : 64
        NextHop  : 2001:db8:2001::1                         LocPrf    : 100
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
    *>i Network  : 2001:db8:2000::4                         PrefixLen : 128
        NextHop  : 2001:db8:2001::1                         LocPrf    : 100
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
      i Network  : 2001:db8:2001::                          PrefixLen : 64
        NextHop  : 2001:db8:2001::1                         LocPrf    : 100
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
   
   ```
   
   You can see that DeviceD has learned the IPv6 NDP Vlink direct route 2001:db8:2000::4/128, whereas the route 2001:db8:2000::3/128 has been filtered out.
6. Use the route-policy **policy2** to filter out the network segment route 2001:db8:2000::/64 on DeviceC when BGP4+ routes are advertised.
   
   
   
   # Configure DeviceC.
   
   ```
   [~DeviceC] ip ipv6-prefix prefix2 index 10 deny 2001:db8:2000:: 64
   ```
   ```
   [*DeviceC] ip ipv6-prefix prefix2 index 20 permit :: 0 less-equal 128
   ```
   ```
   [*DeviceC] route-policy policy2 permit node 10
   ```
   ```
   [*DeviceC-route-policy] if-match ipv6 address prefix-list prefix2
   ```
   ```
   [*DeviceC-route-policy] quit
   ```
   ```
   [*DeviceC] bgp 100
   ```
   ```
   [*DeviceC-bgp] ipv6-family unicast
   ```
   ```
   [*DeviceC-bgp-af-ipv6] peer 2001:db8:2001::2 route-policy policy2 export
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
   ```
   [~DeviceC] quit
   ```
   ```
   <DeviceC> refresh bgp all export
   ```
   
   # Display the BGP4+ routing table of DeviceD.
   
   ```
   [~DeviceD] display bgp ipv6 routing-table
   ```
   ```
    BGP Local router ID is 2.2.2.2
    Status codes: * - valid, > - best, d - damped, x - best external, a - add path,
                  h - history,  i - internal, s - suppressed, S - Stale
                  Origin : i - IGP, e - EGP, ? - incomplete
    RPKI validation codes: V - valid, I - invalid, N - not-found
   
    Total Number of Routes: 2
    *>i Network  : 2001:db8:2000::4                         PrefixLen : 128
        NextHop  : 2001:db8:2001::1                         LocPrf    : 100
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
      i Network  : 2001:db8:2001::                          PrefixLen : 64
        NextHop  : 2001:db8:2001::1                         LocPrf    : 100
        MED      : 0                                        PrefVal   : 0
        Label    :
        Path/Ogn : ?
   
   ```
   
   You can see that the route 2001:db8:2000::/64 does not exist in the BGP4+ routing table of DeviceD. As a result, DeviceD can communicate with DeviceB, but cannot communicate with DeviceA.

#### Configuration Files

* SwitchA configuration file
  
  ```
  #
  sysname SwitchA
  #
  vlan batch 10
  #
  interface Vlanif10
   ipv6 enable
   ipv6 address 2001:db8:2000::2/64
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
  #
  interface GigabitEthernet0/2/0
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
  #
  interface GigabitEthernet0/3/0
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
  #
  return
  ```
* DeviceA configuration file
  
  ```
  #
  sysname DeviceA
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2000::3/64
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
   ipv6 address 2001:db8:2000::4/64
  #
  return
  ```
* DeviceC configuration file
  
  ```
  #
  sysname DeviceC
  #
  ip ipv6-prefix prefix1 index 10 permit 2001:db8:2000::4 128
  ip ipv6-prefix prefix2 index 10 deny 2001:db8:2000:: 64
  ip ipv6-prefix prefix2 index 20 permit :: 0 less-equal 128
  #
  route-policy policy1 permit node 10
   if-match ip-prefix prefix1
   if-match ipv6 address prefix-list prefix1
  #
  route-policy policy2 permit node 10
   if-match ipv6 address prefix-list prefix2
  #
  ipv6 nd vlink-direct-route advertise route-policy policy1
  #
  vlan batch 10
  #
  interface Vlanif10
   ipv6 enable
   ipv6 address 2001:db8:2000::1/64
  #
  interface GigabitEthernet0/1/0
   portswitch
   undo shutdown
   port link-type access
   port default vlan 10
  #
  interface GigabitEthernet0/2/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2001::1/64
  #
  bgp 100
   router-id 1.1.1.1
   peer 2001:db8:2001::2 as-number 100
   #
   ipv4-family unicast
    undo synchronization 
   #
   ipv6-family unicast
    undo synchronization 
    import-route direct
    peer 2001:db8:2001::2 enable
    peer 2001:db8:2001::2 route-policy policy2 export
  #
  return
  ```
* DeviceD configuration file
  
  ```
  #
  sysname DeviceD
  #
  interface GigabitEthernet0/1/0
   undo shutdown
   ipv6 enable
   ipv6 address 2001:db8:2001::2/64
  #
  bgp 100
   router-id 2.2.2.2
   peer 2001:db8:2001::1 as-number 100
   #
   ipv4-family unicast
    undo synchronization 
   #
   ipv6-family unicast
    undo synchronization 
    peer 2001:db8:2001::1 enable
  #
  return
  ```