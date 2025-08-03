peer next-hop-local (BGP-VPN instance IPv6 address family view)(IPv4)
=====================================================================

peer next-hop-local (BGP-VPN instance IPv6 address family view)(IPv4)

Function
--------



The **peer next-hop-local** command configures a BGP device to set its IP address as the next hop of routes when the BGP device advertises routes to an IBGP peer.

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
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer next-hop-local** command is usually run on an ASBR. By default, when an ASBR forwards a route learned from an EBGP peer to its IBGP peers, the ASBR does not change the Next\_Hop of the route. Therefore, the Next\_Hop address of the route remains the EBGP peer IP address. After being forwarded to the IBGP peers, the route cannot become active because of the unreachable Next\_Hop. The **peer next-hop-local** command needs to be run to configure the ASBR to modify the Next\_Hop of the route to the local IP address before advertising the route to IBGP peers. After being forwarded to the IBGP peers, the route can be active because the Next\_Hop is reachable (an IGP is configured in the AS).

**Configuration Impact**

If the command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The **peer next-hop-local** command is applicable only to IBGP peers.If you run both the peer next-hop-local and peer next-hop-invariable commands, the latest configuration overrides the previous one.If this command is run on a route reflector, the command takes effect for BGP labeled routes, VPNv4 routes, and VPNv6 routes.Except BGP labeled routes, VPNv4 routes, and VPNv6 routes, running this command on an RR or a peer in a BGP confederation to change the next hop of BGP routes does not take effect.


Example
-------

# Configure a BGP device to set its IP address as the next hop of routes when advertising the routes to peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpna
[*HUAWEI-bgp-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpna] quit
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 10.1.1.1 enable
[*HUAWEI-bgp-6-vpna] peer 10.1.1.1 next-hop-local

```