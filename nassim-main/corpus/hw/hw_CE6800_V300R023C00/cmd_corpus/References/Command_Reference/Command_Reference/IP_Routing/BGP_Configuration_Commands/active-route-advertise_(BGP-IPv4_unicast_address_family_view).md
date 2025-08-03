active-route-advertise (BGP-IPv4 unicast address family view)
=============================================================

active-route-advertise (BGP-IPv4 unicast address family view)

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

BGP-IPv4 unicast address family view


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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] active-route-advertise

```