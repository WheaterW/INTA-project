import-route (RIPng view)
=========================

import-route (RIPng view)

Function
--------



The **import-route** command configures RIPng to import routes from other routing protocols or RIPng processes.

The **undo import-route** command prevents RIPng from importing routes from other routing protocols or RIPng processes.



By default, RIPng does not import routes from any other routing protocols or RIPng processes.


Format
------

**import-route** { { **static** | **direct** | **bgp** } | { { **ripng** | **ospfv3** | **isis** } [ *process-id* ] } } [ [ **cost** *cost* | **inherit-cost** ] | [ **route-policy** *route-policy-name* ] ] \*

**undo import-route** { { **direct** | **static** | **bgp** } | { { **ospfv3** | **ripng** | **isis** } [ *process-id* ] } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **static** | Imports static routes. | - |
| **direct** | Imports direct routes. | - |
| **bgp** | Imports BGP routes. | - |
| **ripng** | Imports RIPng routes. | - |
| **ospfv3** | Imports OSPFv3 routes. | - |
| **isis** | Imports IS-IS routes. | - |
| *process-id* | Specifies the ID of a ripng, ospf, or isis process.  A device can import RIPng routes from another process only when its ID is different from the local one. | The value is an integer ranging from 1 to 4294967295. The default value is 1. |
| **cost** *cost* | Specifies the cost of imported routes. | The value is an integer ranging from 0 to 15. The default value is 0. |
| **inherit-cost** | Retains the original cost of the imported route. | - |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy used to filter imported routes. A device imports only routes matching the policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

RIPng view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When RIPng and other routing protocols are deployed on a network, you can enable the traffic within a RIPng domain to reach a destination outside the RIPng domain using **import-route** command.

**Prerequisites**



A RIPng process has been created and the RIPng view has been displayed using the **ripng** command.



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
[~HUAWEI] ripng 1
[*HUAWEI-ripng-1] import-route isis 7 cost 5

```