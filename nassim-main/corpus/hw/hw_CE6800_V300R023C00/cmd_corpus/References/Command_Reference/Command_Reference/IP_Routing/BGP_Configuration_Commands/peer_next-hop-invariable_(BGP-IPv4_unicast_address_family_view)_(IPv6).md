peer next-hop-invariable (BGP-IPv4 unicast address family view) (IPv6)
======================================================================

peer next-hop-invariable (BGP-IPv4 unicast address family view) (IPv6)

Function
--------



The **peer next-hop-invariable** command configures the device not to change the next hop of a route when advertising the route to a peer group.

The **undo peer next-hop-invariable** command restores the default configuration.



By default:

* A device sets its interface IP address as the Next\_Hops of routes when advertising these routes to EBGP peers.
* A device does not modify the Next\_Hops of non-labeled routes if the routes are learned from EBGP peers and are to be advertised to IBGP peers; the device sets its interface IP address as the Next\_Hops of labeled routes if the routes are learned from EBGP peers and are to be advertised to IBGP peers.
* A device does not change the Next\_Hops of routes if the routes are learned from an IBGP peer and are to be advertised to another IBGP peer.
* A device sets its interface IP address as the Next\_Hops of routes when advertising imported IGP routes to IBGP peers.
* A device modifies the Next\_Hop of imported static routes to the local interface's IP address when advertising the routes to IBGP peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **next-hop-invariable**

**undo peer** *peerIpv6Addr* **next-hop-invariable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies an IPv6 peer address. | The value is in the format of X:X:X:X:X:X:X:X. |



Views
-----

BGP-IPv4 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer next-hop-invariable** command has the following functions:

* A BGP speaker does not change the next hop of a route when advertising the route to an EBGP peer group.
* A BGP speaker does not change the next hop of a labeled route when advertising the route to an IBGP peer group.
* A BGP speaker uses the next hop address of an imported IGP route when advertising the route to an IBGP peer group.

**Prerequisites**

A peer has been created using the **peer as-number** command.

**Precautions**

The **peer next-hop-invariable** command takes effect only on received routes. In the IPv4 unicast address family view, the command takes effect only on received IPv4 unicast routes, not on labeled routes.If both the peer next-hop-invariable and **peer next-hop-local** commands are run, the latest configuration overrides the previous one.


Example
-------

# Configure a BGP speaker not to change the next hop address when advertising routes to an IBGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer FE80::1 as-number 100
[*HUAWEI-bgp] ipv4-family unicast
[~HUAWEI-bgp-af-ipv4] peer FE80::1 enable
[*HUAWEI-bgp-af-ipv4] peer FE80::1 next-hop-invariable

```