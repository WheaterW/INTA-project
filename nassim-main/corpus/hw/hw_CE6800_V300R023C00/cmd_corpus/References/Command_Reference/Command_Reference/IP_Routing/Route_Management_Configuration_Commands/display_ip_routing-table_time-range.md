display ip routing-table time-range
===================================

display ip routing-table time-range

Function
--------



The **display ip routing-table time-range** command displays routes that are generated within a specified period.




Format
------

**display ip routing-table vpn-instance** *vpn-instance-name* [ **time-range** *min-age* *max-age* ] **verbose**

**display ip routing-table** [ [ **vpn-instance** *vpn-instance-name* ] | [ **protocol** { **bgp** | **direct** | **isis** | **rip** | **static** | **ospf** } ] ] **time-range** *min-age* *max-age*

**display ip routing-table vpn-instance** *vpn-instance-name* **protocol** { **bgp** | **direct** | **isis** | **rip** | **static** | **ospf** } **time-range** *min-age* *max-age* [ **verbose** | **inactive** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **time-range** | Displays routes that are generated within a specified period. | - |
| *min-age* | Specifies the start generation time. | The value is a string of characters, in the format of XXdXXhXXmXXs. |
| *max-age* | Specifies the end generation time. | The value is a string of characters, in the format of XXdXXhXXmXXs. |
| **verbose** | Displays detailed information about active and inactive routes. | - |
| **vpn-instance** *vpn-instance-name* | Displays information about the routing table of an IPv4 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **protocol** | Displays routes of a specified protocol. | - |
| **bgp** | Displays BGP routes. | - |
| **direct** | Displays direct routes. | - |
| **isis** | Displays IS-IS routes. | - |
| **rip** | Displays RIP routes. | - |
| **static** | Displays static routes. | - |
| **ospf** | Displays OSPF routes. | - |
| **inactive** | Displays the summary of inactive routes only. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If neither verbose nor inactive is specified, only brief information about active routes of each routing protocol is displayed.If verbose is not specified in the command output, each line indicates a route. The contents include the destination address, mask length, protocol, priority, route cost, route tag, next hop, and outbound interface.This command without verbose displays only the currently preferred routes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display routes that are generated within a specified period.
```
<HUAWEI> display ip routing-table time-range 1d1h1m1s 2d2h2m2s
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routing Table : a
         Destinations : 3        Routes : 3         

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

        1.1.1.1/32  Static  60   0             DT  0.0.0.0         _public_
      127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0

```

**Table 1** Description of the **display ip routing-table time-range** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flag:   * R: indicates an iterated route. * D: indicates a route that is downloaded to the FIB. * T: indicates a route whose next hop belongs to a VPN instance. * B: indicates a black-hole rout. |
| Routing Table | Routing Table. |
| Destinations | Total number of destination networks or hosts. |
| Routes | Total number of routes. |
| Destination/Mask | Address and mask length of the destination network or host. |
| Proto | Routing protocol. |
| Pre | Priority. |
| Cost | Route cost. |
| Flags | Route flags in the header of the routing table. |
| NextHop | Next hop. |
| Interface | Outbound interface through which the next hop is reachable. |