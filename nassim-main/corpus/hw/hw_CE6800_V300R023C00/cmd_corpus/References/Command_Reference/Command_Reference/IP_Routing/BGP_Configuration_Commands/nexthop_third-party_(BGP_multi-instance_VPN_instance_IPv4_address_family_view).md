nexthop third-party (BGP multi-instance VPN instance IPv4 address family view)
==============================================================================

nexthop third-party (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **nexthop third-party** command prevents a BGP speaker from changing the next hop address of a route when the BGP speaker advertises the route to its peers in the following scenarios:

**-** The route is learned from a directly connected peer and is to be advertised to a directly connected EBGP peer, the original next hop of the route resides on the same network segment as the local interface that is used to establish the BGP peer relationship with the EBGP peer, and all directly connected interfaces are broadcast interfaces.

**-** The route is locally imported and is to be advertised to a directly connected IBGP or EBGP peer, the next hop to which the route recurses resides on the same network segment as the local interface that is used to establish the BGP peer relationship with the IBGP or EBGP peer, and all directly connected interfaces are broadcast interfaces.

The **undo nexthop third-party** command restores the default configurations.



The default configurations are as follows:

* Before advertising a route that is learned from a directly connected peer to a directly connected EBGP peer, the device changes the next hop of the route to the IP address of the local interface that is used to establish the BGP peer relationship with the EBGP peer.
* Before advertising a locally imported route to a directly connected IBGP or EBGP peer, the device changes the next hop of the route to the IP address of the local interface that is used to establish the BGP peer relationship with the IBGP or EBGP peer.


Format
------

**nexthop third-party**

**undo nexthop third-party**


Parameters
----------

None

Views
-----

BGP multi-instance VPN instance IPv4 address family view


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
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] nexthop third-party

```