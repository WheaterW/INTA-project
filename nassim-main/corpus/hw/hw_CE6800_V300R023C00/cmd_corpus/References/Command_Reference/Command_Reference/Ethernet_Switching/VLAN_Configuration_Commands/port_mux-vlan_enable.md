port mux-vlan enable
====================

port mux-vlan enable

Function
--------



The **port mux-vlan enable** command enables the MUX VLAN function on an interface.

The **undo port mux-vlan enable** command disables the MUX VLAN function on an interface.



By default, the MUX VLAN function is disabled on an interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**port mux-vlan enable** { **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> }

**undo port mux-vlan enable** [ **vlan** { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10> ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Specifies the start VLAN ID. | The value is an integer ranging from 1 to 4094. |
| **to** *vlan-id2* | Specifies the end VLAN ID. | The value is an integer ranging from 1 to 4094. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The MUX VLAN function provides a mechanism for isolating Layer 2 traffic between VLAN interfaces. The MUX VLAN function provides principal VLANs and subordinate VLANs. Subordinate VLANs consist of separate and group VLANs. Interfaces in a principal VLAN can communicate with any other interfaces in a MUX VLAN. Interfaces in different subordinate VLANs cannot communicate with each other. Interfaces in a group VLAN can communicate with each other. Interfaces in a separate VLAN cannot communicate with each other.The preceding functions (isolation or communication) can be implemented only after the MUX VLAN function is enabled.

**Configuration Impact**

The interface enabled with the MUX VLAN function cannot be added to other VLANs.

**Precautions**

Access interfaces can be added to only one MUX VLAN group. Trunk and hybrid interfaces can be added to multiple MUX VLAN groups.


Example
-------

# Enable the MUX VLAN function on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] vlan 10
[*HUAWEI-vlan10] mux-vlan
[*HUAWEI-vlan10] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo shutdown
[*HUAWEI-100GE1/0/1] port mux-vlan enable vlan 10

```