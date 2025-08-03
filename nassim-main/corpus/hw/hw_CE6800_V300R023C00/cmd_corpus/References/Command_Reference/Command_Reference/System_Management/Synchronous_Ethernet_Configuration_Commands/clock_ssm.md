clock ssm
=========

clock ssm

Function
--------



The **clock ssm** command configures an SSM level for a line clock source.

The **undo clock ssm** command deletes the SSM level configured for a line clock source.



By default, the line clock source learns SSM levels sent by an upstream device.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock ssm** { **unk** | **prc** | **ssua** | **ssub** | **sec** | **dnu** }

**undo clock ssm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **unk** | Indicates that the SSM level is unknown clock synchronization quality. | - |
| **prc** | Indicates that the SSM level is PRC (G.811 clock signal). | - |
| **ssua** | Indicates that the SSM level is SSUA (G.812 transit node clock signal). | - |
| **ssub** | Indicates that the SSM level is SSUB (G.812 local node clock signal). | - |
| **sec** | Indicates that the SSM level is SDH. | - |
| **dnu** | Indicates that the SSM level is not used for clock synchronization. | - |



Views
-----

100GE interface view,10GE interface view,200GE interface view,25GE interface view,400GE interface view,50GE interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A synchronization status message (SSM) transmits the quality level of timing signals on a synchronous timing link. Node clocks on a synchronization network parse the SSM to obtain the quality level of an upstream clock.

If SSM levels are configured to participate in clock source selection, the system selects a clock source to be traced based on the SSM levels of clock sources. By default, the line clock source learns SSM levels sent by an upstream device. You can manually configure an SSM level for the line clock source.


Example
-------

# Set the SSM level the line clock source to prc on 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] clock ssm prc

```