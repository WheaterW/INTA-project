auto-frr (BGP-IPv6 unicast address family view)
===============================================

auto-frr (BGP-IPv6 unicast address family view)

Function
--------



The **auto-frr** command enables BGP Auto fast reroute (FRR).

The **undo auto-frr** command restores the default configuration.



By default, BGP Auto FRR is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**auto-frr**

**undo auto-frr**


Parameters
----------

None

Views
-----

BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

As networks evolve continuously, voice, on-line video, and financial services raise increasingly high requirements for real-time performance. Usually, primary and backup links are deployed on a network to ensure the stability of these services. In a traditional forwarding mode, a device selects a route out of several routes that are bound for the same destination network as the optimal route and delivers the route to the FIB table to guide data forwarding. If the optimal route fails, a device has to wait for route convergence to be completed before reselecting an optimal route. During this period, services are interrupted. After a device delivers the reselected optimal route to the FIB table, services are restored. Service interruption in this mode lasts a long time, which cannot meet services' requirements.After BGP Auto FRR is enabled on a device, the device selects the optimal route from the routes that are bound for the same destination network. In addition, a device automatically adds information about the second optimal route to the backup forwarding entries of the optimal route. If the primary link fails, a device quickly switches traffic to the backup link. The switchover does not depend on route convergence. Therefore, the service interruption time is very short, reaching the sub-second level.


Example
-------

# Enable Auto FRR in the BGP-IPv6 unicast address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] auto-frr

```