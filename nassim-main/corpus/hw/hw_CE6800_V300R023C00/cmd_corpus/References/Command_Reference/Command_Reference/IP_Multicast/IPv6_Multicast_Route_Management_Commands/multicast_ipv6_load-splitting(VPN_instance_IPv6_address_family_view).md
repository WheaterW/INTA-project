multicast ipv6 load-splitting(VPN instance IPv6 address family view)
====================================================================

multicast ipv6 load-splitting(VPN instance IPv6 address family view)

Function
--------



The **multicast ipv6 load-splitting** command configures an IPv6 multicast load splitting policy.

The **undo multicast ipv6 load-splitting** command restores the default configuration.



By default, no IPv6 multicast load splitting policy is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**multicast ipv6 load-splitting** { **group** | **source** | **source-group** | **stable-preferred** | **balance-ucmp** }

**undo multicast ipv6 load-splitting**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **group** | Indicates group address-based load splitting. This policy applies to the scenario where one multicast source has multiple multicast groups. | - |
| **source** | Indicates source address-based load splitting. This policy applies to the scenario where one multicast group has multiple multicast sources. | - |
| **source-group** | Indicates source and group addresses-based load splitting, which is applicable to the scenario of multiple sources to multiple groups. | - |
| **stable-preferred** | Indicates stable-preferred load splitting, which is applicable to a stable multicast networking. | - |
| **balance-ucmp** | Indicates link bandwidth-based load splitting. This policy is applicable to the scenario in which links have different bandwidth. | - |



Views
-----

VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If multiple IPv6 equal-cost routes exist on a network, run the **multicast ipv6 load-splitting** command to realize load splitting among these routes. The Router selects equal-cost routes from unicast, MBGP, MIGP, and multicast static routing tables, and determines the routing table for creating multicast routing entries based on the mask lengths and preferences of routes. The Router supports IPv6 load splitting among the routes in only one routing table.


Example
-------

# In the IPv6 VPN instance, configure stable-preferred IPv6 multicast load splitting.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance abcde
[*HUAWEI-vpn-instance-abcde] ipv6-family
[*HUAWEI-vpn-instance-abcde-af-ipv6] route-distinguisher 200:200
[*HUAWEI-vpn-instance-abcde-af-ipv6] multicast ipv6 routing-enable
[*HUAWEI-vpn-instance-abcde-af-ipv6] multicast ipv6 load-splitting stable-preferred

```