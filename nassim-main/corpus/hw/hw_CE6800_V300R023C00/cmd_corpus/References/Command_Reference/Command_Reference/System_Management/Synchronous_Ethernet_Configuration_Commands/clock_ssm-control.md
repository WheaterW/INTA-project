clock ssm-control
=================

clock ssm-control

Function
--------



The **clock ssm-control** command configures whether SSM levels participate in clock source selection.



By default, SSM levels do not participate in clock source selection.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock ssm-control** { **on** | **off** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **on** | Indicates that SSM levels participate in clock source selection. | - |
| **off** | Indicates that SSM levels do not participate in clock source selection. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

SSM levels indicate the quality levels of clock signals. After you configure SSM levels to participate in clock source selection, the device preferentially selects a high-quality clock source.When the device works in automatic clock source selection mode, it selects a clock source based on priorities of clock sources. If SSM levels are configured to participate in clock source selection, the device preferentially selects a clock source based on the SSM levels. If multiple clock sources have the same highest SSM level, the system selects a clock source based on the priorities of these clock sources.


Example
-------

# Configure SSM levels to participate in clock source selection.
```
<HUAWEI> system-view
[~HUAWEI] clock ssm-control on

```