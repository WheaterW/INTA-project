port vlan-stacking
==================

port vlan-stacking

Function
--------



The **port vlan-stacking vlan** command enables VLAN stacking on an interface. That is, it configures the interface to add a VLAN tag to each received single-tagged packet.

The **port vlan-stacking untagged** command configures a device to add double VLAN tags to an untagged packet.

The **undo port vlan-stacking** command restores the default configuration.

The **undo port vlan-stacking untagged** command cancels the configuration of adding double VLAN tags to an untagged packet.



By default, VLAN stacking is not configured on interfaces.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**port vlan-stacking vlan** *vlan-id1* [ **to** *vlan-id2* ] **stack-vlan** *vlan-id3*

**port vlan-stacking vlan** *vlan-id1* [ **to** *vlan-id2* ] **stack-vlan** *vlan-id3* **remark-8021p** *8021p-value3*

**port vlan-stacking untagged stack-vlan** *vlan-id3* **stack-inner-vlan** *stackInnerVid*

**undo port vlan-stacking vlan** *vlan-id1* [ **to** *vlan-id2* ] [ **stack-vlan** *vlan-id3* ]

**undo port vlan-stacking untagged** [ **stack-vlan** *vlan-id3* **stack-inner-vlan** *stackInnerVid* ]

**undo port vlan-stacking vlan** *vlan-id1* [ **to** *vlan-id2* ] **stack-vlan** *vlan-id3* **remark-8021p** *8021p-value3*

**undo port vlan-stacking all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id1* | Indicates the start value of the inner VLAN range. | The value is an integer ranging from 1 to 4094. |
| *vlan-id2* | Indicates the end value of the inner VLAN range. | The value is an integer ranging from 1 to 4094. |
| **stack-vlan** *vlan-id3* | Specifies the VLAN ID in the outer tag to be added to a packet. | The value is an integer ranging from 1 to 4094. |
| **remark-8021p** *8021p-value3* | Specifies the VLAN priority. | The value is an integer ranging from 0 to 7. |
| **untagged** | Specifies the untagged packet type. | - |
| **stack-inner-vlan** *stackInnerVid* | Specifies the inner VLAN tag added to an untagged frame. | The value is an integer ranging from 1 to 4094. |
| **all** | Deletes all non-untagged VLAN stacking configurations on the interface. | - |



Views
-----

Layer 2 100GE interface view,Layer 2 10GE interface view,Layer 2 200GE interface view,25GE-L2 view,400GE-L2 view,Layer 2 50GE interface view,Layer 2 Eth-Trunk interface view,Layer 2 GE interface view,Interface group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

VLAN stacking, also known as selective QinQ, is a Layer 2 technology that adds outer VLAN tags to packets based on their VLAN IDs.On access networks of carriers, users must be differentiated based on their applications and access locations or devices. After VLAN stacking is configured on an interface, the interface adds different outer VLAN tags to packets based on their VLAN IDs to differentiate users.A VLAN stacking interface has the following features:

* The interface can be configured with multiple outer VLAN tags. Therefore, the interface can add different outer VLAN tags to frames from different VLANs.
* When receiving a frame, the interface adds an outer tag to the frame. When sending a frame, the interface removes the outer tag from the frame.

VLSN-Stacking untagged enables a Layer 2 port to add double tags to received untagged packets according to actual services or users. In this manner, services or users can be differentiated according to the added tags.For a sent packet:

* The VLAN tag of a packet is removed and the packet becomes untagged only when the VLAN of the packet matches both the outer and inner VLAN tags.
* If only the outer VLAN ID is matched and the outer VLAN is configured for the interface in untagged mode, the outer VLAN ID is removed and the inner VLAN ID is retained.

**Prerequisites**

Before you run the **port vlan-stacking** command:

* If the interface is a Layer 3 interface, it has been switched to a Layer 2 interface using the **portswitch** command.
* You must run the port link-type { hybrid | trunk } command to set the link type of an Ethernet interface to hybrid or trunk.By default, the link type of an Ethernet interface is hybrid.

**Precautions**

When configuring VLAN stacking, pay attention to the following points:

* It is recommended that the interface type be hybrid or trunk and take effect only in the inbound direction.
* The interface must be added to the outer stack VLAN in hybrid or trunk mode.
* After VLAN stacking is configured on an interface, if the interface needs to remove the outer tag from a frame, the interface must be added to the stack VLAN in untagged mode. If the interface does not need to remove the outer tag from a frame, the interface must be added to the stack VLAN in tagged mode.
* If the PVID of an interface is not VLAN 1, restore the PVID to the default value before running the **port vlan-stacking untagged** command.
* Adding double VLAN tags to untagged packets belongs to interface-based VLAN assignment. The priorities of different VLAN assignment modes are as follows: Policy-VLAN > MAC-VLAN > IP-Subnet-VLAN > Protocol-VLAN > Interface-based VLAN assignment.
* If the **port vlan-stacking untagged** command is run on an interface, the interface processes the received packets tagged with VLAN 0 as untagged packets.
* VLAN segments cannot be split.
* An IP address cannot be configured on the VLANIF interface of the outer VLAN of VLAN stacking to access IP services.
* The VLAN specified by stack-vlan takes effect only after being created.


Example
-------

# Add double VLAN tags to untagged packets received on 100GE 1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] vlan 100
[*HUAWEI] q
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] port link-type hybrid
[*HUAWEI-100GE1/0/1] port hybrid untagged vlan 100
[*HUAWEI-100GE1/0/1] port vlan-stacking untagged stack-vlan 100 stack-inner-vlan 200

```

# Enable VLAN stacking on 100GE 1/0/1 and configure 100GE 1/0/1 to add the outer VLAN ID 20 to packets carrying VLAN IDs 40 to 50.
```
<HUAWEI> system-view
[~HUAWEI] vlan 20
[*HUAWEI] q
[*HUAWEI] interface 100GE 1/0/1
[*HUAWEI-100GE1/0/1] portswitch
[*HUAWEI-100GE1/0/1] port link-type trunk
[*HUAWEI-100GE1/0/1] port trunk allow-pass vlan 20
[*HUAWEI-100GE1/0/1] port vlan-stacking vlan 40 to 50 stack-vlan 20

```