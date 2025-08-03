peer preferred-value (BGP-VPN instance IPv6 address family view) (IPv6)
=======================================================================

peer preferred-value (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer preferred-value** command sets a preferred value for the routes that a BGP device learns from its peer.

The **undo peer preferred-value** command deletes the preferred value set for the routes that a BGP device learns from its peer.



By default, the preferred value of a route learned from a BGP peer is 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **preferred-value** *preferredvalue*

**undo peer** *ipv6-address* **preferred-value**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |
| *preferredvalue* | Specifies the preferred value for routes. | The value is an integer in the range from 0 to 65535. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


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

If a preferred value is set for the routes that a BGP device learns from a peer group, all members of the peer group inherit the configuration.


Example
-------

# Set the preferred value of a route received from a specified peer to 50.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 200
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 preferred-value 50

```