peer route-policy import (BGP-IPv4 unicast address family view)(IPv4)
=====================================================================

peer route-policy import (BGP-IPv4 unicast address family view)(IPv4)

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
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| *route-policy-name* | Specifies the name of a routing policy. | The value is a string of 1 to 200 case-sensitive characters, spaces not supported. |



Views
-----

BGP-IPv4 unicast address family view


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

After the **peer route-policy import** command is run, only the routes that match the route-policy are accepted. Replacing or modifying the route-policy may cause a large number of routes to match the route-policy and be accepted.If **route-policy** *route-policy-name*is specified in this command, the following items can be matched: the RPKI origin AS validation, IPv4 ACL list, AS\_Path filter, AS\_Path length, community filter, route cost, VPN-Target extended community filter, bandwidth extended community filter, outbound interface, MPLS label, Large-Community filter, IPv4 route next-hop address ACL list, IPv6 route next-hop address ACL list, IPv4 route next-hop address prefix list, IPv6 route next-hop address prefix list, route preference, IP route destination address prefix list, route modulo, routing protocol type, route source IPv4 address ACL list, route source IPv6 address ACL list, route source IPv4 address prefix list, route source IPv6 address prefix list, route type, and route tag. The following items can be set: the BGP Large-Community attribute, BGP route AIGP value, AS\_Path attribute, BGP community attribute, BGP route MED, discarding the entropy label of routes, BGP route VPN-Target extended community attribute, BGP route color extended community attribute, BGP route SoO extended community attribute, BGP route bandwidth extended community attribute, MPLS label, BGP route local preference, route next-hop address, BGP route origin, BGP route PreVal, and QoS parameters.If the referenced policy contains unsupported attribute matching or behavior setting, unexpected results may occur. For some attribute matching behaviors, the device may display warning-level messages.Outbound interface-based matching applies only to directly connected EBGP peers.


Example
-------

# Apply the route-policy named test-policy to the routes received from a peer.
```
<HUAWEI> system-view
[~HUAWEI] route-policy test-policy permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 200
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.2 route-policy test-policy import

```