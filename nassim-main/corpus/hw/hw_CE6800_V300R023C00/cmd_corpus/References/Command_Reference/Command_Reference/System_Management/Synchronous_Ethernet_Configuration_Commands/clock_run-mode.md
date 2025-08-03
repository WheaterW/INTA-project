clock run-mode
==============

clock run-mode

Function
--------



The **clock run-mode** command sets the clock working mode to the free, hold, or normal mode.



By default, the system clock works in normal mode.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock run-mode** { **free** | **hold** | **normal** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **free** | Indicates that the clock works in free-running mode. | - |
| **hold** | Indicates that the clock works in holdover mode. | - |
| **normal** | Sets the clock source selection mode to normal. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run this command to configure a clock running mode for the device.

* If you configure free, the system clock works in free-running mode. In this mode, the device does not use the clock source selection algorithm to select a clock source.
* If you configure hold, the system clock works in hold mode. In this mode, the device uses the locked clock signals.
* If you configure normal, the switch uses the clock source selection algorithm to select a clock source. If no clock source is available, the system clock automatically works in free-running or hold mode.

Example
-------

# Set the clock running mode to hold.
```
<HUAWEI> system-view
[~HUAWEI] clock run-mode hold

```