ipv6 route-static frr
=====================

ipv6 route-static frr

Function
--------



The **ipv6 route-static frr** command enables FRR for IPv6 static routes.

The **undo ipv6 route-static frr** command disables FRR for IPv6 static routes.



By default, FRR is disabled for IPv6 static routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 route-static frr** [ **vpn-instance** *vpn-instance-name* ]

**undo ipv6 route-static frr** [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To protect IPv6 static routes, run the ipv6 route-static frr command to configure FRR for IPv6 static routes.If the name of a VPN instance is specified, FRR is enabled for the static routes of the VPN instance.

**Prerequisites**

A VPN instance has been configured if you want to configure FRR for the VPN.

**Configuration Impact**

Enabling or disabling FRR takes effect on all the static routes in the VPN instance.


Example
-------

# Enable FRR for the IPv6 static route.
```
<HUAWEI> system-view
[~HUAWEI] ipv6 route-static frr

```