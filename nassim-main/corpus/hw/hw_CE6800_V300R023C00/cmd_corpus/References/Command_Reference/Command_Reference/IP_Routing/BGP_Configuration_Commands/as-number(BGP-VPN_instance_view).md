as-number(BGP-VPN instance view)
================================

as-number(BGP-VPN instance view)

Function
--------



The **as-number ipv4** command configures an independent AS number for an IPv4 peer of a VPN instance.

The **undo as-number ipv4** command restores the default configuration.

The **as-number ipv6** command configures an independent AS number for an IPv6 peer of a VPN instance.

The **undo as-number ipv6** command restores the default configuration.



By default, a VPN instance uses the AS number of BGP.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**as-number ipv4** *ipv4-as* [ **no-prepend** ]

**undo as-number ipv4** *ipv4-as* [ **no-prepend** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**as-number ipv6** *ipv6-as* [ **no-prepend** ]

**undo as-number ipv6** *ipv6-as* [ **no-prepend** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv6-as* | Specifies the AS number of an IPv6 peer.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x is an integer that ranges from 1 to 65535, and y is an integer ranging from 0 to 65535. |
| *ipv4-as* | Specifies the AS number of an IPv4 peer. | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x is an integer that ranges from 1 to 65535, and y is an integer ranging from 0 to 65535. |
| **no-prepend** | Indicates whether the AS number is prepended. | - |



Views
-----

BGP-VPN instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During network transfer or service identification in a scenario where the YANG management mode is enabled for BGP VPN instances, if a physical device needs to be simulated as multiple logical BGP devices, you can run the as-number { ipv4 | ipv6 } command to configure a different AS number for each VPN instance.After this command is run:

* Peers in the VPN instance use the configured AS number to establish connections.
* During route summarization, the configured AS number is used to generate the aggregator attribute.
* When routes are advertised to EBGP peers, they carry the AS number configured in the VPN instance.

If an AS number is configured for a VPN instance, the AS\_Path attribute of the route sent to VPNv4/VPNv6/EVPN carries the AS number configured for the VPN instance.If an AS number is configured for a VPN instance and no-prepend is specified after as-number, the AS\_Path attribute of routes sent to VPNv4/VPNv6/EVPN does not carry the VPN instance's AS number.

**Prerequisites**

If a BGP peer or a BGP peer group has been configured in the VPN instance, delete the configuration of the BGP peer or peer group before configuring or deleting an AS number.

**Precautions**

1. If a VPN instance has been configured with a separate AS number, no confederation can be configured. When configuring a confederation, you cannot configure a separate AS number in the VPN instance.
2. The AS number configured in the VPN instance cannot be the same as the AS number configured in the BGP view.
3. The AS number of a BGP VPN instance address family cannot coexist with the AS number of a BGP VPN instance.
4. If a peer or group exists, the AS number of the BGP VPN instance cannot be modified.
5. After an AS number is configured for a BGP VPN instance, the peer in the BGP VPN instance view can be enabled only in the VPN IPv4 address family and VPN IPv6 address family.
6. When a 4-byte AS number is configured for BGP, OSPF does not support automatic tag-based loop prevention.

Example
-------

# Set the independent AS number of the VPN instance named vpna to 65001.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] route-distinguisher 1:4
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 10:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] vpn-instance vpna
[*HUAWEI-bgp-instance-vpna] as-number ipv4 65001
[*HUAWEI-bgp-instance-vpna] as-number ipv6 65001

```