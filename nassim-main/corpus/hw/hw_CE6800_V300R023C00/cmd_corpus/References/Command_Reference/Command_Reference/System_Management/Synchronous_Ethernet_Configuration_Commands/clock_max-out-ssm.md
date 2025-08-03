clock max-out-ssm
=================

clock max-out-ssm

Function
--------



The **clock max-out-ssm** command configures the maximum output SSM level for clock signals.

The **undo clock max-out-ssm** command deletes the maximum output SSM level configured for clock signals.



By default, no maximum output SSM level is configured for clock signals. That is, the actual output SSM level is used.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock max-out-ssm** { **prc** | **ssua** | **ssub** | **sec** }

**undo clock max-out-ssm**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **prc** | Indicates that the SSM level is PRC (G.811 clock signal). | - |
| **ssua** | Indicates that the SSM level is SSUA (G.812 transit node clock signal). | - |
| **ssub** | Indicates that the SSM level is SSUB (G.812 local node clock signal). | - |
| **sec** | Indicates that the SSM level is SDH. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the device transmits poor-quality clock signals to a downstream device, run the clock max-out-ssm command to configure a low maximum output SSM level for clock signals. If SSM levels are also configured to participate in clock source selection on this downstream device, there is a low probability that this downstream device traces this clock source.When the maximum output SSM level of the clock signal is configured, the system automatically degrades the output SSM level to the preset value if the SSM level of the clock signal is higher than the configured maximum output SSM level. If the SSM level of the clock signal is lower than the configured SSM level, the system outputs the clock signal according to the actual SSM level.


Example
-------

# Set the maximum output SSM level to ssua for clock signals.
```
<HUAWEI> system-view
[~HUAWEI] clock max-out-ssm ssua

```