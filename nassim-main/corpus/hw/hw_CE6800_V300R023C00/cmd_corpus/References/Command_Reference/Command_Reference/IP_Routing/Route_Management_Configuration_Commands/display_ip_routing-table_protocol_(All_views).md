display ip routing-table protocol (All views)
=============================================

display ip routing-table protocol (All views)

Function
--------



The **display ip routing-table protocol** command displays routing information about the specified routing protocol.




Format
------

**display ip routing-table** [ **vpn-instance** *vpn-instance-name* ] [ **protocol** { **bgp** | **direct** | **isis** | **ospf** | **rip** | **static** } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays information about the routing table of an IPv4 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **protocol** | Displays routes of a specified protocol. | - |
| **bgp** | Displays BGP routes. | - |
| **direct** | Displays direct routes. | - |
| **isis** | Displays IS-IS routes. | - |
| **ospf** | Displays OSPF routing information. | - |
| **rip** | Displays RIP routing information. | - |
| **static** | Displays static routes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

In the command output, each line indicates a route. The contents include the destination address, mask length, protocol, priority, route cost, route flag, next hop, and outbound interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about all direct routes.
```
<HUAWEI> display ip routing-table protocol direct
Proto: Protocol        Pre: Preference
------------------------------------------------------------------------------
_public_ Routing Table : Direct
Destinations : 6           Routes : 6
Direct Routing Table Status : < Active>
Destinations : 5           Routes : 5
Destination/Mask  Proto  Pre  Cost  Flags  Nexthop   Interface
10.1.1.1/32    DIRECT  0    0     D     127.0.0.1  100GE1/0/1
127.0.0.0/8    DIRECT  0    0     D     127.0.0.1  InLoopBack0
127.0.0.1/32   DIRECT  0    0     D     127.0.0.1  InLoopBack0
127.255.255.255/32   DIRECT  0    0     D     127.0.0.1  InLoopBack0
255.255.255.255/32   DIRECT  0    0     D     127.0.0.1  InLoopBack0
Direct Routing Table Status : < Inactive>
Destinations : 1           Routes : 1
Destination/Mask  Proto  Pre  Cost  Flags  Nexthop       Interface
192.168.0.1/32/32   DIRECT  0    0     D     127.0.0.1  100GE1/0/1

```

# Display all the direct routes of VPN instance named vpn1.
```
<HUAWEI> display ip routing-table vpn-instance vpn1 protocol direct
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
vpn1 routing table : Direct
         Destinations : 4           Routes : 4

Direct routing table status : <Active>
         Destinations : 4           Routes : 4

Destination/Mask    Proto  Pre  Cost     Flags NextHop         Interface

        1.1.1.0/24  Direct 0    0           D  1.1.1.1         100GE1/0/1
        1.1.1.1/32  Direct 0    0           D  127.0.0.1       100GE1/0/1
      1.1.1.255/32  Direct 0    0           D  127.0.0.1       100GE1/0/1
255.255.255.255/32  Direct 0    0           D  127.0.0.1       InLoopBack0
Direct routing table status : <Inactive>
         Destinations : 0           Routes : 0

```

**Table 1** Description of the **display ip routing-table protocol (All views)** command output
| Item | Description |
| --- | --- |
| \_public\_ Routing Table | Contents of the public routing table:   * direct: displays direct routes. * static: displays static routes. * bgp: displays BGP routes. * isis: displays IS-IS routes. * ospf: displays OSPF routes. * rip: displays RIP routes. * opr: displays OP-routes. |
| Direct Routing Table Status | Status of the direct routing table: inactive or active. |
| Destinations | Number of the destination networks or hosts. |
| Routes | Total number of routes. |
| Destination/Mask | Address and mask length of the destination network or host. |
| Proto | Route Protocol. |
| Pre | EXP value. |
| Cost | Route cost. |
| Flags | Route flag in the heading of the routing table. |
| Interface | Indicates the egress where the next hop can be reachable. |
| vpn1 routing table | vpn1 routing table. |
| Route Flags | Route flag:   * R: indicates that the route is a recursive route. * D: indicates that the route is delivered to the FIB. * T: indicates that the next hop is a VPN instance. * B: indicates a blackhole route. |
| NextHop | Next hop information. |