rewrite egress vid
==================

rewrite egress vid

Function
--------



The **rewrite egress vid** command changes the VLAN tag that a dot1q Layer 2 sub-interface adds to packets when decapsulating these packets.

The **undo rewrite egress vid** command restores the VLAN tag that a dot1q Layer 2 sub-interface adds to packets when decapsulating these packets.



By default, when packets are decapsulated on a Layer 2 sub-interface that uses Dot1q encapsulation, the VLAN tag to be added is the same as the VLAN tag to be removed when packets are encapsulated.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**rewrite egress vid** *vlan-id*

**undo rewrite egress vid** *vlan-id*

**undo rewrite egress vid**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *vlan-id* | Specifies the VLAN tag that a Layer 2 sub-interface using Dot1q encapsulation adds to packets when decapsulating the packets. | The value is an integer that ranges from 1 to 4094 . |



Views
-----

100GE Layer 2 sub-interface view,10GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,25GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

By default, when packets are decapsulated on a Layer 2 sub-interface that uses dot1q encapsulation, the VLAN tag to be added is the same as the VLAN tag to be removed when packets are encapsulated. You can run this command to change the VLAN tag that a Layer 2 sub-interface adds to packet when decapsulating the packets, so that packets sent and received by the Layer 2 sub-interface use different VLAN tags.


Example
-------

# Change the VLAN tag to be added to packets when the packets are decapsulated to 20 on the Layer 2 sub-interface 100GE1/0/1.1.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.1 mode l2
[*HUAWEI-100GE1/0/1.1] encapsulation dot1q vid 10
[*HUAWEI-100GE1/0/1.1] rewrite egress vid 20

```