nexthop recursive-lookup restrain disable (BGP-EVPN address family view)
========================================================================

nexthop recursive-lookup restrain disable (BGP-EVPN address family view)

Function
--------



The **nexthop recursive-lookup restrain disable** command disables BGP recursion suppression in case of next hop flapping.

The **undo nexthop recursive-lookup restrain disable** command enables BGP recursion suppression in case of next hop flapping.



By default, BGP recursion suppression in case of next hop flapping is enabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**nexthop recursive-lookup restrain disable**

**undo nexthop recursive-lookup restrain disable**


Parameters
----------

None

Views
-----

BGP-EVPN address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If a large number of routes recurse to the same next hop that flaps frequently, the system will be busy processing changes of these routes, which consumes excessive system resources and leads to high CPU usage. To address this problem, configure BGP recursion suppression in case of next hop flapping. If you do not care about whether the system is busy processing route selection and advertisement and the possible high CPU usage, run the **nexthop recursive-lookup restrain disable** command to disable BGP recursion suppression in case of next hop flapping.


Example
-------

# Disable BGP recursion suppression in case of next hop flapping in the BGP-EVPN address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] l2vpn-family evpn
[*HUAWEI-bgp-af-evpn] nexthop recursive-lookup restrain disable

```