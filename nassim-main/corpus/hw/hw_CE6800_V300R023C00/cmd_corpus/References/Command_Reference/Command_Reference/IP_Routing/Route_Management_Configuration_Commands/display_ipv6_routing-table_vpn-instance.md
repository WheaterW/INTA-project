display ipv6 routing-table vpn-instance
=======================================

display ipv6 routing-table vpn-instance

Function
--------



The **display ipv6 routing-table vpn-instance** command displays the routing table of an IPv6 address family-enabled VPN instance.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 routing-table vpn-instance** *vpn-instance-name* *ipv6-address* [ *prefix-length* ] [ **longer-match** ] [ **verbose** ]

**display ipv6 routing-table vpn-instance** *vpn-instance-name* [ **table-name** **msr** ] { *ipv6-address* [ *prefix-length* ] | **host-name** *host-name* } [ **longer-match** ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **table-name** | Specifies the name of a routing table. | - |
| *ipv6-address* | Specifies the destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the length of the IPv6 address prefix. | The value is an integer ranging from 0 to 128. |
| **host-name** *host-name* | Specifies the hostname. | The value is a string of 1 to 255 case-sensitive characters, spaces not supported. |
| **longer-match** | Displays only the VPN IPv6 routes that match the specified network and mask. | - |
| **verbose** | Displays detailed information about active and inactive routes. | - |
| **vpn-instance** *vpn-instance-name* | Displays information about the routing table of an IPv6 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **msr** | Indicates the multicast static routing table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check the routing table of the IPv6 address family-enabled VPN instance, run the display ipv6 routing-table vpn-instance command. The command output includes the destination address, prefix length, protocol type, priority, cost, next hop, and outbound interface.a recursive route is counted as one route no matter how many outbound interfaces and next hops the route finds.This command without verbose specified displays preferred routes only.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the routes of the IPv6 address family-enabled VPN instance.
```
<HUAWEI> display ipv6 routing-table vpn-instance vrf1 2001:db8:1::1 verbose
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : vrf1
Summary Count : 1

Destination  : 2001:db8:1::                            PrefixLength : 64
NextHop      : ::                                      Preference   : 60
Neighbour    : ::                                      ProcessID    : 0
Label        : NULL                                    Protocol     : Static
State        : Active Adv                              Cost         : 0
Entry ID     : 0                                       EntryFlags   : 0x00000000
Reference Cnt: 0                                       Tag          : 0
Priority     : low                                     Age          : 135sec
IndirectID   : 0x10000CD                               Instance     : 
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : NULL0                                   Flags        : DB

```

**Table 1** Description of the **display ipv6 routing-table vpn-instance** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flag:   * R: indicates a recursive route. * D: indicates a route that is downloaded to the FIB. * T: indicates a route whose next hop belongs to a VPN instance. * B: indicates a black-hole rout. |
| Routing Table | Routing Table. |
| Summary Count | Number of summary routes. |
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
| RelayNextHop | Recursive next hop. |
| TunnelID | Tunnel ID.  The value 0x0 indicates that no tunnel is used or no tunnel has been set up. |
| Interface | Outbound interface through which the next hop is reachable. |
| Flags | Route flags. |