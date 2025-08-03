import-route (OSPFv3 view) (Non-IGP)
====================================

import-route (OSPFv3 view) (Non-IGP)

Function
--------



The **import-route** command imports external routes. Before the routes are imported, the OSPFv3 process of the route must be active.

The **undo import-route** command cancels the configuration.



By default, routes learned by other protocols are not imported.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**import-route** { **direct** | **static** | **bgp** [ **permit-ibgp** ] } [ { **cost** *cost* | **inherit-cost** } | **type** *type* | **tag** *tag* | { **route-policy** *route-policy-name* } ] \*

**undo import-route** { **direct** | **static** | **bgp** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **direct** | Imports direct routes. | - |
| **static** | Imports static routes. | - |
| **bgp** | Imports BGP routes.  For an OSPF process that is not bound to a VPN instance or is bound to a VPN instance but the vpn-instance-capability simple command is run, the parameter imports only EBGP routes. | - |
| **permit-ibgp** | Imports IBGP routes.  For an OSPF process that is not bound to a VPN instance or is bound to a VPN instance but the vpn-instance-capability simple command is run, importing IBGP routes may cause routing loops. Therefore, exercise caution when using this parameter. | - |
| **cost** *cost* | Specifies the cost of the imported route. | The value is an integer that ranges from 0 to 16777214. |
| **inherit-cost** | Indicates that the imported route inherits the original cost. | - |
| **type** *type* | Indicates the type of the imported route. | The value is 1 or 2.   * 1: Type 1 external route * 2: Type 2 external route   The default value is 2. |
| **tag** *tag* | Specifies the tag of the external LSA. | The value is an integer ranging from 0 to 4294967295. The default value is 1. |
| **route-policy** *route-policy-name* | Imports only the route that matches the specified route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

OSPFv3 view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By importing routes of other routing protocols, you can expand OSPFv3 routing information.OSPFv3 uses four types of routes, which are listed in descending order of priority:

* Intra-area routes: refer to the routes within an AS area.
* Inter-area routes: refer to the routes between different areas in an AS. Both intra-area routes and external routes are internal routes of an AS.
* Type 1 external route: When the cost of an external route is equal to the cost of an AS internal route and is comparable to the cost of an OSPFv3 route, the external route has a high reliability and can be configured as a Type 1 external route.
* Type 2 external routes: When the cost of the route from an ASBR to the destination outside an AS is greater than the cost of the internal route to the ASBR, Type 2 external routes have low reliability and can be configured as Type 2 external routes.If an OSPFv3 process is not bound to any VPN instance or is bound to a VPN instance but the **vpn-instance-capability simple** command is run, only EBGP routes are imported after the **import-route bgp** command is run, and IBGP routes are also imported after the **import-route bgp permit-ibgp** command is run, routing loops may occur. In this case, run the preference (OSPFv3) and preference (BGP) commands to specify the priorities of OSPFv3 and BGP routes to prevent loops. To import IBGP routes, run the **import-route bgp permit-ibgp** command, change the priority of OSPFv3 ASE routes to be smaller than that of IBGP routes to ensure that active routes are IBGP routes. That is, the OSPFv3 priority configured using the preference (OSPFv3) and preference (BGP) commands is greater than the IBGP priority.If an OSPFv3 process is bound to a VPN instance and the **vpn-instance-capability simple** command is not run for the OSPFv3 process, running the **import-route bgp** command imports BGP routes, including EBGP and IBGP routes. Whether the **import-route bgp permit-ibgp** command is run does not affect the imported routes. If both the import-route bgp permit-ibgp and default-route-advertise (OSPFv3) commands are run, active IBGP default routes in the routing table can be imported into OSPFv3.

**Prerequisites**

A route-policy has been created using the **route-policy** command if you want to import external routes using the route-policy.

**Implementation Procedure**

The costs of a Type 1 external route and a Type 2 external route are as follows:

* The cost of a Type 1 external route equals the cost for the OSPF device to reach an ASBR plus the cost of the route from the ASBR to the destination.
* The cost of a Type 2 external route equals the cost of the route from an ASBR to the destination.

**Configuration Impact**



OSPFv3 does not have a good mechanism to prevent loops of imported external routes. Therefore, exercise caution when configuring OSPFv3 to import external routes to prevent loops caused by manual configurations. You are advised to specify a tag, route-filter, or route-policy when importing routes and configure the policy to inherit the cost mode.If the cost parameter is not specified, the default cost value is used.To inherit the cost, you need to configure the cost inheritance mode in the policy or specify the inherit-cost parameter.After a policy for importing routes is configured using the route-filter or route-policy parameter in the command, the OSPFv3 process can import only the network segment routes that meet the specified conditions. This prevents the device from passively importing unnecessary routes. If no policy is specified for importing routes, a large number of unexpected routes may be imported. As a result, the number of routes exceeds the upper limit or the memory is overloaded.



**Precautions**

* You can run the default (OSPFv3) command to set default parameters for importing external routes, including the cost, type (Type 1 or Type 2), tag, and number of routes.
* The import-route (OSPFv3) command cannot import the default route of an external routing table. To advertise the default route of an external routing table that is learned when OSPF updates the routing table in a common OSPF area, run the default-route-advertise (OSPFv3) command.
* Exercise caution when configuring OSPFv3 to import external routes to prevent loops caused by manual configurations. You are advised to specify a tag or route-policy when importing routes and configure the policy to inherit the cost mode.
* If an OSPFv3 process is not bound to any VPN instance or is bound to a VPN instance but the **vpn-instance-capability simple** command is run, only EBGP routes are imported after the **import-route bgp** command is run, and IBGP routes are also imported after the **import-route bgp permit-ibgp** command is run, routing loops may occur. To prevent routing loops, run the preference (OSPFv3) and preference (BGP) commands to specify OSPFv3 and BGP route priorities. To import IBGP routes, run the **import-route bgp permit-ibgp** command, change the priority of OSPFv3 ASE routes to be smaller than that of IBGP routes to ensure that active routes are IBGP routes. That is, the preference configured for OSPFv3 is greater than that configured for IBGP.
* If an OSPFv3 process is bound to a VPN instance and the **vpn-instance-capability simple** command is not run for the OSPFv3 process, running the **import-route bgp** command imports BGP routes, including EBGP and IBGP routes. Whether the **import-route bgp permit-ibgp** command is run does not affect the imported routes. If both the import-route bgp permit-ibgp and default-route-advertise (OSPFv3) commands are run, active IBGP default routes in the routing table can be imported to OSPFv3.
* If tag is not specified, the default tag value is used for the process that is not bound to any VPN instance or the process that is bound to a VPN instance but has the **vpn-instance-capability simple** command configured. This cannot prevent loops caused by manual configuration.
* If the cost parameter is not specified, the default cost value is used. To inherit the cost, you need to configure the cost inheritance mode in the policy or specify the inherit-cost parameter.


Example
-------

# Import the bgp routes to OSPFv3 process 100.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 100
[*HUAWEI-ospfv3-100] import-route bgp

```

# Import type 1 static routes, with cost 10.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] import-route static cost 10 type 1

```

# Import type 2 direct routes, with cost 10.
```
<HUAWEI> system-view
[~HUAWEI] ospfv3 1
[*HUAWEI-ospfv3-1] import-route direct cost 10 type 2

```