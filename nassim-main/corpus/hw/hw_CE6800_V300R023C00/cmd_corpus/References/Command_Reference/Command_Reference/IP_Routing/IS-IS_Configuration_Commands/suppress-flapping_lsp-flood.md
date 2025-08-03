suppress-flapping lsp-flood
===========================

suppress-flapping lsp-flood

Function
--------



The **suppress-flapping lsp-flood** command configures a period for the system to delay LSP flooding during route flapping.

The **suppress-flapping lsp-flood disable** command restores the default configuration.

The **undo suppress-flapping lsp-flood** command restores the default configuration.



By default, if route flapping occurs, the device delays LSP flooding for 10s.


Format
------

**suppress-flapping lsp-flood** { **disable** | **timer** *delay-interval* [ **threshold** *threshold-value* ] }

**undo suppress-flapping lsp-flood**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **timer** *delay-interval* | Specifies a period for the system to delay LSP flooding during route flapping. | The value is an integer ranging from 1 to 600, in seconds. |
| **threshold** *threshold-value* | Specifies a route flapping threshold. If a route flaps for the specified number of times, LSP flooding is delayed. | The value is an integer ranging from 3 to 100, in times. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an IS-IS network, if a device receives an LSP with a routing information change, it floods LSPs to advertise the change. If routing information changes frequently, flooding LSPs immediately consumes a large number of system resources. To prevent this problem, run the **suppress-flapping lsp-flood** command to configure the device to suppress LSP flooding. That is, LSPs are flooded after a specified delay.The flapping suppression process is as follows:

* If an LSP is flooded repeatedly within 3s, a flapping event is recorded and the flapping\_count increases by 1. If the interval at which the system floods the same LSP is greater than 10s before flapping suppression takes effect, the device clears the flapping\_count. If the flapping\_count is greater than threshold-value, flapping suppression takes effect.
* During the flapping suppression period, the device does not flood the same LSP, but the flapping\_count may increase during this period. After the delay-interval elapses, the device exits flapping suppression and clears the flapping\_count.If an LSP is suppressed locally, the corresponding LSP on neighbors may age. To prevent this problem, a mechanism is provided. Specifically, if the Remaining Lifetime field in an LSP is less than or equal to delay-interval plus 60s, the LSP is not suppressed.

**Prerequisites**

An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.

**Configuration Impact**

If the device delays LSP flooding too long, other devices on the network cannot detect the route information change in time, slowing down route convergence.


Example
-------

# Configure the device to delay flooding LSPs for 5s after a route flaps 10 times.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] suppress-flapping lsp-flood timer 5 threshold 10

```