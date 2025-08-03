import-route (RIP view)
=======================

import-route (RIP view)

Function
--------



The **import-route** command imports other routing protocol routes to RIP.

The **undo import-route** command deletes other routing protocol routes from RIP.



By default, RIP does not import routes from any other processes or routing protocols.


Format
------

**import-route** { { **static** | **direct** | **bgp** } | { { **rip** | **ospf** | **isis** } [ *process-id* ] } } [ [ **cost** *cost* ] | [ **route-policy** *route-policy-name* ] ] \*

**import-route bgp** { **cost** **transparent** **route-policy** *route-policy-name* | **route-policy** *route-policy-name* **cost** **transparent** | **cost** **transparent** }

**undo import-route** { { **direct** | **static** | **bgp** } | { { **ospf** | **rip** | **isis** } [ *process-id* ] } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **static** | Imports static routes. | - |
| **direct** | Imports direct routes. | - |
| **bgp** | Imports BGP routes. | - |
| **rip** | Imports RIP routes. | - |
| **ospf** | Imports OSPF routes. | - |
| **isis** | Imports IS-IS routes. | - |
| *process-id* | Specifies the ID of an IS-IS, OSPF, or RIP process.  A device can import RIP routes from other processes with an ID different from the local one. | The value is an integer ranging from 1 to 4294967295. The default value is 1. |
| **cost** *cost* | Specifies the cost for imported routes. | The value is an integer ranging from 0 to 15. The default value is 0. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy used to filter imported routes. A device imports only routes matching the policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **transparent** | Retains the Multi\_Exit Discriminator (MED) value of an imported BGP route as its cost. transparent takes effect only when the protocol is BGP. | - |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When RIP and other routing protocols are deployed on a network, you can enable the traffic within a RIP domain to reach a destination outside the RIP domain using the **import-route** command.

**Prerequisites**



A RIP process has been created and the RIP view has been displayed using the **rip** command.



**Configuration Impact**



Importing routes of another routing protocol may lead to routing loops. Therefore, exercise caution when running the command.



**Precautions**

* Default routes cannot be imported using the **import-route** command.
* If route-policy route-policy-name is specified in this command, the following items can be matched: the outbound interface, IP route next-hop address ACL, IP route next-hop address prefix list, route cost, route type, route tag, routing protocol type, and route preference. If the referenced policy contains unsupported attribute matching or behavior setting, unexpected results may occur.

Example
-------

# Import a route from IS-IS process 7 and set the cost of the route to 5.
```
<HUAWEI> system-view
[~HUAWEI] rip 1
[*HUAWEI-rip-1] import-route isis 7 cost 5

```