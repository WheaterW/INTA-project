mld snooping
============

mld snooping

Function
--------



The **mld snooping** command sets a multicast group model in a VLAN.

The **undo mld snooping** command restores the default multicast group model.



By default, the multicast group model is ASM-SSM, allowing the device to support both any-source multicast (ASM) and source-specific multicast (SSM) messages in a VLAN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping** { **ssm-only** | **asm-only** | **asm-ssm** }

**undo mld snooping** { **ssm-only** | **asm-only** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ssm-only** | Enables the device to learn multicast group entries in the SSM range. | - |
| **asm-only** | Enables the device to learn multicast group entries in the ASM range. | - |
| **asm-ssm** | Enables the device to learn multicast group entries in both the ASM and SSM ranges. | - |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Based on whether multicast messages carry source addresses, multicast messages are categorized as ASM and SSM messages. To configure the type of multicast message that the device can process in a VLAN, run the mld snooping command.

**Prerequisites**

MLD snooping has been enabled both globally and in the VLAN view using the **mld snooping enable** command.

**Precautions**

The mld snooping command applies only to MLDv2.


Example
-------

# Configure the device to process only ASM messages in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] mld snooping enable
[*HUAWEI-vlan2] mld snooping asm-only

```