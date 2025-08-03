peer preferred-value (BGP-VPN-Target address family view)
=========================================================

peer preferred-value (BGP-VPN-Target address family view)

Function
--------



The **peer preferred-value** command sets a preferred value for the routes that a BGP device learns from its peer.

The **undo peer preferred-value** command deletes the preferred value set for the routes that a BGP device learns from its peer.



By default, the preferred value of a route learned from a BGP peer is 0.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**peer** { *ipv4-address* | *ipv6-address* } **preferred-value** *preferredvalue*

**undo peer** { *ipv4-address* | *ipv6-address* } **preferred-value**

For CE6885-LL (low latency mode):

**peer** *ipv4-address* **preferred-value** *preferredvalue*

**undo peer** *ipv4-address* **preferred-value**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a peer. | The value is in dotted decimal notation. |
| *ipv6-address* | Specifies an IPv6 peer address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| *preferredvalue* | Specifies the preferred value of the routes that a BGP device learns from its peer. | The value is an integer ranging from 0 to 65535. |



Views
-----

BGP-VPN-target address family view


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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] peer 10.2.2.2 as-number 200
[*HUAWEI-bgp] ipv4-family vpn-target
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 enable
[*HUAWEI-bgp-af-vpn-target] peer 10.2.2.2 preferred-value 50

```