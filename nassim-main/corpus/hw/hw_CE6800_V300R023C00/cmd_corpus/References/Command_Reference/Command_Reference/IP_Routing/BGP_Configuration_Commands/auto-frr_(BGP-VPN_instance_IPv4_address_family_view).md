auto-frr (BGP-VPN instance IPv4 address family view)
====================================================

auto-frr (BGP-VPN instance IPv4 address family view)

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

BGP-VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

As networks evolve continuously, voice, on-line video, and financial services raise increasingly high requirements for real-time performance. Usually, primary and backup links are deployed on a network to ensure the stability of these services. In a traditional forwarding mode, a device selects a route out of several routes that are bound for the same destination network as the optimal route and delivers the route to the FIB table to guide data forwarding. If the optimal route fails, a device has to wait for route convergence to be completed before reselecting an optimal route. During this period, services are interrupted. After a device delivers the reselected optimal route to the FIB table, services are restored. Service interruption in this mode lasts a long time, which cannot meet services' requirements.After BGP Auto FRR is enabled on a device, the device selects the optimal route from the routes that are bound for the same destination network. In addition, a device automatically adds information about the second optimal route to the backup forwarding entries of the optimal route. If the primary link fails, a device quickly switches traffic to the backup link. The switchover does not depend on route convergence. Therefore, the service interruption time is very short, reaching the sub-second level.

**Precautions**

It is recommended that this function be used together with BFD so that link faults can be quickly detected and services can be quickly switched to the backup link.If both the ip frr and **auto-frr** commands are run, the **auto-frr** command takes precedence over the **ip frr** command.


Example
-------

# Enable BGP Auto FRR in the BGP-VPN instance IPv4 address family view.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] auto-frr

```