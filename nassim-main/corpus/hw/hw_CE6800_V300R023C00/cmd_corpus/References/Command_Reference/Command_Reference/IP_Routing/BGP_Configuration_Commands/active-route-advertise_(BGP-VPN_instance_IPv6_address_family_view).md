active-route-advertise (BGP-VPN instance IPv6 address family view)
==================================================================

active-route-advertise (BGP-VPN instance IPv6 address family view)

Function
--------



The **active-route-advertise** command enables BGP to advertise only the selected routes in the IP routing table.

The **undo active-route-advertise** command restores the default setting.



By default, BGP advertises all selected routes in the BGP routing table to peers.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**active-route-advertise**

**undo active-route-advertise**


Parameters
----------

None

Views
-----

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, BGP advertises all selected routes in the BGP routing table to peers. After the active-route-advertise command is configured, only the routes selected by BGP and also active at the routing management layer are advertised to peers.

**Precautions**



The active-route-advertise and **routing-table rib-only** commands are mutually exclusive.




Example
-------

# Enable BGP to advertise only the selected routes in the IP routing table to peers.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] active-route-advertise

```