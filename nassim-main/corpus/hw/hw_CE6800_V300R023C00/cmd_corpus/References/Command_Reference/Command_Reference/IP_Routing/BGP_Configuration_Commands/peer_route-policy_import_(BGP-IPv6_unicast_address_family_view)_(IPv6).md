peer route-policy import (BGP-IPv6 unicast address family view) (IPv6)
======================================================================

peer route-policy import (BGP-IPv6 unicast address family view) (IPv6)

Function
--------



The **peer route-policy import** command specifies a route-policy for filtering routes received from a peer.

The **undo peer route-policy import** command deletes a specified route-policy.



By default, no route-policy is configured for filtering routes received from a peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **route-policy** *route-policy-name* **import**

**undo peer** *ipv6-address* **route-policy** *route-policy-name* **import**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies the IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters, spaces not supported. |



Views
-----

BGP-IPv6 unicast address family view


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

If both a peer group and a peer are configured with a route-policy, the configuration on the peer takes precedence. If a peer group is configured with a route-policy but peers in the group are not configured with their own ones, the peers inherit the configuration of the peer group. If the route-policy configuration of a peer group is the same as that of a peer in the group, the configuration is displayed in the configuration file only for the peer group.If a BGP peer relationship is established, then an import policy is bound to the peer or the import policy bound to the peer is modified, and the device does not support the Refresh capability, the peer relationship is re-established because the import policy addition or modification causes the peer to resend Refresh messages.

**Precautions**

After the **peer route-policy import** command is run, only the routes that match the route-policy are accepted. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be accepted.If **route-policy** *route-policy-name*is specified in the command, the following items can be matched: RPKI origin AS validation, AS\_Path filter, AS\_Path length, community filter, route cost, IPv6 route destination address, VPN-Target extended community filter, bandwidth extended community filter, outbound interface, MPLS label, Large-Community filter, IPv4 route next hop address ACL, IPv6 route next hop address ACL, IPv4 route next hop address prefix list, IPv6 route next hop address prefix list, route preference, IPv6 route destination address prefix list, route modulo, routing protocol type, route source IPv4 address ACL, route source IPv6 address ACL, route source IPv4 address prefix list, route source IPv6 address prefix list, route type, and route tag. The following items can be set: BGP Large-Community attribute, BGP route AIGP value, AS\_Path attribute, BGP route community attribute, BGP route MED value, BGP route VPN target extended community attribute, BGP route color extended community attribute, BGP route SoO extended community attribute, BGP route bandwidth extended community attribute, MPLS label, BGP route local preference, route next hop IPv6 address, BGP route origin, BGP route PreVal, and QoS parameters.If the referenced policy contains unsupported attribute matching or behavior setting, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.Outbound interface-based matching applies only to directly connected EBGP peers.


Example
-------

# Apply the route-policy named test-policy to the routes received from a peer.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 2001:DB8:1::1 route-policy test-policy import

```