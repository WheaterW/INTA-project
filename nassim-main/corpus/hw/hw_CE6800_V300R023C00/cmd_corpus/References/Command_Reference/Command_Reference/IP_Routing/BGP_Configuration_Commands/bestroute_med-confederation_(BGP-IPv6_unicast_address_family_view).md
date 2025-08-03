bestroute med-confederation (BGP-IPv6 unicast address family view)
==================================================================

bestroute med-confederation (BGP-IPv6 unicast address family view)

Function
--------



The **bestroute med-confederation** command enables BGP to compare the Multi Exit Discriminator (MED) values of routes in a confederation when BGP selects the optimal route.

The **undo bestroute med-confederation** command restores the default settings.



By default, BGP compares the MED values of only the routes that are learned from peers in the same AS.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bestroute med-confederation**

**undo bestroute med-confederation**


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

By default, BGP compares the MED values of only the routes that are learned from peers in the same AS (excluding confederation sub-ASs). To enable BGP to compare MED values of routes in a confederation when selecting the optimal route, run the **bestroute med-confederation** command.

**Configuration Impact**

After the **bestroute med-confederation** command is configured, BGP compares MED values only when AS\_Path does not contain any external AS (AS that is not in the confederation) numbers.For example, ASs 65000, 65001, 65002, and 65004 belong to the same confederation. Routes to the same destination are listed as follows:

* path1: AS\_Path=65000 65004, med=2
* path2: AS\_Path=65001 65004, med=3
* path3: AS\_Path=65002 65004, med=4
* path4: AS\_Path=65003 65004, med=1After the **bestroute med-confederation** command is run, the AS\_Path attributes of paths 1, 2, and 3 does not contain external AS numbers. Therefore, when selecting routes based on MED values, BGP compares the MED values of paths 1, 2, and 3 only. The AS\_Path of path4 contains an AS outside the confederation; therefore, its MED is not compared.

Example
-------

# Configure BGP to compare the MED values of routes only in the confederation when selecting the optimal route.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] bestroute med-confederation

```