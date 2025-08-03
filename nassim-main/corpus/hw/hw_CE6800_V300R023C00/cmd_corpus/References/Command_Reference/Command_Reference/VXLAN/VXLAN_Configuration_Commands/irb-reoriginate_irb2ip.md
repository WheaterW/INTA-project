irb-reoriginate irb2ip
======================

irb-reoriginate irb2ip

Function
--------



The **irb-reoriginate irb2ip enable** command allows IRB/IRBv6 routes to be re-generated as IP prefix routes.

The **undo irb-reoriginate irb2ip enable** command restores the default configuration.



By default, IRB/IRBv6 routes can be regenerated as ARP/ND routes only.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**irb-reoriginate irb2ip** { **enable** }

**undo irb-reoriginate irb2ip** { **enable** }


Parameters
----------

None

Views
-----

VPN instance IPv4 address family view,VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, after the route regeneration function is enabled, IRB/IRBv6 routes can be regenerated as ARP/ND routes only. To allow IRB/IRBv6 routes to be regenerated as IP prefix routes for Layer 3 forwarding, run the **irb-reoriginate irb2ip enable** command.


Example
-------

# Enable a device to regenerate IRB routes as IP prefix routes.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 1:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] irb-reoriginate irb2ip enable

```