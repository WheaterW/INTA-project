peer next-hop-invariable (BGP view) (group)
===========================================

peer next-hop-invariable (BGP view) (group)

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


Format
------

**peer** *group-name* **next-hop-invariable** [ **include-static-route** | **include-unicast-route** ] \*

**undo peer** *group-name* **next-hop-invariable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **include-static-route** | Configures the device to retain the original Next\_Hop of static routes when advertising the routes to the peer. | - |
| **include-unicast-route** | Configures the device to retain the original next hop of the unicast routes learned from peers when advertising the routes. | - |



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

* The BGP speaker does not change the next hop when advertising routes to EBGP peers.
* The BGP speaker does not change the next hop when advertising labeled routes to IBGP peers.
* When advertising imported IGP routes to IBGP peers, the BGP speaker uses the next hop addresses of the IGP routes.If the **peer next-hop-invariable include-static-route** command is run, the BGP speaker retains the original next hop address of an imported public network static route when advertising the route to an IBGP peer under the condition that the original next hop address is valid; if the original next hop address of the public network static route is invalid, the next hop of the public network static route belongs to a VPN instance, or the public network static route is imported from a VPN instance, the BGP speaker uses its interface address as the next hop of the route.Using the **peer next-hop-invariable include-unicast-route** command, you can configure a BGP speaker not to change the next hop address when advertising unicast routes learned from other peers to EBGP peers.

**Prerequisites**

A peer group has been created using the **group** command.

**Precautions**

The **peer next-hop-invariable** command takes effect only on received routes. In the IPv4 unicast address family view, the command takes effect only on received labeled IPv4 unicast routes. If include-unicast-route is specified, the command also takes effect on unlabeled routes.If both the peer next-hop-invariable and peer next-hop-local commands are run, the latest configuration overrides the previous one.


Example
-------

# Configure a BGP speaker to use the next hop address of an imported static route when advertising the route to an IBGP peer group.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] peer test next-hop-invariable include-static-route

```