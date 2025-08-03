peer peer-as-check (BGP-IPv4 unicast address family view/BGP-IPv6 unicast address family view)(IPv6)
====================================================================================================

peer peer-as-check (BGP-IPv4 unicast address family view/BGP-IPv6 unicast address family view)(IPv6)

Function
--------



The **peer peer-as-check** command prevents the routes received from an EBGP peer from being broadcast to other peers with the same AS number as the EBGP peer.

The **undo peer peer-as-check** command cancels the configuration.



By default, the routes received from an EBGP peer are broadcast to other EBGP peers in the same AS.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **peer-as-check**

**peer** *peerIpv6Addr* **peer-as-check** **disable**

**undo peer** *peerIpv6Addr* **peer-as-check**

**undo peer** *peerIpv6Addr* **peer-as-check** **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
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
[*HUAWEI-bgp] peer 2001:db8:1::1 as-number 200
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer 2001:db8:1::1 enable
[*HUAWEI-bgp-af-ipv6] peer 2001:db8:1::1 peer-as-check

```