as-number(BGP-VPN instance IPv4 address family view)
====================================================

as-number(BGP-VPN instance IPv4 address family view)

Function
--------



The **as-number** command configures an AS number for a VPN instance.

The **undo as-number** command restores the default setting.



By default, a VPN instance uses the AS number of BGP.


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

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During network migration or service identification, if a physical device needs to be logically simulated as multiple BGP devices, you can run the **as-number** command to configure a unique AS number for each VPN instance.After the **as-number** command is run:

* Peers in a VPN instance use the configured AS number to establish a connection.
* During route summarization, the configured independent AS number is used to generate the aggregator attribute.
* Routes advertised to EBGP peers carry the AS number configured in the VPN instance.

If no-prepend is not specified, the AS\_Path attributes of VPN routes sent to VPNv4 carry the configured AS number. If no-prepend is specified, the AS\_Path attributes of VPN routes sent to VPNv4 do not carry the configured AS number.

**Prerequisites**

If a BGP peer or a BGP peer group has been configured in the VPN instance, delete the configuration of the BGP peer or peer group before configuring or deleting an AS number.

**Precautions**

If a VPN instance has been configured with a separate AS number, no confederation can be configured for the VPN instance. When a confederation is configured, no separate AS number can be configured in the VPN instance.The AS number configured in the VPN instance cannot be the same as the AS number configured in the BGP view.This command cannot be configured in the YANG management mode of BGP. To configure a separate AS number for the VPN instance IPv4 address family, run the **as-number ipv4 ipv4-as** command in the BGP-VPN instance view.When a 4-byte AS number is configured for BGP, OSPF does not support automatic tag-based loop prevention.


Example
-------

# Set the AS number of the VPN instance named vpn1 to 65001.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpn1
[*HUAWEI-bgp-vpn1] as-number 65001

```