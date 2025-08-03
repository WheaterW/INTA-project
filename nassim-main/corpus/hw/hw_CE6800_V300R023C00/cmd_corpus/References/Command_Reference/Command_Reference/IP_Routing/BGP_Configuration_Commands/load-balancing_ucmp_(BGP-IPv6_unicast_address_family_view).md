load-balancing ucmp (BGP-IPv6 unicast address family view)
==========================================================

load-balancing ucmp (BGP-IPv6 unicast address family view)

Function
--------

By default, BGP UCMP is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**load-balancing ucmp**

**undo load-balancing ucmp**


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

If there are multiple egresses to the destination, if the **load-balancing ucmp** command is run when BGP routes are available for load balancing, the device can implement unequal-cost load balancing among BGP routes based on the Link Bandwidth attribute carried in the routes.

**Precautions**

The load-balance ecmp stateful enable and **load-balancing ucmp** commands cannot be used together.The vxlan-overlay local-preference enable and **load-balancing ucmp** commands cannot be used together.The load-balance ecmp rail-group enable and **load-balancing ucmp** commands cannot be used together.


Example
-------

# Enable BGP UCMP.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] load-balancing ucmp

```