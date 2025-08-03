display ip routing-table protocol
=================================

display ip routing-table protocol

Function
--------



The **display ip routing-table protocol** command displays routing information about the specified routing protocol.




Format
------

**display ip routing-table protocol** { **bgp** | **direct** | **isis** | **rip** | **static** | **ospf** } [ **time-range** *min-age* *max-age* ] { **inactive** | **verbose** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bgp** | Displays BGP routes. | - |
| **direct** | Displays direct routes. | - |
| **isis** | Displays IS-IS routes. | - |
| **rip** | Displays RIP routing information. | - |
| **static** | Displays static routes. | - |
| **ospf** | Displays OSPF routing information. | - |
| **time-range** | Displays routes that are generated within a specified period. | - |
| *min-age* | Specifies the start generation time. | The value is a character string in the format of XXdXXhXXmXXs. |
| *max-age* | Specifies the end generation time. | The value is a character string in the format of XXdXXhXXmXXs. |
| **inactive** | Displays brief information about inactive routes. If this parameter is not specified, brief information about all the active and inactive routes is displayed. | - |
| **verbose** | Displays detailed information about the active and inactive routes that match the filtering rule. If this parameter is not specified, only the brief information about the active routes that match the filtering rule is displayed. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

If neither verbose nor inactive is specified, only the summary of active routes of each routing protocol is displayed. To learn the detailed information about the active and inactive routes, specify verbose.


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
Destinations : 5           Routes : 5
Direct Routing Table Status : < Active>
Destinations : 5           Routes : 5
Destination/Mask  Proto  Pre  Cost  Flags  Nexthop  Interface
10.1.1.1/32    DIRECT  0    0     D     127.0.0.1  LoopBack1
127.0.0.0/8    DIRECT  0    0     D     127.0.0.1  InLoopBack0
127.0.0.1/32   DIRECT  0    0     D     127.0.0.1  InLoopBack0
127.255.255.255/32   DIRECT  0    0     D     127.0.0.1  InLoopBack0
255.255.255.255/32   DIRECT  0    0     D     127.0.0.1  InLoopBack0
Direct routing table status : <Inactive>
         Destinations : 0        Routes : 0

```

**Table 1** Description of the **display ip routing-table protocol** command output
| Item | Description |
| --- | --- |
| Protocol | Routing protocol type. |
| Preference | Priority of the routing protocol. |
| \_public\_ Routing Table | Contents of the public routing table:   * direct: displays direct routes. * static: displays static routes. * bgp: displays BGP routes. * isis: displays IS-IS routes. * ospf: displays OSPF routes. * rip: displays RIP routes. * opr: displays OP-routes. |
| Direct Routing Table Status | Status of the direct routing table: inactive or active. |
| Destinations | Total number of destination addresses. |
| Routes | Total number of routes in the routing table. |
| Destination/Mask | Destination Address/Mask Length. |
| Proto | Routing protocol type. |
| Pre | Priority of the routing protocol. |
| Cost | Cost of the route. |
| Flags | Route flag in the heading of the routing table. |
| Nexthop | Next hop. |
| Interface | Outbound interface name. |
| Active | Active routes in the routing table. |
| Inactive | Inactive routes in the routing table. |