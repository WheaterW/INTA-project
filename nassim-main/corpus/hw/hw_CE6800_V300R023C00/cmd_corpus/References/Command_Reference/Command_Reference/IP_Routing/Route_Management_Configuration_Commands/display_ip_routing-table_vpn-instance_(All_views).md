display ip routing-table vpn-instance (All views)
=================================================

display ip routing-table vpn-instance (All views)

Function
--------



The **display ip routing-table table-name** command displays information about a specified IPv4 routing table.

The **display ip routing-table vpn-instance** command displays information about the routing table of an IPv4 VPN instance.




Format
------

**display ip routing-table vpn-instance** *vpn-instance-name* *ip-address* { *mask* | *mask-length* } *ip-address* { *mask* | *mask-length* } [ **verbose** ]

**display ip routing-table table-name msr** [ **time-range** *min-age* *max-age* ]

**display ip routing-table vpn-instance** *vpn-instance-name* **protocol** { **bgp** | **direct** | **isis** | **rip** | **static** | **ospf** } { **verbose** | **inactive** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Displays information about the routing table of an IPv4 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **table-name** | Specifies the name of a routing table. | - |
| **msr** | Displays information about the multicast static routing table. | - |
| *ip-address* | Displays information about a route to a specified IP destination address. | The value is in dotted decimal notation. |
| *mask* | Specifies mask. | The mask is in dotted decimal notation. |
| *mask-length* | Specifies the length of the mask. | The value is an integer ranging from 0 to 32. |
| **verbose** | Displays detailed information about active and inactive routes. | - |
| **protocol** | Displays routes of a specified protocol. | - |
| **bgp** | Displays BGP routes. | - |
| **direct** | Displays direct routes. | - |
| **isis** | Displays IS-IS routes. | - |
| **rip** | Displays RIP routes. | - |
| **static** | Displays static routes. | - |
| **ospf** | Displays OSPF routes. | - |
| **inactive** | Displays the summary of inactive routes only. | - |
| **time-range** | Displays routes that are generated within a specified period. | - |
| *min-age* | Specifies the start generation time. | The value is a string of characters, in the format of XXdXXhXXmXXs. |
| *max-age* | Specifies the end generation time. | The value is a string of characters, in the format of XXdXXhXXmXXs. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When the verbose parameter is not specified, information about only one route is displayed in each line. The contents include the destination address, mask length, protocol, priority, route cost, route flag, next hop, and outbound interface. This command displays only the preferred routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display detailed information about the routes with the destination address 10.34.34.3 in the routing table of the IPv4 VPN instance named vpna.
```
<HUAWEI> display ip routing-table vpn-instance vpna 10.34.34.3 verbose
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : vpna
Summary Count : 1

Destination: 10.34.34.3/32
     Protocol: Direct          Process ID: 0
   Preference: 0                     Cost: 0
      NextHop: 127.0.0.1        Neighbour: 0.0.0.0
        State: Active NoAdv           Age: 18d08h24m42s
          Tag: 0                 Priority: low
        Label: NULL               QoSInfo: 0x0
   IndirectID: 0x0
 RelayNextHop: 0.0.0.0          Interface: InLoopBack0
     TunnelID: 0x0                  Flags:  D
   RouteColor: 0

```

**Table 1** Description of the **display ip routing-table vpn-instance (All views)** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flag:   * R: indicates an iterated route. * D: indicates a route that is downloaded to the FIB. * T: indicates a route whose next hop belongs to a VPN instance. * B: indicates a black-hole rout. |
| Routing Table | Routing Table. |
| Summary Count | Number of summary routes. |
| Process ID | Process ID of the routing protocol. |
| Destination | Address and mask length of the destination network or host. |
| Cost | Route cost. |
| Flags | Route flags in the header of the routing table. |
| NextHop | Next hop. |
| Interface | Outbound interface through which the next hop is reachable. |
| Protocol | Routing protocol. |
| Preference | Priority of the routing protocol. |
| State | Route status:   * Active: indicates active routes. * Invalid: indicates invalid routes. * Inactive: indicates inactive routes. * NoAdv: indicates the routes that cannot be advertised. * Adv: indicates the routes that can be advertised. * Del: indicates the routes to be deleted. * Relied: indicates the route that finds the next hop and outbound interface or the route that finds the tunnel during packet forwarding. * Stale: indicates the routes with the stale flag. The routes are used in GR. |
| Age | Time since the route was generated. |
| Tag | Tag for importing routes. |
| Priority | Priority. |
| Label | VPN label. |
| QoSInfo | QoS information. |
| IndirectID | Keyword of the indirect next hop, which is generated by the system. If route recursion is not performed, the value is 0x0. |
| RelayNextHop | Recursive next hop. |
| TunnelID | Tunnel ID. The value 0x0 indicates that no tunnel is used or no tunnel has been set up. |
| Neighbour | Neighbor. |
| RouteColor | Color value of the forwarding plane. The value is related to the network slice configuration function. The related command is color network-slice. |