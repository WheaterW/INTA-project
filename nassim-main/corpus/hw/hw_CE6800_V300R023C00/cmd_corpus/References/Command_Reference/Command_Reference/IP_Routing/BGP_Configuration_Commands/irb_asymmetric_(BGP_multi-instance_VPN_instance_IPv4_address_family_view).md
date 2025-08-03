irb asymmetric (BGP multi-instance VPN instance IPv4 address family view)
=========================================================================

irb asymmetric (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **irb asymmetric** command enables the asymmetric mode for IRB routes.

The **undo irb asymmetric** command restores the default configuration.



By default, the asymmetric mode is disabled for IRB routes.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**irb asymmetric** [ **route-policy** *route-policy-name* ]

**undo irb asymmetric** [ **route-policy** *route-policy-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy. After this parameter is specified, the asymmetric IRB function takes effect only for the routes to which the route-policy applies. | The name is a string of 1 to 200 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, a device generates an IP prefix route based on the IP address in an IRB route that it has received from a BGP EVPN peer. IP prefix routes can be used for Layer 3 traffic forwarding. If Layer 2 forwarding is required, run the **irb asymmetric** command to enable the asymmetric mode for IRB routes. Specifically, after this configuration is performed, the device does not generate IP prefix routes after receiving IRB routes.


Example
-------

# Enable the asymmetric mode for IRB routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100 instance a1
[*HUAWEI-bgp-instance-a1] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a1-vpna] irb asymmetric

```