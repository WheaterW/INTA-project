import-route (BGP multi-instance VPN instance IPv4 address family view) (route)
===============================================================================

import-route (BGP multi-instance VPN instance IPv4 address family view) (route)

Function
--------



The **import-route** command configures BGP to import routes from other protocols.

The **undo import-route** command cancels the configuration.



By default, BGP does not import routes from other protocols.


Format
------

**import-route** { { **ospf** | **isis** | **rip** } *processId* } [ [ **med** *med-value* ] | [ **route-policy** *route-policy-name* ] ] \*

**undo import-route** { { **ospf** | **isis** | **rip** } *processId* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **med** *med-value* | Specifies a MED value for imported routes. | The value is an integer ranging from 0 to 4294967295. |
| **route-policy** *route-policy-name* | Specifies the route-policy used to filter routes and modify route attributes when these routes are imported from other protocols. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **ospf** | Imports OSPF routes. | - |
| **isis** | Imports IS-IS routes. | - |
| **rip** | Imports RIP routes. | - |
| *processId* | Specifies the ID of a process for matching. | The value ranges from 1 to 4294967295. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP can import routes using the import-route or **network** command.

* The **import-route** command imports routes from a specified protocol, such as RIP routes, OSPF routes, IS-IS routes, static routes, or direct routes, into the BGP routing table.
* The **network** command imports a route with the specified prefix and mask into the BGP routing table, which is more accurate than the **import-route** command.Description:When the **import-route static** command is used to import static routes, only active routes can be imported.

**Precautions**



If the **import-route ospf** command is run to import OSPF routes but the MED value is not set, the MED value of the corresponding BGP routes is the cost value of the OSPF routes plus 1.If the same route is imported between different protocols, the loop prevention attribute of the route is lost, leading to routing loop risks. To prevent this problem, you are advised to specify a route-policy when importing routes.After the **import-route** command is run, a large number of routes from other protocols may be imported. To prevent unnecessary routes from being imported, set the route-policy parameter in the **import-route** command to limit the number of imported routes.




Example
-------

# Import routes from OSPF process 1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] import-route ospf 1

```