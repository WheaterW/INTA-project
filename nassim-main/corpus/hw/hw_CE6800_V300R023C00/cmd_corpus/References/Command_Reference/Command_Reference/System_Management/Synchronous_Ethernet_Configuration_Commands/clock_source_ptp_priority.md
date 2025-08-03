clock source ptp priority
=========================

clock source ptp priority

Function
--------



The **clock source ptp priority** command configures a priority for a PTP clock source.

The **undo clock source ptp priority** command deletes the configured priority of a PTP clock source.



By default, a clock source does not have a priority.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock source ptp priority** *priority-value*

**undo clock source ptp priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **priority** *priority-value* | Specifies the priority of a clock source. | The value is an integer that ranges from 1 to 255. A smaller value indicates a higher priority. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, a clock source does not have a priority. That is, this clock source cannot participate in clock source selection. To enable this clock source to participate in clock source selection, configure a priority for this clock source.


Example
-------

# Set the priority of a PTP clock source to 15.
```
<HUAWEI> system-view
[~HUAWEI] clock source ptp priority 15

```