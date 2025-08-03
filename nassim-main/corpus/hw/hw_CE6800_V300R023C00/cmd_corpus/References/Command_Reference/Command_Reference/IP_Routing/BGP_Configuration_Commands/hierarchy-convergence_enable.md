hierarchy-convergence enable
============================

hierarchy-convergence enable

Function
--------



The **hierarchy-convergence enable** command enables hierarchical convergence.

The **undo hierarchy-convergence enable** command restores the default configurations.



By default, hierarchical convergence is not enabled.


Format
------

**hierarchy-convergence enable**

**undo hierarchy-convergence enable**


Parameters
----------

None

Views
-----

BGP-IPv4 unicast address family view,BGP-IPv6 unicast address family view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

By default, received hierarchical routes are processed as common routes. If the **hierarchy-convergence enable** command is run to enable hierarchical convergence, base routes converge first, and then hierarchical routes rely on the recursion results of the base routes.

**Configuration Impact**

After the command is run, hierarchical routes may become unreachable.

**Precautions**

Hierarchical routes use base routes for recursion. If the base routes are not reachable, enabling this capability will cause the hierarchical routes to be unreachable.


Example
-------

# Enable hierarchical convergence.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv4-family unicast
[*HUAWEI-bgp-af-ipv4] hierarchy-convergence enable

```