peer discard-ext-community(BGP-VPN instance IPv6 address family view)(IPv4)
===========================================================================

peer discard-ext-community(BGP-VPN instance IPv6 address family view)(IPv4)

Function
--------



The **peer discard-ext-community** command configures a BGP device to discard the extended community attributes carried by routes received from a specified peer.

The **undo peer discard-ext-community** command cancels the configuration.



By default, the extended community attributes in the routing information of peers are not discarded.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv4-address* **discard-ext-community**

**undo peer** *ipv4-address* **discard-ext-community**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |



Views
-----

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a peer only needs to accepts routes but not extended community attributes, you can run this command on the peer to discard the extended community attributes from the received routes.


Example
-------

# Configure a BGP device to discard the extended community attribute carried by a route.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpna
[*HUAWEI-bgp-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpna] quit
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 10.1.1.1 enable
[*HUAWEI-bgp-6-vpna] peer 10.1.1.1 discard-ext-community

```