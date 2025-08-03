bestroute med-plus-igp (BGP multi-instance VPN instance IPv4 address family view)
=================================================================================

bestroute med-plus-igp (BGP multi-instance VPN instance IPv4 address family view)

Function
--------



The **bestroute med-plus-igp** command configures BGP to preferentially select the route with the smallest sum of MED multiplied by a MED multiplier and IGP cost multiplied by an IGP cost multiplier when BGP needs to compare MEDs to select the optimal route.

The **undo bestroute med-plus-igp** command restores the default configuration.



By default, the MED and IGP cost of each route are used as separate route selection criteria.


Format
------

**bestroute med-plus-igp** [ **igp-multiplier** *igp-multiplier* | **med-multiplier** *med-multiplier* ] \*

**undo bestroute med-plus-igp** [ **igp-multiplier** *igp-multiplier* | **med-multiplier** *med-multiplier* ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **igp-multiplier** *igp-multiplier* | Specifies an IGP cost multiplier. | The value is an integer ranging from 1 to 1000. The default value is 1. |
| **med-multiplier** *med-multiplier* | Specifies a MED multiplier. | The value is an integer ranging from 1 to 1000. The default value is 1. |



Views
-----

BGP multi-instance VPN instance IPv4 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



By default, MED values and IGP metrics are used as separate BGP route selection criteria. After the **bestroute med-plus-igp** command is run, BGP preferentially selects the route with the smallest sum of the MED multiplied by a MED multiplier and the IGP cost multiplied by an IGP cost multiplier. If two routes have different MED values and IGP cost values and load balancing is required, you can run this command to ensure that the two routes have the same sum of the MED multiplied by a MED multiplier and the IGP cost multiplied by an IGP cost multiplier.If a route does not have an MED value, the MED value 0 is used.




Example
-------

# Enable BGP to use the sum of MED multiplied by an MED multiplier and IGP cost multiplied by an IGP cost multiplier to select routes when MED is required to determine the optimal route.
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
[*HUAWEI-bgp-instance-a-vrf1] bestroute med-plus-igp

```