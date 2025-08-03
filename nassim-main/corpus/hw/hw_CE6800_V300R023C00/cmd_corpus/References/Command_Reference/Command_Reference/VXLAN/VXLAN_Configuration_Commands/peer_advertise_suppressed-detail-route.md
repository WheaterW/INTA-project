peer advertise suppressed-detail-route
======================================

peer advertise suppressed-detail-route

Function
--------



The **peer advertise suppressed-detail-route** command enables the advertisement of locally suppressed specific routes to peers in a specified BGP EVPN peer.

The **undo peer advertise suppressed-detail-route** command restores the default configuration.



By default, the locally suppressed specific routes are not advertised to peers in a specified BGP EVPN peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv4Addr* **advertise** **suppressed-detail-route**

**undo peer** *peerIpv4Addr* **advertise** **suppressed-detail-route**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies the IPv4 address of a BGP EVPN peer. | The value is in dotted decimal notation. |



Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Generally, route summarization is configured to control the scale of BGP routing tables. If route summarization is configured for a BGP-VPN instance address family, the locally suppressed specific routes are by default not advertised to BGP EVPN peers. To enable the advertisement of specific routes to a specified BGP EVPN peer, run the peer advertise suppressed-detail-route command.

**Prerequisites**

The specified peer has been enabled in the BGP-EVPN address family view.

**Precautions**

The priority of the peer configuration method is higher than the priorities of the global configuration method and peer group configuration method.


Example
-------

# Enable the advertisement of locally suppressed specific routes to a specified BGP EVPN peer.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.1.1.9 as-number 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] peer 10.1.1.9 enable
[*HUAWEI-bgp-af-evpn] peer 10.1.1.9 advertise suppressed-detail-route

```