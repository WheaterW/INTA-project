display ipv6 routing-table topology
===================================

display ipv6 routing-table topology

Function
--------



The **display ipv6 routing-table** command displays information about an IPv6 routing table.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display ipv6 routing-table** *ipv6-address1* [ *prefix-length1* ] *ipv6-address2* *prefix-length2* [ **verbose** ]

**display ipv6 routing-table** [ **table-name** **msr** ] *ipv6-address1* [ *prefix-length1* ] *ipv6-address2* *prefix-length2* [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address1* | Specifies the IPv6 address. ipv6-address1 and ipv6-address2 determine an address range. Only the routes in the address range are displayed. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length1* | Specifies the length of an IPv6 prefix. | The value is an integer ranging from 0 to 128. |
| *ipv6-address2* | Specifies the IPv6 address. ipv6-address1 and ipv6-address2 determine an address range. Only the routes in the address range are displayed. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *prefix-length2* | Specifies the length of an IPv6 prefix. | The value is an integer ranging from 0 to 128. |
| **verbose** | Displays detailed information about the active and inactive routes that match the filtering rule. If verbose is not specified, only the summary of the active routes that match the filtering rule is displayed. | - |
| **msr** | Indicates the multicast static routing table. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The command output includes the destination address, prefix length, protocol type, priority, cost, next hop, outbound interface, tunnel ID, label value carried by the route, time when the route was generated, and route status.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the brief information about IPv6 static routes.
```
<HUAWEI> display ipv6 routing-table protocol static
Route Flags: R - relay, D - download to fib, B - black hole route
------------------------------------------------------------------------------
_public_ Routing Table : Static
Summary Count : 1

Static routing table status : <Active>
Summary Count : 1

Destination  : 2001:db8:1::1                           PrefixLength : 128
NextHop      : ::                                      Preference   : 1
Cost         : 0                                       Protocol     : Static
RelayNextHop : ::                                      TunnelID     : 0x0
Interface    : NULL0                                   Flags        : DB

Static routing table status : <Inactive>
Summary Count : 0

```

**Table 1** Description of the **display ipv6 routing-table topology** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flags.   * R: indicates that the route is a recursive route. * D: indicates that the route is delivered to the FIB table. |
| Routing Table | Routing table. |
| Static routing table status | The state of static routing table. |
| Summary Count | Number of summary routes. |
| Destination | Address of the destination network or host. |
| PrefixLength | Length of the address prefix. |
| NextHop | Next hop. |
| Preference | Protocol priority. |
| Cost | Route cost. |
| Protocol | Protocol of imported routes. |
| RelayNextHop | Recursive next hop. |
| TunnelID | Tunnel ID.  The value 0x0 indicates that no tunnel is used or no tunnel has been set up. |
| Interface | Outbound interface through which the next hop is reachable. |
| Flags | Route flags. |