pim ipv6 vpn-instance
=====================

pim ipv6 vpn-instance

Function
--------



The **pim ipv6 vpn-instance** command enables IPv6 PIM and displays the IPv6 PIM VPN instance view.

The **undo pim ipv6 vpn-instance** command deletes all configurations in the IPv6 PIM VPN instance view.



By default, IPv6 PIM is not enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**pim ipv6 vpn-instance** *vpn-instance-name*

**undo pim ipv6 vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot be \_public\_. If spaces are used, the string must be enclosed in double quotation marks (" "). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Global parameters related to IPv6 PIM must be configured in the IPv6 PIM view.

**Prerequisites**

The **multicast ipv6 routing-enable** command is run in the vpn instance view.

**Configuration Impact**

Running the **undo pim ipv6 vpn-instance** command interrupts IPv6 PIM VPN services. Therefore, exercise caution when running this command.


Example
-------

# Enter the IPv6 PIM VPN-instance view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance abc
[*HUAWEI-vpn-instance-abc] ipv6-family
[*HUAWEI-vpn-instance-abc-af-ipv6] route-distinguisher 1003:1
[*HUAWEI-vpn-instance-abc-af-ipv6] multicast ipv6 routing-enable
[*HUAWEI-vpn-instance-abc-af-ipv6] quit
[*HUAWEI-vpn-instance-abc] quit
[*HUAWEI] pim ipv6 vpn-instance abc

```