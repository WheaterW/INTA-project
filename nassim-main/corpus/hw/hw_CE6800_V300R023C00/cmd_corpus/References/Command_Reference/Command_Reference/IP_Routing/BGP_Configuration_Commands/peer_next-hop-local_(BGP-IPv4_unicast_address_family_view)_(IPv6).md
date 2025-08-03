peer next-hop-local (BGP-IPv4 unicast address family view) (IPv6)
=================================================================

peer next-hop-local (BGP-IPv4 unicast address family view) (IPv6)

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

**peer** *peerIpv6Addr* **next-hop-local**

**undo peer** *peerIpv6Addr* **next-hop-local**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a BGP peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-IPv4 unicast address family view


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

The **peer next-hop-local** command is applicable to IBGP peers.If both the peer next-hop-local and peer next-hop-invariable commands are run, the latest configuration overrides the previous one.


Example
-------

# Configure a BGP device to set its IP address as the next hop of routes when advertising the routes to peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer FE80::1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer FE80::1 enable
[*HUAWEI-bgp-af-ipv4] peer FE80::1 next-hop-local

```