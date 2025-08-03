bestroute med-none-as-maximum (BGP-IPv6 unicast address family view)
====================================================================

bestroute med-none-as-maximum (BGP-IPv6 unicast address family view)

Function
--------



The **bestroute med-none-as-maximum** command configures BGP to assign the maximum MED (4294967295) to a route without MED in route selection.

The **undo bestroute med-none-as-maximum** command restores the default configuration.



By default, BGP assigns 0 to a route without MED.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**bestroute med-none-as-maximum**

**undo bestroute med-none-as-maximum**


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

The **bestroute med-none-as-maximum** command takes effect during BGP route selection and is used only when no MED is carried by BGP routes. If no MED is carried and the **bestroute med-none-as-maximum** command is not run, the system cannot select the desired route as the optimal route.

**Configuration Impact**

During BGP route selection, if the **bestroute med-none-as-maximum** command is run, a route without MED is assigned the maximum MED (4294967295).


Example
-------

# Configure BGP to assign the maximum MED (4294967295) to a route without MED in route selection.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] ipv6-family unicast
[*HUAWEI-bgp-af-ipv6] bestroute med-none-as-maximum

```