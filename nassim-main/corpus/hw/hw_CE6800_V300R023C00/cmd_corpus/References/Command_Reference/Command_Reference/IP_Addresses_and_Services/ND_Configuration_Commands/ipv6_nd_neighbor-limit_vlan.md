ipv6 nd neighbor-limit vlan
===========================

ipv6 nd neighbor-limit vlan

Function
--------



The **ipv6 nd neighbor-limit vlan** command configures the maximum number of dynamic ND entries related to a Layer 2 interface that the VLANIF interface corresponding to the Layer 2 interface can learn.

The **undo ipv6 nd neighbor-limit vlan** command restores the default configuration.



By default, if a VLANIF interface contains only one Layer 2 interface, it can learn a maximum of 16384 dynamic ND entries related to the Layer 2 interface; if a VLANIF interface contains multiple Layer 2 interfaces, it can learn a maximum of 16384 or less dynamic ND entries related to each Layer 2 interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ipv6 nd neighbor-limit vlan** *vlanBegValue* [ **to** *vlanEndValue* ] **maximum** *limit-number*

**undo ipv6 nd neighbor-limit vlan** *vlanBegValue* [ **to** *vlanEndValue* ] **maximum** *limit-number*

**undo ipv6 nd neighbor-limit vlan** *vlanBegValue* [ **to** *vlanEndValue* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **to** *vlanEndValue* | Specifies an end VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **maximum** *limit-number* | Specifies the maximum number of each dynamic ND entry related to a Layer 2 interface that the VLANIF interface corresponding to the Layer 2 interface can learn. | The value is an integer ranging from 0 to 16384. |
| **vlan** *vlanBegValue* | Specifies a start VLAN ID. | The value is an integer ranging from 1 to 4094. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When an attacker sends a large number of ND messages to a Layer 2 interface, the VLANIF interface corresponding to the Layer 2 interface learns dynamic ND entries. If the number of dynamic ND entries learned by the VLANIF interface reaches the allowed maximum value, the VLANIF interface cannot learn dynamic ND entries related to the other Layer 2 interfaces in it, affecting authorized users' access to the network. To resolve this issue, run the **ipv6 nd neighbor-limit** command to configure the maximum number of dynamic ND entries related to a Layer 2 interface that the VLANIF interface corresponding to the Layer 2 interface can learn.

**Precautions**

* The end VLAN ID must be greater than or equal to the start VLAN ID.
* If the VLAN range configured in the command does not overlap with the range of the VLANs that a Layer 2 interface joins, the maximum number of dynamic ND entries configured using the command does not take effect.
* If both the maximum number of dynamic ND entries related to a Layer 2 interface that the VLANIF interface corresponding to the Layer 2 interface can learn and the maximum number of dynamic ND entries that the VLANIF interface can learn are configured, a smaller number takes effect.

Example
-------

# Set the maximum number of dynamic ND entries from VLAN 10 to VLAN 20 on a Layer 2 Eth-Trunk interface that the VLANIF interface corresponding to the Layer 2 Eth-Trunk interface can learn to 30.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] portswitch
[*HUAWEI-Eth-Trunk1] ipv6 nd neighbor-limit vlan 10 to 20 maximum 30

```