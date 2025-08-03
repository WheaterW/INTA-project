mld snooping version
====================

mld snooping version

Function
--------



The **mld snooping version** command sets the version of MLD messages that can be processed in MLD snooping.

The **undo mld snooping version** command restores the default value.



By default, the device can process MLDv1 and MLDv2 messages.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping version** *number*

**undo mld snooping version**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *number* | Indicates the version number of MLD. | The value can be 1 or 2. |



Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

If hosts connected to a Layer 2 device support different MLD versions, run the mld snooping version command to set the version of MLD messages that can be processed.If the version is set to 1, only MLDv1 messages can be processed. If the version is set to 2, both MLDv1 and MLDv2 messages can be processed.


Example
-------

# Set the MLD Snooping version in VLAN 100.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[*HUAWEI] vlan 100
[*HUAWEI-vlan100] mld snooping enable
[*HUAWEI-vlan100] mld snooping version 2

```