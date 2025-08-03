import-route bgp permit-ibgp (RIP view)
=======================================

import-route bgp permit-ibgp (RIP view)

Function
--------



The **import-route bgp permit-ibgp** command imports other routing protocol routes to RIP.

The **undo import-route bgp permit-ibgp** command deletes other routing protocol routes from RIP.



By default, RIP does not import routes from any other processes or routing protocols.


Format
------

**import-route bgp permit-ibgp** [ [ **cost** *cost* ] | [ **route-policy** *route-policy-name* ] ] \*

**import-route bgp permit-ibgp** { **cost** **transparent** **route-policy** *route-policy-name* | **route-policy** *route-policy-name* **cost** **transparent** | **cost** **transparent** }

**undo import-route bgp permit-ibgp**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **cost** *cost* | Specifies the cost for imported routes. | The value is an integer ranging from 0 to 15. The default value is 0. |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy used to filter imported routes. A device imports only routes matching the policy. | The value is a string of 1 to 200 case-sensitive characters. It cannot contain spaces. If spaces are used, the string must start and end with double quotation marks ("). |
| **bgp** | Imports BGP routes. | - |
| **permit-ibgp** | Imports IBGP routes to the public network instance.  If this parameter is not specified, RIP can import only EBGP routes, not IBGP routes. | - |
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

When RIP and other routing protocols are deployed on a network, you can import routes to other routing domains to RIP using the **import-route** command so that the traffic within a RIP domain can reach a destination outside the RIP domain.If the **import-route bgp** command is run in the public network instance view, RIP can import only EBGP routes by default. To enable RIP to import both EBGP and IBGP routes, run the **import-route bgp permit-ibgp** command.However, if the **import-route bgp** command is run in a VPN instance view, both EBGP and IBGP routes can be imported by default. Therefore, the **import-route bgp permit-ibgp** command does not need to be run in the VPN instance view.

**Prerequisites**



A RIP process has been created and the RIP view has been displayed using the **rip** command.



**Configuration Impact**



Importing routes of another routing protocol may lead to routing loops. Therefore, exercise caution when running the command.



**Precautions**

* Default routes cannot be imported using the **import-route** command.
* If route-policy route-policy-name is specified in this command, the following items can be matched: the outbound interface, IP route next-hop address ACL, IP route next-hop address prefix list, route cost, route type, route tag, routing protocol type, and route preference. If the referenced policy contains unsupported attribute matching or behavior setting, unexpected results may occur.


Example
-------

# Import IBGP routes to RIP process 1 with cost 5 using route-policy abc.
```
<HUAWEI> system-view
[~HUAWEI] route-policy abc permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] rip 1
[*HUAWEI-rip-1] import-route bgp permit-ibgp cost 5 route-policy abc

```