qos buffer headroom-pool
========================

qos buffer headroom-pool

Function
--------



The **qos buffer headroom-pool** command configures the chip-level headroom buffer threshold.

The **undo qos buffer headroom-pool** command cancels the configuration.



By default, the chip-level headroom buffer threshold is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**qos buffer headroom-pool size** *size* { **kbytes** | **mbytes** } **slot** *slot-id*

**undo qos buffer headroom-pool** [ **size** *size* { **kbytes** | **mbytes** } ] **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **size** *size* | Specifies the headroom buffer threshold. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 16 to 30720, in kbytes.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer that ranges from 1 to 2048, in kbytes.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 16 to 9216, in kbytes. |
| **kbytes** | Specifies the unit as kilobytes. | - |
| **mbytes** | Specifies the unit as megabytes. | - |
| **slot** *slot-id* | Specifies the slot ID. | The value is an integer. You can enter the question mark (?) and select the value as prompted. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To absorb more packets from a link, run this command.

**Precautions**



For the CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ:You need to delete the PFC profile applied to an interface in the interface view before deleting the manually configured chip-level headroom buffer threshold.This command is used to configure the chip-level headroom buffer threshold on a card. If a card has multiple chips, the headroom buffer configured using this command is allocated to each chip core.It is recommended that the chip-level headroom buffer threshold be set to 4 MB. If the networking environment and traffic model are complex and packet loss occurs, contact technical support personnel to adjust the chip-level headroom buffer threshold.Properly configure the chip-level headroom buffer threshold. If the threshold is too large, the available queue buffer is insufficient, causing packet loss.




Example
-------

# Set the headroom buffer threshold in slot 1 to 1 MB. (CE6866, CE6860-SAN, CE6866K, CE6860-HAM, CE8851-32CQ8DQ-P, CE8850-SAN, CE8851K, and CE8850-HAM)
```
<HUAWEI> system-view
[~HUAWEI] qos buffer headroom-pool size 1 mbytes slot 1

```

# Set the headroom buffer threshold in slot 1 to 4 MB. (CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-SAN, CE6885-LL, CE6885-T, and CE6863E-48S8CQ)
```
<HUAWEI> system-view
[~HUAWEI] qos buffer headroom-pool size 4 mbytes slot 1

```