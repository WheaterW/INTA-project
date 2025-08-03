import-route (OSPF view)
========================

import-route (OSPF view)

Function
--------



The **import-route** command imports routes learned by other protocols.

The **undo import-route** command cancels the configuration.



By default, routes learned by other protocols are not imported.


Format
------

**import-route** { **direct** | **static** | **bgp** [ **permit-ibgp** ] } [ { **inherit-cost** | **cost** *cost* } | { **route-policy** *route-policy-name* } | **tag** *tag* | **type** *type* ] \*

**import-route** { **ospf** | **isis** | **rip** } [ *process-id-rip* ] [ { **inherit-cost** | **cost** *cost* } | { **route-policy** *route-policy-name* } | **tag** *tag* | **type** *type* ] \*

**undo import-route** { **direct** | **static** | **bgp** }

**undo import-route** { **ospf** | **isis** | **rip** } [ *process-id-rip* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **direct** | Imports direct routes. | - |
| **static** | Imports static routes. After the parameter is specified, only active static routes can be imported. | - |
| **bgp** | Imports BGP routes.  For an OSPF process that is not bound to a VPN instance or is bound to a VPN instance but the vpn-instance-capability simple command is run, the parameter imports only EBGP routes. | - |
| **permit-ibgp** | Imports IBGP routes. NOTICE:  For an OSPF process that is not bound to a VPN instance or is bound to a VPN instance but the vpn-instance-capability simple command is run, importing IBGP routes may cause routing loops. Therefore, exercise caution when using this parameter. | - |
| **inherit-cost** | Retains the original costs of the imported routes. | - |
| **cost** *cost* | Specifies a route cost. | The value is an integer ranging from 0 to 16777214. The default value is 1. |
| **route-policy** *route-policy-name* | Specifies the name of the route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **tag** *tag* | Specifies the tag of the external LSA. | The value is an integer ranging from 0 to 4294967295. The default value is 1. |
| **type** *type* | Specifies the type of the external routes. | The value is 1 or 2.   * 1: Type 1 external route * 2: Type 2 external route   The default value is 2. |
| **ospf** | Imports OSPF routes. | - |
| **isis** | Imports IS-IS routes. | - |
| **rip** | Imports RIP routes. | - |
| *process-id-rip* | Specifies the process ID of the protocol whose routes are imported. | The value is an integer ranging from 1 to 4294967295. The default value is 1. |



Views
-----

OSPF view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Importing the routes discovered by other routing protocols can enrich OSPF routing information.OSPF routes are classified into the following types in the descending order of priorities:

* Intra-area routes: refer to the routes in an area within an AS.
* Inter-area routes: refer to the routes between areas of the same AS. Intra-area routes and area external routes are internal routes of an AS.
* Type 1 external routes: When the cost of external routes is almost the same as that of AS internal routes and can be compared with the cost of OSPF routes, these external routes have a high reliability and can be configured as Type 1 external routes.
* Type 2 external routes: When the cost of the routes from an ASBR to the destination outside an AS is greater than the cost of the internal routes to the ASBR, these external routes have a low reliability and can be configured as Type 2 external routes.

**Prerequisites**

A route-policy has been created using the **route-policy** command if you want to import external routes using the route-policy.

**Implementation Procedure**

The costs of a Type 1 external route and a Type 2 external route are as follows:

* The cost of a Type 1 external route equals the cost for the OSPF device to reach an ASBR plus the cost of the route from the ASBR to the destination.
* The cost of a Type 2 external route equals the cost of the route from an ASBR to the destination.

**Configuration Impact**

OSPF does not have a good mechanism to prevent loops of imported external routes. Therefore, exercise caution when configuring OSPF to import external routes to prevent loops caused by manual configurations. You are advised to specify a tag, route-filter, or route-policy when importing routes and configure the policy to inherit the cost mode.If the cost parameter is not specified, the default cost value is used.To inherit the cost, you need to configure the cost inheritance mode in the policy, use the default cost inherit-metric mode, or specify the inherit-cost parameter.After a policy for importing routes is configured using the route-filter or route-policy parameter in the command, the OSPF process can import only the routes that meet the specified conditions. This prevents the device from passively importing unnecessary routes. If no policy is specified for importing routes, a large number of unexpected routes may be imported. As a result, the number of routes exceeds the upper limit or the memory is overloaded.Running the **import-route bgp** command may import a large number of routes. Therefore, you are advised to run the **import-route limit** command together with the **import-route bgp** command.

**Precautions**

* You can run the default (OSPF) command to set default parameters for an OSPF process on a public network or an OSPF process on a private network for which the **vpn-instance-capability simple** command is run. The default parameters include the cost, type (Type 1 or Type 2), tag, and number of routes imported by OSPF.
* The import-route (OSPF) command cannot import the default route of an external route. To advertise the default route of an external route that is learned when OSPF updates the routing table in a common OSPF area, run the default-route-advertise (OSPF) command.
* Exercise caution when configuring OSPF to import external routes to prevent loops caused by manual configurations. You are advised to specify a tag or route-policy when importing routes and configure the policy to inherit the cost mode.
* If an OSPF process is not bound to any VPN instance or is bound to a VPN instance but the **vpn-instance-capability simple** command is run, only EBGP routes are imported after the **import-route bgp** command is run, and IBGP routes are also imported after the **import-route bgp permit-ibgp** command is run. In this case, routing loops may occur. You can run the preference (OSPF) and preference (BGP) commands to specify the preference values of OSPF and BGP routes to prevent loops. To import IBGP routes, run the **import-route bgp permit-ibgp** command, and change the preference values of OSPF ASE routes to be larger than those of IBGP routes to ensure that the active routes are IBGP routes.
* If an OSPF process is bound to a VPN instance and the **vpn-instance-capability simple** command is not run for the OSPF process, running the **import-route bgp** command imports BGP routes, including EBGP and IBGP routes. Whether the **import-route bgp permit-ibgp** command is run does not affect the imported routes.
* If tag is not specified, the default tag value (specified using the **default tag** command) is used for the process that is not bound to any VPN instance or the process that is bound to a VPN instance but has the **vpn-instance-capability simple** command configured. This cannot prevent loops caused by manual configurations.
* If the cost parameter is not specified, the default cost value (specified by the **default cost** command) is used. To inherit the cost, you need to configure the cost inheritance mode in the policy, use the default cost inherit-metric mode, or specify the inherit-cost parameter.
* For details about the rules for generating the tag values carried in the routes imported using the import-route (OSPF) command, see the usage scenario description of the **route-tag** command.
* An OSPF process bound to a VPN instance can import only the routes of the same VPN instance.


Example
-------

# Import Type 2 OSPF routes, with tag 33 and cost 50.
```
<HUAWEI> system-view
[~HUAWEI] ospf 100
[*HUAWEI-ospf-100] import-route isis 1 type 2 tag 33 cost 50

```