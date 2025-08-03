alarm-threshold route vpn-instance
==================================

alarm-threshold route vpn-instance

Function
--------



The **alarm-threshold route vpn-instance** command sets a threshold and log recovery percentage for the number of routes in a VPN instance.

The **undo alarm-threshold route vpn-instance** command cancels the settings.



By default, the threshold and log recovery percentage for the number of routes in an L3VPN instance are not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**alarm-threshold route** *route-number* [ **recovery-percentage** *percentage* ] { **ipv4** | **ipv6** } **vpn-instance** *vpn-instance-name*

**undo alarm-threshold route** *route-number* [ **recovery-percentage** *percentage* ] { **ipv4** | **ipv6** } **vpn-instance** *vpn-instance-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *route-number* | Specifies the threshold for the number of routes. | The value is an integer ranging from 1 to 4294967295. |
| **recovery-percentage** *percentage* | Specifies the log recovery percentage. | The value is an integer ranging from 1 to 95. After the threshold for the number of routes is set, the log recovery percentage is 80 by default. |
| **ipv4** | Specifies the VPN instance IPv4 address family. | - |
| **ipv6** | Specifies the VPN instance IPv6 address family. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

As the number of access hosts increases, routes stored control plane increase greatly, consuming a lot of memory resources. To better monitor the impact of an increase in route quantity on memory and prevent device restart caused by memory insufficiency, run the **alarm-threshold route vpn-instance** command to set a threshold for the number of routes by VPN instance. When the number of routes exceeds the threshold, a user log will be generated. When the number of routes equals the log recovery percentage, a recovery log will be generated.


Example
-------

# Set a threshold and log recovery percentage for the number of routes in a VPN instance.
```
<HUAWEI> system-view
[~HUAWEI] alarm-threshold route 10000 recovery-percentage 90 ipv4 vpn-instance vrf1

```