hierarchy-convergence base-route hierarchy-route (BGP-IPv6 unicast address family view)
=======================================================================================

hierarchy-convergence base-route hierarchy-route (BGP-IPv6 unicast address family view)

Function
--------



The **hierarchy-convergence base-route hierarchy-route** command configures base routes and hierarchical routes.

The **undo hierarchy-convergence base-route hierarchy-route** cancels the configuration.



By default, base routes and hierarchical routes are not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**hierarchy-convergence base-route** *ipv6-address* *ipv6-mask-length* **hierarchy-route** { **all** | **route-policy** *policy-name* }

**undo hierarchy-convergence base-route** *ipv6-address* *ipv6-mask-length* **hierarchy-route** { **all** | **route-policy** *policy-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 address of a base route. | The value is in the format of X:X:X:X:X:X:X:X. |
| *ipv6-mask-length* | Specifies the mask length of a base route. | It is an integer ranging from 1 to 128. |
| **all** | All routes without the hierarchical convergence attribute will be mapped to the current base route. | - |
| **route-policy** *policy-name* | Routes that do not carry the hierarchical convergence attribute and match the route-policy are mapped to the current base route. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

BGP routes converge one by one in case of a failure. In the underlay BGP scenario of a data center, routes are classified into base routes (device reachability routes) and hierarchical routes (learned service routes). To configure base routes and hierarchical routes, run the **hierarchy-convergence base-route hierarchy-route** command. Base routes converge first, and then hierarchical routes rely on the recursion results of the base routes. BGP hierarchical routing speeds up route convergence in the case of faults on data center networks, especially when hierarchical routes greatly outnumber base routes.


Example
-------

# Configure base routes and hierarchical routes.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] hierarchy-convergence base-route 2001:DB8:1::1 128 hierarchy-route route-policy test-policy

```