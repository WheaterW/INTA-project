bestroute med-plus-igp (BGP-VPN instance IPv6 address family view)
==================================================================

bestroute med-plus-igp (BGP-VPN instance IPv6 address family view)

Function
--------



The **bestroute med-plus-igp** command configures BGP to preferentially select the route with the smallest sum of MED multiplied by a MED multiplier and IGP cost multiplied by an IGP cost multiplier when BGP needs to compare MEDs to select the optimal route.

The **undo bestroute med-plus-igp** command restores the default configuration.



By default, the MED and IGP cost of each route are used as separate route selection criteria.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



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

BGP-VPN instance IPv6 address family view,BGP multi-instance VPN instance IPv6 address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, MED values and IGP metrics are used as separate BGP route selection criteria. After the **bestroute med-plus-igp** command is run, BGP preferentially selects the route with the smallest sum of the MED multiplied by a MED multiplier and the IGP cost multiplied by an IGP cost multiplier. If two routes have different MED values and IGP cost values and load balancing is required, you can run this command to ensure that the two routes have the same sum of the MED multiplied by a MED multiplier and the IGP cost multiplied by an IGP cost multiplier.If a route does not have an MED value, the MED value 0 is used.


Example
-------

# Enable BGP to use the sum of MED multiplied by an MED multiplier and IGP cost multiplied by an IGP cost multiplier to select routes when MED is required to determine the optimal route.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpna
[*HUAWEI-vpn-instance-vpna] ipv6-family
[*HUAWEI-vpn-instance-vpna-af-ipv6] quit
[*HUAWEI-vpn-instance-vpna] quit
[*HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family vpn-instance vpna
[*HUAWEI-bgp-6-vpna] bestroute med-plus-igp

```