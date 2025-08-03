flow-aggregation export interval
================================

flow-aggregation export interval

Function
--------



The **flow-aggregation export interval** command configures the interval for reporting aggregation flow entries.

The **undo flow-aggregation export interval** command restores the default interval for reporting aggregation flow entries.



By default, the interval for reporting aggregation flow entries is 300s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**flow-aggregation export interval** *interval-time*

**undo flow-aggregation export interval** [ *interval-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-time* | Specifies the interval for reporting aggregation flow entries. | The value is an integer that ranges from 10 to 1800,in seconds. The default value is 300. |



Views
-----

any-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The aggregation flow entries generated on the built-in CPU must be reported to an analyzer for further processing. You can run this command to set a proper reporting interval. When the reporting interval expires, aggregation flow entries will be reported to the specified analyzer.


Example
-------

# Set the interval for reporting aggregation flow entries to 400s.
```
<HUAWEI> system-view
[~HUAWEI] any-flow
[*HUAWEI-any-flow] flow-aggregation export interval 400

```