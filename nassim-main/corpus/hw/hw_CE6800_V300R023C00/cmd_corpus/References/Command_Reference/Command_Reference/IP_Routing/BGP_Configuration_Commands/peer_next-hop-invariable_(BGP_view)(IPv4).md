peer next-hop-invariable (BGP view)(IPv4)
=========================================

peer next-hop-invariable (BGP view)(IPv4)

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


Format
------

**peer** *ipv4-address* **next-hop-invariable** [ **include-static-route** | **include-unicast-route** ] \*

**undo peer** *ipv4-address* **next-hop-invariable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| **include-static-route** | Configures the device to retain the original Next\_Hop of static routes when advertising the routes to the peer. | - |



Views
-----

BGP-IPv4 unicast address family view,BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **peer next-hop-invariable** command has the following functions:

* A BGP speaker does not change the next hop of a route when advertising the route to an EBGP peer group.
* A BGP speaker does not change the next hop of a labeled route when advertising the route to an IBGP peer group.
* A BGP speaker uses the next hop address of an imported IGP route when advertising the route to an IBGP peer group.If the **peer next-hop-invariable include-static-route** command is run, the BGP speaker retains the original next hop address of an imported static route when it advertises the static route to the specified IBGP peer. However, the local interface address is used as the next hop in the following situations: (1) The imported static route is a public network static route, and its original next hop is invalid. (2) The imported static route is a public network static route, and its original next hop recurses to a VPN route. (3) The imported static route is a VPN static route and is imported from the public network instance.Using the **peer next-hop-invariable include-unicast-route** command, you can configure a BGP speaker not to change the next hop address when advertising unicast routes learned from other peers to EBGP peers.

**Prerequisites**

A peer has been created using the **peer as-number** command.

**Precautions**

The **peer next-hop-invariable** command takes effect only on received routes. In the IPv4 unicast address family view, the command takes effect only on received labeled IPv4 unicast routes. If include-unicast-route is specified, the command also takes effect on unlabeled routes.If both the peer next-hop-invariable and peer next-hop-local commands are run, the latest configuration overrides the previous one.


Example
-------

# Configure a BGP speaker to use the next hop address of an imported static route when advertising the route to an IBGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.2 as-number 100
[*HUAWEI-bgp] peer 10.1.1.2 next-hop-invariable include-static-route

```