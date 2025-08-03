load-balancing igp-metric-ignore (BGP view)
===========================================

load-balancing igp-metric-ignore (BGP view)

Function
--------

By default, a device compares IGP costs when selecting routes for load balancing.


Format
------

**load-balancing igp-metric-ignore**

**undo load-balancing igp-metric-ignore**


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

To prevent a router from comparing IGP costs when selecting routes for load balancing, run the **load-balancing igp-metric-ignore** command.When routes with different IGP costs are available and load balancing among them is required, run the command. Exercise caution when using the command because the execution of this command will change the conditions of load balancing.


Example
-------

# Configure a device not to compare the IGP metrics of the routes to be used for load balancing.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] load-balancing igp-metric-ignore

```