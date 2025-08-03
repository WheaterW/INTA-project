display ipv6 routing-table vpn-instance (All views)
===================================================

display ipv6 routing-table vpn-instance (All views)

Function
--------



The **display ipv6 routing-table vpn-instance** command displays the routing table of an IPv6 address family-enabled VPN instance.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 routing-table vpn-instance** *vpn-instance-name* *ipv6-address* [ *prefix-length* ] *ipv6-address* *prefix-length* [ **verbose** ]

**display ipv6 routing-table vpn-instance** *vpn-instance-name* [ **table-name** **msr** ] *ipv6-address* [ *prefix-length* ] *ipv6-address* *prefix-length* [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies the name of an IPv6 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| *ipv6-address* | Specifies the IPv6 address prefix. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the length of the IPv6 address prefix. | The value is an integer ranging from 0 to 128. |
| **verbose** | Displays detailed information about active and inactive routes in the routing table of the IPv6 address family-enabled VPN instance. | - |
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

To check the routing table of the IPv6 address family-enabled VPN instance, run the display ipv6 routing-table vpn-instance command. The command output includes the destination address, prefix length, protocol type, priority, cost, next hop, and outbound interface.a recursive route is counted as one route no matter how many outbound interfaces and next hops the route finds.This command without verbose specified displays preferred routes only.

**Precautions**

If the specified ipv6-prefix ipv6-prefix-name does not exist, the command displays all preferred routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the routes of the IPv6 address family-enabled VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] display ipv6 routing-table vpn-instance vrf1 2001:db8:1::1 verbose
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : vrf1
Summary Count : 1

Destination  : 2001:db8::                              PrefixLength : 64
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

**Table 1** Description of the **display ipv6 routing-table vpn-instance (All views)** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flags.   * R: indicates that the route is a recursive route. * D: indicates that the route is delivered to the FIB table. |
| Routing Table | Routing Table. |
| Summary Count | Number of summary routes. |
| Destination | Address of the destination network or host. |
| PrefixLength | Length of the prefix. |
| NextHop | IPv6 address of the adjacent next hop through which the packet reaches the destination. |
| Preference | Priority of the route. |
| Neighbour | Neighbour. |
| ProcessID | Process ID of the routing protocol. |
| Label | Label. |
| Protocol | Routing protocol. |
| State | Status of routes. |
| Cost | Route cost. |
| Entry ID | Keyword of the retrieval index of routes in the routing table. |
| EntryFlags | Information about route flags. |
| Reference Cnt | Number of times that the route is referenced. |
| Tag | Administrative tag for routes. |
| Priority | Priority. |
| Age | Lifetime of the route. |
| IndirectID | Indicates the keyword of indirect next hop. |
| Instance | Instance. |
| RelayNextHop | Indicates the iterated next hop address. |
| TunnelID | Tunnel ID.  The value 0x0 indicates that no tunnel is used or no tunnel has been set up. |
| Interface | Outbound interface through which the next hop is reachable. |
| Flags | Route flags. |