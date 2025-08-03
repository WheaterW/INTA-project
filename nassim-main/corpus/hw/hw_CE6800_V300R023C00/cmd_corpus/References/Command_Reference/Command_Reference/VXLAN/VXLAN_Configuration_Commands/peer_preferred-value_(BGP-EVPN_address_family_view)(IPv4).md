peer preferred-value (BGP-EVPN address family view)(IPv4)
=========================================================

peer preferred-value (BGP-EVPN address family view)(IPv4)

Function
--------



The **peer preferred-value** command sets a preferred value for the routes that a BGP device learns from its peer.

The **undo peer preferred-value** command deletes the preferred value set for the routes that a BGP device learns from its peer.



By default, the preferred value of a route learned from a BGP peer is 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv4Addr* **preferred-value** *preferredvalue*

**undo peer** *peerIpv4Addr* **preferred-value**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a peer. | It is in dotted decimal notation. |
| *preferredvalue* | Specifies the preferred value of the routes that a BGP device learns from its peer. | The value is an integer ranging from 0 to 65535. |



Views
-----

BGP-EVPN address family view,bgp-muli-instance-af-evpn view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a preferred value is configured for a peer, all the routes learned from the peer have the preferred value. If multiple routes with the same prefix are available, the route with the largest preferred value is preferred.

**Prerequisites**

A BGP peer has been configured. If the peer preferred-value command is used but no BGP peer exists, a message is displayed, indicating that the peer does not exist.

**Configuration Impact**

If a preferred value is set for the routes that a device learns from a peer group, all members of the peer group inherit the configuration.


Example
-------

# In the BGP-EVPN address family view, set a preferred value to 50 for the routes that a BGP device learns from a specified peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 1.1.1.2 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 1.1.1.2 enable
[*HUAWEI-bgp-af-evpn] peer 1.1.1.2 preferred-value 50

```