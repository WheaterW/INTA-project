nexthop recursive-lookup default-route (BGP-IPv6 unicast address family view)
=============================================================================

nexthop recursive-lookup default-route (BGP-IPv6 unicast address family view)

Function
--------



The **nexthop recursive-lookup default-route** command enables BGP route recursion to the default route.

The **undo nexthop recursive-lookup default-route** command restores the default configuration.



By default, BGP route recursion to the default route is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**nexthop recursive-lookup default-route**

**undo nexthop recursive-lookup default-route**


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

The next hop of a BGP route may not be directly reachable. In this case, route recursion is required. During route recursion, you can run the **nexthop recursive-lookup default-route** command to enable BGP route recursion to the default IP route in the IPv6 address family view.

**Precautions**

After the **nexthop recursive-lookup default-route** command is run, BGP routes can recurse to the default route, which may lead to a forwarding path change.


Example
-------

# Enable BGP route recursion to the default route in the BGP-IPv6 unicast address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] nexthop recursive-lookup default-route

```