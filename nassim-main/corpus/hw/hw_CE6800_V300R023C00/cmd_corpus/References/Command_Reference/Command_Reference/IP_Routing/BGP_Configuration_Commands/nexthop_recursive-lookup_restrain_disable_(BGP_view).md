nexthop recursive-lookup restrain disable (BGP view)
====================================================

nexthop recursive-lookup restrain disable (BGP view)

Function
--------



The **nexthop recursive-lookup restrain disable** command disables BGP recursion suppression in case of next hop flapping.

The **undo nexthop recursive-lookup restrain disable** command enables BGP recursion suppression in case of next hop flapping.



By default, BGP recursion suppression in case of next hop flapping is enabled.


Format
------

**nexthop recursive-lookup restrain disable**

**undo nexthop recursive-lookup restrain disable**


Parameters
----------

None

Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a large number of routes are recursed to the same next hop and the next hop flaps frequently, the system frequently processes the changes of these routes, consuming a large number of resources and causing high CPU usage. To address this problem, recursion suppression in case of next hop flapping is enabled by default. This function slows down route processing, saves system resources, and reduces CPU usage.If you do not want to slow down recursion processing or do not care about the high CPU usage caused by recursion change processing, run the **nexthop recursive-lookup restrain disable** command to disable recursion suppression in case of next hop flapping.


Example
-------

# Disable BGP recursion suppression in case of next hop flapping.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] nexthop recursive-lookup restrain disable

```