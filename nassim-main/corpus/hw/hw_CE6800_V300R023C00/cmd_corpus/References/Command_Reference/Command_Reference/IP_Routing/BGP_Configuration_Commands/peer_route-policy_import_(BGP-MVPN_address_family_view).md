peer route-policy import (BGP-MVPN address family view)
=======================================================

peer route-policy import (BGP-MVPN address family view)

Function
--------



The **peer route-policy import** command specifies a route-policy for filtering routes received from a peer.

The **undo peer route-policy import** command deletes a specified route-policy.



By default, no route-policy is configured for filtering routes received from a peer.


Format
------

**peer** *ipv4-address* **route-policy** *route-policy-name* **import**

**undo peer** *ipv4-address* **route-policy** *route-policy-name* **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *route-policy-name* | Specifies the name of a route-policy. | The value is a string of 1 to 200 case-sensitive characters. It cannot contain spaces. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a route-policy is created, the **peer route-policy import** command is used to apply a Route-Policy to a peer so that the routes received from the peer can be controlled. To be specific, only the necessary routes are received from the peer. In this manner, route management is implemented, the scale of the routing table is reduced, and fewer network resources are consumed.

**Prerequisites**

If a route-policy that does not exist is specified in the command, use the route-policy command to create the route-policy.

**Configuration Impact**

If both a peer group and a peer are configured with a route-policy, the configuration on the peer takes precedence. If a peer group is configured with a route-policy but peers in the group are not configured with their own ones, the peers inherit the configuration of the peer group. If the route-policy configuration of a peer group is the same as that of a peer in the group, the configuration is displayed in the configuration file only for the peer group.If a BGP peer relationship is established, then an import policy is bound to the peer or the import policy bound to the peer is modified, and the device does not support the Refresh capability, the peer relationship is re-established because the import policy addition or modification causes the peer to resend Refresh messages.If you run both this command and the **peer route-filter** command, the latest configuration overrides the previous one.

**Precautions**

After the **peer route-policy import** command is run, only the routes that match the route-policy are accepted. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be accepted.If **route-policy** *route-policy-name*is specified in the command, the following information can be matched: AS\_Path filter, AS\_Path length, community filter, route cost, VPN-Target extended community filter, outbound interface, IP address of the NG MVPN route advertiser, Large-Community filter, Next-hop address ACL list of routing information, next-hop address ACL list of IPv6 routing information, next-hop address prefix list of routing information, next-hop address prefix list based on IPv6 routing information, routing protocol type, RD attribute filter, source IP address ACL list of routing information, route source IPv6 address ACL list, route source IP address prefix list, route source IPv6 address prefix list, route type, and route tag. The following information can be set: BGP Large-Community attribute, AS\_Path attribute, BGP community attribute, MED of BGP routes, local preference of BGP routes, next hop address (IPv4) of BGP routes, origin of BGP routes, and preferred value of BGP routes.If the referenced policy contains unsupported attribute matching or setting behavior, unexpected results may occur.


Example
-------

# Apply the route-policy named test-policy to the routes received from a peer.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 10
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.1 route-policy test-policy import

```