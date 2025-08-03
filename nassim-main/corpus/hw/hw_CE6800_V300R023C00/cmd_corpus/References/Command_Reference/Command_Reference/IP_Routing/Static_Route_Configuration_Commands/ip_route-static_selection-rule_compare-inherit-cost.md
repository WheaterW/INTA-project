ip route-static selection-rule compare-inherit-cost
===================================================

ip route-static selection-rule compare-inherit-cost

Function
--------



The **ip route-static selection-rule compare-inherit-cost** command enables a device to compare the costs of inherited routes during static route selection.

The **undo ip route-static selection-rule compare-inherit-cost** command restores the default configuration.



By default, the device is disabled from comparing the costs of inherited routes during static route selection.


Format
------

**ip route-static selection-rule compare-inherit-cost**

**undo ip route-static selection-rule compare-inherit-cost**


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



By default, the device does not compare the costs of inherited routes during static route selection, and static routes with different costs work in load-balancing mode. To enable the device to compare the costs of inherited routes and only select the static route with the smallest cost, run the **ip route-static selection-rule compare-inherit-cost** command.




Example
-------

# Enable the device to compare the costs of inherited routes during static route selection.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static selection-rule compare-inherit-cost

```