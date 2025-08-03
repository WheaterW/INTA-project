as-number (BGP-VPN instance IPv6 address family view)
=====================================================

as-number (BGP-VPN instance IPv6 address family view)

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
| **no-prepend** | Indicates whether the AS number is prepended. | - |



Views
-----

BGP-VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During network migration or service identification, if a physical device needs to be logically simulated as multiple BGP devices, you can run the **as-number** command to configure a unique AS number for each VPN instance.After the **as-number** command is run:

* Peers in a VPN instance use the configured AS number to establish a connection.
* During route summarization, the configured AS number is used to generate the aggregator attribute.
* Routes advertised to EBGP peers carry the AS number configured in the VPN instance.

If as-number is configured for a VPN instance, the AS\_Path attribute of the route to be sent to the VPNv6 routing table carries as-number configured for the VPN instance.If as-number is configured for a VPN instance and no-prepend is specified after as-number, the AS\_Path attribute of the route to be sent to the VPNv6 routing table does not carry as-number configured for the VPN instance.If no-prepend is not specified, the AS\_Path attributes of VPN routes to be sent to VPNv6 carry the configured AS numbers. If no-prepend is specified, the AS\_Path attributes of VPN routes to be sent to VPNv6 do not carry the configured AS numbers.

**Prerequisites**

If a BGP peer or a BGP peer group has been configured in the VPN instance, delete the configuration of the BGP peer or peer group before configuring or deleting an AS number.

**Precautions**

If a VPN instance has been configured with a separate AS number, no confederation can be configured for the VPN instance. When a confederation is configured, no separate AS number can be configured in the VPN instance.The AS number configured in the VPN instance cannot be the same as the AS number configured in the BGP view.When a 4-byte AS number is configured for BGP, OSPF does not support automatic tag-based loop prevention.


Example
-------

# Set the independent AS number of the VPN instance named vpna to 65001.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] as-number 65001

```