Configuring a Route-Policy
==========================

Each node of a route-policy can comprise a set of **if-match**, **apply**, and **goto next-node** clauses.

#### Usage Scenario

A route-policy includes various matching rules and hence can meet the requirements of various scenarios. Except ACLs, IP prefix lists, and AS\_Path filters, other filters need to be used with a route-policy.

A route-policy is used to match routes or route attributes, and to change route attributes when the matching rules are met. ACLs, IP prefix lists, AS\_Path filters, community filters, extended community filters, and RD filters can be used to define matching conditions.

A route-policy can consist of multiple nodes, and each node can comprise the following clauses:

* **if-match** clauses: define the matching rules that are used to match certain route attributes. The matching rules are conditions defined by the route-policy against which routes are matched.
* **apply** clauses: specify actions. When a route matches a node, the **apply** clauses set certain attributes for the route.
* **goto next-node** clauses: further match routes against a specified node after the routes match the current node.

For more information about a route-policy, refer to the *HUAWEI NE40E-M2 series Universal Service Router Feature Description - IP Routing*.


#### Pre-configuration Tasks

Before configuring a route-policy, complete the following tasks:

* [Configure an IP prefix list](dc_vrp_route-policy_cfg_0003.html).
* Configure a routing protocol.


[Creating a Route-Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0008.html)

By applying a route-policy, you can set attributes for the imported routes as required.

[(Optional) Configuring an if-match Clause](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0009.html)

The **if-match** clauses define the matching rules that are used to match certain route attributes.

[(Optional) Configuring an apply Clause](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0010.html)

The **apply** clauses specify actions to set certain route attributes.

[(Optional) Further Matching Routes Against a Specified Node](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0043.html)

A route-policy can be configured to match routes against two or more nodes.

[Applying a Route-Policy](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0042.html)

A route-policy takes effect only when it is applied to a routing protocol.

[Verifying the Route-Policy Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_route-policy_cfg_0011.html)

After configuring a route-policy, verify information about the route-policy.