display fwm vxlan statistics
============================

display fwm vxlan statistics

Function
--------



The **display fwm vxlan statistics** command displays VXLAN module statistics on a specified board.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**display fwm vxlan** { **l2subif** | **bridge-domain** | **tunnel** | **evpn** | **oam** } **statistics** [ **all** ] **slot** *slotid*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **l2subif** | Specifies a Layer 2 sub-interface. | - |
| **bridge-domain** | Specifies a broadcast domain. | - |
| **tunnel** | Indicates the tunnel module. | - |
| **evpn** | Indicates the EVPN module. | - |
| **oam** | Indicates the OAM module. | - |
| **all** | Indicates all statistics. | - |
| **slot** *slotid* | Specifies the slot ID. | The value is a string of 1 to 49 case-sensitive characters, spaces not supported. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

You can run this command to check the delivery of each sub-service of the VXLAN modules. This command displays statistics in a list. Each line indicates a piece of statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about the VXLAN module on a specified board.
```
<HUAWEI> display fwm vxlan bridge-domain statistics slot 1
Id     Statistic description                    Counter           Last timestamp
--------------------------------------------------------------------------------
1      BD read bdentrystate                           1  04-27-2020 15:41:49.930
2      BD write bdentry                               4  04-27-2020 15:41:49.934

```

**Table 1** Description of the **display fwm vxlan statistics** command output
| Item | Description |
| --- | --- |
| Id | Statistics counter ID. |
| Statistic description | Statistics counter description about a specific service. |
| Counter | Number of statistics counters. |
| Last timestamp | Last update time of the statistics counter. |