export interval(any-flow view)
==============================

export interval(any-flow view)

Function
--------



The **export interval** command configures the interval for reporting entries in the flow table on the built-in CPU.

The **undo export interval** command restores the default interval for reporting entries in the flow table on the built-in CPU.



By default, the interval for reporting entries in the flow table on the built-in CPU is 10s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**export interval** *interval-time*

**undo export interval** [ *interval-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-time* | Specifies the interval for reporting entries in the flow table on the built-in CPU. | The value is an integer ranging from 10 to 1800, in seconds. The default value is 10. |



Views
-----

any-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The flow entries generated on the chip built in the CPU must be reported to an analyzer for further processing. You can run this command to set a proper reporting interval. When the reporting interval expires, flow entries will be reported to the specified analyzer.

**Precautions**

If the export interval command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the interval for reporting entries in the flow table on the built-in CPU to 300s.
```
<HUAWEI> system-view
[~HUAWEI] any-flow
[*HUAWEI-any-flow] export interval 300

```