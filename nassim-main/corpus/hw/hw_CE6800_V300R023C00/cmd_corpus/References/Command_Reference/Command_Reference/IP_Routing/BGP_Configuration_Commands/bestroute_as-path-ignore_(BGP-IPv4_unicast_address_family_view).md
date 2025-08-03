bestroute as-path-ignore (BGP-IPv4 unicast address family view)
===============================================================

bestroute as-path-ignore (BGP-IPv4 unicast address family view)

Function
--------



The **bestroute as-path-ignore** command configures BGP to ignore the AS\_Path attribute when it selects optimal routes.

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

BGP-IPv4 unicast address family view


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
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] bestroute as-path-ignore

```