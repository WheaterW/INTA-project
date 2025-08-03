import-route (BGP-VPN instance IPv4 address family view)
========================================================

import-route (BGP-VPN instance IPv4 address family view)

Function
--------



The **import-route** command configures BGP to import routes from other protocols.

The **undo import-route** command cancels the configuration.



By default, BGP does not import routes from other protocols.


Format
------

**import-route** { **ospf** | **isis** | **rip** } *process-id* [ [ **med** *med* ] | [ **route-policy** *route-policy-name* ] ] \*

**undo import-route** { **ospf** | **isis** | **rip** } *process-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ospf** *process-id* | Specifies the ID of an OSPF process. | The value ranges from 1 to 4294967295. |
| **isis** *process-id* | Specifies the ID of an IS-IS process. | The value is an integer ranging from 1 to 4294967295. |
| **rip** | Imports RIP routes. | - |
| **med** *med* | Specifies a MED value for imported routes. | The value is an integer ranging from 0 to 4294967295. |
| **route-policy** *route-policy-name* | Specifies the route-policy used to filter routes and modify route attributes when these routes are imported from other protocols. | The value is a string of 1 to 200 case-sensitive characters. It cannot contain spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN instance IPv4 address family view


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

If load balancing routes are imported, only the first route in the IP routing table can be imported.If the same route is imported between different protocols, the loop prevention attribute of the route is lost, which may lead to routing loops. To prevent this problem, you are advised to specify a route-policy when importing routes.After the **import-route** command is run, a large number of routes from other protocols may be imported. To prevent unnecessary routes from being imported, set the route-policy parameter in the **import-route** command to limit the number of imported routes.If the **import-route ospf** command is run to import OSPF routes but the MED value is not set, the MED value of the corresponding BGP routes is the cost value of the OSPF routes plus 1.


Example
-------

# Import routes from OSPF process 1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] import-route ospf 1

```