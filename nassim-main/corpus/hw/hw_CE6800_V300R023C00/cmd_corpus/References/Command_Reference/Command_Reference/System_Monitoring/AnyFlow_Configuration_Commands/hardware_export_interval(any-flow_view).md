hardware export interval(any-flow view)
=======================================

hardware export interval(any-flow view)

Function
--------



The **hardware export interval** command configures the interval for reporting entries in the hardware flow table.

The **undo hardware export interval** command restores the default interval for reporting entries in the hardware flow table.



By default, the interval for reporting entries in the hardware flow table is 10 ms.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**hardware export interval** *interval-time*

**undo hardware export interval** [ *interval-time* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval-time* | Specifies the interval for reporting entries in the hardware flow table. | The value is an integer ranging from 5 to 100, in milliseconds. The default value is 10. |



Views
-----

any-flow view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Hardware-based flow entries generated for traffic collected by the device need to be reported to the chip built in the CPU for further processing. You can run this command to set a proper reporting interval. When the reporting interval expires, flow entries will be reported to the chip built in the CPU.

**Precautions**

If the hardware export command is run more than once, the latest configuration overrides the previous one.


Example
-------

# Set the interval for reporting entries in the hardware flow table to 100 ms.
```
<HUAWEI> system-view
[~HUAWEI] any-flow
[*HUAWEI-any-flow] hardware export interval 100

```