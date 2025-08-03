nexthop third-party (BGP-IPv6 unicast address family view)
==========================================================

nexthop third-party (BGP-IPv6 unicast address family view)

Function
--------



The **nexthop third-party** command prevents a BGP speaker from changing the next hop address of a route when the BGP speaker advertises the route to its peers in the following scenarios:

**-** The route is learned from a directly connected peer and is to be advertised to a directly connected EBGP peer, the original next hop of the route resides on the same network segment as the local interface that is used to establish the BGP peer relationship with the EBGP peer, and all directly connected interfaces are broadcast interfaces.

**-** The route is locally imported and is to be advertised to a directly connected IBGP or EBGP peer, the next hop to which the route recurses resides on the same network segment as the local interface that is used to establish the BGP peer relationship with the IBGP or EBGP peer, and all directly connected interfaces are broadcast interfaces.

The **undo nexthop third-party** command restores the default configurations.



The default configurations are as follows:

* Before advertising a route that is learned from a directly connected peer to a directly connected EBGP peer, the device changes the next hop of the route to the IP address of the local interface that is used to establish the BGP peer relationship with the EBGP peer.
* Before advertising a locally imported route to a directly connected IBGP or EBGP peer, the device changes the next hop of the route to the IP address of the local interface that is used to establish the BGP peer relationship with the IBGP or EBGP peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**nexthop third-party**

**undo nexthop third-party**


Parameters
----------

None

Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a Layer 2 protocol tunneling scenario, to ensure that traffic is transmitted along the optimal route, run the **nexthop third-party** command.

**Precautions**

If the command and load balancing function are both configured, this command does not take effect.


Example
-------

# Prevent a BGP speaker from changing the next hop address of a route when the BGP speaker advertises the route to a peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] nexthop third-party

```