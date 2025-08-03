active-route-advertise (BGP multi-instance VPN instance IPv4 address family view)
=================================================================================

active-route-advertise (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **active-route-advertise** command enables BGP to advertise only the selected routes in the IP routing table.

The **undo active-route-advertise** command restores the default setting.



By default, BGP advertises all selected routes in the BGP routing table to peers.


Format
------

**active-route-advertise**

**undo active-route-advertise**


Parameters
----------

None

Views
-----

BGP multi-instance VPN instance IPv4 address family view


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
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-instance-a-vpna] active-route-advertise

```