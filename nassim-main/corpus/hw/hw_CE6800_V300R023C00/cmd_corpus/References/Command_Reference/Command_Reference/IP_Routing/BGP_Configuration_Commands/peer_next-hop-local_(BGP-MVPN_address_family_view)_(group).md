peer next-hop-local (BGP-MVPN address family view) (group)
==========================================================

peer next-hop-local (BGP-MVPN address family view) (group)

Function
--------



The **peer next-hop-local** command configures a BGP MVPN device to set its IP address as the next hop of routes when advertising the routes to an IBGP peer group.

The **undo peer next-hop-local** command restores the default configuration.



By default:

* When advertising routes to EBGP peers, BGP sets the next hops of the routes to the IP address of its interface connected to the EBGP peers.
* When advertising an unlabeled route from an EBGP peer to an IBGP peer, a BGP device does not change the next hop of the route. When advertising a labeled route, a BGP device changes the next hop of the route to the IP address of its interface connected to the IBGP peer.
* BGP does not change the next hop of a route when advertising the route from an IBGP peer to another IBGP peer.
* When advertising locally generated routes to IBGP peers, BGP sets the next hops of the routes to the IP address of its interface connected to the IBGP peers.
* When advertising a VPN instance route to a VPN peer, BGP sets the next hop of the route to the IP address of the interface connected to the peer.


Format
------

**peer** *group-name* **next-hop-local** [ **reflect-effective** ]

**undo peer** *group-name* **next-hop-local**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **reflect-effective** | Configures the device to set its IP address as the next hop of routes when the device advertises the routes to an IBGP peer or peer group in RR scenarios. | - |



Views
-----

BGP-MVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The **peer next-hop-local** command is usually run on an ASBR. By default, a device does not change the next hop address of a route learned from an EBGP peer before forwarding the route to IBGP peers. The next hop address of a route advertised by an EBGP peer to this device is the peer address of the EBGP peer. After being forwarded to IBGP peers in the local AS, this route is not active because the next hop is unreachable. The **peer next-hop-local** command needs to be run to configure the ASBR to change the next hop of the route to its IP address when the ASBR advertises the route to an IBGP peer. Therefore, after being forwarded to the IBGP peer, the route can become an active route because the next hop is reachable.


Example
-------

# Configure a BGP MVPN device to set its IP address as the next hop when advertising routes to the IBGP peer group test.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test internal
[*HUAWEI-bgp] ipv4-family mvpn
[*HUAWEI-bgp-af-mvpn] peer test enable
[*HUAWEI-bgp-af-mvpn] peer test next-hop-local

```