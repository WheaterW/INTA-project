import-route (BGP view) (Non-IGP)
=================================

import-route (BGP view) (Non-IGP)

Function
--------



The **import-route** command configures BGP to import routes from other protocols.

The **undo import-route** command cancels the configuration.



By default, BGP does not import routes from other protocols.


Format
------

**import-route** { **direct** | **static** } [ [ **med** *med* ] | [ **route-policy** *route-policy-name* ] ] \*

**undo import-route** { **direct** | **static** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **direct** | Configures the device to import direct routes. | - |
| **static** | Imports static routes. | - |
| **med** *med* | Specifies a MED value for imported routes. | The value is an integer ranging from 0 to 4294967295. |
| **route-policy** *route-policy-name* | Specifies the route-policy used to filter routes and modify route attributes when these routes are imported from other protocols. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

BGP can import routes using the import-route or **network** command.

* The **import-route** command imports routes from a specified protocol, such as RIP routes, OSPF routes, IS-IS routes, static routes, or direct routes, into the BGP routing table.
* The **network** command imports a route with the specified prefix and mask into the BGP routing table, which is more accurate than the **import-route** command.Description:When the **import-route static** command is used to import static routes, only active routes can be imported.

Example
-------

# Import direct routes.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] import-route direct

```