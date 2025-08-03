mld snooping enable (VLAN view)
===============================

mld snooping enable (VLAN view)

Function
--------



The **mld snooping enable** command enables MLD snooping in a specified VLAN.

The **undo mld snooping enable** command disables MLD snooping in a specified VLAN.



By default, MLD snooping is disabled.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**mld snooping enable**

**undo mld snooping enable**


Parameters
----------

None

Views
-----

VLAN range view,VLAN view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

MLD snooping runs on a Layer 2 device between a Layer 3 multicast device and user hosts. MLD snooping listens on multicast protocol messages exchanged between the Layer 3 device and user hosts to maintain forwarding entries of multicast packets. MLD snooping manages and controls forwarding of multicast data packets. Enabling MLD snooping is the prerequisite for implementing Layer 2 multicast. You can run this command to enable MLD snooping in a specified VLAN.

**Precautions**

Running the **mld snooping enable** command in the system view enables MLD snooping globally. If you run the **undo mld snooping enable** command in the system view, MLD snooping is disabled on the entire device.Running this command in the VLAN view enables or disables MLD snooping in the VLAN. MLD snooping can be enabled in a VLAN only after MLD snooping is enabled globally. After MLD snooping is enabled in the system view, MLD snooping is still disabled in a VLAN by default.The **mld snooping enable** command fails to be run in the following situations:In a scenario where both IPv6 Layer 2 and Layer 3 multicast are configured (Layer 2 multicast is configured in a VLAN and Layer 3 multicast is configured on the corresponding VLANIF interface), the following functions must be configured together to ensure on-demand multicast traffic forwarding:

* MLD snooping is enabled in a VLAN.
* Enable IPv6 PIM (PIM-SM or Bidir-PIM) and MLD on the corresponding VLANIF interface.When this function is configured in the VLAN view, the configuration fails in the following situations:
* MLD snooping cannot be used together with VLAN mapping or VLAN stacking in a VLAN.


Example
-------

# Enable MLD snooping in VLAN 2.
```
<HUAWEI> system-view
[~HUAWEI] mld snooping enable
[~HUAWEI] vlan 2
[*HUAWEI-vlan2] mld snooping enable

```