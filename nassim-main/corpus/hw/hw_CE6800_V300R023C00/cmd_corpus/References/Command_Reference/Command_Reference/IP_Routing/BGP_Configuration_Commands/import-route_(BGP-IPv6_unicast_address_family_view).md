import-route (BGP-IPv6 unicast address family view)
===================================================

import-route (BGP-IPv6 unicast address family view)

Function
--------



The **import-route** command configures BGP to import routes from other protocols.

The **undo import-route** command cancels the configuration.



By default, BGP does not import routes from other protocols.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**import-route** { **direct** | **static** | { **ospfv3** | **isis** | **ripng** } *process-id* } [ **med** *med* | **route-policy** *route-policy-name* ] \*

**undo import-route** { **direct** | **static** | { **ospfv3** | **isis** | **ripng** } *process-id* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **direct** | Configures the device to import direct routes. | - |
| **static** | Imports static routes. | - |
| **ospfv3** | Imports OSPFv3 routes. | - |
| **isis** | Imports IS-IS routes. | - |
| **ripng** | Configures BGP to import RIPng routes. | - |
| *process-id* | Specifies the ID of a process for matching. | The value ranges from 1 to 4294967295. |
| **med** *med* | Specifies a MED value for imported routes. | The value is an integer ranging from 0 to 4294967295. |
| **route-policy** *route-policy-name* | Specifies the route-policy used to filter routes and modify route attributes when these routes are imported from other protocols. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP-IPv6 unicast address family view


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



**Precautions**

If the **import-route ospf** command is run to import OSPF routes but the MED value is not set, the MED value of the corresponding BGP routes is the cost value of the OSPF routes plus 1.If the same route is imported between different protocols, the loop prevention attribute of the route is lost, leading to routing loop risks. To prevent this problem, you are advised to specify a route-policy when importing routes.After the **import-route** command is run, a large number of routes from other protocols may be imported. To prevent unnecessary routes from being imported, set the route-policy parameter in the **import-route** command to limit the number of imported routes.


Example
-------

# Import static routes.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] import-route static

```