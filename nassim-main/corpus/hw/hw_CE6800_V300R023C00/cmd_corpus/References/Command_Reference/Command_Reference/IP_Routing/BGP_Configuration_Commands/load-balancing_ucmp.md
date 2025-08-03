load-balancing ucmp
===================

load-balancing ucmp

Function
--------

By default, BGP UCMP is disabled.


Format
------

**load-balancing ucmp**

**undo load-balancing ucmp**


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

**Usage Scenario**



If there are multiple egresses to the destination, if the **load-balancing ucmp** command is run when BGP routes are available for load balancing, the device can implement unequal-cost load balancing among BGP routes based on the Link Bandwidth attribute carried in the routes.



**Precautions**



The load-balancing adaptive-routing and **load-balancing ucmp** commands cannot be used together.The load-balance ecmp stateful enable and **load-balancing ucmp** commands cannot be used together.The vxlan-overlay local-preference enable and **load-balancing ucmp** commands cannot be used together.The load-balance ecmp rail-group enable and **load-balancing ucmp** commands cannot be used together.




Example
-------

# Enable BGP UCMP.
```
<HUAWEI> system-view
[~HUAWEI] bgp 100
[*HUAWEI-bgp] load-balancing ucmp

```