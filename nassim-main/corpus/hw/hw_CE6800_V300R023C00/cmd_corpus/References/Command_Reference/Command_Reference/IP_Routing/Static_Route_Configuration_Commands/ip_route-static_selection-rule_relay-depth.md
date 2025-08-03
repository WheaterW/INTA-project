ip route-static selection-rule relay-depth
==========================================

ip route-static selection-rule relay-depth

Function
--------



The **ip route-static selection-rule relay-depth** command configures static routes to be selected based on recursion depths.

The **undo ip route-static selection-rule relay-depth** command cancels the configuration.



By default, static routes are not selected based on recursion depths.


Format
------

**ip route-static selection-rule relay-depth**

**undo ip route-static selection-rule relay-depth**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To prevent inter-board service transmission or routing loop in a static route scenario, configure recursion depth-based static route selection.



**Implementation Procedure**

* Use the **ip route-static selection-rule relay-depth** command.
* The static routes with the same prefix have the same priority but different recursion depths. The static route module selects the static route with the smallest recursion depth as the active route and sends it to the RM.

**Configuration Impact**



In the system, some static routes have the same prefix and priority but different recursion depths. After static routes are configured to be selected based on recursion depths, the static route module selects the static route with smallest recursion depth as the active route and adds it to the RM. Other static routes become inactive.



**Precautions**



The routes whose recursion depth is greater than 10 are inactive.After recursion depth-based static route selection is configured, the load balancing result may change because load balancing cannot be implemented among static routes with different recursion depths.




Example
-------

# Configure static routes to be selected according to recursion depths.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static selection-rule relay-depth

```