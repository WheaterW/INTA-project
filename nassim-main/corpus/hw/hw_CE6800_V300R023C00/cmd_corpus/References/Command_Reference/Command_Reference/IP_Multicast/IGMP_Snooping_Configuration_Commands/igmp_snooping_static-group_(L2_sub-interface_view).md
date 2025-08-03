igmp snooping static-group (L2 sub-interface view)
==================================================

igmp snooping static-group (L2 sub-interface view)

Function
--------



The **igmp snooping static-group** command configures a static multicast group member interface.

The **undo igmp snooping static-group** command cancels the configuration.



By default, a static multicast group member interface is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**igmp snooping static-group** [ **source-address** *source-addr* ] **group-address** *group-addr*

**igmp snooping static-group** [ **source-address** *source-addr* ] **group-address** *group-addr* **dot1q** **vid** *vidValue*

**igmp snooping static-group** [ **source-address** *source-addr* ] **group-address** *group-addr* **qinq** **pe-vid** *pe-vidValue* **ce-vid** *ce-vidValue*

**undo igmp snooping static-group** [ **source-address** *source-addr* ] **group-address** { *group-addr* | **all** }

**undo igmp snooping static-group** [ **source-address** *source-addr* ] **group-address** { *group-addr* | **all** } **qinq** **pe-vid** *pe-vidValue* **ce-vid** *ce-vidValue*

**undo igmp snooping static-group** [ **source-address** *source-addr* ] **group-address** { *group-addr* | **all** } **dot1q** **vid** *vidValue*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **source-address** *source-addr* | Specifies a multicast source address. | The address is in dotted decimal notation and ranges from 1.0.0.0 to 223.255.255.255. |
| **group-address** *group-addr* | Specifies a multicast group address. | The value ranges from 224.0.1.0 to 239.255.255.255, in dotted decimal notation. |
| **dot1q** | Enables dot1q encapsulation to allow a Layer 2 sub-interface to receive packets each with one or more tags. | - |
| **vid** *vidValue* | Specifies a range of VLAN IDs for single-tagged packets to be received by a Layer 2 sub-interface. | The value is an integer in the range 1 to 4094. |
| **qinq** | Enables QinQ encapsulation to allow a Layer 2 sub-interface to receive packets with two or more tags. | - |
| **pe-vid** *pe-vidValue* | Specifies an outer VLAN ID for double-tagged packets to be received by a Layer 2 sub-interface. | The value is an integer in the range 1 to 4094. |
| **ce-vid** *ce-vidValue* | Specifies a range of inner VLAN IDs for double-tagged packets to be received by a Layer 2 sub-interface. | The value is an integer in the range 1 to 4094. |
| **all** | Specifies all of multicast group addresses. | - |



Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If hosts connected to an interface need to regularly receive data for a multicast group or a source-specific multicast group, the l2-multicast static-groupigmp snooping static-group command can be used to configure the interface as a static member interface. Static member interfaces can be configured on different positions on a network to enable users to receive data for specific multicast groups or source-specific multicast groups regularly.

**Prerequisites**

Before running this command, ensure that the following requirements are met:

* Enable IGMP snooping globally or enable IGMP on the VBDIF interface corresponding to the BD.
* A Layer 2 sub-interface can be bound to only one BD, and this command can be run only once.
* After the Layer 2 sub-interface is configured as a member interface in a BD, the Layer 2 sub-interface cannot be configured as a member interface in another BD.

**Configuration Impact**

A static member interface does not respond to IGMP Query messages. After the undo igmp snooping static-group command is run on a static member interface, the interface does not initiate an IGMP Leave message.If the igmp snooping static-group command is run more than once, all configurations take effect.

**Precautions**

This command and the igmp snooping port-fast-control command are mutually exclusive.


Example
-------

# Configure 100GE1/0/1.1 as a static multicast group member interface and configure the static member interface to join multicast group 225.1.1.2.
```
<HUAWEI> system-view
[~HUAWEI] igmp snooping enable
[*HUAWEI] bridge-domain 100
[*HUAWEI-bd100] quit
[*HUAWEI] interface 100GE1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] portswitch
[*HUAWEI-100GE1/0/1.1] encapsulation untag
[*HUAWEI-100GE1/0/1.1] bridge-domain 100
[*HUAWEI-100GE1/0/1.1] igmp snooping static-group group-address 225.1.1.2

```