deterministic-med (BGP-IPv4 unicast address family view)
========================================================

deterministic-med (BGP-IPv4 unicast address family view)

Function
--------



The **deterministic-med** command enables the BGP deterministic-MED function so that the route selection result is irrelevant to the sequence in which routes are received.

The **undo deterministic-med** command restores the default configuration.



By default, the BGP deterministic-MED function is disabled.


Format
------

**deterministic-med**

**undo deterministic-med**


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

If the **deterministic-med** command is not run, routes are compared based on the sequence in which they are received. The sequence in which routes are received is related to the result of route selection.After the BGP deterministic-med function is enabled, when an optimal route is selected from the routes that are received from different ASs and have the same prefix, the routes are first grouped based on the leftmost AS number in the AS\_Path. After the comparison in the group, the optimal route in the group is compared with the optimal route in another group. In this manner, the sequence in which routes are received is irrelevant to the result of route selection.For detailed applications of this command, see Configuration - IP Routing - BGP Configuration - BGP Route Selection Rules - Route Attributes - MED.

**Configuration Impact**

If the **deterministic-med** command is run, routes are grouped based on the AS\_Path before route selection, which may change the route selection result. Therefore, exercise caution when running this command.

**Precautions**

The bestroute add-path and **deterministic-med** commands are mutually exclusive.The bestroute best-external and **deterministic-med** commands are mutually exclusive.


Example
-------

# Enable the deterministic-MED function.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] deterministic-med

```