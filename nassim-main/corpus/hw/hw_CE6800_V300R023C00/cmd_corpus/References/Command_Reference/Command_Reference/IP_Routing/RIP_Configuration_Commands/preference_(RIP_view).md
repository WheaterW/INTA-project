preference (RIP view)
=====================

preference (RIP view)

Function
--------



The **preference** command specifies the priority for RIP routes. Alternatively, you can set a priority for a specific route using a route-policy.

The **undo preference** command restores the default setting.



By default, the priority of RIP routes is 100.


Format
------

**preference** { { **route-policy** *route-policy-name* } | *value* } \*

**undo preference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-policy** *route-policy-name* | Specifies the name of a route-policy used to filter routes. | The value is a string of 1 to 200 case-sensitive characters without spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| *value* | Specifies the priority of RIP routes. | The value is an integer ranging from 1 to 255. |



Views
-----

RIP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A smaller value indicates a higher preference. To enable RIP routes to have a higher preference than the routes learned from other IGPs, set a smaller preference value for RIP routes. The preference determines the routing algorithm through which the optimal route is obtained in the IP routing table.

**Prerequisites**

Before setting a route priority using a route-policy, the route-policy must have been configured using the **route-policy** command.

**Configuration Impact**

If you run the command multiple times, only the latest configuration takes effect.


Example
-------

# Set the priority for the routes in RIP process 1 to 120 and apply the route-policy named filter1.
```
<HUAWEI> system-view
[~HUAWEI] route-policy filter1 permit node 10
[*HUAWEI-route-policy] quit
[*HUAWEI] rip 1
[*HUAWEI-rip-1] preference route-policy filter1 120

```