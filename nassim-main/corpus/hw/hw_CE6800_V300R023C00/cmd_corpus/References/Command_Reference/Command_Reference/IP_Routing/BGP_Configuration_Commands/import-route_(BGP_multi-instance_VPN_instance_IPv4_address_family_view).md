import-route (BGP multi-instance VPN instance IPv4 address family view)
=======================================================================

import-route (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **import-route** command configures BGP to import routes from other protocols.

The **undo import-route** command cancels the configuration.



By default, BGP does not import routes from other protocols.


Format
------

**import-route** { **static** | **direct** } [ [ **med** *med-value* ] | [ **route-policy** *route-policy-name* ] ] \*

**undo import-route** { **static** | **direct** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **static** | Imports static routes. | - |
| **direct** | Configures the device to import direct routes. | - |
| **med** *med-value* | Specifies a MED value for imported routes. | The value is an integer ranging from 0 to 4294967295. |
| **route-policy** *route-policy-name* | Specifies the route-policy used to filter routes and modify route attributes when these routes are imported from other protocols. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



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


Example
-------

# Import static routes.
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
[*HUAWEI-bgp-instance-a-vpna] import-route static

```