ipv6-family vpn-instance (BGP view)
===================================

ipv6-family vpn-instance (BGP view)

Function
--------



The **ipv6-family vpn-instance** command enables a BGP-VPN instance IPv6 address family and displays the BGP-VPN instance IPv6 address family view.

The **undo ipv6-family vpn-instance** command disables the BGP-VPN instance IPv6 address family view and deletes all configurations in the view.



By default, the IPv6 address family view of BGP is disabled.

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
| **vpn-instance** *vpn-instance-name* | Associates a specified VPN instance with the IPv6 address family. You can enter the BGP-VPN instance IPv6 address family view using the parameter. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. |



Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If no parameter is specified, the IPv6 unicast address family view is displayed by default. Similarly, if you run the **undo ipv6-family** command without specifying any parameter, the configurations of the IPv6 unicast address family are deleted.

**Configuration Impact**

The **undo ipv6-family** command with no VPN instance specified deletes all IPv6 unicast address family configurations.

**Precautions**

If the YANG management mode is enabled for BGP VPN instances using the **bgp yang-mode enable** command, the **ipv6-family vpn-instance** command can be run only after a VPN instance is created.If the YANG management mode is disabled for BGP VPN instances, running the **ipv6-family vpn-instance** command does not depend on the creation of VPN instances.


Example
-------

# Enter the BGP VPN instance IPv6 address family view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna]

```