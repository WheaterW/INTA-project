encapsulation dot1q
===================

encapsulation dot1q

Function
--------



The **encapsulation dot1q** command enables a Layer 2 sub-interface to receive packets with a specified 802.1Q tag.

The **undo encapsulation dot1q** command disables a Layer 2 sub-interface from receiving packets with a specified 802.1Q tag.



By default, no encapsulation type is specified on an EVC Layer 2 sub-interface.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**encapsulation dot1q** [ **vid** *low-pe-vid* ]

**undo encapsulation dot1q** [ **vid** *low-pe-vid* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vid** *low-pe-vid* | Specifies a VLAN ID for single-tagged packets to be received by an EVC Layer 2 sub-interface.  low-pe-vid specifies the start VLAN ID. | The value is an integer ranging from 1 to 4094. |



Views
-----

100GE Layer 2 sub-interface view,200GE Layer 2 sub-interface view,400GE Layer 2 sub-interface view,50GE Layer 2 sub-interface view,Eth-Trunk Layer 2 sub-interface view,Layer 2 sub-interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a Layer 2 Ethernet network, packets may not carry VLAN tags, or may carry one or two VLAN tags. To enable an EVC Layer 2 sub-interface to forward different types of packets, run the command to configure an encapsulation type for the EVC Layer 2 sub-interface. Using the **encapsulation dot1q** command, you can configure a Layer 2 sub-interface to accept VLAN-encapsulated packets by default.

**Precautions**



Each EVC Layer 2 sub-interface can be configured with only one encapsulation type. If traffic encapsulation has been configured on an EVC Layer 2 sub-interface and you want to change the encapsulation type, run the **undo encapsulation** command to delete the original encapsulation type.




Example
-------

# Enable the encapsulation type of the EVC Layer 2 sub-interface to dot1q.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1.2 mode l2
[*HUAWEI-100GE1/0/1.2] encapsulation dot1q vid 10
[*HUAWEI-100GE1/0/1.2] encapsulation dot1q vid 100
[*HUAWEI-100GE1/0/1.2] encapsulation dot1q vid 60
[*HUAWEI-100GE1/0/1.2] encapsulation dot1q vid 5
Warning: Changing the smallest VLAN ID of the interface will temporarily affect services on the interface. Continue?[Y/N]:

```