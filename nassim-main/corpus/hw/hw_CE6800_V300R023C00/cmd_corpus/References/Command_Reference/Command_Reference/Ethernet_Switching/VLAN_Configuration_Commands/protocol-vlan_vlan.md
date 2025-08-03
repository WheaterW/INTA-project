protocol-vlan vlan
==================

protocol-vlan vlan

Function
--------



The **protocol-vlan vlan** command associates interfaces with protocol-based VLANs.

The **undo protocol-vlan vlan** command deletes the association.



By default, no interface is associated with any VLAN.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**protocol-vlan vlan** *vlan-id* { **all** | *protocol-index1* [ **to** *protocol-index2* ] } [ **priority** *priority* ]

**undo protocol-vlan** { **vlan** *vlan-id* { **all** | *protocol-index1* [ **to** *protocol-index2* ] [ **priority** *priority* ] } }

**undo protocol-vlan all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies the ID of the VLAN classified based on protocols. | The value is an integer ranging from 1 to 4094. |
| **all** | Specifies all the protocol VLAN. | - |
| *protocol-index1* | Specifies the index of a protocol template. | The value is an integer in the range 0 to 15. |
| *protocol-index2* | Specifies the index of a protocol template. | The value is an integer in the range 0 to 15. |
| **priority** *priority* | Specifies the 802.1p priority of the VLAN to be associated with the protocol. | The value is an integer ranging from 0 to 7. A larger value indicates a higher priority. The default value is 0. |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After running the protocol-vlan <protoIdx1> command, you must run the **protocol-vlan vlan** command to associate the interface with the VLAN. After an interface is associated with a VLAN, the system automatically assigns the VLAN ID to the protocol when the associated protocol enters the interface.

**Precautions**

If you do not manually configure the protocol index, the system automatically generates an index based on the sequence of associations between protocols and VLANs.


Example
-------

# Associate 100GE 1/0/1 with protocol-based VLAN 2 of which the protocol template index is 0.
```
<HUAWEI> system-view
[*HUAWEI] vlan 2
[*HUAWEI-vlan2] protocol-vlan ipv4
[*HUAWEI-vlan2] quit
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI] portswitch
[*HUAWEI-100GE1/0/1] protocol-vlan vlan 2 0

```