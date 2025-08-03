encapsulation qinq
==================

encapsulation qinq

Function
--------



The **encapsulation qinq** command enables a Layer 2 sub-interface to receive packets with a specified 802.1Q in 802.1Q tag.

The **undo encapsulation qinq** command disables a Layer 2 sub-interface from receiving packets with a specified 802.1Q in 802.1Q tag.



By default, no encapsulation type is specified on an EVC Layer 2 sub-interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**encapsulation qinq** [ **vid** *pe-vid* **ce-vid** *low-ce-vid* ]

**undo encapsulation qinq** [ **vid** *pe-vid* **ce-vid** *low-ce-vid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vid** *pe-vid* | Specifies a VLAN ID in the outer tag of packets to be received by an EVC Layer 2 sub-interface. | The value is an integer ranging from 1 to 4094. |
| **ce-vid** *low-ce-vid* | Specifies a VLAN ID in the inner tag of double-tagged packets to be received by an EVC Layer 2 sub-interface. low-ce-vid specifies the start VLAN ID. | The value is an integer ranging from 1 to 4094. |



Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a Layer 2 Ethernet network, packets may not carry VLAN Tags or carry one or two VLAN Tags. To enable different packets to be forwarded through different EVC Layer 2 sub-interfaces, run this command to configure different encapsulation modes for Layer 2 sub-interfaces of the EVC Layer 2 sub-interface. When two VLAN TAGs are carried, the packets can enter this interface if the preceding configurations are met.

**Precautions**



Each EVC Layer 2 sub-interface can be configured with only one encapsulation type. If traffic encapsulation has been configured on an EVC Layer 2 sub-interface, you must run the **undo encapsulation** command first to delete the original traffic encapsulation type before setting a new type.




Example
-------

# Set the encapsulation type of the EVC Layer 2 sub-interface to QinQ.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.3 mode l2
[*HUAWEI-100GE1/0/1.3] encapsulation qinq vid 10 ce-vid 100

```