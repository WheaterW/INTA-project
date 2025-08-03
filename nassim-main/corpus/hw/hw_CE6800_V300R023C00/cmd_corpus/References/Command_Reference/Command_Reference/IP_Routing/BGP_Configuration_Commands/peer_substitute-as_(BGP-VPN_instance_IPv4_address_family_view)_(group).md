peer substitute-as (BGP-VPN instance IPv4 address family view) (group)
======================================================================

peer substitute-as (BGP-VPN instance IPv4 address family view) (group)

Function
--------



The **peer substitute-as** command enables AS number substitution in the advertisement direction. That is, the AS number of a specified peer group in the AS\_Path attribute is replaced with the local AS number.

The **undo peer substitute-as** command disables AS number substitution.



By default, AS number substitution is disabled.


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

BGP-VPN instance IPv4 address family view


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
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpn-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] group test external
[*HUAWEI-bgp-vpna] peer test substitute-as

```