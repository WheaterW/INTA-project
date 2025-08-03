compare-different-as-med (BGP-VPN instance IPv4 address family view)
====================================================================

compare-different-as-med (BGP-VPN instance IPv4 address family view)

Function
--------



The **compare-different-as-med** command enables BGP to compare the MEDs in the routes learned from peers in different ASs.

The **undo compare-different-as-med** command restores the default configuration.



By default, BGP does not compare the MEDs in the routes learned from peers in different ASs.


Format
------

**compare-different-as-med**

**undo compare-different-as-med**


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
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family vpn-instance vpna
[*HUAWEI-bgp-vpna] compare-different-as-med

```