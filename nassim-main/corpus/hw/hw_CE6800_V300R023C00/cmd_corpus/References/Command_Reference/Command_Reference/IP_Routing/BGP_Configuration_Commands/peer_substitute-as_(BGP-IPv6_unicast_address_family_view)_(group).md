peer substitute-as (BGP-IPv6 unicast address family view) (group)
=================================================================

peer substitute-as (BGP-IPv6 unicast address family view) (group)

Function
--------



The **peer substitute-as** command enables AS number substitution in the advertisement direction. That is, the AS number of a specified peer group in the AS\_Path attribute is replaced with the local AS number.

The **undo peer substitute-as** command disables AS number substitution.



By default, AS number substitution is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**peer** *group-name* **substitute-as**

**undo peer** *group-name* **substitute-as**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of a BGP peer group. | The value is a string of 1 to 47 case-sensitive characters and cannot contain spaces. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

In a BGP public network scenario, when two devices with the same AS number learn a BGP route from each other through the same EBGP peer, the route may be discarded because the AS\_Path attribute contains duplicate AS numbers. To prevent this problem, run the **peer substitute-as** command on this EBGP peer to enable AS number substitution in the advertisement direction.

**Prerequisites**

Enabling BGP AS number substitution may cause route loops in a CE multi-homing network. The **peer soo** command must be run to prevent a routing loop in a VPN site.On BGP public networks, if three or more BGP peers form a ring network, the **peer substitute-as** command cannot be run; otherwise, a routing loop may occur.

**Precautions**

If the **peer substitute-as** command is run, the AS number of the route is replaced, which may cause routing loops. To solve this problem, run the **peer soo** command to configure the SoO feature.


Example
-------

# Configure a device to replace the AS number of a specified peer group in the AS\_Path of a route with the local AS number.
```
<HUAWEI> system-view
[*HUAWEI] bgp 100
[*HUAWEI-bgp] group test external
[*HUAWEI-bgp] peer test as-number 200
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] peer test enable
[*HUAWEI-bgp-af-ipv6] peer test substitute-as

```