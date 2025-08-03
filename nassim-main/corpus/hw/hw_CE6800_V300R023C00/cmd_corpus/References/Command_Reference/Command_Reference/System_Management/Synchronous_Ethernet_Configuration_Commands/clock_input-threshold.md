clock input-threshold
=====================

clock input-threshold

Function
--------



The **clock input-threshold** command configures a lower threshold for the input quality level of a clock source.

The **undo clock input-threshold** command restores the default configuration.



By default, the lower threshold for the input quality level of a clock source is sec.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock input-threshold** { **dnu** | **prc** | **sec** | **ssua** | **ssub** }

**undo clock input-threshold** [ **dnu** | **prc** | **sec** | **ssua** | **ssub** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **dnu** | Indicates that the clock source is not synchronized. | - |
| **prc** | Indicates that the lower threshold for the input quality level of a clock source is for G.811 clock signals. | - |
| **sec** | Indicates that the lower threshold for the input quality level of a clock source is for SDH device clock signals. | - |
| **ssua** | Indicates that the lower threshold for the input quality level of a clock source is for G.812 transit node clock signals. | - |
| **ssub** | Indicates that the lower threshold for the input quality level of a clock source is for G.812 local node clock signals. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

When the input quality level of a clock source falls below the threshold, the clock source will not be synchronized. To configure the lower threshold of the input quality level of a clock source, run the clock input-threshold command.


Example
-------

# Configure the lower threshold of the input quality level for a clock source as ssua.
```
<HUAWEI> system-view
[~HUAWEI] clock input-threshold ssua

```