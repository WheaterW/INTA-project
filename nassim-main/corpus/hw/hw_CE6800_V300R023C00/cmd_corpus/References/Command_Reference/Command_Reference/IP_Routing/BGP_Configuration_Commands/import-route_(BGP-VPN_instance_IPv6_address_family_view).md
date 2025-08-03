import-route (BGP-VPN instance IPv6 address family view)
========================================================

import-route (BGP-VPN instance IPv6 address family view)

Function
--------



The **import-route** command configures BGP to import routes from other protocols.

The **undo import-route** command cancels the configuration.



By default, BGP does not import routes from other protocols.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**import-route** { **direct** | **static** | { **ospfv3** | **isis** | **ripng** } *process-id* } [ [ **med** *med* ] | [ **route-policy** *route-policy-name* ] ] \*

**undo import-route** { **direct** | **static** | { **ospfv3** | **isis** | **ripng** } *process-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **direct** | Configures the device to import direct routes. | - |
| **static** | Imports static routes. | - |
| **ospfv3** | Configures BGP to import OSPFv3 routes. | - |
| **isis** | Imports IS-IS routes. | - |
| **ripng** | Configures BGP to import RIPng routes. | - |
| *process-id* | Specifies the ID of a process for matching. | The value ranges from 1 to 4294967295. |
| **med** *med* | Specifies a MED value for imported routes. | The value is an integer ranging from 0 to 4294967295. |
| **route-policy** *route-policy-name* | Specifies the route-policy used to filter routes and modify route attributes when these routes are imported from other protocols. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP can import routes using the import-route or **network** command.

* The **import-route** command imports routes from a specified protocol, such as RIP routes, OSPF routes, IS-IS routes, static routes, or direct routes, into the BGP routing table.
* The **network** command imports a route with the specified prefix and mask into the BGP routing table, which is more accurate than the **import-route** command.Description:When the **import-route static** command is used to import static routes, only active routes can be imported.

**Prerequisites**



If you want to import both the routes of other protocols and the default route, run the **default-route imported** command first.




Example
-------

# Import static routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] import-route static

```