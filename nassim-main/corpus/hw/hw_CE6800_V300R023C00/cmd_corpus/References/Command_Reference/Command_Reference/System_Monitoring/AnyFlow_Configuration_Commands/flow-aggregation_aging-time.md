flow-aggregation aging-time
===========================

flow-aggregation aging-time

Function
--------



The **flow-aggregation aging-time** command configures the aging time for aggregation flow entries.

The **undo flow-aggregation aging-time** command restores the default aging time for aggregation flow entries.



By default, the aging time for aggregation flow entries is 60s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**flow-aggregation aging-time** *time-value*

**undo flow-aggregation aging-time** [ *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies the aging time for aggregation flow entries. | The value is an integer that ranges from 5 to 500,in seconds. The default value is 60. |



Views
-----

any-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Network traffic may burst intermittently and a large number of flows are generated in a short period of time. However, the memory capacity of the built-in CPU is limited. Old flow entries in the memory need to be deleted to release memory space for new flow entries. The process of deleting old flow entries is called aging.After flow aggregation is enabled, you need to specify the aging time for aggregation flow entries. When the active time (from flow creation time to the current time) of an aggregation flow exceeds the aging time for aggregation flow entries, the flow is exported to the analyzer.

**Precautions**

If the flow-aggregation aging-time command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the aging time for aggregation flow entries to 300s.
```
<HUAWEI> system-view
[~HUAWEI] any-flow
[*HUAWEI-any-flow] flow-aggregation aging-time 300

```