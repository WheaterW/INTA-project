apply ipv6 gateway-ip
=====================

apply ipv6 gateway-ip

Function
--------



The **apply ipv6 gateway-ip** command sets a gateway IPv6 address for routes.

The **undo apply ipv6 gateway-ip** command cancels the configuration.



By default, no gateway IPv6 address is set for routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**apply ipv6 gateway-ip** { **origin-nexthop** | *address* }

**undo apply ipv6 gateway-ip** [ *address* | **origin-nexthop** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **origin-nexthop** | Sets the next-hop IPv6 address of a route as its gateway IPv6 address. | - |
| *address* | Sets a gateway IPv6 address for a route. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

Route-policy view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When configuring an L3VPN instance on a Layer 2 or Layer 3 gateway to advertise static VPN routes that can reach a VNF to an EVPN, you need to first create a route-policy to match such routes in the L3VPN instance. You can run the **apply ipv6 gateway-ip origin-nexthop** command to set the original next hop addresses of the static VPN routes as the gateway IPv6 addresses.

* Run the **route-policy** command to enter the route-policy view.
* A route-policy may consist of multiple nodes, and the relationship among these nodes is OR. The device matches routes against the nodes in a route-policy in order of node IDs. If a route matches one of the nodes, the route matches this route-policy and is no longer matched against other nodes.Each node comprises a set of if-match and apply clauses. The if-match clauses define filtering rules based on route attributes. The relationship among if-match clauses that are based on different route attributes is AND in the same route-policy node. Specifically, a route is considered to match a node only when it matches all the if-match clauses of the node. The relationship among if-match clauses that are based on the same route attribute is OR in the same route-policy node. Specifically, a route is matched against the if-match clauses in order; if the route matches an if-match clause, the route is considered to match the route-policy and will not be matched against the rest if-match clauses. For example, node 10 has two if-match clauses: if-match community-filter 1 and if-match as-path-filter 1. The two if-match clauses are based on different route attributes. Therefore, the relationship between them is AND. Node 20 also has two if-match clauses: if-match community-filter 1 and if-match community-filter 2. The two if-match clauses are both based on the community attribute. Therefore, the relationship between them is OR. The apply clauses specify actions. If a route matches a node, the apply clauses set route attributes for the route.

**Prerequisites**



A route-policy has been created using the **route-policy** command.



**Configuration Impact**



If a route matches the route-policy, a gateway IPv6 address is set for the route.




Example
-------

# Set the next-hop IPv6 address of a route as its gateway IPv6 address.
```
<HUAWEI> system-view
[~HUAWEI] route-policy policy permit node 10
[*HUAWEI-route-policy] apply ipv6 gateway-ip origin-nexthop

```