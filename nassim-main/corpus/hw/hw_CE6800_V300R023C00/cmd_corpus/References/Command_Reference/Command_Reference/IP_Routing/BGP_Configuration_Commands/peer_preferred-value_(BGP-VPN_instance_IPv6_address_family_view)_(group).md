peer preferred-value (BGP-VPN instance IPv6 address family view) (group)
========================================================================

peer preferred-value (BGP-VPN instance IPv6 address family view) (group)

Function
--------



The **peer preferred-value** command sets a preferred value for the peer group.

The **undo peer preferred-value** command deletes the preferred value set for the peer group.



By default, the preferred value of the routes learned from other BGP peer groups is 0.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **preferred-value** *preferredvalue*

**undo peer** *group-name* **preferred-value**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a peer group. | The name is a string of 1 to 47 case-sensitive characters, with spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. |
| *preferredvalue* | Specifies the preferred value for routes. | The value is an integer ranging from 0 to 65535. |



Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a preferred value is configured for a peer group, all the routes learned from the peer group have the preferred value. If multiple routes with the same prefix are available, the route with the largest preferred value is preferred.

**Prerequisites**

A BGP peer group must be configured before the preferred value is assigned to the peer group. If you run this command for a peer group that does not exist, the system displays a message indicating that the peer group does not exist.

**Configuration Impact**

If a preferred value is set for the routes that a BGP device learns from a peer group, all members of the peer group inherit the configuration.


Example
-------

# Set the preferred value of the routes received from a specified peer group to 50.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv6-family
[*HUAWEI-vpn-instance-vpn1-af-ipv6] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn1-af-ipv6] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpn1
[*HUAWEI-bgp-6-vpn1] group test external
[*HUAWEI-bgp-6-vpn1] peer test as-number 200
[*HUAWEI-bgp-6-vpn1] peer test preferred-value 50

```