hierarchy-convergence base-route hierarchy-route (BGP-IPv4 unicast address family view)
=======================================================================================

hierarchy-convergence base-route hierarchy-route (BGP-IPv4 unicast address family view)

Function
--------



The **hierarchy-convergence base-route hierarchy-route** command configures base routes and hierarchical routes.

The **undo hierarchy-convergence base-route hierarchy-route** cancels the configuration.



By default, base routes and hierarchical routes are not configured.


Format
------

**hierarchy-convergence base-route** *ip-address* *mask-length* **hierarchy-route** { **all** | **route-policy** *policy-name* }

**undo hierarchy-convergence base-route** *ip-address* *mask-length* **hierarchy-route** { **all** | **route-policy** *policy-name* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the mask length of a base route. | It is an integer ranging from 1 to 32. |
| **all** | All routes without the hierarchical convergence attribute will be mapped to the current base route. | - |
| **route-policy** *policy-name* | Routes that do not carry the hierarchical convergence attribute and match the route-policy are mapped to the current base route. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



BGP routes converge one by one in case of a failure. In the underlay BGP scenario of a data center, routes are classified into base routes (device reachability routes) and hierarchical routes (learned service routes). To configure base routes and hierarchical routes, run the **hierarchy-convergence base-route hierarchy-route** command. Base routes converge first, and then hierarchical routes rely on the recursion results of the base routes. BGP hierarchical routing speeds up route convergence in the case of faults on data center networks, especially when hierarchical routes greatly outnumber base routes.




Example
-------

# Configure base routes and hierarchical routes.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] hierarchy-convergence base-route 10.1.1.1 32 hierarchy-route route-policy test-policy

```