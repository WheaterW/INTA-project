as-number(BGP multi-instance VPN instance IPv6 address family view)
===================================================================

as-number(BGP multi-instance VPN instance IPv6 address family view)

Function
--------



The **as-number** command configures an AS number for a VPN instance.

The **undo as-number** command restores the default setting.



By default, a VPN instance uses the AS number of BGP.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**as-number** *vrf-as* [ **no-prepend** ]

**undo as-number**

**undo as-number** *vrf-as* **no-prepend**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vrf-as* | Specifies a destination AS number. | For an integral AS number, the value is an integer ranging from 1 to 4294967295.  For an AS number in dotted notation, the value is in the format of x.y, where x is an integer that ranges from 1 to 65535, and y is an integer ranging from 0 to 65535. |
| **no-prepend** | Indicates whether to prepend the AS number. | - |



Views
-----

BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During network transfer or service identification, you must simulate a device as multiple logical BGP devices. In this case, you can run the **as-number** command to configure an AS number for each VPN instance.After the **as-number** command is used:

* Peers in the VPN instance use the configured AS number to establish connections.
* The configured AS number is used to generate the aggregator attribute during route aggregation.
* When advertising routes to an EBGP (External Border Gateway Protocol) peer, the local device carries the AS number configured in the VPN instance.

If an AS number is configured for a VPN instance, the AS\_Path attribute of the routes sent to the VPNv6 routing table carries the AS number configured for the VPN instance.If as-number is configured for a VPN instance and no-prepend is specified after as-number, the AS\_Path attribute of the route sent to the VPNv6 routing table does not carry the VPN instance's AS number.

**Prerequisites**

If a BGP peer or a BGP peer group has been configured in the VPN instance, delete the configuration of the BGP peer or peer group before configuring or deleting an AS number.

**Precautions**

If a VPN instance has been configured with a separate AS number, no confederation can be configured for the VPN instance. When a confederation is configured, no separate AS number can be configured in the VPN instance.The AS number configured in the VPN instance cannot be the same as the AS number configured in the BGP view.This command cannot be configured in the YANG management mode of BGP. To configure a separate AS number for the VPN instance IPv4 address family, run the **as-number ipv4 ipv4-as** command in the BGP-VPN instance view.When a 4-byte AS number is configured for BGP, OSPF does not support automatic tag-based loop prevention.


Example
-------

# Set the independent AS number of the VPN instance named vpna to 65001.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-6-vpna] as-number 65001

```