aging-time(any-flow view)
=========================

aging-time(any-flow view)

Function
--------



The **aging-time** command configures the aging time for entries in the flow table on the built-in CPU.

The **undo aging-time** command restores the default aging time for entries in the flow table on the built-in CPU.



By default, the aging time for entries in the flow table on the built-in CPU is 30s.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**aging-time** *time-value*

**undo aging-time** [ *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies the aging time for entries in the flow table on the built-in CPU. | The value is an integer ranging from 5 to 500, in seconds. The default value is 30. |



Views
-----

any-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Network traffic may burst intermittently and a large number of flows are generated in a short period of time. However, the memory capacity of the built-in CPU is limited. Old flow entries in the memory need to be deleted to release memory space for new flow entries. The process of deleting old flow entries is called aging.

You can run the aging-time command to set a proper aging time for entries in the flow table on the built-in CPU. When the active time (from the flow entry creation time to the current time) of a flow entry exceeds the configured aging time, the flow entry will be deleted locally and reported to the specified destination.

**Precautions**

If the aging-time command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the aging time for entries in the flow table on the built-in CPU to 300s.
```
<HUAWEI> system-view
[~HUAWEI] any-flow
[*HUAWEI-any-flow] aging-time 300

```