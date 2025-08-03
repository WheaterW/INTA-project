bestroute as-path-ignore (BGP multi-instance VPN instance IPv4 address family view)
===================================================================================

bestroute as-path-ignore (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **bestroute as-path-ignore** command configures BGP to ignore the AS\_Path attribute when it selects the optimal route.

The **undo bestroute as-path-ignore** command restores the default configuration.



By default, BGP uses the AS\_Path attribute as one of route selection rules.


Format
------

**bestroute as-path-ignore**

**undo bestroute as-path-ignore**


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



After the **bestroute as-path-ignore** command is used, BGP does not compare the AS path attributes of routes (including the AS\_Path length and content).



**Configuration Impact**



If the **bestroute as-path-ignore** command is run, the AS\_Path attribute is not used as a BGP route selection rule, which may affect the route selection result. Therefore, exercise caution when running this command.




Example
-------

# Configure BGP to ignore the AS\_Path attribute when selecting the optimal route.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv4-family
[*HUAWEI-vpn-instance-vpna-af-ipv4] route-distinguisher 100:1
[*HUAWEI-vpn-instance-vpna-af-ipv4] vpn-target 111:1 both
[*HUAWEI-vpn-instance-vpna-af-ipv4] quit
[*HUAWEI-instance-vpna] quit
[*HUAWEI] bgp 100 instance a
[*HUAWEI-bgp-instance-a] ipv4-family vpn-instance vrf1
[*HUAWEI-bgp-instance-a-vrf1] bestroute as-path-ignore

```