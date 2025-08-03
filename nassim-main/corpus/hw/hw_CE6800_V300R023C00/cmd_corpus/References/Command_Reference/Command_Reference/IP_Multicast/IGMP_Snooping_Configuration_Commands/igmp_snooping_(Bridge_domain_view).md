igmp snooping (Bridge domain view)
==================================

igmp snooping (Bridge domain view)

Function
--------



The **igmp snooping** command sets a multicast group model in a BD.

The **undo igmp snooping** command restores the default configuration.



By default, the multicast group model is ASM-SSM and both ASM and SSM packets are supported in a BD.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping** { **ssm-only** | **asm-only** | **asm-ssm** }

**undo igmp snooping** { **ssm-only** | **asm-only** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ssm-only** | Indicates that entries with the group address type of SSM are learned. | - |
| **asm-only** | Indicates that entries with the group address type of ASM are learned. | - |
| **asm-ssm** | Indicates that entries with the group address type of ASM or SSM are learned. | - |



Views
-----

Bridge domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

There are two multicast group models: any-source multicast (ASM) and source-specific multicast (SSM). The igmp-snooping command can be used to configure a device to forward data only for multicast groups of the ASM or SSM model in a BD.

**Prerequisites**

The **igmp snooping enable** command has been run to enable IGMP snooping globally and in a BD.

**Configuration Impact**

If asm-only is specified in the igmp snooping command, only (\*, G) messages are processed, and other packets are discarded.


Example
-------

# Set the multicast group model to ASM-only in BD 10.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 10
[*HUAWEI-bd10] igmp snooping enable
[*HUAWEI-bd10] igmp snooping asm-only

```