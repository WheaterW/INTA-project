peer next-hop-local (BGP-IPv6 unicast address family view)(IPv4)
================================================================

peer next-hop-local (BGP-IPv6 unicast address family view)(IPv4)

Function
--------



The **peer next-hop-local** command configures a BGP device to set its IP address as the next hop of routes when the BGP device advertises the routes to its IBGP peer.

The **undo peer next-hop-local** command restores the default setting.



By default:

* When advertising routes to EBGP peers, BGP sets the next hops of the routes to the IP address of its interface connected to the EBGP peers.
* When advertising an unlabeled route from an EBGP peer to an IBGP peer, a BGP device does not change the next hop of the route. When advertising a labeled route, a BGP device changes the next hop of the route to the IP address of its interface connected to the IBGP peer.
* BGP does not change the next hop of a route when advertising the route from an IBGP peer to another IBGP peer.
* When advertising locally generated routes to IBGP peers, BGP sets the next hops of the routes to the IP address of its interface connected to the IBGP peers.
* When advertising a VPN instance route to a VPN peer, BGP sets the next hop of the route to the IP address of the interface connected to the peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **next-hop-local**

**undo peer** *ipv4-address* **next-hop-local**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer next-hop-local** command is usually run on an ASBR. By default, a device does not change the next hop address of a route learned from an EBGP peer before forwarding the route to IBGP peers. The next hop address of a route advertised by an EBGP peer to this device is the peer address of the EBGP peer. After being forwarded to IBGP peers in the local AS, this route is not active because the next hop is unreachable. The **peer next-hop-local** command needs to be run to configure the ASBR to change the next hop of the route to its IP address when the ASBR advertises the route to an IBGP peer. Therefore, after being forwarded to the IBGP peer, the route can become an active route because the next hop is reachable.

**Configuration Impact**

If the command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The **peer next-hop-local** command is applicable only to IBGP peers.If you run both the peer next-hop-local and peer next-hop-invariable commands, the latest configuration overrides the previous one.If this command is run on a route reflector, the command takes effect for BGP labeled routes, VPNv4 routes, and VPNv6 routes.Except BGP labeled routes, VPNv4 routes, and VPNv6 routes, running this command on an RR or a peer in a BGP confederation to change the next hop of BGP routes does not take effect.


Example
-------

# Configure a BGP device to set its IP address as the next hop of routes when advertising the routes to peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 10.1.1.1 enable
[*HUAWEI-bgp-af-ipv6] peer 10.1.1.1 next-hop-local

```