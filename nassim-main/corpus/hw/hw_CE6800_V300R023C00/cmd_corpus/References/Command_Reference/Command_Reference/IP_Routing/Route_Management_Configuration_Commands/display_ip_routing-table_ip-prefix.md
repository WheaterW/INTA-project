display ip routing-table ip-prefix
==================================

display ip routing-table ip-prefix

Function
--------



The **display ip routing-table ip-prefix** command displays information about routes with a specified IP prefix list.




Format
------

**display ip routing-table** [ **vpn-instance** *vpn-instance-name* ] **ip-prefix** *ip-prefix-name* [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Displays information about the routing table of an IPv4 address family-enabled VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **ip-prefix** *ip-prefix-name* | Displays information about routes with a specified IP prefix list. | The name is a string of 1 to 169 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **verbose** | Displays detailed information about active and inactive routes. If the parameter verbose is not specified, brief information about active routes is displayed. | - |



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


# Display the IPv4 routes that match the IP prefixes in the specified IP prefix list.
```
<HUAWEI> display ip routing-table ip-prefix aa
Route Flags: R - relay, D - download to fib, T - to vpn-instance, B - black hole route
------------------------------------------------------------------------------
Routes Matched by Prefix-list aa:
         Destinations : 1        Routes : 1        

Destination/Mask    Proto  Pre  Cost        Flags NextHop         Interface

       1.1.1.0/24   Static 22   0             D  0.0.0.0         NULL0

```

**Table 1** Description of the **display ip routing-table ip-prefix** command output
| Item | Description |
| --- | --- |
| Route Flags | Indicates the route flag:   * R: indicates a recursive route. * D: indicates that the route is downloaded to the Forwarding Information Base (FIB) table. |
| Routes | Indicates the total number of routes. |
| Destinations | Indicates the total number of destination networks or hosts. |
| Destination/Mask | Indicates the address and mask length of the destination network or host. |
| Proto | Indicates the protocol through which routes are learned. |
| Pre | Indicates the preference. |
| Cost | Indicates the route cost. |
| Flags | Indicates the route flag, that is, Route Flags in the header of the routing table. |
| NextHop | Indicates the next hop. |
| Interface | Indicates the outbound interface through which the next hop is reachable. |