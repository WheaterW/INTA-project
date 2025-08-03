peer route-policy import (BGP-MVPN address family view) (group)
===============================================================

peer route-policy import (BGP-MVPN address family view) (group)

Function
--------



The **peer route-policy import** command specifies a route-policy for routes received from a peer group.

The **undo peer route-policy import** command deletes a specified route-policy.



By default, no route-policy is specified for a peer group. That is, no route-policy is applied to the routes to be received from peers.


Format
------

**peer** *group-name* **route-policy** *route-policy-name* **import**

**undo peer** *group-name* **route-policy** *route-policy-name* **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| *route-policy-name* | Specifies a route-policy. | The value is a string of 1 to 200 case-sensitive characters without spaces. |



Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a route-policy is created, the **peer route-policy import** command is used to apply a Route-Policy to a peer group so that the routes received from a peer group can be controlled. To be specific, only the necessary routes are received from the peer group. In this manner, route management is implemented, the scale of the routing table is reduced, and fewer network resources are consumed.

**Prerequisites**

If a route-policy that does not exist is specified in the command, use the route-policy command to create the route-policy.

**Configuration Impact**

If both a peer group and a peer are configured with a route-policy, the configuration on the peer takes precedence. If a peer group is configured with a route-policy but peers in the group are not configured with their own ones, the peers inherit the configuration of the peer group. If the route-policy configuration of a peer group is the same as that of a peer in the group, the configuration is displayed in the configuration file only for the peer group.If a BGP peer relationship is established, then an import policy is bound to the peer or the import policy bound to the peer is modified, and the device does not support the Refresh capability, the peer relationship is re-established because the import policy addition or modification causes the peer to resend Refresh messages.If you run both this command and the **peer route-filter** command, the latest configuration overrides the previous one.

**Precautions**

After the **peer route-policy import** command is run, only the routes that match the route-policy are received. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be received.When configuring **route-policy** *route-policy-name*, you can run this command to filter routes based on the AS\_Path filter, AS\_Path length, community filter, route cost, VPN-Target extended community filter, outbound interface, IP address of the NG MVPN route advertiser, Large-Community filter, next-hop address ACL list of routing information, next-hop address ACL list of IPv6 routing information, next-hop address prefix list of routing information, next-hop address prefix list based on IPv6 routing information, routing protocol type, RD attribute filter, route source IP address ACL list, route source IPv6 address ACL list, route source IP address prefix List, route source IPv6 address prefix list, route type, and route tag. You can set the BGP Large-Community attribute, AS\_Path attribute, BGP community attribute, MED of BGP routes, local preference of BGP routes, next hop address (IPv4) of BGP routes, origin for BGP routes, and preferred value of BGP routes.If the referenced policy contains unsupported attribute matching or setting behavior, unexpected results may occur.


Example
-------

# Apply the route-policy named test-policy to the routes received from a peer group.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer test enable
[*HUAWEI-bgp-af-mvpn] peer test route-policy test-policy import

```