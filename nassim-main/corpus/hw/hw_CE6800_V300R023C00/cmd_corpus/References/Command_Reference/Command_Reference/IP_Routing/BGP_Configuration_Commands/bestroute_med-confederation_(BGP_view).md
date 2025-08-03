bestroute med-confederation (BGP view)
======================================

bestroute med-confederation (BGP view)

Function
--------



The **bestroute med-confederation** command enables BGP to compare the Multi Exit Discriminator (MED) values of routes in a confederation when BGP selects the optimal route.

The **undo bestroute med-confederation** command restores the default settings.



By default, BGP compares the MED values of only the routes that are learned from peers in the same AS.


Format
------

**bestroute med-confederation**

**undo bestroute med-confederation**


Parameters
----------

None

Views
-----

BGP-IPv4 unicast address family view,BGP view


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
[*HUAWEI-bgp] bestroute med-confederation

```