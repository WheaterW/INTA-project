display ipv6 routing-table vpn-instance verbose
===============================================

display ipv6 routing-table vpn-instance verbose

Function
--------



The **display ipv6 routing-table vpn-instance verbose** command displays detailed information about active and inactive routes in the routing table of the IPv6 address family-enabled VPN instance.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 routing-table vpn-instance** *vpn-instance-name* [ **time-range** *min-age* *max-age* ] **verbose**

**display ipv6 routing-table vpn-instance** *vpn-instance-name* [ **table-name** **msr** ] [ **time-range** *min-age* *max-age* ] **verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **table-name** | Specifies the name of a routing table. | - |
| **time-range** | Displays routes that are generated within a specified period. | - |
| *min-age* | Specifies the start generation time. | The value is a string of characters, in the format of XXdXXhXXmXXs. |
| *max-age* | Specifies the end generation time. | The value is a string of characters, in the format of XXdXXhXXmXXs. |
| **verbose** | Displays detailed information about active and inactive routes. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the IPv6 VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **msr** | Indicates the multicast static routing table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display ipv6 routing-table vpn-instance verbose** command displays detailed information about active and inactive routes in the routing table of the IPv6 address family-enabled VPN instance.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the detailed information of the routing table of the IPv6 address family-enabled VPN instance named a.
```
<HUAWEI> display ipv6 routing-table vpn-instance a verbose
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : a
         Destinations : 2        Routes : 2         

Destination  : 2001:db8::                                     PrefixLength : 128
NextHop      : ::                                      Preference   : 60
Neighbour    : ::                                      ProcessID    : 0
Label        : NULL                                    Protocol     : Static
State        : Active Adv                              Cost         : 0
Entry ID     : 0                                       EntryFlags   : 0x00000000
Reference Cnt: 0                                       Tag          : 0
Priority     : low                                     Age          : 93807sec
IndirectID   : 0x10000D1                               Instance     : 
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : _public_                                Flags        : DT
RouteColor   : 0                                       QoSInfo      : 0x0

Destination  : 2001:db8:1::1                                    PrefixLength : 64
NextHop      : ::                                      Preference   : 60
Neighbour    : ::                                      ProcessID    : 0
Label        : NULL                                    Protocol     : Static
State        : Active Adv                              Cost         : 0
Entry ID     : 0                                       EntryFlags   : 0x00000000
Reference Cnt: 0                                       Tag          : 0
Priority     : low                                     Age          : 96703sec
IndirectID   : 0x10000D1                               Instance     : 
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : _public_                                Flags        : DT
RouteColor   : 0                                       QoSInfo      : 0x0

```

**Table 1** Description of the **display ipv6 routing-table vpn-instance verbose** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flag:   * R: indicates a recursive route. * D: indicates a route that is downloaded to the FIB. * T: indicates a route whose next hop belongs to a VPN instance. * B: indicates a black-hole rout. |
| Routing Table | Routing Table. |
| Destinations | Total number of destination networks or hosts. |
| Routes | Total number of routes. |
| Destination | Address of the destination network or host. |
| PrefixLength | Length of the prefix. |
| NextHop | IPv6 address of the adjacent next hop through which the packet reaches the destination. |
| Preference | Priority of the route. |
| Neighbour | IP address of the neighbor interface. |
| ProcessID | Process ID of the routing protocol. |
| Label | Label value carried by the route. |
| Protocol | Routing protocol. |
| State | Route status:   * Active: indicates active routes. * Invalid: indicates invalid routes. * Inactive: indicates inactive routes. * NoAdv: indicates the routes that cannot be advertised. * Adv: indicates the routes that can be advertised. * Del: indicates the routes to be deleted. * Relied: indicates the route that finds the next hop and outbound interface or the route that finds the tunnel during packet forwarding. * Stale: indicates the routes with the stale flag. The routes are used in GR. |
| Cost | Route cost. |
| Entry ID | Keyword of the retrieval index of routes in the routing table. |
| EntryFlags | Information about route flags. |
| Reference Cnt | Number of times that the route is referenced. |
| Tag | Tag for importing routes. |
| Priority | Priority of the route:   * critical. * high. * medium. * low. |
| Age | Time since the route was generated. |
| IndirectID | Keyword of the indirect next hop, which is generated by the system. If route recursion is not performed, the value is 0x0. |
| Instance | Instance. |
| RelayNextHop | Indicates the iterated next hop address. |
| TunnelID | Tunnel ID.  The value 0x0 indicates that no tunnel is used or no tunnel has been set up. |
| Interface | Outbound interface through which the next hop is reachable. |
| Flags | Route flags. |
| RouteColor | Route color value. |
| QosInfo | QoS information. |