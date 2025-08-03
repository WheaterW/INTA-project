ipv6-family vpn-instance (BGP multi-instance view)
==================================================

ipv6-family vpn-instance (BGP multi-instance view)

Function
--------



The **ipv6-family vpn-instance** command enables and enters the IPv6 address family view of BGP multi-instance VPN instance.

The **undo ipv6-family vpn-instance** command disables the IPv6 address family view of BGP multi-instance VPN instance and deletes the configurations in the view.



By default, the IPv6 address family view of BGP multi-instance VPN instance is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6-family vpn-instance** *vpn-instance-name*

**undo ipv6-family vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Associates a specified VPN instance with the IPv6 address family. You can enter the IPv6 address family view of BGP multi-instance VPN instance using the parameter. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP multi-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

Before performing configurations in the BGP multi-instance VPN instance IPv6 address family view, you must run the **ipv6-family vpn-instance** command in the BGP multi-instance view to enable the BGP multi-instance VPN instance IPv6 address family view and enter the address family view.


Example
-------

# Enter the IPv6 address family view of BGP multi-instance VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] vpn-target 100:1 both
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-instance-a-6-vpn1]

```