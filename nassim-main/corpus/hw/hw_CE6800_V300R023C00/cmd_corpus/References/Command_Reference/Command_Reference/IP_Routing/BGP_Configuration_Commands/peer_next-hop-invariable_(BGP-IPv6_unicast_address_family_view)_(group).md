peer next-hop-invariable (BGP-IPv6 unicast address family view) (group)
=======================================================================

peer next-hop-invariable (BGP-IPv6 unicast address family view) (group)

Function
--------



The **peer next-hop-invariable** command configures the device not to change the next hop of a route when advertising the route to a peer.

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

**peer** *peerGroupName* **next-hop-invariable** [ **include-static-route** | **include-unicast-route** ] \*

**undo peer** *peerGroupName* **next-hop-invariable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerGroupName* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| **include-static-route** | Configures the BGP speaker to retain the original Next\_Hop of imported static routes when advertising the routes to the peer. | - |
| **include-unicast-route** | Configures the device to retain the original Next\_Hop of unicast routes learned from peers when advertising the routes. | - |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer next-hop-invariable** command has the following functions:

* The BGP speaker does not change the next hop when advertising routes to EBGP peers.
* The BGP speaker does not change the next hop when advertising labeled routes to IBGP peers.
* When advertising imported IGP routes to IBGP peers, the BGP speaker uses the next hop addresses of the IGP routes.You can run the **peer next-hop-invariable include-static-route** command to configure a BGP speaker to use the next hop address of an imported static route when advertising the static route to an IBGP peer. If the imported static route has the original next hop address, the BGP speaker uses the original next hop address. If the original next hop address is invalid, the BGP speaker uses the interface address of the BGP speaker. For a public network static route whose next hop points to a VPN routing table or a VPN static route imported between public and private networks, the next hop is the IP address of an interface on the device.Using the **peer next-hop-invariable include-unicast-route** command, you can configure a BGP speaker not to change the next hop address when advertising unicast routes learned from other peers to EBGP peers.

**Prerequisites**

A peer group has been created using the **group** command.

**Precautions**

The **peer next-hop-invariable** command takes effect only on received routes. In the IPv6 unicast address family view, the command takes effect only on received labeled IPv6 unicast routes. If include-unicast-route is specified, the command also takes effect on unlabeled routes.If both the peer next-hop-invariable and peer next-hop-local commands are run, the latest configuration overrides the previous one.


Example
-------

# Configure a BGP speaker not to change the next hop address when advertising routes to an EBGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] ipv6-family unicast
[~HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test next-hop-invariable

```

# Configure a BGP speaker to use the next hop address of an imported static route when advertising the route to an IBGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] ipv6-family unicast
[~HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test next-hop-invariable include-static-route

```