as-number (BGP multi-instance VPN instance IPv4 address family view)
====================================================================

as-number (BGP multi-instance VPN instance IPv4 address family view)

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
| **no-prepend** | Indicates whether to prepend the AS number. | - |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

During network transfer or service identification, if a device needs to be simulated as multiple BGP devices logically, you can run the **as-number** command to configure an AS number for each VPN instance.After the **as-number** command is used:

* BGP peer relationships in the VPN instance are established using the configured AS number.
* The configured AS number is used to generate the aggregator attribute during route summarization.
* When advertising routes to an EBGP peer, the local device adds the AS number configured in the VPN instance in the routes.If an AS number is configured for a VPN instance, the AS\_Path attribute of the routes sent to VPNv4 carries the AS number configured for the VPN instance. If an AS number is configured for a VPN instance and no-prepend is specified after as-number, the AS\_Path attribute of the route sent to VPNv4 does not carry the VPN instance's AS number.

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
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] as-number 65001

```