peer next-hop-local (BGP-MVPN address family view)
==================================================

peer next-hop-local (BGP-MVPN address family view)

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


Format
------

**peer** *ipv4-address* **next-hop-local** [ **reflect-effective** ]

**undo peer** *ipv4-address* **next-hop-local**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| **reflect-effective** | Configures the device to set its IP address as the next hop of routes when the device advertises the routes to an IBGP peer or peer group in RR scenarios. | - |



Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer next-hop-local** command is usually run on an ASBR. By default, when an ASBR forwards a route learned from an EBGP peer to its IBGP peers, the ASBR does not change the Next\_Hop of the route. Therefore, the Next\_Hop address of the route remains the EBGP peer IP address. After being forwarded to the IBGP peers, the route cannot become active because of the unreachable Next\_Hop. The **peer next-hop-local** command needs to be run to configure the ASBR to modify the Next\_Hop of the route to the local IP address before advertising the route to IBGP peers. After being forwarded to the IBGP peers, the route can be active because the Next\_Hop is reachable (an IGP is configured in the AS).The **peer next-hop-local** command is valid only for the labeled routes and VPNv4 routes on a BGP route reflector. If the keyword reflect-effective is configured, the command is valid for MVPN address family routes, IPv6 MVPN address family routes, and MDT address family routes. To configure a BGP device to set its IP address as the next hop of other types of routes, you can apply an export policy.

**Configuration Impact**

If the command is run more than once, the latest configuration overrides the previous one.

**Precautions**

The **peer next-hop-local** command is applicable only to IBGP peers.If you run both the peer next-hop-local and peer next-hop-invariable commands, the latest configuration overrides the previous one.If this command is run on a route reflector, the command takes effect for BGP labeled routes, VPNv4 routes, and VPNv6 routes.Except BGP labeled routes, VPNv4 routes, and VPNv6 routes, running this command on an RR or a peer in a BGP confederation to change the next hop of BGP routes does not take effect.


Example
-------

# Configure a BGP MVPN device to set its IP address as the next hop of routes when advertising the routes to peer 10.1.1.2
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.2 enable
[*HUAWEI-bgp-af-mvpn] peer 10.1.1.2 next-hop-local

```