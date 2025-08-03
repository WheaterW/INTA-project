display ipv6 routing-table (All views)
======================================

display ipv6 routing-table (All views)

Function
--------



The **display ipv6 routing-table simple** command displays brief information about the IPv6 routing table.

The **display ipv6 routing-table** command displays information about an IPv6 routing table.

The **display ipv6 routing-table protocol** command displays the IPv6 routes of the specified protocol.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 routing-table protocol** { **bgp** | **direct** | **isis** | **ospfv3** | **ripng** | **static** } [ **time-range** *min-age* *max-age* ] [ **inactive** | **verbose** ]

**display ipv6 routing-table** [ **vpn-instance** *vpn-instance-name* ] [ **time-range** *min-age* *max-age* ]

**display ipv6 routing-table** [ **vpn-instance** *vpn-instance-name* ] **ipv6-prefix** *ipv6-prefix-name* [ **verbose** ]

**display ipv6 routing-table all-vpn-instance** [ **verbose** ]

**display ipv6 routing-table brief**

**display ipv6 routing-table** [ **vpn-instance** *vpn-instance-name* ] **protocol** **direct** **sub-protocol** { **vlink** | **vlink-trm** } [ **inactive** | **verbose** | **brief** ]

**display ipv6 routing-table** [ **vpn-instance** *vpn-instance-name* ] **simple**

**display ipv6 routing-table vpn-instance** *vpn-instance-name* **table-name** **msr** [ **time-range** *min-age* *max-age* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **table-name** | Specifies the name of a routing table. | - |
| **protocol** | Displays the routes of the specified protocol. | - |
| **bgp** | displays BGP IPv6 routes. | - |
| **direct** | Displays direct IPv6 routes. | - |
| **isis** | displays IS-IS IPv6 routes. | - |
| **ospfv3** | displays OSPFv3 routes. | - |
| **ripng** | displays RIPng routes. | - |
| **static** | Displays static IPv6 routes. | - |
| **time-range** | Displays routes that are generated within a specified period. | - |
| *min-age* | Specifies the start generation time. | The value is a character string in the format of XXdXXhXXmXXs. |
| *max-age* | Specifies the end generation time. | The value is a character string in the format of XXdXXhXXmXXs. |
| **inactive** | Displays the summary of inactive routes only. | - |
| **verbose** | Displays details about all active and inactive routes in the current routing table. | - |
| **ipv6-prefix** *ipv6-prefix-name* | Specifies the name of the IPv6 prefix list. | The value is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance enabled with an IPv6 address family. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **all-vpn-instance** | Specifies all VPN instances. | - |
| **brief** | Displays brief information about active routes in the current routing table. | - |
| **sub-protocol** | Displays the information about sub-protocol routes of direct routes. | - |
| **vlink** | Displays the information about Vlink direct routes. | - |
| **vlink-trm** | Displays the information about Vlink-TRM direct routes. | - |
| **msr** | Indicates the multicast static routing table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The command output includes the destination address, prefix length, protocol type, priority, cost, next hop, outbound interface, tunnel ID, label value carried by the route, time when the route was generated, and route status.This command without verbose specified displays preferred routes only.a recursive route is counted as one route no matter how many outbound interfaces and next hops the route finds.

**Precautions**

If the specified ipv6-prefix ipv6-prefix-name does not exist, the command displays all preferred routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the summary of the routing table.
```
<HUAWEI> display ipv6 routing-table
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _Public_
         Destinations : 2        Routes : 2

 Destination  : 2001:db8:1::1                   PrefixLength : 128
 NextHop      : 2001:db8:2::1                   Preference   : 0
 Cost         : 0                               Protocol     : Direct
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : NULL0                           Flags        : D

 Destination  : 2001:db8:1::2                   PrefixLength : 10
 NextHop      : ::                              Preference   : 0
 Cost         : 0                               Protocol     : Direct
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : NULL0                           Flags        : D

```

# Display the routes that match the IPv6 prefixes in the specified IPv6 prefix list in the routing table of the specified IPv6 VPN instance.
```
<HUAWEI> display ipv6 routing-table vpn-instance vrf1 ipv6-prefix 33
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : vrf1
         Destinations : 2        Routes : 2         

Destination  : 2001:db8:1::1                           PrefixLength : 128
NextHop      : 2001:db8:2::1                           Preference   : 0
Cost         : 0                                       Protocol     : Direct
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : LoopBack4                               Flags        : D

Destination  : 2001:db8:1::2                           PrefixLength : 10
NextHop      : ::                                      Preference   : 0
Cost         : 0                                       Protocol     : Direct
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : NULL0                                   Flags        : D

```

# Display the summary of the routing table of the IPv6 address family-enabled VPN instance named vpn1.
```
<HUAWEI> display ipv6 routing-table vpn-instance vrf1
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : vrf1
         Destinations : 2        Routes : 2         

Destination  : 2001:db8:1::1                           PrefixLength : 128
NextHop      : 2001:db8:2::1                           Preference   : 0
Cost         : 0                                       Protocol     : Direct
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : LoopBack4                               Flags        : D

Destination  : 2001:db8:1::2                           PrefixLength : 10
NextHop      : ::                                      Preference   : 0
Cost         : 0                                       Protocol     : Direct
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : NULL0

```

# Display the brief information about all direct IPv6 routes.
```
<HUAWEI> display ipv6 routing-table protocol direct
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : Direct
Summary Count : 1

Direct Routing Table Status : < Active >
Summary Count : 1

 Destination  : 2001:db8:1::1                   PrefixLength : 128
 NextHop      : 2001:db8:1::1                   Preference   : 0
 Cost         : 0                               Protocol     : Direct
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : NULL0                           Flags        : D

Direct routing table status :<Inactive>
Summary Count : 0

```

# Display the summary of the IPv6 routing table.
```
<HUAWEI> display ipv6 routing-table simple
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
-----------------------------------------------------------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 5        Routes : 5         
 
Destination/Mask                             Proto   Pre  Cost        Flags NextHop                                 Interface       
 
2001:db8:1::1/128                            Direct  0    0           D     2001:db8:1::1                           InLoopBack0
2001:db8:2::/64                              Direct  0    0           D     2001:db8:2::1                           LoopBack1       
2001:db8:2::1/128                            Direct  0    0           D     2001:db8:1::1                           LoopBack1       
2001:db8:4::1/64                             Static  60   0           RD    2001:db8:4::2                           LoopBack1       
2001:db8::/10                                Direct  0    0           DB    ::                                      NULL0

```

# Display brief information about active routes in the current routing table.
```
<HUAWEI> display ipv6 routing-table brief
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 2        Routes : 2        

Format :
Destination/Mask                             Protocol
Nexthop                                      Interface
------------------------------------------------------------------------------
 2001:db8:1::1/128                           Static                             
  ::                                         NULL0                             

 2001:db8:1::2/128                           Static                             
  ::                                         NULL0

```

# Display the summary of the active routes that match the prefix list named abc2.
```
<HUAWEI> display ipv6 routing-table ipv6-prefix abc2
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routes matched by prefix-list : abc2
Summary count: 1

 Destination  : 2001:db8:1::1                   PrefixLength : 128
 NextHop      : 2001:db8:2::1                   Preference   : 0
 Cost         : 0                               Protocol     : Direct
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : NULL0                           Flags        : D

```

**Table 1** Description of the **display ipv6 routing-table (All views)** command output
| Item | Description |
| --- | --- |
| Route Flags | Route distinguisher. |
| Routing Table | Routing table. |
| Destinations | Total number of destination networks or hosts. |
| Routes | Total number of routes. |
| Destination | IP addresses of the destination network or host. |
| PrefixLength | Prefix length. |
| NextHop | IPv6 address of the adjacent next hop through which the packet reaches the destination. |
| Preference | Priority. |
| Cost | Route cost. |
| Protocol | Name of the routing protocol. |
| Direct Routing Table Status | Status of the direct routing table, indicating the status of the current direct route. |
| RelayNextHop | Recursive next hop. |
| TunnelID | Tunnel ID.  The value 0x0 indicates that no tunnel is used or no tunnel has been set up. |
| Interface | Outbound interface through which the next hop is reachable. |
| Flags | Route distinguisher. |
| Summary Count | Number of summary routes. |
| Destination/Mask | Address and mask length of the destination network or host. |
| Format | Format. |