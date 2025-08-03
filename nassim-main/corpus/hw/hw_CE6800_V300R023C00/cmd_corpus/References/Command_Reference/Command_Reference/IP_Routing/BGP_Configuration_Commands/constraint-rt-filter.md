constraint-rt-filter
====================

constraint-rt-filter

Function
--------



The **constraint-rt-filter enable** command enables a route target (RT) filter to guide EVPN route advertisement.

The **undo constraint-rt-filter** command restores the default configuration.



By default, the RT filter is enabled in the BGP-VPN-Target address family.


Format
------

**constraint-rt-filter** { **enable** | **disable** }

**undo constraint-rt-filter**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **enable** | Enables the RT filter. | - |
| **disable** | Disables the RT filter. | - |



Views
-----

BGP-VPN-target address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In a VPN ORF scenario, after an RT filter is enabled in the BGP-VPN-Target address family view, a BGP peer filters EVPN routes to be sent based on the import target (IRT) of the peer. After the RT filter is disabled, routes are no longer filtered based on the peer IRT.In the RR scenario, only VPN target routes need to be forwarded, and RT filters do not need to be enabled to guide route advertisement. After the RT filter is disabled in the RR scenario, BGP peers directly forward VPN target routes without guiding route advertisement. This reduces the burden on the RR and speeds up route convergence.




Example
-------

# Enable the RT filter.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[~HUAWEI-bgp] ipv4-family vpn-target
[~HUAWEI-bgp-af-vpn-target] constraint-rt-filter enable

```