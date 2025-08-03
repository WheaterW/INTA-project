peer advertise-large-community (BGP-VPN instance IPv6 address family view)
==========================================================================

peer advertise-large-community (BGP-VPN instance IPv6 address family view)

Function
--------



The **peer advertise-large-community** command enables a device to advertise the Large-Community attribute to a peer.

The **undo peer advertise-large-community** command cancels the configuration.



By default, a device does not advertise the Large-Community attribute to its peer.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *peerIpv4Addr* **advertise-large-community** [ **disable** ]

**undo peer** *peerIpv4Addr* **advertise-large-community** [ **disable** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *peerIpv4Addr* | Specifies an IPv4 peer address. | The value is in dotted decimal notation. |
| **disable** | Disables the Large-Community attribute from being advertised to a BGP peer. | - |



Views
-----

BGP-VPN instance IPv6 address family view


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
[*HUAWEI-bgp] vpn-instance vpna
[*HUAWEI-bgp-vpna] peer 10.1.1.1 as-number 100
[*HUAWEI-bgp-vpna] quit
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] peer 10.1.1.1 enable
[*HUAWEI-bgp-6-vpna] peer 10.1.1.1 advertise-large-community

```