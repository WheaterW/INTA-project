display ip routing-table
========================

display ip routing-table

Function
--------



The **display ip routing-table** command displays the summary of an IPv4 routing table.




Format
------

**display ip routing-table** [ **table-name** **msr** ] *prefix* { *mask* | *masklength* } *prefix* { *mask* | *masklength* } [ **verbose** ]

**display mrt routing-table** [ **vpn-instance** *vpn-instance-name* ] [ *prefix* [ [ *mask* ] | [ *masklength* ] ] [ **longer-match** ] ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **table-name** | Specifies a table of a producer. | - |
| **msr** | Indicates a multicast static routing table. (When topology topology-name is specified, the multicast static routing table cannot be displayed.). | - |
| *prefix* | Displays information about a route to a specified IP destination address. | The value is in dotted decimal notation. |
| *mask* | Specifies the mask of a destination address. | The value is in dotted decimal notation. |
| *masklength* | Specifies a mask length. The 1s in each 32-bit mask must be consecutive. Therefore, a mask in dotted decimal notation can be presented by a mask length. | The value is an integer ranging from 0 to 32. |
| **verbose** | Displays detailed information about all the routes in the routing table, including active and inactive routes. If this parameter is not specified, only brief information about active routes is displayed. | - |
| **mrt** | Indicates a MRT routing table. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **longer-match** | Displays the routes matching the specified network or mask. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If verbose is not specified, each line in the command output indicates a route. The information includes the destination address, mask length, protocol, priority, route cost, route tag, next hop, and outbound interface. Only the currently preferred route is displayed.If longer-match is configured, all the routes that match the destination address and mask are displayed according to the shortest matching rule.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the routes with the destination address in the range of 1.0.0.0/8 to 4.0.0.0/24.
```
<HUAWEI> display ip routing-table 1.0.0.0 8 4.0.0.0 24
Proto: Protocol        Pre: Preference
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
         Destinations : 5       Routes : 5 

Destination/Mask  Proto  Pre  Cost  Flags  NextHop  Interface

   1.0.0.0/8     Static  60    0     D    10.0.0.1  100GE1/0/1
   1.1.1.0/24    Static  60    0     D    2.1.1.1   100GE1/0/1
   1.2.0.0/16    Static  60    0     D    10.0.0.1  100GE1/0/1
   2.1.1.0/24    Static  40    0     D    10.0.0.1  100GE1/0/1
   3.1.1.0/24    Static  60    0     D    4.1.1.1   100GE1/0/1

```

**Table 1** Description of the **display ip routing-table** command output
| Item | Description |
| --- | --- |
| Protocol | Routing protocol. |
| Preference | Preference of the route. |
| Route Flags | Route flags.   * R: indicates that the route is a recursive route. * D: indicates that the route is delivered to the FIB table. |
| Routing Table | Routing table. |
| Destinations | Total number of destination networks or hosts. |
| Routes | Total number of routes. |
| Destination/Mask | Address and mask length of the destination network or host. |
| Proto | Protocol used to learn routes. |
| Pre | Priority. |
| Cost | Route cost. |
| Flags | Route flags in the header of the routing table. |
| NextHop | Next-hop address. |
| Interface | Outbound interface through which the next hop is reachable. |
| Destination | IP addresses of the destination network or host. |