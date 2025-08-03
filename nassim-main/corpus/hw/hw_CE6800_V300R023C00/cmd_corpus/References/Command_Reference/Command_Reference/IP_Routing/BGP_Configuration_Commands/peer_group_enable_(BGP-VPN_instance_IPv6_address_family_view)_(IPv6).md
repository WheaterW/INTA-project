peer group enable (BGP-VPN instance IPv6 address family view) (IPv6)
====================================================================

peer group enable (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer group enable** command enables a peer to be added to a peer group in the BGP VPN instance address family.

The **undo peer group enable** command disables a peer from being added to a peer group in the BGP VPN instance address family.



By default, a peer is disabled from being added to a peer group in the BGP VPN instance address family.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *ipv6-address* **group** *group-name* **enable**

**undo peer** *ipv6-address* **group** *group-name* **enable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-address* | Specifies an IPv6 peer address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A large number of BGP peers may exist on a large-scale BGP network. Among these BGP peers, many of them may use the same policies and have the same command configurations. In this situation, you can use peer groups to simplify configurations. Specifically, when configuring multiple peers in the same way, you can create and configure a peer group, and add multiple peers to the peer group. Then, all peers in the peer group will inherit the configurations of the peer group. The **peer group enable** command enables a peer to be added to a peer group in the BGP VPN instance address family. After being added to a peer group, a peer automatically inherits the configurations of the peer group.


Example
-------

# Create an IBGP peer group named test and add a peer to the peer group.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpn1
[*HUAWEI-bgp-instance-vpn1] group test internal
[*HUAWEI-bgp-instance-vpn1] peer 2001:DB8:1::1 group test
[*HUAWEI-bgp-instance-vpn1] quit
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] peer test enable
[*HUAWEI-bgp-6-vpn1] peer 2001:DB8:1::1 group test enable

```