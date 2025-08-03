clock map unk
=============

clock map unk

Function
--------



The **clock map unk** command maps an SSM level to the clock source with an SSM level of unk.



By default, dnu is mapped to the clock source with an SSM level of unk. If SSM levels are configured to participate in clock source selection, the clock source with an SSM level of unk cannot participate in clock source selection.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**clock map unk** { **prc** | **ssua** | **ssub** | **sec** | **dnu** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **prc** | Indicates that the SSM level is PRC (G.811 clock signal). | - |
| **ssua** | Indicates that the SSM level is SDH. | - |
| **ssub** | Indicates that the SSM level is SSUA (G.812 transit node clock signal). | - |
| **sec** | Indicates that the SSM level is SSUB (G.812 local node clock signal). | - |
| **dnu** | Indicates that the SSM level is not used for synchronization. | - |
| **map** | Indicates that the SSM level is not used for clock synchronization. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If the SSM level of an upstream clock source is unk, but you want the device to trace this upstream clock source, run the clock map unk command to map an SSM level higher than dnu to this upstream clock source.The SSM levels in descending order are as follows: prc, ssua, ssub, sec, dnu.


Example
-------

# Map ssua to the clock source with an SSM level of unk.
```
<HUAWEI> system-view
[~HUAWEI] clock map unk ssua

```