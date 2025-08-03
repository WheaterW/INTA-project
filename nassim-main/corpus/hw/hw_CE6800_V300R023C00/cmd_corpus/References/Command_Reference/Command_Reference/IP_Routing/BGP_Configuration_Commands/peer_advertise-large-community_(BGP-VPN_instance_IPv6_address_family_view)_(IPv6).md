peer advertise-large-community (BGP-VPN instance IPv6 address family view) (IPv6)
=================================================================================

peer advertise-large-community (BGP-VPN instance IPv6 address family view) (IPv6)

Function
--------



The **peer advertise-large-community** command enables a device to advertise the Large-Community attribute to a peer.

The **undo peer advertise-large-community** command cancels the configuration.



By default, a device does not advertise the Large-Community attribute to its peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv6Addr* **advertise-large-community** [ **disable** ]

**undo peer** *peerIpv6Addr* **advertise-large-community** [ **disable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv6Addr* | Specifies the IPv6 address of a peer. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X |
| **disable** | Disables the Large-Community attribute from being advertised to a BGP peer. | - |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable a device to advertise the Large-Community attribute to its BGP peer or peer group, run the **peer advertise-large-community** command. If the Large-Community attribute is advertised to a peer group, all the peer members in the group inherit this configuration. This simplifies the application of route-policies and facilitates route maintenance and management.

**Prerequisites**

Specific Large-Community values have been defined in a route-policy.


Example
-------

# Enable a device to advertise the Large-Community attribute to a BGP peer.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 as-number 100
[*HUAWEI-bgp-6-vpna] peer 2001:DB8:1::1 advertise-large-community

```