clock priority
==============

clock priority

Function
--------



The **clock priority** command configures a priority for a line clock source.

The **undo clock priority** command deletes the priority for a line clock source.



The default priority of a line clock source is 0. That is, this line clock source does not participate in clock source selection.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock priority** *priority-value*

**undo clock priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **priority** *priority-value* | Priority of a line clock source. | The value is an integer ranging from 1 to 255. A smaller value indicates a higher priority.The default priority of a line clock source is 0. That is, this line clock source does not participate in clock source selection. |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To enable this line clock source to participate in clock source selection, configure a priority for this line clock source. In actual situations, the QL of a clock source is higher than the priority of the clock source.

* If clock source selection based on SSM levels is enabled, the system selects a clock reference source by the QL of a clock source.
* If clock source selection based on SSM levels is disabled or clock source selection based SSM levels is enabled but the QLs are the same, the system selects the clock reference source by the priority of a clock source.

**Precautions**

If external input clock signals or a 1588 clock source needs to be configured to participate in clock source selection, the level of the external clock source must be specified. Otherwise, the clock signals cannot participate in clock source selection.


Example
-------

# Set the priority of the line clock source to 10 on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] clock priority 10

```