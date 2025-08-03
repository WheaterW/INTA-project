display ip routing-table protocol direct sub-protocol
=====================================================

display ip routing-table protocol direct sub-protocol

Function
--------



The **display ip routing-table protocol direct sub-protocol** command displays the information about sub-protocol routes of direct routes.




Format
------

**display ip routing-table** [ **vpn-instance** *vpn-instance-name* ] **protocol** **direct** **sub-protocol** { **vlink** | **vlink-trm** } [ **verbose** | **inactive** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays information about the routing table of an IPv4 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **protocol** | Displays routes of a specified protocol. | - |
| **direct** | Displays direct routes. | - |
| **sub-protocol** | Displays the information about sub-protocol routes of direct routes. | - |
| **vlink** | Displays the information about Vlink direct routes. | - |
| **vlink-trm** | Displays the information about Vlink-TRM direct routes. | - |
| **verbose** | Displays detailed information about active and inactive routes. | - |
| **inactive** | Displays the summary of inactive routes only. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



In the command output, each line indicates a route. The contents include the destination address, mask length, protocol, priority, route cost, route flag, next hop, and outbound interface.This command without verbose specified displays the preferred routes only.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display brief information about the routing table.
```
<HUAWEI> display ip routing-table protocol direct sub-protocol vlink
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
a Routing Table : Direct
         Destinations : 2        Routes : 2         

Direct routing table status : <Active>
         Destinations : 2        Routes : 2         

Destination/Mask    Proto   Pre  Cost        Flags NextHop         Interface

      127.0.0.0/8   Direct  0    0             D   127.0.0.1       InLoopBack0
255.255.255.255/32  Direct  0    0             D   127.0.0.1       InLoopBack0

Direct routing table status : <Inactive>
         Destinations : 0        Routes : 0

```

**Table 1** Description of the **display ip routing-table protocol direct sub-protocol** command output
| Item | Description |
| --- | --- |
| Route Flags | Route flags.   * R: indicates that the route is a recursive route. * D: indicates that the route is delivered to the FIB table. |
| a Routing Table | Routing table. |
| Direct routing table status | Status of the direct routing table: inactive or active. |
| Destinations | Number of the destination networks or hosts. |
| Routes | Total number of routes. |
| Destination/Mask | Address and mask length of the destination network or host. |
| Proto | Routing protocol name. |
| Pre | EXP value. |
| Cost | Route cost. |
| Flags | Route Distinguisher. |
| NextHop | IPv4 address of the adjacent next hop through which the packet reaches the destination. |
| Interface | Indicates the egress where the next hop can be reachable. |