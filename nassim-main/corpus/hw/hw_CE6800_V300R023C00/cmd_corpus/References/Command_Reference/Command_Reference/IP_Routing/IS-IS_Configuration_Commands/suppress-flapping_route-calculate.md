suppress-flapping route-calculate
=================================

suppress-flapping route-calculate

Function
--------



The **suppress-flapping route-calculate** command configures a period for the device to delay route calculation when the device receives an LSP during route flapping.

The **suppress-flapping route-calculate disable** command restores the default configuration.

The **undo suppress-flapping route-calculate** command restores the default configuration.



By default, if the device receives an LSP during route flapping, it delays route calculation for 10s.


Format
------

**suppress-flapping route-calculate** { **disable** | **timer** *delay-interval* [ **threshold** *threshold-value* ] }

**undo suppress-flapping route-calculate**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **timer** *delay-interval* | Specifies a period for the device to delay route calculation when the device receives an LSP during route flapping. | The value is an integer ranging from 1 to 600, in seconds. |
| **threshold** *threshold-value* | Specifies a route flapping threshold. If a route flaps for the specified number of times, route calculation is delayed. | The value is an integer ranging from 3 to 100, in times. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an IS-IS network, if the Router receives an LSP with a routing information change, the device needs to calculate routes based on the LSP. If routing information changes frequently and routes are calculated immediately, a lot of system resources will be consumed. To prevent this problem, run the **suppress-flapping route-calculate** command to configure a period for the device to delay route calculation when the Router receives an LSP during route flapping.The flapping suppression process is as follows:

* If the same LSP with a routing information change is received repeatedly within 3s, IS-IS records a flapping event and increases the flapping\_count by 1. If the interval at which the system receives the same LSP with a routing information change is greater than 10s before flapping suppression takes effect, IS-IS clears the flapping\_count. If the flapping\_count is greater than threshold-value, flapping suppression takes effect.
* During the flapping suppression period, IS-IS does not calculate routes in response to the LSP, but the flapping\_count may increase during this period. After the delay-interval elapses, IS-IS exits from flapping suppression and clears the flapping\_count.

**Prerequisites**



An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.




Example
-------

# Configure the device to delay route calculation for 5s after a route flaps 10 times.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] suppress-flapping route-calculate timer 5 threshold 10

```