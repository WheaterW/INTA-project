suppress-flapping lsp-generation
================================

suppress-flapping lsp-generation

Function
--------



The **suppress-flapping lsp-generation** command configures a period for the system to delay generation of the same LSP during route flapping.

The **suppress-flapping lsp-generation disable** command restores the default configuration.

The **undo suppress-flapping lsp-generation** command restores the default configuration.



By default, the system delays generation of the same LSP for 10s during route flapping.


Format
------

**suppress-flapping lsp-generation** { **disable** | **timer** *delay-interval* [ **threshold** *threshold-value* ] }

**undo suppress-flapping lsp-generation**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **timer** *delay-interval* | Specifies a period for the system to delay generation of the same LSP during route flapping. | The value is an integer ranging from 1 to 600, in seconds. |
| **threshold** *threshold-value* | Specifies a route flapping threshold. If a route flaps for the specified number of times, LSP generation is delayed. | The value is an integer ranging from 3 to 100, in times. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On an IS-IS network, when the local routing information changes, the device sends LSPs to advertise the change. If the local routing information changes frequently and new LSPs are generated immediately, a lot of system resources will be consumed. To prevent this problem, run the **suppress-flapping lsp-generation** command to configure a period for the router to delay generation of the same LSP during route flapping.The flapping suppression process is as follows:

* If the same LSP is generated repeatedly within 3s, IS-IS records a flapping event and increases the flapping\_count by 1. If the interval at which the system generates the same LSP is greater than 10s before flapping suppression takes effect, IS-IS clears the flapping\_count. If the flapping\_count is greater than threshold-value, flapping suppression takes effect.
* During the flapping suppression period, IS-IS does not generate the same LSP, but the flapping\_count may increase during this period. After the delay-interval elapses, IS-IS exits from flapping suppression and clears the flapping\_count.

**Prerequisites**

An IS-IS process has been created and the IS-IS view has been displayed using the **isis** command.

**Configuration Impact**

If the device delays generation of the same LSP too long, the local routing information cannot be advertised to neighbors in time, slowing down route convergence.


Example
-------

# Configure the device to delay generation of the same LSP for 5s after a route flaps 10 times.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] suppress-flapping lsp-generation timer 5 threshold 10

```