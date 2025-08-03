igmp snooping
=============

igmp snooping

Function
--------



The **igmp snooping** command sets a multicast group model in a VLAN.

The **undo igmp snooping** command restores the default configuration.



By default, the multicast group model is ASM-SSM and both ASM and SSM packets are supported in a VLAN.


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

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

There are two multicast group models: any-source multicast (ASM) and source-specific multicast (SSM). The igmp snooping command can be used to configure a device to forward data only for multicast groups of the ASM or SSM model in a VLAN.

**Prerequisites**

The **igmp snooping enable** command has been run to enable IGMP snooping globally and in a VLAN.

**Configuration Impact**

If asm-only is specified in the igmp snooping command, only (\*, G) messages are processed, and other packets are discarded.


Example
-------

# Set the multicast group model to ASM-only in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] igmp snooping enable
[*HUAWEI-vlan2] igmp snooping asm-only

```