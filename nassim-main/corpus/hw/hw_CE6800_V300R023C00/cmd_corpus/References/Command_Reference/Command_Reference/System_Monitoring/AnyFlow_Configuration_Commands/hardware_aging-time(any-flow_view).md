hardware aging-time(any-flow view)
==================================

hardware aging-time(any-flow view)

Function
--------



The **hardware aging-time** command configures the aging time for entries in the hardware flow table.

The **undo hardware aging-time** command restores the default aging time for entries in the hardware flow table.



By default, the aging time for entries in the hardware flow table is 10 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**hardware aging-time** *time-value*

**undo hardware aging-time** [ *time-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *time-value* | Specifies the aging time for entries in the hardware flow table. | The value is an integer ranging from 2 to 300000, in milliseconds. The default value is 10. |



Views
-----

any-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Network traffic may burst intermittently and a large number of flows are generated in a short period of time. However, the hardware memory capacity is limited. Old flow entries in the memory need to be deleted to release memory space for new flow entries. The process of deleting old flow entries is called aging.You can run this command to set a proper aging time for entries in the hardware flow table. When the active time (from the flow entry creation time to the current time) of a flow entry exceeds the configured aging time, the flow entry will be deleted locally and reported to the chip built in the CPU.

**Precautions**

If the **hardware aging-time** command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the aging time for entries in the hardware flow table to 300 ms.
```
<HUAWEI> system-view
[~HUAWEI] any-flow
[*HUAWEI-any-flow] hardware aging-time 300

```