peer peer-as-check (BGP-VPN instance IPv6 address family view)
==============================================================

peer peer-as-check (BGP-VPN instance IPv6 address family view)

Function
--------



The **peer peer-as-check** command configures a device not to advertise the routes received from an EBGP peer to other EBGP peers in the same AS with this EBGP peer.

The **undo peer peer-as-check** command restores the default configuration.



By default, the routes received from an EBGP peer are broadcast to other EBGP peers in the same AS.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



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

BGP-VPN instance IPv6 address family view


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
[~HUAWEI] ip vpn-instance a
[*HUAWEI-vpn-instance-a] ipv6-family
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance a
[*HUAWEI-bgp-instance-a] peer 10.1.1.1 as-number 200
[*HUAWEI-bgp-instance-a] quit
[*HUAWEI-bgp] ipv6-family vpn-instance a
[*HUAWEI-bgp-instance-a-6-a] peer 10.1.1.1 enable
[*HUAWEI-bgp-instance-a-6-a] peer 10.1.1.1 peer-as-check

```