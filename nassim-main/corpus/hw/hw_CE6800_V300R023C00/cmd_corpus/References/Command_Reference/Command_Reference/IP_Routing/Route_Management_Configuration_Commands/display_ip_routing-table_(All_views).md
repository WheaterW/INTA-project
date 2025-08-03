display ip routing-table (All views)
====================================

display ip routing-table (All views)

Function
--------



The **display ip routing-table** command displays the summary of an IPv4 routing table.




Format
------

**display ip routing-table** [ **table-name** **msr** ] *ip-address* [ [ *mask* ] | [ *mask-length* ] ] [ **longer-match** ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **table-name** | Specifies a table of a producer. | - |
| **msr** | Indicates a multicast static routing table. | - |
| *ip-address* | Displays information about a route to a specified IP destination address. | The value is in dotted decimal notation. |
| *mask* | Specifies the mask of a destination address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies a mask length. The 1s in each 32-bit mask must be consecutive. Therefore, a mask in dotted decimal notation can be presented by a mask length. | The value is an integer ranging from 0 to 32. |
| **longer-match** | Displays the routes that match the specified network or mask only. | - |
| **verbose** | Displays detailed information about active and inactive routes. | If the parameter is not specified, only brief information about active routes is displayed. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

In the command output, each line indicates a route. The information includes the destination address, mask length, protocol, priority, weight, next hop, and outbound interface.If verbose is not specified in the command output, each line indicates a route. The information includes the destination address, mask length, protocol, priority, route cost, route tag, next hop, and outbound interface. Only the currently preferred route is displayed.If longer-match is configured, all the routes that match the destination address and mask are displayed according to the shortest matching rule.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the routes with the destination address 3.3.3.3/32.
```
<HUAWEI> display ip routing-table 3.3.3.3 verbose
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : _public_
Summary Count : 1

Destination: 3.3.3.3/32
     Protocol: Direct          Process ID: 0
   Preference: 0                     Cost: 0
      NextHop: 127.0.0.1        Neighbour: 0.0.0.0
        State: Active Adv             Age: 11d00h51m05s
          Tag: 0                 Priority: high
        Label: NULL               QoSInfo: 0x0
   IndirectID: 0x0
 RelayNextHop: 0.0.0.0          Interface: InLoopBack0
     TunnelID: 0x0                  Flags:  D
   RouteColor: 0

```

# Display detailed information about the route with destination IP address of 192.168.1.1/32 when BGP load balancing is configured.
```
<HUAWEI> display ip routing-table 192.168.1.1 verbose
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : Public
Summary Count : 1

Destination: 192.168.1.1/32
     Protocol: EBGP            Process ID: 0
   Preference: 255                   Cost: 80
     NextHop: 10.1.1.2       Neighbour: 10.1.1.2
        State: Active Adv             Age: 00h05m41s
          Tag: 0                 Priority: low
        Label: NULL               QoSInfo: 0x0
   IndirectID: 0x2
 RelayNextHop: 0.0.0.0          Interface: 100GE1/0/1
     TunnelID: 0x0                  Flags:  D
   RouteColor: 0
   BkNextHop: 10.2.1.2     BkInterface: 100GE1/0/2
      BkLabel: NULL           SecTunnelID: 0x0
 BkPETunnelID: 0x0        BkPESecTunnelID: 0x0
 BkIndirectID: 0x1

```

# Specify the IP address 10.0.0.0 in the IP routing table. Display the summary of the route that matches the natural mask range.
```
<HUAWEI> display ip routing-table 10.0.0.0
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table: _public_
Summary count: 1

Destination/Mask    Proto  Pre  Cost  Flags  Nexthop  Interface

   10.0.0.0/16      Static  60    0     D    2.1.1.1  LoopBack1

```

# Display the routes with the destination address in the range of 1.0.0.0/8 to 4.0.0.0/24.
```
<HUAWEI> display ip routing-table 1.0.0.0 8 4.0.0.0 24
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table: _public_

Destination/Mask  Proto  Pre  Cost  Flags  NextHop  Interface

   1.0.0.0/8     Static  60    0     D    10.0.0.1  100GE1/0/1
   1.1.1.0/24    Static  60    0     D    2.1.1.1   100GE1/0/1
   1.2.0.0/16    Static  60    0     D    10.0.0.1  100GE1/0/1
   2.1.1.0/24    Static  40    0     D    10.0.0.1  100GE1/0/1
   3.1.1.0/24    Static  60    0     D    4.1.1.1   100GE1/0/1

```

**Table 1** Description of the **display ip routing-table (All views)** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flags.   * R: indicates that the route is a recursive route. * D: indicates that the route is delivered to the FIB table. |
| Routing Table | Routing table. |
| Summary Count | Number of summary routes. |
| Process ID | Process ID of the routing protocol. |
| Destination/Mask | Address and mask length of the destination network or host. |
| Proto | Protocol through which routes are learned. |
| Pre | EXP value. |
| Cost | Route cost. |
| Flags | Route flag in the heading of the routing table. |
| Interface | Indicates the egress where the next hop can be reachable. |
| NextHop | IPv4 address of the adjacent next hop through which the packet reaches the destination. |
| Destination | Address of the destination network or host. |
| Protocol | Route Protocol. |
| Preference | Indicates the preference of the route. |
| State | Status of routes. The status of routes is as follows:   * Active: indicates routes in the Active state. * Invalid: indicates invalid routes. * Inactive: indicates routes in the Inactive state. * NoAdv: indicates routes that cannot be advertised. * Adv: indicates routes that can be advertised. * Del: indicates routes to be deleted. * GotQ: indicates routes that are relayed successfully. * WaitQ: indicates routes that are not relayed successfully yet. * Stale: indicates routes with the Stale flag. The routes are used in GR. |
| Age | Indicates the lifetime of the route. |
| Tag | Indicates the administrative tag for routes. |
| Priority | EXP value. |
| Label | Allocated MPLS label. |
| QoSInfo | Indicates QoS information. |
| IndirectID | Keyword of the indirect next hop, which is generated by the system. If route recursion is not performed, the value is 0x0. |
| RelayNextHop | Indicates the iterated next hop address. |
| TunnelID | Tunnel ID. The value 0x0 indicates that no tunnel is used or no tunnel has been set up. |
| BkLabel | Backup label. |
| SecTunnelID | Bypass tunnel. |
| BkPESecTunnelID | Backup tunnel on the backup PE. |
| BkPETunnelID | backup PE Tunnel ID. |
| BkInterface | Backup outbound interface. |
| BkNextHop | Backup next hop. |
| BkIndirectID | Backup IID value. |
| Neighbour | Neighbour. |
| RouteColor | Color value of the forwarding plane. The value is related to the network slice configuration function. The related command is color network-slice. |