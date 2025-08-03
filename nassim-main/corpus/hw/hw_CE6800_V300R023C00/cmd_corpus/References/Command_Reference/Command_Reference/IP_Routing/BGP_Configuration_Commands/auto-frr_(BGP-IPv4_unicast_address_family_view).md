auto-frr (BGP-IPv4 unicast address family view)
===============================================

auto-frr (BGP-IPv4 unicast address family view)

Function
--------



The **auto-frr** command enables BGP Auto fast reroute (FRR).

The **undo auto-frr** command restores the default configuration.



By default, BGP Auto FRR is disabled.


Format
------

**auto-frr**

**undo auto-frr**


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

With the development of networks, voice, online video, and finance services have higher requirements on real-time performance. Generally, primary and backup links are used to ensure service stability during network deployment. In traditional forwarding mode, when there are multiple routes to the same destination network, the device always selects the optimal route and delivers it to the FIB table to guide data forwarding. If the optimal route fails, services can be restored only after route convergence is complete, a new optimal route is selected, and this optimal route is delivered to the FIB table. During this process, services are interrupted for a long time, which cannot meet service requirements.After BGP Auto FRR is enabled, the device selects the optimal route from multiple routes to the same destination network and automatically adds information about the suboptimal route as the backup forwarding entry of the optimal route. When the primary link fails, the system quickly switches traffic to the backup link. This process does not depend on route convergence. Therefore, the service interruption time is very short and can reach the subsecond level. For labeled BGP routes, FRR is supported only on the ingress and transit nodes.


Example
-------

# Enable BGP Auto FRR for unicast routes.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] auto-frr

```