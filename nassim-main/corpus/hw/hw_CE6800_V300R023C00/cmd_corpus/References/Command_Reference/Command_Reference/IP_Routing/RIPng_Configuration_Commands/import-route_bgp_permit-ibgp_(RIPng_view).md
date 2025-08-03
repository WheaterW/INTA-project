import-route bgp permit-ibgp (RIPng view)
=========================================

import-route bgp permit-ibgp (RIPng view)

Function
--------



The **import-route bgp permit-ibgp** command configures RIPng to import routes from other routing protocols or RIPng processes.

The **undo import-route bgp permit-ibgp** command prevents RIPng from importing routes from other routing protocols or RIPng processes.



By default, RIPng does not import routes from any other routing protocols or RIPng processes.


Format
------

**import-route bgp permit-ibgp** [ [ **cost** *cost* | **inherit-cost** ] | [ **route-policy** *route-policy-name* ] ] \*

**undo import-route bgp permit-ibgp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cost** *cost* | Specifies the cost for imported routes. | The value is an integer ranging from 0 to 15. The default value is 0. |
| **inherit-cost** | Retains the original cost of the imported route. | - |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy used to filter imported routes. A device imports only routes matching the policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **bgp** | Imports BGP routes. | - |
| **permit-ibgp** | Imports IBGP routes. | - |



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

# Import IBGP routes to RIPng process 1 with cost 5 using route-policy abc.
```
<HUAWEI> system-view
[~HUAWEI] route-policy abc permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] ripng 1
[*HUAWEI-ripng-1] import-route bgp permit-ibgp cost 5 route-policy abc

```