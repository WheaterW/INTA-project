clock source ssm
================

clock source ssm

Function
--------



The **clock source ssm** command configures an SSM quality level for a PTP clock source.

The **undo clock source ssm** command deletes the SSM quality level of a PTP clock source.



By default, no SSM quality level is configured for a PTP clock source.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock source ptp ssm** { **prc** | **ssua** | **ssub** | **sec** | **dnu** | **unk** }

**undo clock source ptp ssm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **prc** | Indicates that the SSM level is PRC (G.811 clock signal). | - |
| **ssua** | Indicates that the SSM level is SSUA (G.812 transit node clock signal). | - |
| **ssub** | Indicates that the SSM level is SSUB (G.812 local node clock signal). | - |
| **sec** | Indicates that the SSM level is SDH. | - |
| **dnu** | Indicates that the SSM level is not used for clock synchronization. | - |
| **unk** | Indicates that the SSM level is unknown clock synchronization quality. | - |
| **ptp** | Specifies a PTP clock source as the master clock source. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A synchronization status message (SSM) transmits the quality level of timing signals on a synchronous timing link. Node clocks on a synchronization network parse the SSM to obtain the quality level of an upstream clock.

If SSM levels are configured to participate in clock source selection, the system selects a clock source to be traced based on the SSM levels of clock sources. If the SSM level is enabled for clock source selection, the system selects a clock source to be synchronized based on the SSM level of each clock source. In this case, you need to configure an SSM level for the clock source to participate in clock source selection.The SSM levels are as follows: prc, ssua, ssub, sec, and dnu.


Example
-------

# Set the SSM level to prc for the clock source.
```
<HUAWEI> system-view
[~HUAWEI] clock source ptp ssm prc

```