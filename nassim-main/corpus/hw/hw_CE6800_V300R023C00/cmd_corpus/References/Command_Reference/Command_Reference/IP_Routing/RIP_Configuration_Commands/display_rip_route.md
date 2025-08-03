display rip route
=================

display rip route

Function
--------



The **display rip route** command displays information about all the activated and deactivated RIP routes that are learned from other devices and the values of the timers associated with each RIP route.

The **display ripng route** command displays all the RIPng routes that are learned from other devices and the values of different timers related to each route.




Format
------

**display rip** *process-id* **route** [ **destination-address** *destination-ipv4-address* [ *mask-length* ] ] [ [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ **neighbor-address** *neighbor-ipv4-address* ] ]

**display ripng** *process-id* **route** [ **destination-address** *destination-ipv6-address* [ *ipv6-mask-length* ] ] [ [ **interface** { *interface-name* | *interface-type* *interface-number* } ] [ **neighbor-address** *neighbor-ipv6-address* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies the ID of a process. | The value is an integer ranging from 1 to 4294967295. |
| **destination-address** *destination-ipv4-address* | Displays routes to a specific destination IPv4 address. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask of a specific destination IPv4 address. | The value is an integer in the range from 0 to 32. |
| **interface** *interface-type* *interface-number* | Specifies the interface type and interface number. | - |
| **neighbor-address** *neighbor-ipv4-address* | Displays routes to a specific IPv4 neighbor. | The value is in dotted decimal notation. |
| *destination-ipv6-address* | Displays routes to a specific destination IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *ipv6-mask-length* | Specifies the mask length of a specific destination IPv6 address. | It is an integer ranging from 0 to 128. |
| *neighbor-ipv6-address* | Displays routes to a specific IPv6 neighbor. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check information about all the activated and deactivated RIP routes that are learned from other devices and the values of the timers associated with each RIP route, run the display rip route command. You can specify different parameters to view information about the specified routes.By viewing routing information, you can learn key information carried in routes, which helps debug and detect protocols. When a route becomes inactive, you can check the Aging, Suppressed, or Garbage-collect field to learn the route status and the time during which the route remains in a specific state.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about all the routes in RIP process 1.
```
<HUAWEI> display rip 1 route
Route Flags: R - RIP
A - Aging, S - Suppressed, G - Garbage-collect
---------------------------------------------------------------------------------------
Peer 1.1.1.1 on 100GE1/0/1
Destination/Mask          Nexthop         Cost       Tag       Flags      Sec
10.1.23.0/24              1.1.1.1          1          0          RA        9
10.1.22.0/24              1.1.1.1          1          0          RA        9
10.1.21.0/24              1.1.1.1          1          0          RA        9
10.1.20.0/24              1.1.1.1          1          0          RA        9

```

# Display all RIPng routes and the values of different timers related to each route.
```
<HUAWEI> display ripng 100 route
   Route Flags: A - Aging, S - Suppressed, G - Garbage-collect
 ----------------------------------------------------------------

 Peer FE80::200:5EFF:FE04:B602  on 100GE1/0/1
 Dest 2001:DB8:C18:1::/64,
     via FE80::200:5EFF:FE04:B602, cost  2, tag 0, A, 34 Sec
 Dest 2001:DB8:C18:2::/64,
     via FE80::200:5EFF:FE04:B602, cost  2, tag 0, A, 34 Sec
 Peer FE80::200:5EFF:FE04:B601  on 100GE1/0/7
 Dest 2001:DB8:C18:1::/64,
     via FE80::200:5EFF:FE04:B601, cost  2, tag 0, A, 13 Sec
 Dest 2001:DB8:C18:3::/64,
     via FE80::200:5EFF:FE04:B601, cost  2, tag 0, A, 13 Sec

```

**Table 1** Description of the **display rip route** command output
| Item | Description |
| --- | --- |
| Route Flags | Flags of RIPng routes.   * A - Aging: Route in the aging state. * S - Suppressed: Route in the suppressed state. * G - Garbage-collect: Route in the garbage collection state. |
| Peer | Neighbor that is connected to the interface. |
| Destination/Mask | Destination address. |
| Nexthop | Next hop of the route. |
| Cost | Cost of the route. |
| Tag | Tag of the route. |
| Flags | First character to distinguish RIP routes from TRIP routes and the second character to indicate the route state. |
| Sec | Time during which a route remains in a specific state. |
| Dest | IPv6 destination address. |
| via | IPv6 address of the next hop. |