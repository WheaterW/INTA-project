load-balancing igp-metric-ignore (BGP-IPv6 unicast address family view)
=======================================================================

load-balancing igp-metric-ignore (BGP-IPv6 unicast address family view)

Function
--------

By default, a device compares IGP costs when selecting routes for load balancing.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**load-balancing igp-metric-ignore**

**undo load-balancing igp-metric-ignore**


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

To prevent a router from comparing IGP costs when selecting routes for load balancing, run the **load-balancing igp-metric-ignore** command.When routes with different IGP costs are available and load balancing among them is required, run the command. Exercise caution when using the command because the execution of this command will change the conditions of load balancing.


Example
-------

# Prevent a router from comparing IGP costs when selecting routes for load balancing.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] load-balancing igp-metric-ignore

```