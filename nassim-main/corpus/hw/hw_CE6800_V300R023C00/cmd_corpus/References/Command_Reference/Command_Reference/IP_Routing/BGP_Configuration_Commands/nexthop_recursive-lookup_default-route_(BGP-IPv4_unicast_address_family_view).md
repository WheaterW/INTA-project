nexthop recursive-lookup default-route (BGP-IPv4 unicast address family view)
=============================================================================

nexthop recursive-lookup default-route (BGP-IPv4 unicast address family view)

Function
--------



The **nexthop recursive-lookup default-route** command enables BGP route recursion to the default route.

The **undo nexthop recursive-lookup default-route** command restores the default configuration.



By default, BGP route recursion to the default route is disabled.


Format
------

**nexthop recursive-lookup default-route**

**undo nexthop recursive-lookup default-route**


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

The next hop of a BGP route may not be directly reachable. In this case, route recursion is required. To allow BGP routes to be recursed to the default IP route in the IPv4 address family view, run the **nexthop recursive-lookup default-route** command.

**Precautions**

After the **nexthop recursive-lookup default-route** command is run, BGP routes can recurse to the default route, which may lead to a forwarding path change.


Example
-------

# Enable BGP route recursion to the default route in the BGP-IPv4 unicast address family view.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] nexthop recursive-lookup default-route

```