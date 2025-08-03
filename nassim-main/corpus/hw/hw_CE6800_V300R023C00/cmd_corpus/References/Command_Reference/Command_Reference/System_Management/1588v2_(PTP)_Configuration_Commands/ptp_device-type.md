ptp device-type
===============

ptp device-type

Function
--------



The **ptp device-type** command sets a clock mode for a 1588v2 device.

The **undo ptp device-type** command deletes the configured 1588v2 clock mode for a 1588v2 device.



By default, no 1588v2 clock mode is configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ptp device-type** { **bc** | **oc** }

**undo ptp device-type**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **bc** | Configures a 1588v2 device as a boundary clock (BC). A BC has multiple 1588v2 clock interfaces. One interface of a BC synchronizes time signals with its upstream clock, and other interfaces advertise the time to downstream clocks. | - |
| **oc** | Configures a 1588v2 device as an ordinary clock (OC). Only a single interface on an OC belongs to a 1588v2 domain. This interface synchronizes time signals with its upstream clock and advertises the time to downstream clocks. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before 1588v2 is used for clock synchronization, you must configure the clock mode for the device according to the network plan.

**Precautions**

Each 1588v2 device can be configured only with a single type. Perform either of the following procedures to change a clock type on a 1588v2-enabled device:

1. In principle, perform the following steps:

* Run the **undo ptp enable** command in the interface view to disable 1588v2.
* Run the **undo ptp device-type** command to disable the original clock mode.
* For an OC, run the **undo ptp slaveonly** command to disable the slaveonly mode.

1. Directly run the ptp device-type command to change the clock type. This command does not affect 1588v2 functions or parameters configured on interfaces. Ensure that a device of a specific type must meet requirements of an updated type. If the device has configurations that are not supported by the updated type, delete the configurations before switching the device types.


Example
-------

# Set the clock mode of a 1588v2 device to BC.
```
<HUAWEI> system-view
[~HUAWEI] ptp device-type bc

```