display ipv6 routing-table
==========================

display ipv6 routing-table

Function
--------



The **display ipv6 routing-table** command displays information about an IPv6 routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 routing-table** *ipv6-address* [ *prefix-length* ] [ **longer-match** ] [ **verbose** ]

**display ipv6 routing-table** [ **table-name** **msr** ] { *ipv6-address* [ *prefix-length* ] | **host-name** *host-name* } [ **longer-match** ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **table-name** | Table to which a producer belongs. | - |
| *ipv6-address* | Specifies the IPv6 destination address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length* | Specifies the length of an IPv6 prefix. | It is an integer ranging from 0 to 128. |
| **host-name** *host-name* | Specifies the hostname. | The value is a string of 1 to 255 case-sensitive characters, spaces not supported. |
| **longer-match** | Displays the routes that match the specified network or mask only. | - |
| **verbose** | Displays details about all active and inactive routes in the current routing table. | - |
| **msr** | Indicates the multicast static routing table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The command output includes the destination address, prefix length, protocol type, priority, cost, next hop, outbound interface, tunnel ID, label value carried by the route, time when the route was generated, and route status.This command without verbose specified displays preferred routes only.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the summary of the specified route. There is one route that matches the prefix range.
```
<HUAWEI> display ipv6 routing-table 2001:db8:1::1 64
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table :_Public_
Summary Count : 1

 Destination  : 2001:db8:1::                    PrefixLength : 64
 NextHop      : 2001:db8:1::2                   Preference   : 0
 Cost         : 0                               Protocol     : Direct
 RelayNextHop : ::                              TunnelID     : 0x0
 Interface    : 100GE 1/0/1                     Flags        : D

```

**Table 1** Description of the **display ipv6 routing-table** command output
| Item | Description |
| --- | --- |
| Routing Table | Routing table. |
| Summary Count | Total number of routes. |
| Destination | Address of the destination network or host. |
| PrefixLength | Length of the prefix. |
| NextHop | IPv6 address of the next hop. |
| Preference | EXP value. |
| Cost | Route cost. |
| Protocol | Routing protocol name. |
| RelayNextHop | Recursive next hop. |
| TunnelID | Tunnel ID. The value 0x0 indicates that no tunnel is used or no tunnel has been set up. |
| Interface | Indicates the egress where the next hop can be reachable. |
| Flags | Route Distinguisher. |
| Route Flags | Route flags.   * R: indicates that the route is a recursive route. * D: indicates that the route is delivered to the FIB table. |