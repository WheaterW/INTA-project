import-route (BGP-IPv4 unicast address family view)
===================================================

import-route (BGP-IPv4 unicast address family view)

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
| **ospf** | Imports OSPF routes. | - |
| **isis** | Imports IS-IS routes. | - |
| **rip** | Imports RIP routes. | - |
| *process-id* | Specifies the ID of a process for matching. | The value is an integer ranging from 1 to 4294967295. |
| **med** *med* | Specifies a MED value for imported routes. | The value is an integer ranging from 0 to 4294967295. |
| **route-policy** *route-policy-name* | Specifies the route-policy used to filter routes and modify route attributes when these routes are imported from other protocols. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

BGP can import routes using the **import-route** command or **network** command:

* The **import-route** command imports routes of a specified type into the BGP routing table, such as RIP, OSPF, IS-IS, static, or direct routes.
* The **network** command imports routes with the specified prefix and mask into the BGP routing table. Compared with the **import-route** command, the **network** command imports more specific routes.

**Prerequisites**



If you want to import both the routes of other protocols and the default route, run the **default-route imported** command first.



**Precautions**

If the **import-route ospf** command is run to import OSPF routes but the MED value is not set, the MED value of the corresponding BGP routes is the cost value of the OSPF routes plus 1.If the same route is imported between different protocols, the loop prevention attribute of the route is lost, leading to routing loop risks. To prevent this problem, you are advised to specify a route-policy when importing routes.After the **import-route** command is run, a large number of routes from other protocols may be imported. To prevent unnecessary routes from being imported, set the route-policy parameter in the **import-route** command to limit the number of imported routes.


Example
-------

# Import routes from OSPF process 1.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] import-route ospf 1

```