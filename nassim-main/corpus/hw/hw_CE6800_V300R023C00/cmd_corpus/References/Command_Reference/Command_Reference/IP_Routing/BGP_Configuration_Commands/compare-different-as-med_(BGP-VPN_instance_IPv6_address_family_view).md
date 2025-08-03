compare-different-as-med (BGP-VPN instance IPv6 address family view)
====================================================================

compare-different-as-med (BGP-VPN instance IPv6 address family view)

Function
--------



The **compare-different-as-med** command enables BGP to compare the MEDs in the routes learned from peers in different ASs.

The **undo compare-different-as-med** command restores the default configuration.



By default, BGP does not compare the MEDs in the routes learned from peers in different ASs.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**compare-different-as-med**

**undo compare-different-as-med**


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

The command is used to change BGP route selection rules. If the **compare-different-as-med** command is run, BGP will compare the MEDs of the routes learned from peers in different ASs. If there are multiple reachable routes to the same destination, BGP prefers the route with the smallest MED.

**Configuration Impact**



After the **compare-different-as-med** command is run, the system compares the MEDs in the routes learned from peers in different ASs.



**Precautions**



Do not run the **compare-different-as-med** command unless different ASs use the same IGP and route selection mode.




Example
-------

# Enable BGP to compare the MEDs in the routes learned from peers in different ASs.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] compare-different-as-med

```