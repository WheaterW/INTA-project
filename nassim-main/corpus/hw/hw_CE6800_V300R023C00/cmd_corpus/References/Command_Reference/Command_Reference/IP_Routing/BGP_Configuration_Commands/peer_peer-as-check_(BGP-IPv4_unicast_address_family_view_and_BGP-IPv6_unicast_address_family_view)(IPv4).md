peer peer-as-check (BGP-IPv4 unicast address family view/BGP-IPv6 unicast address family view)(IPv4)
====================================================================================================

peer peer-as-check (BGP-IPv4 unicast address family view/BGP-IPv6 unicast address family view)(IPv4)

Function
--------



The **peer peer-as-check** command prevents the routes received from an EBGP peer from being broadcast to other peers with the same AS number as the EBGP peer.

The **undo peer peer-as-check** command cancels the configuration.



By default, the routes received from an EBGP peer are broadcast to other EBGP peers in the same AS.


Format
------

**peer** *peerIpv4Addr* **peer-as-check**

**peer** *peerIpv4Addr* **peer-as-check** **disable**

**undo peer** *peerIpv4Addr* **peer-as-check**

**undo peer** *peerIpv4Addr* **peer-as-check** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **disable** | Disables the function. | - |



Views
-----

BGP-IPv4 unicast address family view,BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, after receiving a route from an EBGP peer in AS 200, the local device in AS 100 advertises the route to all EBGP peers in AS 200. After the **peer peer-as-check** command is run, the local device does not advertise the routes received from an EBGP peer to other EBGP peers in the same AS with this EBGP peer. This reduces BGP memory and CPU consumption and shortens route convergence time during route flapping.

**Configuration Impact**

After this command is run, the number of BGP update peer-groups on the device is affected. If the AS numbers of BGP peers configured with this function are different, these BGP peers cannot be added to the same BGP update peer-group.

**Precautions**

This command applies only to EBGP peers.


Example
-------

# Configure a device not to advertise the routes learned from an EBGP peer to a specified peer with the same AS number as this EBGP peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] peer 10.1.1.1 peer-as-check

```